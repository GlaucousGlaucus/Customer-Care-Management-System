import time
from datetime import datetime
from colorama import Fore
import actions

import pandas as pd
import matplotlib.pyplot as plt

from menu_options_module import print_menu

print(f"[{datetime.now()}] Initializing...")
print(f"[{datetime.now()}] Loading Files...")

# Read the Files
customers = pd.read_csv('Data\customers.csv', index_col='id', parse_dates=[
                        'dob'], infer_datetime_format=True)
orders = pd.read_csv('Data\orders.csv')
products = pd.read_csv('Data\products.csv', index_col='id')
tickets = pd.read_csv(r'Data\tickets.csv')

print(f"[{datetime.now()}] Files Loaded")

# Creating the Menu
menu_level = "0"
pause = actions.pause
cls = actions.cls


def amc_Search():
    global menu_level
    df = customers.copy()
    while True:
        print_menu(menu_level)
        cmd_n = input("Command: ")
        if cmd_n == "1":
            qry = input(f"{Fore.CYAN}Enter Query: {Fore.RESET}")
            qry_result = df.loc[qry] if qry in df.index else pd.DataFrame()
        # Search by name
        elif cmd_n == "2":
            print(f"{Fore.LIGHTMAGENTA_EX}Current Dataframe: \n{df}\n")
            qry = input(
                f"{Fore.RED}You can use RegEX\n{Fore.CYAN}Enter Query: {Fore.RESET}")
            qry_df = df["first_name"] + " " + df["last_name"]
            qry_result = df.loc[qry_df.str.contains(qry)]
        # Search by DOB
        elif cmd_n == "3":
            print(f"{Fore.LIGHTMAGENTA_EX}Current Dataframe: \n{df}\n")
            qry_start = input(
                f"{Fore.RED}You can use RegEX\n{Fore.CYAN}Enter range for date \nStart: {Fore.RESET}")
            qry_end = input(f"{Fore.CYAN}End: {Fore.RESET}")
            qry_start, qry_end = pd.to_datetime(actions.date_decoder(
                qry_start), format=r"%Y-%m-%d"), pd.to_datetime(actions.date_decoder(qry_end), format=r"%Y-%m-%d")
            if qry_end is not None:
                qry_df = (qry_end > df["dob"]) & (df["dob"] > qry_start)
                qry_result = df[qry_df]
            else:
                qry_df = df["dob"] > qry_start
                qry_result = df[qry_df]
        # Search by Gender
        elif cmd_n == "4":
            qry = input(
                f"{Fore.CYAN}Enter Query: {Fore.RESET}").strip().lower()
            qry = "Male" if qry in ["male", "m"] else "Female" if qry in [
                "female", "f", "fe"] else "Unknown"
            qry_result = df.loc[df["gender"] == qry]
        # General String Search
        elif cmd_n in ["5", "6", "7", "8", "9", "10", "11"]:
            print(f"{Fore.LIGHTMAGENTA_EX}Current Dataframe: \n{df}\n")
            qry = input(
                f"{Fore.RED}You can use RegEX\n{Fore.CYAN}Enter Query: {Fore.RESET}")
            column = customers.columns[int(cmd_n)-1]
            qry_df = df[column].astype(str)
            qry_result = df.loc[qry_df.str.contains(qry)]
        # Search by Prime
        elif cmd_n == "12":
            qry = input(
                f"{Fore.CYAN}Enter Query: {Fore.RESET}").strip().lower()
            qry = "PRIME" if qry in ["Prime", "PRIME",
                                     "Yes", "1", "Y", "P", "p"] else "-"
            qry_result = df.loc[df["prime"] == qry]
        # Reset the operating df
        elif cmd_n == "13":
            if input(f"{Fore.RED}Are you sure you want to reset \nthe dataframe for searching?\n> {Fore.RESET}").strip().lower() in "y1":
                df = customers.copy()
                print(f"{Fore.CYAN}DataFrame was reset.\n{Fore.RESET}")
        elif cmd_n == "14":
            menu_level = "1.1"
            break
        # Check if the user wants to use the generated df for further queries
        if cmd_n in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]:
            print(f"\n\n{Fore.CYAN}Your Query Result: {Fore.RESET}\n")
            if not qry_result.empty:
                print(qry_result)
                if cmd_n != "1":
                    udf = input(
                        f"{Fore.CYAN}Do you want to use the above dataframe for rest of the queries?\n(Y/N): {Fore.RESET}")
                    if udf.strip().lower() in "y1":
                        df = qry_result.copy()
            else:
                print(f"\nEmpty dataframe\n")
        pause()


def amc_Sort():
    global menu_level
    df = customers
    while True:
        print_menu(menu_level)
        cmd_n = input("Command: ")
        if cmd_n == "14":
            menu_level = "1.1"
            break
        reversee = input(
            f"{Fore.LIGHTMAGENTA_EX}Do you want to sort in reverse order? (Y/N)\n> {Fore.RESET}").strip().lower() not in "y1"
        sort_df = None
        in_place = input(
            f"{Fore.RED}Do you want to modify the original data?\nNOTE: This action will not be reversible! Proceed with caution!\n>  {Fore.RESET}").strip().lower() in "y1"
        if cmd_n == "1":
            sort_df = df.sort_index(ascending=reversee, inplace=in_place)
        elif cmd_n in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]:
            col = df.columns[int(cmd_n)-2]
            sort_df = df.sort_values(
                by=col, ascending=reversee, inplace=in_place)
        print(Fore.LIGHTMAGENTA_EX, sort_df if not in_place else df, Fore.RESET)
        pause()
        cls()
    return df


def amc_DA():
    global menu_level
    while True:
        print_menu(menu_level)
        cmd_n = input("Command: ")
        if cmd_n == "1":
            menu_level = "1.1.3.1"
            amcDAPieChart()
        elif cmd_n == "2":
            menu_level = "1.1.3.2"
            amcDABarGraph()
        elif cmd_n == "3":
            menu_level = "1.1"
            break


def amcDAPieChart():
    global menu_level
    while True:
        print_menu(menu_level)
        cmd = input("Command: ")
        if cmd == "5":
            menu_level = "1.1.3"
            break
        # Gender
        elif cmd == "1":
            print(f"{Fore.CYAN}Displaying Gender Graph...{Fore.RESET}")
            customers.groupby(["gender"]).size().plot(kind='pie', autopct="%.2f", colors=[
                "pink", "aqua"], title="Gender", legend=False)
            plt.ylabel("Gender")
            plt.show()
        # Country
        elif cmd == "2":
            print(f"{Fore.CYAN}Displaying Country Graph...{Fore.RESET}")
            customers.groupby(["country"]).size().plot(
                kind='pie', autopct="%.2f", title="Country", legend=False)
            plt.ylabel("Country")
            plt.show()
        # State
        elif cmd == "3":
            print(f"{Fore.CYAN}Displaying State Graph...{Fore.RESET}")
            customers.groupby(["state"]).size().plot(
                kind='pie', autopct="%.2f", title="State", legend=False)
            plt.ylabel("State")
            plt.show()
        # Prime
        elif cmd == "4":
            print(f"{Fore.CYAN}Displaying Prime Graph...{Fore.RESET}")
            customers.groupby(["prime"]).size().plot(
                kind='pie', autopct="%.2f", title="Prime", legend=False)
            plt.ylabel("Prime")
            plt.show()
        pause()
        cls()


def amcDABarGraph():
    global menu_level
    while True:
        print_menu(menu_level)
        cmd = input("Command: ")
        if cmd == "2":
            menu_level = "1.1.3"
            break
        # Age of Customers
        elif cmd == "1":
            print(f"{Fore.CYAN}Displaying Age of Customers Graph...{Fore.RESET}")
            (pd.Timestamp("now") - customers['dob']
             ).astype("<m8[Y]").plot(kind='hist')
            plt.ylabel("Age")
            plt.show()
        pause()
        cls()


def am_cust_f():
    global menu_level
    global customers
    while True:
        print_menu(menu_level)
        cmd = input("Command: ")
        if cmd == "1":
            cls()
            print(customers)
            pause()
        # Search
        elif cmd == "2":
            menu_level = "1.1.1"
            amc_Search()
        # Adding a Customer
        elif cmd == "3":
            if input("Do you want to add a customer ? (Y/N) ").lower() in ["y", "1", "yes", "oui"]:
                n = input("How many customers would you like to add? ")
                try:
                    for _ in range(int(n)):
                        cls()
                        actions.add_a_Customer(customers)
                except Exception as e:
                    actions.throw_error('error', f"{e}", e.with_traceback)
            else:
                print("Command Cancelled: Add a customer.")
                pause()
        # Updating a customer
        elif cmd == "4":
            if input("Do you want to update a customer ? (Y/N) ").lower() in ["y", "1", "yes", "oui"]:
                actions.update_customer(customers)
            else:
                print("Command Cancelled: Update a customer.")
                pause()
        # Delete a customer
        elif cmd == "5":
            if input("Do you want to delete a customer ? (Y/N) ").lower() in ["y", "1", "yes", "oui"]:
                actions.delete_customer(customers)
            else:
                print("Command Cancelled: Delete a customer.")
                pause()
        # Sort
        elif cmd == "6":
            menu_level = "1.1.2"
            customers = amc_Sort()
        # Data Analysis
        elif cmd == "7":
            menu_level = "1.1.3"
            amc_DA()
        elif cmd == "8":
            menu_level = "1"
            break


def amp_Search():
    global menu_level
    df = products.copy()
    while True:
        print_menu(menu_level)
        cmd = input("Command: ")
        if cmd == "1":
            qry = input(f"{Fore.CYAN}Enter Query: {Fore.RESET}")
            qry_result = df.loc[qry] if qry in df.index else pd.DataFrame()
        elif cmd in ["2", "3", "4"]:
            print(f"{Fore.LIGHTMAGENTA_EX}Current Dataframe: \n{df}\n")
            qry = input(
                f"{Fore.RED}You can use RegEX\n{Fore.CYAN}Enter Query: {Fore.RESET}")
            column = products.columns[int(cmd)-2]
            qry_df = df[column]
            qry_result = df.loc[qry_df.str.contains(qry)]
        elif cmd in ["5", "6", "8"]:
            print(f"{Fore.LIGHTMAGENTA_EX}Current Dataframe: \n{df}\n")
            column = products.columns[int(cmd)-2]
            qry_df = df[column].replace("-", "0").astype(int)
            min, max = input(f"{Fore.LIGHTMAGENTA_EX}Enter Min: {Fore.RESET}"), input(
                f"{Fore.LIGHTMAGENTA_EX}Enter Max: {Fore.RESET}")
            if min == "":
                min = "0"
            if max == "":
                max = str(qry_df.max())
            try:
                min, max = float(min), float(max)
                qry_result = df.loc[(qry_df >= min) & (qry_df <= max)]
            except Exception as e:
                print(f"{Fore.RED}\nPlease enter a valid range!\n{Fore.RESET}")
                qry_result = pd.DataFrame()
        elif cmd == "7":
            # Search By Returnable
            menu_level = "1.2.1.1"
            print_menu(menu_level)
            cmdn = input("Command: ")
            qry_df = df["Returnable"]
            if cmdn == "1":
                qry_result = df.loc[qry_df == "Returnable"]
            elif cmdn == "2":
                qry_result = df.loc[qry_df == "Exchange-Only"]
            elif cmdn == "3":
                qry_result = df.loc[qry_df == "Not Returnable"]
            menu_level = "1.2.1"
        elif cmd == "9":
            menu_level = "1.2"
            break
        elif cmd == "10":
            if input(f"{Fore.RED}Are you sure you want to reset \nthe dataframe for searching?\n> {Fore.RESET}").strip().lower() in "y1":
                df = products.copy()
                print(f"{Fore.CYAN}DataFrame was reset.\n{Fore.RESET}")
        # Check if the user wants to use the generated df for further queries
        if cmd in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            print(f"\n\n{Fore.CYAN}Your Query Result: {Fore.RESET}\n")
            if not qry_result.empty:
                print(qry_result)
                if cmd != "1":
                    udf = input(
                        f"{Fore.CYAN}Do you want to use the above dataframe for rest of the queries?\n(Y/N): {Fore.RESET}")
                    if udf.strip().lower() in "y1":
                        df = qry_result.copy()
            else:
                print(f"\nEmpty dataframe\n")
        pause()


def amp_Sort():
    global menu_level
    df = products
    while True:
        print_menu(menu_level)
        cmd = input("Command: ")
        if cmd == "9":
            menu_level = "1.2"
            break
        reversee = input(
            f"{Fore.LIGHTMAGENTA_EX}Do you want to sort in reverse order? (Y/N)\n> {Fore.RESET}").strip().lower() not in "y1"
        sort_df = None
        in_place = input(
            f"{Fore.RED}Do you want to modify the original data?\nNOTE: This action will not be reversible! Proceed with caution!\n>  {Fore.RESET}").strip().lower() in "y1"
        if cmd == "1":
            sort_df = df.sort_index(ascending=reversee, inplace=in_place)
        elif cmd in ["2", "3", "4", "5", "6", "7", "8"]:
            col = df.columns[int(cmd)-2]
            sort_df = df.sort_values(
                by=col, ascending=reversee, inplace=in_place)
        print(Fore.LIGHTMAGENTA_EX, sort_df if not in_place else df, Fore.RESET)
        pause()
        cls()
    return df


def amp_DA():
    global menu_level
    while True:
        print_menu(menu_level)
        cmd = input("Command: ")
        if cmd == "1":
            print(f"{Fore.CYAN}Displaying Categories (In-Stock) Graph...{Fore.RESET}")
            g = products.groupby(['category'])["In-Stock"].sum()
            g.plot(kind='bar')
            plt.ylabel("In-Stock")
            plt.xlabel("Category")
            plt.show()
        elif cmd == "2":
            print(f"{Fore.CYAN}Displaying Returnable Graph...{Fore.RESET}")
            products.groupby(['Returnable']).size().plot(
                kind='pie', autopct="%.2f")
            plt.ylabel("Returnable")
            plt.show()
        elif cmd == "3":
            print(f"{Fore.CYAN}Displaying AvgRating Graph...{Fore.RESET}")
            g = products.groupby(['category'])["AvgRating"].mean()
            g.plot(kind='bar')
            plt.ylabel("AvgRating")
            plt.xlabel("Category")
            plt.show()
        elif cmd == "99":
            menu_level = "1.2"
            break


def am_prod_f():
    global menu_level
    while True:
        print_menu(menu_level)
        cmd = input("Command: ")
        # Show all products
        # Exit
        if cmd == "8":
            menu_level = "1"
            break
        elif cmd == "1":
            cls()
            print(products)
            pause()
        # Search
        elif cmd == "2":
            menu_level = "1.2.1"
            amp_Search()
        # Add products
        elif cmd == "3":
            if input("Do you want to add a product ? (Y/N) ").lower() in ["y", "1", "yes", "oui"]:
                n = input("How many products would you like to add? ")
                try:
                    for _ in range(int(n)):
                        cls()
                        actions.add_a_Product(products)
                except Exception as e:
                    actions.throw_error('error', f"{e}", e.with_traceback)
            else:
                print("Command Cancelled: Add a product.")
                pause()
        # Update products
        elif cmd == "4":
            if input("Do you want to update a product ? (Y/N) ").lower() in ["y", "1", "yes", "oui"]:
                actions.update_product(products)
            else:
                print("Command Cancelled: Update a customer.")
                pause()
        # Delete products
        elif cmd == "5":
            if input("Do you want to delete a product ? (Y/N) ").lower() in ["y", "1", "yes", "oui"]:
                actions.delete_product(products)
            else:
                print("Command Cancelled: Delete a product.")
                pause()
        # Sort products
        elif cmd == "6":
            menu_level = "1.2.2"
            amp_Sort()
        # Data Analysis
        elif cmd == "7":
            menu_level = "1.2.3"
            amp_DA()


def amo_Search():
    global menu_level
    while True:
        print_menu(menu_level)
        cmd_n = input("Command: ")
        if cmd_n == "1":
            pass
        elif cmd_n == "2":
            pass
        elif cmd_n == "3":
            pass
        elif cmd_n == "4":
            pass
        elif cmd_n == "5":
            pass
        elif cmd_n == "6":
            pass
        elif cmd_n == "7":
            pass
        elif cmd_n == "8":
            pass
        elif cmd_n == "9":
            pass
        elif cmd_n == "10":
            pass
        elif cmd_n == "11":
            pass
        elif cmd_n == "12":
            menu_level = "1.3"
            break


def amo_Sort():
    global menu_level
    while True:
        print_menu(menu_level)
        cmd_n = input("Command: ")
        if cmd_n == "1":
            pass
        elif cmd_n == "2":
            pass
        elif cmd_n == "3":
            pass
        elif cmd_n == "4":
            pass
        elif cmd_n == "5":
            pass
        elif cmd_n == "6":
            pass
        elif cmd_n == "7":
            pass
        elif cmd_n == "8":
            pass
        elif cmd_n == "9":
            pass
        elif cmd_n == "10":
            pass
        elif cmd_n == "11":
            pass
        elif cmd_n == "12":
            menu_level = "1.3"
            break


def am_ord_f():
    global menu_level
    while True:
        print_menu(menu_level)
        cmd = input("Command: ")
        if cmd == "1":
            print("Show all Orders")
        elif cmd == "2":
            menu_level = "1.3.1"
            amo_Search()
        elif cmd == "3":
            print("Add an order")
        elif cmd == "4":
            print("Update an order")
        elif cmd == "5":
            print("Delete an order")
        elif cmd == "6":
            menu_level = "1.3.2"
            amo_Sort()
        elif cmd == "7":
            menu_level = "1"
            break


def amt_Search():
    global menu_level
    while True:
        print_menu(menu_level)
        cmd = input("Command: ")
        if cmd == "1":
            pass
        elif cmd == "2":
            pass
        elif cmd == "3":
            pass
        elif cmd == "4":
            pass
        elif cmd == "5":
            pass
        elif cmd == "6":
            pass
        elif cmd == "7":
            pass
        elif cmd == "8":
            pass
        elif cmd == "9":
            pass
        elif cmd == "10":
            pass
        elif cmd == "11":
            pass
        elif cmd == "12":
            pass
        elif cmd == "13":
            pass
        elif cmd == "14":
            pass
        elif cmd == "15":
            pass
        elif cmd == "16":
            pass
        elif cmd == "17":
            menu_level = "1.4"
            break


def amt_Sort():
    global menu_level
    while True:
        print_menu(menu_level)
        cmd = input("Command: ")
        if cmd == "1":
            pass
        elif cmd == "2":
            pass
        elif cmd == "3":
            pass
        elif cmd == "4":
            pass
        elif cmd == "5":
            pass
        elif cmd == "6":
            pass
        elif cmd == "7":
            pass
        elif cmd == "8":
            pass
        elif cmd == "9":
            pass
        elif cmd == "10":
            pass
        elif cmd == "11":
            pass
        elif cmd == "12":
            pass
        elif cmd == "13":
            pass
        elif cmd == "14":
            pass
        elif cmd == "15":
            pass
        elif cmd == "16":
            pass
        elif cmd == "17":
            menu_level = "1.4"
            break


def amt_DA_PieChart():
    global menu_level
    while True:
        print_menu(menu_level)
        cmd = input("Command: ")
        if cmd == "1":
            pass
        elif cmd == "2":
            pass
        elif cmd == "3":
            menu_level = "1.4.3"
            break


def amt_DA_BarGraph():
    global menu_level
    while True:
        print_menu(menu_level)
        cmd = input("Command: ")
        if cmd == "1":
            pass
        elif cmd == "2":
            pass
        elif cmd == "3":
            pass
        elif cmd == "4":
            menu_level = "1.4.3"
            break


def amt_DA_OtherGraph():
    global menu_level
    while True:
        print_menu(menu_level)
        cmd = input("Command: ")
        if cmd == "1":
            pass
        elif cmd == "2":
            pass
        elif cmd == "3":
            pass
        elif cmd == "4":
            pass
        elif cmd == "5":
            menu_level = "1.4.3"
            break


def amt_DA():
    global menu_level
    while True:
        print_menu(menu_level)
        cmd = input("Command: ")
        if cmd == "1":
            menu_level = "1.4.3.1"
            amt_DA_PieChart()
        elif cmd == "2":
            menu_level = "1.4.3.2"
            amt_DA_BarGraph()
        elif cmd == "3":
            menu_level = "1.4.3.3"
            amt_DA_OtherGraph()
        elif cmd == "4":
            menu_level = "1.4"
            break


def amt_RG_Summerzie():
    global menu_level
    while True:
        print_menu(menu_level)
        cmd = input("Command: ")
        if cmd == "1":
            pass
        elif cmd == "2":
            pass
        elif cmd == "3":
            pass
        elif cmd == "4":
            pass
        elif cmd == "5":
            pass
        elif cmd == "6":
            menu_level = "1.4.4"
            break


def amt_MG_GenFromTemplate():
    global menu_level
    while True:
        print_menu(menu_level)
        cmd = input("Command: ")
        if cmd == "1":
            pass
        elif cmd == "2":
            pass
        elif cmd == "3":
            pass
        elif cmd == "4":
            menu_level = "1.4.5"
            break


def amt_MG_Custom():
    global menu_level
    while True:
        print_menu(menu_level)
        cmd = input("Command: ")
        if cmd == "1":
            pass
        elif cmd == "2":
            menu_level = "1.4.5"
            break


def amt_RG():
    global menu_level
    while True:
        print_menu(menu_level)
        cmd = input("Command: ")
        if cmd == "1":
            menu_level = "1.4.4.1"
            amt_RG_Summerzie()
        elif cmd == "2":
            menu_level = "1.4"
            break


def amt_MG():
    global menu_level
    while True:
        print_menu(menu_level)
        cmd = input("Command: ")
        if cmd == "1":
            menu_level = "1.4.5.1"
            amt_MG_GenFromTemplate()
        elif cmd == "2":
            menu_level = "1.4.5.2"
            amt_MG_Custom()
        elif cmd == "3":
            menu_level = "1.4"
            break


def am_tick_f():
    global menu_level
    while True:
        print_menu(menu_level)
        cmd = input("Command: ")
        if cmd == "1":
            pass
        elif cmd == "2":
            menu_level = "1.4.1"
            amt_Search()
        elif cmd == "3":
            pass
        elif cmd == "4":
            pass
        elif cmd == "5":
            pass
        elif cmd == "6":
            menu_level = "1.4.2"
            amt_Sort()
        elif cmd == "7":
            menu_level = "1.4.3"
            amt_DA()
        elif cmd == "8":
            menu_level = "1.4.4"
            amt_RG()
        elif cmd == "9":
            menu_level = "1.4.5"
            amt_MG()
        elif cmd == "10":
            menu_level = "1"
            break


def admin_menu_f():
    global menu_level
    while True:
        print_menu(menu_level)
        cmd = input("Command: ")
        if cmd == "1":
            menu_level = "1.1"
            am_cust_f()
        elif cmd == "2":
            menu_level = "1.2"
            am_prod_f()
        elif cmd == "3":
            menu_level = "1.3"
            am_ord_f()
        elif cmd == "4":
            menu_level = "1.4"
            am_tick_f()
        elif cmd == "5":
            menu_level = "0"
            break
        else:
            print("Unknown command, please try again.")


def cust_menu_f():
    global menu_level
    while True:
        print_menu(menu_level)
        cmd = input("Command: ")
        if cmd == "1":
            menu_level = "2.1"
            while True:
                print_menu(menu_level)
                cmd = input("Command: ")
                if cmd == "1":
                    print("Open a ticket")
                elif cmd == "2":
                    print("View ticket")
                elif cmd == "3":
                    print("Close a ticket")
                elif cmd == "4":
                    menu_level = "2"
                    break
        elif cmd == "2":
            print("Registering")
        elif cmd == "3":
            menu_level = "0"
            break
        else:
            print("Unknown command, please try again.")


while True:
    print_menu(menu_level)
    cmd = input('Command: ')

    # Handle Administrator login
    if cmd in ["Administrator", "1"]:
        print("Login as Administrator")
        menu_level = "1"
        admin_menu_f()

    # Handle Customer login
    elif cmd in ["Customer", "2"]:
        print("Login as Customer")
        menu_level = "2"
        cust_menu_f()

    # Handle Quit Command
    elif cmd in ['quit', 'Quit', '3', 'Exit', 'exit']:
        break
    else:
        print("Unknown command, please try again.")

print("Thank you for using this software.")
print(f"[{datetime.now()}] Quitting...")
time.sleep(1)

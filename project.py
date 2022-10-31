from http import server
import time
from datetime import date, datetime
from colorama import Fore
from helpfultools import Searchy, print_text
import actions

import pandas as pd
import matplotlib.pyplot as plt

from menu_options_module import print_menu

print(f"[{datetime.now()}] Initializing...")
print(f"[{datetime.now()}] Loading Files...")

# Read the Files
date_format = r"%Y/%m/%d %H:%M:%S"
customers = pd.read_csv('Data\customers1.csv', index_col='id')
customers["dob"] = pd.to_datetime(
    customers["dob"], format=date_format)
orders = pd.read_csv('Data\orders1.csv', index_col='orderID')
orders["dateofOrder"] = pd.to_datetime(
    orders["dateofOrder"], format=date_format)
products = pd.read_csv('Data\products1.csv', index_col='id')
tickets = pd.read_csv(r'Data\tickets1.csv', index_col='TicketID')
tickets["DateOpened"] = pd.to_datetime(
    tickets["DateOpened"], format=date_format)
tickets["DateClosed"] = pd.to_datetime(
    tickets["DateClosed"], format=date_format)

print(f"[{datetime.now()}] Files Loaded")

# Creating the Menu
menu_level = "0"
pause = actions.pause
cls = actions.cls

date_info = f"""{Fore.LIGHTRED_EX}
+============================= FORMAT =============================+
|   > The date must not be blank                                   |
|   > The date must be on the calander                             |
|   > The date must be in any of the following Formats             |
|        "16th Jan 2021"         OR      "16 Jan 2021"             |
|        "16th January 2021"     OR      "16 January 2021"         |
|        "dd/mm/yy"              OR      "dd/mm/yyyy"              |
+==================================================================+{Fore.RESET}\n\n\n"""

def SortData(df: pd.DataFrame, exit_to_level, exit_code: int, other_options: list):
    global menu_level
    other_options = [str(x) for x in other_options]
    while True:
        print_menu(menu_level)
        cmd = input("Command: ")
        if cmd == str(exit_code):
            menu_level = str(exit_to_level)
            break
        reversee = input(
            f"{Fore.LIGHTMAGENTA_EX}Do you want to sort in reverse order? (Y/N)\n> {Fore.RESET}").strip().lower() not in "y1"
        sort_df = None
        in_place = input(
            f"{Fore.RED}Do you want to modify the original data?\nNOTE: This action will not be reversible! Proceed with caution!\n>  {Fore.RESET}").strip().lower() in "y1"
        if cmd == "1":
            sort_df = df.sort_index(ascending=reversee, inplace=in_place)
        elif cmd in other_options:
            col = df.columns[int(cmd)-2]
            sort_df = df.sort_values(
                by=col, ascending=reversee, inplace=in_place)
        print(Fore.LIGHTMAGENTA_EX, sort_df if not in_place else df, Fore.RESET)
        actions.pause()
        actions.cls()
    return df


def amc_Search():
    global menu_level
    df = customers.copy()
    search_engine = Searchy(df)
    def col(x): return customers.columns[int(x)-2]
    while True:
        print_menu(menu_level)
        cmd_n = input("Command: ")
        if cmd_n == "1":
            qry = input(f"{Fore.CYAN}Enter Query: {Fore.RESET}")
            qry_result = search_engine.by_id(qry)
        # Search by DOB
        elif cmd_n == "4":
            print(f"{Fore.LIGHTMAGENTA_EX}Current Dataframe: \n{df}\n")
            qry_result = search_engine.by_date(col(cmd_n))
        # General String Search
        elif cmd_n in ["2", "3", "5", "6", "7", "8", "9", "11", "12"]:
            print(f"{Fore.LIGHTMAGENTA_EX}Current Dataframe: \n{df}\n")
            qry = input(
                f"{Fore.RED}You can use RegEX\n{Fore.CYAN}Enter Query: {Fore.RESET}")
            qry_result = search_engine.by_string(qry, col(cmd_n))
        # Search by Prime
        elif cmd_n == "10":
            print(f"{Fore.LIGHTMAGENTA_EX}Current Dataframe: \n{df}\n")
            qry_result = search_engine.by_num(col(cmd_n))
        elif cmd_n == "13":
            qry = input(
                f"{Fore.CYAN}Index:\n\t1) PRIME\n\t2) Not PRIME\nEnter Query: {Fore.RESET}").strip().lower()
            options = {"1": "PRIME", "2": "-"}
            qry_result = search_engine.by_options(
                qry, col(cmd_n), options=options, like=True)
        # Reset the operating df
        elif cmd_n == "14":
            if input(f"{Fore.RED}Are you sure you want to reset \nthe dataframe for searching?\n> {Fore.RESET}").strip().lower() in "y1":
                df = customers.copy()
                print(f"{Fore.CYAN}DataFrame was reset.\n{Fore.RESET}")
        elif cmd_n == "15":
            menu_level = "1.1"
            break
        # Check if the user wants to use the generated df for further queries
        if cmd_n in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]:
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
            SortData(customers, 1.1, "14", [
                                 "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"])
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
                print("Command Cancelled: Update a product.")
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
            SortData(products, 1.2, "9", [
                                "2", "3", "4", "5", "6", "7", "8"])
        # Data Analysis
        elif cmd == "7":
            menu_level = "1.2.3"
            amp_DA()


def amo_Search():
    global menu_level
    df = orders.copy()
    while True:
        print_menu(menu_level)
        cmd = input("Command: ")
        if cmd == "1":
            qry = input(f"{Fore.CYAN}Enter Query: {Fore.RESET}")
            qry_result = df.loc[qry] if qry in df.index else pd.DataFrame()
        elif cmd in ["2", "3", "4", "5", "6", "11"]:
            print(f"{Fore.LIGHTMAGENTA_EX}Current Dataframe: \n{df}\n")
            qry = input(
                f"{Fore.RED}You can use RegEX\n{Fore.CYAN}Enter Query: {Fore.RESET}")
            column = orders.columns[int(cmd)-2]
            qry_df = df[column]
            qry_result = df.loc[qry_df.str.contains(qry)]
        elif cmd in ["7", "8"]:
            print(f"{Fore.LIGHTMAGENTA_EX}Current Dataframe: \n{df}\n")
            column = orders.columns[int(cmd)-2]
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
        elif cmd == "10":
            # Search By Status
            print(f"{Fore.LIGHTMAGENTA_EX}Current Dataframe: \n{df}\n")
            cmdn = input(
                "Index: \n1) Cancelled\n2) Delivered\n3) Pre-Shipment\n4) Unshipped\nCommand: ")
            qry_df = df["status"]
            if cmdn == "1":
                qry_result = df.loc[qry_df == "Cancelled"]
            elif cmdn == "2":
                qry_result = df.loc[qry_df == "Delivered"]
            elif cmdn == "3":
                qry_result = df.loc[qry_df == "Pre-Shipment"]
            elif cmdn == "4":
                qry_result = df.loc[qry_df == "Unshipped"]
            menu_level = "1.3.1"
        # Search by DOO
        elif cmd == "9":
            print(f"{Fore.LIGHTMAGENTA_EX}Current Dataframe: \n{df}\n")
            qry_start = input(
                f"{Fore.RED}You can use RegEX\n{Fore.CYAN}Enter range for date \nStart: {Fore.RESET}")
            qry_end = input(f"{Fore.CYAN}End: {Fore.RESET}")
            qry_start, qry_end = pd.to_datetime(actions.date_decoder(
                qry_start), format=r"%Y-%m-%d"), pd.to_datetime(actions.date_decoder(qry_end), format=r"%Y-%m-%d")
            if qry_end is not None:
                qry_df = (qry_end > df["dateofOrder"]) & (
                    df["dateofOrder"] > qry_start)
                qry_result = df[qry_df]
            else:
                qry_df = df["dateofOrder"] > qry_start
                qry_result = df[qry_df]
        elif cmd == "12":
            menu_level = "1.3"
            break
        elif cmd == "13":
            if input(f"{Fore.RED}Are you sure you want to reset \nthe dataframe for searching?\n> {Fore.RESET}").strip().lower() in "y1":
                df = orders.copy()
                print(f"{Fore.CYAN}DataFrame was reset.\n{Fore.RESET}")
        # Check if the user wants to use the generated df for further queries
        if cmd in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]:
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


def am_ord_f():
    global menu_level
    while True:
        print_menu(menu_level)
        cmd = input("Command: ")
        if cmd == "7":
            menu_level = "1"
            break
        # Show all orders
        elif cmd == "1":
            cls()
            print(orders)
            pause()
        # Search for orders
        elif cmd == "2":
            menu_level = "1.3.1"
            amo_Search()
        # Add Order
        elif cmd == "3":
            if input("Do you want to add an order ? (Y/N) ").lower() in ["y", "1", "yes", "oui"]:
                n = input("How many orders would you like to add? ")
                try:
                    for _ in range(int(n)):
                        cls()
                        actions.add_an_order(customers, products, orders)
                except Exception as e:
                    actions.throw_error('error', f"{e}", e.with_traceback)
            else:
                print("Command Cancelled: Add an order.")
                pause()
        # Update an order
        elif cmd == "4":
            if input("Do you want to update an order ? (Y/N) ").lower() in ["y", "1", "yes", "oui"]:
                actions.update_order(customers, products, orders)
            else:
                print("Command Cancelled: Update an order.")
                pause()
        elif cmd == "5":
            if input("Do you want to delete an order ? (Y/N) ").lower() in ["y", "1", "yes", "oui"]:
                actions.delete_order(orders)
            else:
                print("Command Cancelled: Delete an order.")
                pause()
        elif cmd == "6":
            menu_level = "1.3.2"
            SortData(orders, 1.3, "12", [
                              "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"])


def amt_Search():
    global menu_level
    df = tickets.copy()
    search_engine = Searchy(df)
    def col(x): return tickets.columns[int(x)-2]
    while True:
        print_menu(menu_level)
        cmd = input("Command: ")
        # Search by Ticket ID
        if cmd == "1":
            qry = input(f"{Fore.CYAN}Enter Query: {Fore.RESET}")
            qry_result = search_engine.by_id(qry)
        # Search by Strings
        elif cmd in ["2", "3", "4", "5", "6", "7", "10"]:
            qry = input(
                f"{Fore.RED}You can use RegEX\n{Fore.CYAN}Enter Query: {Fore.RESET}")
            qry_result = search_engine.by_string(qry, col(cmd))
        # Search by Status
        elif cmd == "8":
            qry = input("Index: \n\t1) Open\n\t2) Closed\nCommand: ")
            options = {"1": "Open", "2": "Closed"}
            qry_result = search_engine.by_options(qry, col(cmd), options)
        # Search by Issue Category
        elif cmd == "9":  # TODO Maybe use options here
            qry = input(
                f"{Fore.RED}You can use RegEX\n{Fore.CYAN}Enter Query: {Fore.RESET}")
            qry_result = search_engine.by_string(qry, col(cmd))
        # Search by Dates
        elif cmd in ["11", "12"]:
            qry_result = search_engine.by_date(col(cmd), time=True)
        # Search by HoursTaken
        elif cmd in ["13", "14", "15", "16"]:
            qry_result = search_engine.by_num(col(cmd))
        # Exit TODO Move it to top
        elif cmd == "17":
            menu_level = "1.4"
            break
        elif cmd == "18":
            if input(f"{Fore.RED}Are you sure you want to reset \nthe dataframe for searching?\n> {Fore.RESET}").strip().lower() in "y1":
                df = tickets.copy()
                print(f"{Fore.CYAN}DataFrame was reset.\n{Fore.RESET}")
        # Check if the user wants to use the generated df for further queries
        if cmd in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"]:
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


def amt_DA_PieChart():
    global menu_level
    while True:
        print_menu(menu_level)
        cmd = input("Command: ")
        # Status
        if cmd == "1":
            print_text(Fore.CYAN, "Displaying Status Pie Chart...")
            tickets.groupby(["Status"]).size().plot(
                kind="pie", autopct="%.2f", title="Status", legend=True)
            plt.ylabel("")
            plt.show()
        # Prod Cat
        elif cmd == "2":
            print_text(Fore.CYAN, "Displaying Product Categories' Chart...")
            tickets.groupby(["ProductCategory"]).size().plot(
                kind="pie", autopct="%.2f", title="Product Category", legend=True)
            plt.ylabel("")
            plt.show()
        elif cmd == "3":
            menu_level = "1.4.3"
            break


def amt_DA_BarGraph():
    global menu_level
    while True:
        print_menu(menu_level)
        cmd = input("Command: ")
        if cmd in "12":
            col, txt = "DateOpened" if cmd == "1" else "DateClosed", "Opened" if cmd == "1" else "Closed"
            print_text(Fore.CYAN, f"Displaying {col}...")
            g1 = tickets.groupby(
                tickets[tickets[col] != pd.NaT][col].dt.month).size()
            g1 = g1.plot(kind='bar')
            g1.set_xticklabels(("Jan", "Feb", "Mar", "Apr", "May",
                               "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"))
            plt.ylabel(f"Number of Ticket(s) {txt}")
            plt.xlabel("Month")
            plt.show()
        elif cmd == "3":
            print_text(Fore.CYAN, f"Displaying...")
            g1 = tickets.groupby(
                tickets["DateOpened"].dt.month).size().reset_index()
            g2 = tickets.groupby(
                tickets["DateClosed"].dt.month).size().reset_index()
            g1.drop("DateOpened", axis=1, inplace=True)
            g1.rename({0: "DateOpened"}, axis=1, inplace=True)
            g1["DateClosed"] = g2[0]
            print(g1)
            month = ("Jan", "Feb", "Mar", "Apr", "May", "Jun",
                     "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
            g1 = g1.plot(kind='bar')
            g1.set_xticklabels(month)
            plt.ylabel("HoursTaken")
            plt.xlabel("Month")
            plt.show()
        elif cmd == "4":
            menu_level = "1.4.3"
            break


def amt_DA_OtherGraph():
    global menu_level
    while True:
        print_menu(menu_level)
        cmd = input("Command: ")
        if cmd == "1":
            g1 = tickets.groupby(tickets['DateClosed'].dt.month)[
                'HoursTaken'].mean()
            g1 = g1.plot(kind='line')
            month = ("Jan", "Feb", "Mar", "Apr", "May", "Jun",
                     "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
            g1.set_xticklabels(month)
            plt.ylabel(f"Avg. Time Taken (Hrs)")
            plt.xlabel("Month")
            plt.show()
        elif cmd == "2":
            g1 = tickets.groupby(tickets['DateClosed'].dt.month)[
                'FirstResponseTime(Min)'].mean()
            g1 = g1.plot(kind='line')
            month = ("Jan", "Feb", "Mar", "Apr", "May", "Jun",
                     "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
            g1.set_xticklabels(month)
            plt.ylabel(f"Avg. Response Time (min)")
            plt.xlabel("Month")
            plt.show()
        elif cmd == "3":
            g1 = tickets.groupby(tickets['DateClosed'].dt.month)[
                'Replies'].mean()
            g1 = g1.plot(kind='line')
            month = ("Jan", "Feb", "Mar", "Apr", "May", "Jun",
                     "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
            g1.set_xticklabels(month)
            plt.ylabel(f"Avg. Replies")
            plt.xlabel("Month")
            plt.show()
        elif cmd == "4":
            g1 = tickets.groupby(tickets['DateClosed'].dt.month)[
                'CustomerSatisfaction(%)'].mean()
            g1 = g1.plot(kind='line')
            month = ("Jan", "Feb", "Mar", "Apr", "May", "Jun",
                     "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
            g1.set_xticklabels(month)
            plt.ylabel(f"Customer Satisfaction")
            plt.xlabel("Month")
            plt.show()
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
        # TODO Ask to show graph
        tdy = pd.to_datetime(datetime.today().date())
        cmd_index = {1: "Today's", 2: "Weekly",
                     3: "Monthly", 4: "Yearly", 5: "Custom"}
        range_index = {
            1: [tdy, tdy],
            2: [tdy - pd.to_timedelta(7, unit='D'), tdy],
            3: [tdy - pd.to_timedelta(30, unit='D'), tdy],
            4: [tdy - pd.to_timedelta(365, unit='D'), tdy]
        }
        if cmd in "12345":
            # Get The Range
            rangee = []
            if cmd == "5":
                for x in range(2):
                    print(date_info)
                    sore = "Start: " if x == 0 else "End: "
                    do_check = input(Fore.LIGHTMAGENTA_EX + sore + Fore.RESET)
                    do = actions.date_decoder(do_check, time=True)
                    while do is None:
                        actions.throw_error(
                            'error', *actions.data_error_msgs["dob"](do_check))
                        cls()
                        print(date_info)
                        do_check = input(Fore.LIGHTMAGENTA_EX +
                                         sore + Fore.RESET)
                        do = actions.date_decoder(do_check, time=True)
                    rangee.append(do)
            else:
                rangee = range_index[int(cmd)]
            # Generate Dataframe and Report
            start, end = pd.to_datetime(rangee[0]), pd.to_datetime(rangee[1])
            start_cond = (tickets['DateOpened'] >= start) | (
                tickets['DateClosed'] >= start)
            end_cond = (tickets['DateOpened'] <= end) | (
                tickets['DateClosed'] <= end)
            df = tickets[start_cond & end_cond]
            if df.empty:
                return None
            print_text(Fore.CYAN, "Your Data:")
            print(df)
            pause()
            print(Fore.CYAN,
                  f"""
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
                        ___ _   _ _ __ ___  _ __ ___   __ _ _ __ _   _ 
                       / __| | | | '_ ` _ \| '_ ` _ \ / _` | '__| | | |
                       \__ \ |_| | | | | | | | | | | | (_| | |  | |_| |
                       |___/\__,_|_| |_| |_|_| |_| |_|\__,_|_|   \__, |
                                                                  __/ |
                                                                 |___/ 
                                                                                                                                                                                
   
   {cmd_index} Data:                                                                              
                                                                                            
   Date:                       {Fore.RED}{pd.to_datetime(datetime.today())}{Fore.CYAN}                                                  
                                                                                            
   Total Replies:              {Fore.RED}{df['Replies'].sum()}{Fore.CYAN}                                
   Tickets Opened:             {Fore.RED}{len(df[(df['DateOpened'] >= start) & (df['DateOpened'] <= end)])}{Fore.CYAN}                  
   Tickets Closed:             {Fore.RED}{len(df[(df['DateClosed'] >= start) & (df['DateClosed'] <= end)])}{Fore.CYAN}                  
                                                                                            
   Avg First Response:         {Fore.RED}{df['FirstResponseTime(Min)'].mean()}{Fore.CYAN}           
   Avg Customer Satisfaction:  {Fore.RED}{df['CustomerSatisfaction(%)'].mean()}{Fore.CYAN}   
                                                                                            
   Products Categories Reported For {cmd_index}:                                                  
   {Fore.RED}{set(list(df['ProductCategory']))}{Fore.CYAN}                                              
                                                                                            
   Most Popular Issue Category:{Fore.RED}{df['IssueCategory'].mode()[0]}{Fore.CYAN}     
                                                                                            
   Total Replies [Open]:       {Fore.RED}{df[(df['DateOpened'] >= start) & (df['DateOpened'] <= end)]['Replies'].sum()}{Fore.CYAN}                         
   Total Replies [Closed]:     {Fore.RED}{df[(df['DateOpened'] >= start) & (df['DateOpened'] <= end)]['Replies'].sum()}{Fore.CYAN}                       

▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
""", Fore.RESET)
            pause()
        elif cmd == "6":
            menu_level = "1.4.4"
            break


def amt_MG_GenFromTemplate():
    global menu_level
    while True:
        print_menu(menu_level)
        cmd = input("Command: ")
        if cmd == "4":
            menu_level = "1.4.5"
            break
        # TicketID
        TicketID = input(Fore.LIGHTMAGENTA_EX +
                         "Enter Ticket ID: " + Fore.RESET)
        if TicketID not in tickets.index:
            actions.throw_error('error', "Ticket ID not found!")
            continue
        ticket_data = tickets.loc[TicketID]
        # First Response
        if cmd == "1":
            print(
                f"""
  ______ _          _     _____                                      
 |  ____(_)        | |   |  __ \                                     
 | |__   _ _ __ ___| |_  | |__) |___  ___ _ __   ___  _ __  ___  ___ 
 |  __| | | '__/ __| __| |  _  // _ \/ __| '_ \ / _ \| '_ \/ __|/ _ \\
 | |    | | |  \__ \ |_  | | \ \  __/\__ \ |_) | (_) | | | \__ \  __/
 |_|    |_|_|  |___/\__| |_|  \_\___||___/ .__/ \___/|_| |_|___/\___|
                                         | |                         
                                         |_|
══════════════════════════════════════════════════════════════════════════

Dear {ticket_data['CustFirstName']},
Thank you for contacting us, we are sorry to hear you are having problem with
our product(s) {ticket_data['ProductName']}. 
You described your issue labelled under {ticket_data['IssueCategory']} as:
{ticket_data['Issue']}

{Fore.LIGHTMAGENTA_EX}
OrderID:    {ticket_data['OrderID']}
TicketID:   {TicketID}
Status:     {ticket_data['Status']}
{Fore.RESET}
---------------------------------------------------------------------------
Please stand by as we look into your issue, our team will try
thier best to look into your issue and try to resolve it as soon as
possible. This may take upto a few minutes.
""")
        # Denied
        elif cmd == "2":
            print(
                f"""
   _____                            _     _____             _          _ 
  |  __ \                          | |   |  __ \           (_)        | |
  | |__) |___  __ _ _   _  ___  ___| |_  | |  | | ___ _ __  _  ___  __| |
  |  _  // _ \/ _` | | | |/ _ \/ __| __| | |  | |/ _ \ '_ \| |/ _ \/ _` |
  | | \ \  __/ (_| | |_| |  __/\__ \ |_  | |__| |  __/ | | | |  __/ (_| |
  |_|  \_\___|\__, |\__,_|\___||___/\__| |_____/ \___|_| |_|_|\___|\__,_|
                 | |                                                     
                 |_|                                                     
══════════════════════════════════════════════════════════════════════════

Dear {ticket_data['CustFirstName']},
Thank you for contacting us, we are sorry to inform you but your request
was denied for your order {ticket_data['OrderID']}. 
You described your issue labelled under {ticket_data['IssueCategory']} as:
{ticket_data['Issue']}

{Fore.LIGHTMAGENTA_EX}
OrderID:    {ticket_data['OrderID']}
TicketID:   {TicketID}
Status:     {ticket_data['Status']}
{Fore.RESET}
---------------------------------------------------------------------------
Please inform us of any other issue we can help you with.
""")
        # Acknolwegement
        elif cmd == "3":
            print(
                f"""
                _                        _          _                _ 
      /\       | |                      | |        | |              | |
     /  \   ___| | ___ __   _____      _| | ___  __| | __ _  ___  __| |
    / /\ \ / __| |/ / '_ \ / _ \ \ /\ / / |/ _ \/ _` |/ _` |/ _ \/ _` |
   / ____ \ (__|   <| | | | (_) \ V  V /| |  __/ (_| | (_| |  __/ (_| |
  /_/    \_\___|_|\_\_| |_|\___/ \_/\_/ |_|\___|\__,_|\__, |\___|\__,_|
                                                       __/ |           
                                                      |___/            
══════════════════════════════════════════════════════════════════════════

Dear {ticket_data['CustFirstName']},
Thank you for contacting us, we were informed about your request
for your order {ticket_data['OrderID']}. 
You described your issue labelled under {ticket_data['IssueCategory']} as:
{ticket_data['Issue']}

{Fore.LIGHTMAGENTA_EX}
OrderID:    {ticket_data['OrderID']}
TicketID:   {TicketID}
Status:     {ticket_data['Status']}
{Fore.RESET}
---------------------------------------------------------------------------
The process may take upto several minuites to complete, hence please be patient
with us. Thank you for contacting us.
""")


def amt_MG_Custom():
    global menu_level
    while True:
        print_menu(menu_level)
        cmd = input("Command: ")
        if cmd == "1":
            # TicketID
            TicketID = input(Fore.LIGHTMAGENTA_EX +
                             "Enter Ticket ID: " + Fore.RESET)
            while TicketID not in tickets.index:
                if TicketID == "EXT": 
                    break
                actions.throw_error('error', "Ticket ID not found! Type EXT TO QUIT")
                TicketID = input(Fore.LIGHTMAGENTA_EX +
                                 "Enter Ticket ID: " + Fore.RESET)
            else:
                ticket_data = tickets.loc[TicketID]
                print_menu(menu_level)
                message = input("Enter your message: \n")
                print(
                f"""
   _____          _                               _____                              _   
  / ____|        | |                             / ____|                            | |  
 | |    _   _ ___| |_ ___  _ __ ___   ___ _ __  | (___  _   _ _ __  _ __   ___  _ __| |_ 
 | |   | | | / __| __/ _ \| '_ ` _ \ / _ \ '__|  \___ \| | | | '_ \| '_ \ / _ \| '__| __|
 | |___| |_| \__ \ || (_) | | | | | |  __/ |     ____) | |_| | |_) | |_) | (_) | |  | |_ 
  \_____\__,_|___/\__\___/|_| |_| |_|\___|_|    |_____/ \__,_| .__/| .__/ \___/|_|   \__|
                                                             | |   | |                   
                                                             |_|   |_|                   
═════════════════════════════════════════════════════════════════════════════════════════════

Dear {ticket_data['CustFirstName']},
{message}

{Fore.LIGHTMAGENTA_EX}
OrderID:    {ticket_data['OrderID']}
TicketID:   {TicketID}
Status:     {ticket_data['Status']}
{Fore.RESET}
---------------------------------------------------------------------------
Thank you for contacting us.
""")
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
    global tickets
    while True:
        print_menu(menu_level)
        cmd = input("Command: ")
        if cmd == "10":
            menu_level = "1"
            break
        elif cmd == "1":
            cls()
            print(tickets)
            pause()
        elif cmd == "2":
            menu_level = "1.4.1"
            amt_Search()
        elif cmd == "3":
            if input("Do you want to add a ticket ? (Y/N) ").lower() in ["y", "1", "yes", "oui"]:
                n = input("How many tickets would you like to add? ")
                for _ in range(int(n)):
                    cls()
                    actions.add_a_ticket(customers, products, orders, tickets)
                # try:
                #     pass
                # except Exception as e:
                #     actions.throw_error('error', f"{e}", e.with_traceback)
            else:
                print("Command Cancelled: Add a ticket.")
                pause()
        elif cmd == "4":
            if input("Do you want to update a ticket ? (Y/N) ").lower() in ["y", "1", "yes", "oui"]:
                actions.update_ticket(customers, products, orders, tickets)
            else:
                print("Command Cancelled: Update a ticket.")
                pause()
        elif cmd == "5":
            if input("Do you want to delete a ticket ? (Y/N) ").lower() in ["y", "1", "yes", "oui"]:
                actions.delete_ticket(tickets)
            else:
                print("Command Cancelled: Delete a ticket.")
                pause()
        elif cmd == "6":
            menu_level = "1.4.2"
            SortData(tickets, 1.4, "17", [
                               2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
        elif cmd == "7":
            menu_level = "1.4.3"
            amt_DA()
        elif cmd == "8":
            menu_level = "1.4.4"
            amt_RG()
        elif cmd == "9":
            menu_level = "1.4.5"
            amt_MG()


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
            CustID = input(Fore.LIGHTMAGENTA_EX + "Enter ID: " + Fore.RESET)
            if CustID in customers.index:
                print(Fore.LIGHTGREEN_EX + """
                                ╦  ╔═╗╔═╗╦╔╗╔  ╔═╗╦ ╦╔═╗╔═╗╔═╗╔═╗╔═╗╔═╗╦ ╦╦  
                                ║  ║ ║║ ╦║║║║  ╚═╗║ ║║  ║  ║╣ ╚═╗╚═╗╠╣ ║ ║║  
                                ╩═╝╚═╝╚═╝╩╝╚╝  ╚═╝╚═╝╚═╝╚═╝╚═╝╚═╝╚═╝╚  ╚═╝╩═╝
                """, Fore.RESET)
                pause()
                menu_level = "2.1"
                while True:
                    print_menu(menu_level)
                    cmd = input("Command: ")
                    if cmd == "1":
                        cls()
                        actions.add_a_ticket(
                            customers, products, orders, tickets, custid=CustID, register=True)
                    elif cmd == "2":
                        search_engine = Searchy(tickets)
                        qry_result = search_engine.by_string(
                            CustID, tickets.columns[0])
                        print(Fore.LIGHTMAGENTA_EX, qry_result, Fore.RESET)
                        pause()
                    elif cmd == "3":
                        actions.update_ticket(
                            customers, products, orders, tickets, close=True)
                    elif cmd == "4":
                        data = customers.loc[CustID]
                        print(Fore.CYAN,
                              f"""
                                    ╔═╗╦═╗╔═╗╔═╗╦╦  ╔═╗
                                    ╠═╝╠╦╝║ ║╠╣ ║║  ║╣ 
                                    ╩  ╩╚═╚═╝╚  ╩╩═╝╚═╝
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        ______              +===========================================================+
       ╱      ╲              Customer ID:  {Fore.LIGHTGREEN_EX}{CustID}{Fore.CYAN}                                    
      ╱        ╲             Name       :  {Fore.LIGHTGREEN_EX}{data['first_name'] + data['last_name']}{Fore.CYAN}  
     │          │            DOB        :  {Fore.LIGHTGREEN_EX}{data['dob']}{Fore.CYAN}  
     │          │            Gender     :  {Fore.LIGHTGREEN_EX}{data['gender']}{Fore.CYAN}  
     │          │            Email      :  {Fore.LIGHTGREEN_EX}{data['email']}{Fore.CYAN}  
   _╱------------╲_          Phone      :  {Fore.LIGHTGREEN_EX}{data['phone']}{Fore.CYAN}
 _╱                ╲_       +===========================================================+
╱____________________╲

┭╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┭╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┭╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┭╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┭╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┭
│        o         │        o         │        o         │        o         │        o         │
┴╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┴╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┴╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┴╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┴╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┴

      ________________
     /                \\
    /   ____________   \\
   /   /            \   \\
  /   /              \   \      +===========================================================+
  |   |              |   |       Address  :   {Fore.LIGHTGREEN_EX}{data['address']}{Fore.CYAN}                                
  |   |              |   |       Country  :   {Fore.LIGHTGREEN_EX}{data['country']}{Fore.CYAN}
  |   |              |   |       State    :   {Fore.LIGHTGREEN_EX}{data['city']}{Fore.CYAN}                        
   \   \_____________/   /       City     :   {Fore.LIGHTGREEN_EX}{data['state']}{Fore.CYAN}                      
    \                   /        Pincode  :   {Fore.LIGHTGREEN_EX}{data['pincode']}{Fore.CYAN}
     \_               _/         Prime    :   {Fore.LIGHTGREEN_EX}{data['prime']}{Fore.CYAN}
       \_           _/          +===========================================================+
         \_       _/
          \_     _/
            \___/

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                                                 
   
""", Fore.RESET)
                        pause()
                    elif cmd == "5":
                        menu_level = "2"
                        break
            else:
                print(Fore.LIGHTRED_EX + "Wrong Credentials" + Fore.RESET)
                pause()
        elif cmd == "2":
            cls()
            print(Fore.LIGHTCYAN_EX +
                  """
│                        ╦═╗╔═╗╔═╗╦╔═╗╔╦╗╔═╗╦═╗                        │
│                        ╠╦╝║╣ ║ ╦║╚═╗ ║ ║╣ ╠╦╝                        │
│                        ╩╚═╚═╝╚═╝╩╚═╝ ╩ ╚═╝╩╚═                        │
╰──────────────────────────────────────────────────────────────────────╯
""" + Fore.RESET)
            actions.add_a_Customer(customers=customers, register=True)
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
customers.to_csv(r'Data\customers1.csv')
products.to_csv(r'Data\products1.csv')
orders.to_csv(r'Data\orders1.csv')
tickets.to_csv(r'Data\tickets1.csv')
time.sleep(1)

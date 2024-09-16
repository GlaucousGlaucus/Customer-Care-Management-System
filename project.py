import matplotlib.pyplot as plt

from actions import *
from actions import dateformat_info as date_info
from menu_options_module import print_menu


def SaveAll():
    SaveData(customers, "Customers")
    SaveData(products, "Products")
    SaveData(orders, "Orders")
    SaveData(tickets, "Tickets")
    SaveData(msgs, "Messages")


def SortData(df: pd.DataFrame, exit_to_level, exit_code: int | str, other_options: list):
    global menu_level
    other_options = [str(x) for x in other_options]
    while True:
        print_menu(menu_level)
        sort_cmd = input("Command: ")
        if sort_cmd == str(exit_code):
            menu_level = str(exit_to_level)
            break
        reverse_chk = input(
            f"{Fore.LIGHTMAGENTA_EX}Do you want to sort in reverse order? (Y/N)\n> {Fore.RESET}").strip().lower() not in "y1"
        sort_df = None
        in_place = input(
            f"{Fore.RED}Do you want to modify the original data?\nNOTE: This action will not be reversible! Proceed "
            f"with caution!\n>  {Fore.RESET}").strip().lower() in "y1 "
        if sort_cmd == "1":
            sort_df = df.sort_index(ascending=reverse_chk, inplace=in_place)
        elif sort_cmd in other_options:
            col = df.columns[int(sort_cmd) - 2]
            sort_df = df.sort_values(by=col, ascending=reverse_chk, inplace=in_place)
        print(Fore.LIGHTMAGENTA_EX, sort_df if not in_place else df, Fore.RESET)
        pause()
        cls()
    return df


def amc_Search():
    global menu_level
    df = customers.copy()
    df.drop(["password"], axis=1, inplace=True)
    search_engine = CustomSearcher(df)

    def col(x):
        return customers.columns[int(x) - 2]

    qry_result = None
    while True:
        print_menu(menu_level)
        cmd_n = input("Command: ")
        if cmd_n == "1":
            qry = safe_input(f"{Fore.CYAN}Enter Query: {Fore.RESET}")
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
            options = {"1": "PRIME", "2": "NOT PRIME"}
            qry_result = search_engine.by_options(
                qry, col(cmd_n), options=options)
        # Reset the operating df
        elif cmd_n == "14":
            if input(
                    f"{Fore.RED}Are you sure you want to reset \nthe dataframe for searching?\n> {Fore.RESET}").strip().lower() in "y1":
                df = customers.copy()
                search_engine = CustomSearcher(df)
                print(f"{Fore.CYAN}DataFrame was reset.\n{Fore.RESET}")
        elif cmd_n == "15":
            menu_level = "1.1"
            break
        # Check if the user wants to use the generated df for further queries
        ops = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]
        df, search_engine = qry_df_final_func(df, cmd, ops, search_engine, qry_result)
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
        amc_da_pie_cmd = input("Command: ")
        if amc_da_pie_cmd == "5":
            menu_level = "1.1.3"
            break
        # Gender
        elif amc_da_pie_cmd == "1":
            print(f"{Fore.CYAN}Displaying Gender Graph...{Fore.RESET}")
            customers.groupby(["gender"]).size().plot(kind='pie', autopct="%.2f", colors=[
                "pink", "aqua"], title="Gender", legend=False)
            plt.ylabel("Gender")
            plt.show()
        # Country
        elif amc_da_pie_cmd == "2":
            print(f"{Fore.CYAN}Displaying Country Graph...{Fore.RESET}")
            customers.groupby(["country"]).size().plot(
                kind='pie', autopct="%.2f", title="Country", legend=False)
            plt.ylabel("Country")
            plt.show()
        # State
        elif amc_da_pie_cmd == "3":
            print(f"{Fore.CYAN}Displaying State Graph...{Fore.RESET}")
            customers.groupby(["state"]).size().plot(
                kind='pie', autopct="%.2f", title="State", legend=False)
            plt.ylabel("State")
            plt.show()
        # Prime
        elif amc_da_pie_cmd == "4":
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
        amc_da_bar_cmd = input("Command: ")
        if amc_da_bar_cmd == "2":
            menu_level = "1.1.3"
            break
        # Age of Customers
        elif amc_da_bar_cmd == "1":
            print(f"{Fore.CYAN}Displaying Age of Customers Graph...{Fore.RESET}")
            (pd.Timestamp("now") - customers['dob']
             ).astype("<m8[Y]").plot(kind='hist')
            plt.ylabel("Age")
            plt.show()
        pause()
        cls()


def admin_customer_main():
    global menu_level
    global customers
    while True:
        print_menu(menu_level)
        amc_cmd = input("Command: ")
        if amc_cmd == "1":
            cls()
            print(customers.drop(["password"], axis=1))
            pause()
        # Search
        elif amc_cmd == "2":
            menu_level = "1.1.1"
            amc_Search()
        # Adding a Customer
        elif amc_cmd == "3":
            if input("Do you want to add a customer ? (Y/N) ").strip().lower() in ["y", "1", "yes", "oui"]:
                n = safe_input("How many customers would you like to add? ")
                try:
                    for _ in range(n):
                        cls()
                        add_a_Customer(customers)
                except Exception as e:
                    throw_error('error', f"{e}", e.with_traceback)
            else:
                print("Command Cancelled: Add a customer.")
                pause()
        # Updating a customer
        elif amc_cmd == "4":
            if input("Do you want to update a customer ? (Y/N) ").strip().lower() in ["y", "1", "yes", "oui"]:
                update_customer(customers)
            else:
                print("Command Cancelled: Update a customer.")
                pause()
        # Delete a customer
        elif amc_cmd == "5":
            if input("Do you want to delete a customer ? (Y/N) ").strip().lower() in ["y", "1", "yes", "oui"]:
                delete_customer(customers)
            else:
                print("Command Cancelled: Delete a customer.")
                pause()
        # Sort
        elif amc_cmd == "6":
            menu_level = "1.1.2"
            SortData(customers.drop(["password"], axis=1), 1.1, "14", [
                "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"])
        # Data Analysis
        elif amc_cmd == "7":
            menu_level = "1.1.3"
            amc_DA()
        elif amc_cmd == "8":
            menu_level = "1"
            break


# -----------------------------------------------------------------------------------------------------------------------------

def amp_Search():
    global menu_level
    df = products.copy()
    search_engine = CustomSearcher(df)
    qry_result = None

    def col(x):
        return products.columns[int(x) - 2]

    while True:
        print_menu(menu_level)
        amp_cmd = input("Command: ")
        if amp_cmd == "1":
            qry = safe_input(f"{Fore.CYAN}Enter Query: {Fore.RESET}")
            qry_result = search_engine.by_id(qry)
        elif amp_cmd in ["2", "3", "4"]:
            print(f"{Fore.LIGHTMAGENTA_EX}Current Dataframe: \n{df}\n")
            qry = input(
                f"{Fore.RED}You can use RegEX\n{Fore.CYAN}Enter Query: {Fore.RESET}")
            qry_result = search_engine.by_string(qry, col(amp_cmd))
        elif amp_cmd in ["5", "6", "8"]:
            print(f"{Fore.LIGHTMAGENTA_EX}Current Dataframe: {Fore.RESET}\n{df}\n")
            qry_result = search_engine.by_num(col(amp_cmd))
        elif amp_cmd == "7":
            # Search By Returnable
            menu_level = "1.2.1.1"
            print_menu(menu_level)
            options = {"1": "Returnable", "2": "Exchange-Only", "3": "Not Returnable"}
            qry = input("Command: ")
            qry_result = search_engine.by_options(qry, col(amp_cmd), options)
            menu_level = "1.2.1"
        elif amp_cmd == "9":
            menu_level = "1.2"
            break
        elif amp_cmd == "10":
            if input(
                    f"{Fore.RED}Are you sure you want to reset \nthe dataframe for searching?\n> {Fore.RESET}").strip().lower() in "y1":
                df = products.copy()
                print(f"{Fore.CYAN}DataFrame was reset.\n{Fore.RESET}")
        # Check if the user wants to use the generated df for further queries
        ops = ["1", "2", "3", "4", "5", "6", "7", "8"]
        df, search_engine = qry_df_final_func(df, cmd, ops, search_engine, qry_result)
        pause()


def amp_DA():
    global menu_level
    while True:
        print_menu(menu_level)
        amp_da_cmd = input("Command: ")
        if amp_da_cmd == "1":
            print(f"{Fore.CYAN}Displaying Categories (In-Stock) Graph...{Fore.RESET}")
            g = products.groupby(['category'])["In-Stock"].sum()
            g.plot(kind='bar')
            plt.ylabel("In-Stock")
            plt.xlabel("Category")
            plt.show()
        elif amp_da_cmd == "2":
            print(f"{Fore.CYAN}Displaying Returnable Graph...{Fore.RESET}")
            products.groupby(['Returnable']).size().plot(
                kind='pie', autopct="%.2f")
            plt.ylabel("Returnable")
            plt.show()
        elif amp_da_cmd == "3":
            print(f"{Fore.CYAN}Displaying AvgRating Graph...{Fore.RESET}")
            g = products.groupby(['category'])["AvgRating"].mean()
            g.plot(kind='bar')
            plt.ylabel("AvgRating")
            plt.xlabel("Category")
            plt.show()
        elif amp_da_cmd == "4":
            menu_level = "1.2"
            break


def admin_product_main():
    global menu_level
    while True:
        print_menu(menu_level)
        amp_cmd = input("Command: ")
        # Exit
        if amp_cmd == "8":
            menu_level = "1"
            break
        elif amp_cmd == "1":
            cls()
            print(products)
            pause()
        # Search
        elif amp_cmd == "2":
            menu_level = "1.2.1"
            amp_Search()
        # Add products
        elif amp_cmd == "3":
            if input("Do you want to add a product ? (Y/N) ").lower() in ["y", "1", "yes", "oui"]:
                n = safe_input("How many products would you like to add? ")
                try:
                    for _ in range(n):
                        cls()
                        add_a_Product(products)
                except Exception as e:
                    throw_error('error', f"{e}", e.with_traceback)
            else:
                print("Command Cancelled: Add a product.")
                pause()
        # Update products
        elif amp_cmd == "4":
            if input("Do you want to update a product ? (Y/N) ").lower() in ["y", "1", "yes", "oui"]:
                update_product(products)
            else:
                print("Command Cancelled: Update a product.")
                pause()
        # Delete products
        elif amp_cmd == "5":
            if input("Do you want to delete a product ? (Y/N) ").lower() in ["y", "1", "yes", "oui"]:
                delete_product(products)
            else:
                print("Command Cancelled: Delete a product.")
                pause()
        # Sort products
        elif amp_cmd == "6":
            menu_level = "1.2.2"
            SortData(products, 1.2, "9", [
                "2", "3", "4", "5", "6", "7", "8"])
        # Data Analysis
        elif amp_cmd == "7":
            menu_level = "1.2.3"
            amp_DA()


# -----------------------------------------------------------------------------------------------------------------------------

def admin_order_search():
    global menu_level
    df = orders.copy()
    search_engine = CustomSearcher(df)
    qry_result = None

    def col(x):
        return orders.columns[int(x) - 2]

    while True:
        print_menu(menu_level)
        admin_order_search_cmd = input("Command: ")
        if admin_order_search_cmd == "1":
            qry = safe_input(f"{Fore.CYAN}Enter Query: {Fore.RESET}")
            qry_result = search_engine.by_id(qry)
        elif admin_order_search_cmd in "25":
            print(f"{Fore.LIGHTMAGENTA_EX}Current Dataframe: \n{df}\n")
            qry = safe_input(f"{Fore.CYAN}Enter Query: {Fore.RESET}")
            qry_result = search_engine.by_single(qry, col(admin_order_search_cmd))
        elif admin_order_search_cmd in ["3", "4", "6", "11"]:
            print(f"{Fore.LIGHTMAGENTA_EX}Current Dataframe: \n{df}\n")
            qry = input(
                f"{Fore.RED}You can use RegEX\n{Fore.CYAN}Enter Query: {Fore.RESET}")
            qry_result = search_engine.by_string(qry, col(admin_order_search_cmd))
        elif admin_order_search_cmd in ["7", "8"]:
            print(f"{Fore.LIGHTMAGENTA_EX}Current Dataframe: \n{df}\n")
            qry_result = search_engine.by_num(col(admin_order_search_cmd))
        elif admin_order_search_cmd == "10":
            # Search By Status
            print(f"{Fore.LIGHTMAGENTA_EX}Current Dataframe: \n{df}\n")
            status_search_command = input(
                "Index: \n1) Cancelled\n2) Delivered\n3) Pre-Shipment\n4) Unshipped\nCommand: ")
            qry_result = search_engine.by_options(status_search_command, col(
                admin_order_search_cmd), {"1": "Cancelled", "2": "Delivered", "3": "Pre-Shipment", "4": "Unshipped"})
        # Search by DOO
        elif admin_order_search_cmd == "9":
            print(f"{Fore.LIGHTMAGENTA_EX}Current Dataframe: \n{df}\n")
            qry_result = search_engine.by_date(
                col=col(admin_order_search_cmd), formatting=date_format, time=True)
        elif admin_order_search_cmd == "12":
            menu_level = "1.3"
            break
        elif admin_order_search_cmd == "13":
            if input(
                    f"{Fore.RED}Are you sure you want to reset \nthe dataframe for searching?\n> {Fore.RESET}").strip().lower() in "y1":
                df = orders.copy()
                search_engine = CustomSearcher(df)
                print(f"{Fore.CYAN}DataFrame was reset.\n{Fore.RESET}")
        # Check if the user wants to use the generated df for further queries
        ops = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
        df, search_engine = qry_df_final_func(df, admin_order_search_cmd, ops, search_engine, qry_result)
        pause()


def am_ord_f():
    global menu_level
    while True:
        print_menu(menu_level)
        admin_order_cmd = input("Command: ")
        if admin_order_cmd == "7":
            menu_level = "1"
            break
        # Show all orders
        elif admin_order_cmd == "1":
            cls()
            print(orders)
            pause()
        # Search for orders
        elif admin_order_cmd == "2":
            menu_level = "1.3.1"
            admin_order_search()
        # Add Order
        elif admin_order_cmd == "3":
            if input("Do you want to add an order ? (Y/N) ").lower() in ["y", "1", "yes", "oui"]:
                n = safe_input("How many orders would you like to add? ")
                try:
                    for _ in range(n):
                        cls()
                        add_an_order(customers, products, orders)
                except Exception as e:
                    throw_error('error', f"{e}", e.with_traceback)
            else:
                print("Command Cancelled: Add an order.")
                pause()
        # Update an order
        elif admin_order_cmd == "4":
            if input("Do you want to update an order ? (Y/N) ").lower() in ["y", "1", "yes", "oui"]:
                update_order(customers, products, orders)
            else:
                print("Command Cancelled: Update an order.")
                pause()
        elif admin_order_cmd == "5":
            if input("Do you want to delete an order ? (Y/N) ").lower() in ["y", "1", "yes", "oui"]:
                delete_order(orders)
            else:
                print("Command Cancelled: Delete an order.")
                pause()
        elif admin_order_cmd == "6":
            menu_level = "1.3.2"
            SortData(orders, 1.3, "12", [
                "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"])


# -----------------------------------------------------------------------------------------------------------------------------


def amt_Search():
    global menu_level
    df = tickets.copy()
    search_engine = CustomSearcher(df)
    qry_result = None

    def col(x):
        return tickets.columns[int(x) - 2]

    while True:
        print_menu(menu_level)
        admin_ticket_search_cmd = input("Command: ")
        # Search by Ticket ID
        if admin_ticket_search_cmd == "1":
            qry = safe_input(f"{Fore.CYAN}Enter Query: {Fore.RESET}")
            qry_result = search_engine.by_id(qry)
        elif admin_ticket_search_cmd in "23":
            qry = safe_input(f"{Fore.CYAN}Enter Query: {Fore.RESET}")
            qry_result = search_engine.by_single(qry, col(admin_ticket_search_cmd))
        # Search by Strings
        elif admin_ticket_search_cmd in ["4", "5", "6", "7", "10"]:
            qry = input(
                f"{Fore.RED}You can use RegEX\n{Fore.CYAN}Enter Query: {Fore.RESET}")
            qry_result = search_engine.by_string(qry, col(admin_ticket_search_cmd))
        # Search by Status
        elif admin_ticket_search_cmd == "8":
            qry = input("Index: \n\t1) Open\n\t2) Closed\nCommand: ")
            options = {"1": "Open", "2": "Closed"}
            qry_result = search_engine.by_options(qry, col(admin_ticket_search_cmd), options)
        # Search by Issue Category
        elif admin_ticket_search_cmd == "9":
            qry = input(
                f"{Fore.RED}You can use RegEX\n{Fore.CYAN}Enter Query: {Fore.RESET}")
            qry_result = search_engine.by_string(qry, col(admin_ticket_search_cmd))
        # Search by Dates
        elif admin_ticket_search_cmd in ["11", "12"]:
            qry_result = search_engine.by_date(col(admin_ticket_search_cmd), time=True)
        # Search by HoursTaken
        elif admin_ticket_search_cmd in ["13", "14", "15", "16"]:
            qry_result = search_engine.by_num(col(admin_ticket_search_cmd))
        # Exit TODO Move it to top
        elif admin_ticket_search_cmd == "17":
            menu_level = "1.4"
            break
        elif admin_ticket_search_cmd == "18":
            if input(
                    f"{Fore.RED}Are you sure you want to reset \nthe dataframe for searching?\n> {Fore.RESET}").strip().lower() in "y1":
                df = tickets.copy()
                search_engine = CustomSearcher(df)
                print(f"{Fore.CYAN}DataFrame was reset.\n{Fore.RESET}")
        # Check if the user wants to use the generated df for further queries
        ops = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"]
        df, search_engine = qry_df_final_func(df, admin_ticket_search_cmd, ops, search_engine, qry_result)
        pause()


def amt_DA_PieChart():
    global menu_level
    while True:
        print_menu(menu_level)
        admin_ticket_da_pie_cmd = input("Command: ")
        # Status
        if admin_ticket_da_pie_cmd == "1":
            print_text(Fore.CYAN, "Displaying Status Pie Chart...")
            tickets.groupby(["Status"]).size().plot(
                kind="pie", autopct="%.2f", title="Status", legend=True)
            plt.ylabel("")
            plt.show()
        # Prod Cat
        elif admin_ticket_da_pie_cmd == "2":
            print_text(Fore.CYAN, "Displaying Product Categories' Chart...")
            tickets.groupby(["ProductCategory"]).size().plot(
                kind="pie", autopct="%.2f", title="Product Category", legend=True)
            plt.ylabel("")
            plt.show()
        elif admin_ticket_da_pie_cmd == "3":
            menu_level = "1.4.3"
            break


def amt_DA_BarGraph():
    global menu_level
    while True:
        print_menu(menu_level)
        admin_ticket_da_bar_cmd = input("Command: ")
        if admin_ticket_da_bar_cmd in "12":
            col, txt = "DateOpened" if admin_ticket_da_bar_cmd == "1" else "DateClosed", "Opened" if admin_ticket_da_bar_cmd == "1" else "Closed"
            print_text(Fore.CYAN, f"Displaying {col}...")
            g1 = tickets.groupby(
                tickets[tickets[col] != pd.NaT][col].dt.month).size()
            g1 = g1.plot(kind='bar')
            g1.set_xticklabels(("Jan", "Feb", "Mar", "Apr", "May",
                                "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"))
            plt.ylabel(f"Number of Ticket(s) {txt}")
            plt.xlabel("Month")
            plt.show()
        elif admin_ticket_da_bar_cmd == "3":
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
        elif admin_ticket_da_bar_cmd == "4":
            menu_level = "1.4.3"
            break


def amt_DA_OtherGraph():
    global menu_level
    while True:
        print_menu(menu_level)
        admin_ticket_da_other_cmd = input("Command: ")
        if admin_ticket_da_other_cmd == "1":
            g1 = tickets.groupby(tickets['DateClosed'].dt.month)[
                'HoursTaken'].mean()
            g1 = g1.plot(kind='line')
            month = ("Jan", "Feb", "Mar", "Apr", "May", "Jun",
                     "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
            plt.ylabel(f"Avg. Time Taken (Hrs)")
            plt.xlabel("Month")
            plt.show()
        elif admin_ticket_da_other_cmd == "2":
            g1 = tickets.groupby(tickets['DateClosed'].dt.month)[
                'FirstResponseTime'].mean()
            g1 = g1.plot(kind='line')
            month = ("Jan", "Feb", "Mar", "Apr", "May", "Jun",
                     "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
            g1.set_xticklabels(month)
            plt.ylabel(f"Avg. Response Time (min)")
            plt.xlabel("Month")
            plt.show()
        elif admin_ticket_da_other_cmd == "3":
            g1 = tickets.groupby(tickets['DateClosed'].dt.month)[
                'Replies'].mean()
            g1 = g1.plot(kind='line')
            month = ("Jan", "Feb", "Mar", "Apr", "May", "Jun",
                     "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
            g1.set_xticklabels(month)
            plt.ylabel(f"Avg. Replies")
            plt.xlabel("Month")
            plt.show()
        elif admin_ticket_da_other_cmd == "4":
            g1 = tickets.groupby(tickets['DateClosed'].dt.month)[
                'CustomerSatisfaction(%)'].mean()
            g1 = g1.plot(kind='line')
            month = ("Jan", "Feb", "Mar", "Apr", "May", "Jun",
                     "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
            g1.set_xticklabels(month)
            plt.ylabel(f"Customer Satisfaction")
            plt.xlabel("Month")
            plt.show()
        elif admin_ticket_da_other_cmd == "5":
            menu_level = "1.4.3"
            break


def amt_DA():
    global menu_level
    while True:
        print_menu(menu_level)
        admin_ticket_cmd = input("Command: ")
        if admin_ticket_cmd == "1":
            menu_level = "1.4.3.1"
            amt_DA_PieChart()
        elif admin_ticket_cmd == "2":
            menu_level = "1.4.3.2"
            amt_DA_BarGraph()
        elif admin_ticket_cmd == "3":
            menu_level = "1.4.3.3"
            amt_DA_OtherGraph()
        elif admin_ticket_cmd == "4":
            menu_level = "1.4"
            break


def amt_RG_Summarize():
    global menu_level
    while True:
        print_menu(menu_level)
        admin_ticket_report_cmd = safe_input("Command: ")
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
        if admin_ticket_report_cmd in [1, 2, 3, 4, 5]:
            # Get The Range for date
            date_range = []
            if admin_ticket_report_cmd == 5:
                for x in range(2):
                    print(datetimeformat_info)
                    start_or_end = "Start: " if x == 0 else "End: "
                    date_check = input(Fore.LIGHTMAGENTA_EX + start_or_end + Fore.RESET)
                    decoded_date = date_decoder(date_check, time=True)
                    while decoded_date is None:
                        throw_error(
                            'error', *data_error_msgs["dob"](date_check))
                        cls()
                        print(date_info)
                        date_check = input(Fore.LIGHTMAGENTA_EX +
                                           start_or_end + Fore.RESET)
                        decoded_date = date_decoder(date_check, time=True)
                    date_range.append(decoded_date)
            else:
                date_range = range_index[admin_ticket_report_cmd]
            # Generate Dataframe and Report
            start, end = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])
            start_cond = (tickets['DateOpened'] >= start) | (
                    tickets['DateClosed'] >= start)
            end_cond = (tickets['DateOpened'] <= end) | (
                    tickets['DateClosed'] <= end)
            df = tickets[start_cond & end_cond]
            if df.empty:
                throw_error('info', 'EMPTY DATAFRAME', "")
                menu_level = "1.4.4"
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
                                                                                                                                                                                
   
   {cmd_index[admin_ticket_report_cmd]} Data:                                                                              
                                                                                            
   Date:                       {Fore.RED}{pd.to_datetime(datetime.today())}{Fore.CYAN}                                                  
                                                                                            
   Total Replies:              {Fore.RED}{df['Replies'].sum()}{Fore.CYAN}                                
   Tickets Opened:             {Fore.RED}{len(df[(df['DateOpened'] >= start) & (df['DateOpened'] <= end)])}{Fore.CYAN}                  
   Tickets Closed:             {Fore.RED}{len(df[(df['DateClosed'] >= start) & (df['DateClosed'] <= end)])}{Fore.CYAN}                  
                                                                                            
   Avg First Response (Min):         {Fore.RED}{df['FirstResponseTime'].mean()}{Fore.CYAN}           
   Avg Customer Satisfaction:  {Fore.RED}{df['CustomerSatisfaction(%)'].mean()}{Fore.CYAN}   
                                                                                            
   Products Categories Reported For {cmd_index}:                                                  
   {Fore.RED}{set(list(df['ProductCategory']))}{Fore.CYAN}                                              
                                                                                            
   Most Popular Issue Category:{Fore.RED}{df['IssueCategory'].mode()[0]}{Fore.CYAN}     
                                                                                            
   Total Replies [Open]:       {Fore.RED}{df[(df['DateOpened'] >= start) & (df['DateOpened'] <= end)]['Replies'].sum()}{Fore.CYAN}                         
   Total Replies [Closed]:     {Fore.RED}{df[(df['DateOpened'] >= start) & (df['DateOpened'] <= end)]['Replies'].sum()}{Fore.CYAN}                       

▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
""", Fore.RESET)
            pause()
        elif admin_ticket_report_cmd == 6:
            menu_level = "1.4.4"
            break


def amt_MG_GenFromTemplate():
    global menu_level
    while True:
        print_menu(menu_level)
        admin_ticket_message_cmd = input("Command: ")
        if admin_ticket_message_cmd == "4":
            menu_level = "1.4.5"
            break
        # TicketID
        ticket_id = safe_input(Fore.LIGHTMAGENTA_EX +
                               "Enter Ticket ID: " + Fore.RESET)
        if ticket_id not in tickets.index:
            throw_error('error', "Ticket ID not found!")
            continue
        ticket_data = tickets.loc[ticket_id]
        # First Response
        msg = ""
        if admin_ticket_message_cmd == "1":
            msg = f"""

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

OrderID:    {ticket_data['OrderID']}
TicketID:   {ticket_id}
Status:     {ticket_data['Status']}
---------------------------------------------------------------------------
Please stand by as we look into your issue, our team will try
their best to look into your issue and try to resolve it as soon as
possible. This may take upto a few minutes.
"""
        # Denied
        elif admin_ticket_message_cmd == "2":
            msg = f"""
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

OrderID:    {ticket_data['OrderID']}
TicketID:   {ticket_id}
Status:     {ticket_data['Status']}
---------------------------------------------------------------------------
Please inform us of any other issue we can help you with.
"""
        # Acknowledgement
        elif admin_ticket_message_cmd == "3":
            msg = f"""
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

OrderID:    {ticket_data['OrderID']}
TicketID:   {ticket_id}
Status:     {ticket_data['Status']}
---------------------------------------------------------------------------
The process may take upto several minuets to complete, hence please be patient
with us. Thank you for contacting us.
"""
        print(msg)
        send_to_chat = input(
            Fore.LIGHTMAGENTA_EX + "Would you like to send this message to chat ?" + Fore.RESET).strip().lower()
        if send_to_chat in "y1":
            msgs.loc[msgs.sort_index().index[::-1][0] + 1] = [ticket_id,
                                                              "ADMIN", msg, pd.to_datetime(datetime.now())]
            SaveData(msgs, "Messages")


def amt_MG_Custom():
    global menu_level
    while True:
        print_menu(menu_level)
        admin_msg_custom_cmd = input("Command: ")
        if admin_msg_custom_cmd == "1":
            # TicketID
            ticket_id = safe_input(Fore.LIGHTMAGENTA_EX +
                                   "Enter Ticket ID: " + Fore.RESET)
            if ticket_id not in tickets.index:
                throw_error(
                    'error', "Ticket ID not found! Type EXT TO QUIT")
                continue
            else:
                ticket_data = tickets.loc[ticket_id]
                print_menu(menu_level)
                message = input("Enter your message: \n")
                msg = \
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

OrderID:    {ticket_data['OrderID']}
TicketID:   {ticket_id}
Status:     {ticket_data['Status']}
---------------------------------------------------------------------------
Thank you for contacting us.
"""
                print(msg)
                send_to_chat = input(
                    Fore.LIGHTMAGENTA_EX + "Would you like to send this message to chat ?" + Fore.RESET).strip().lower()
                if send_to_chat in "y1":
                    msgs.loc[msgs.sort_index().index[::-1][0] + 1] = [ticket_id,
                                                                      "ADMIN", msg, pd.to_datetime(datetime.now())]
                    SaveData(msgs, "Messages")
        elif admin_msg_custom_cmd == "2":
            menu_level = "1.4.5"
            break


def amt_RG():
    global menu_level
    while True:
        print_menu(menu_level)
        admin_report_gen_cmd = input("Command: ")
        if admin_report_gen_cmd == "1":
            menu_level = "1.4.4.1"
            amt_RG_Summarize()
        elif admin_report_gen_cmd == "2":
            menu_level = "1.4"
            break


def amt_MG():
    global menu_level
    while True:
        print_menu(menu_level)
        admin_ticket_msg_gen_cmd = input("Command: ")
        if admin_ticket_msg_gen_cmd == "1":
            menu_level = "1.4.5.1"
            amt_MG_GenFromTemplate()
        elif admin_ticket_msg_gen_cmd == "2":
            menu_level = "1.4.5.2"
            amt_MG_Custom()
        elif admin_ticket_msg_gen_cmd == "3":
            menu_level = "1.4"
            break


def am_tick_f():
    global menu_level
    global tickets
    while True:
        print_menu(menu_level)
        admin_ticket_command = input("Command: ")
        if admin_ticket_command == "10":
            menu_level = "1"
            break
        elif admin_ticket_command == "1":
            cls()
            print(tickets)
            pause()
        elif admin_ticket_command == "2":
            menu_level = "1.4.1"
            amt_Search()
        elif admin_ticket_command == "3":
            if input("Do you want to add a ticket ? (Y/N) ").lower() in ["y", "1", "yes", "oui"]:
                n = safe_input("How many tickets would you like to add? ")
                for _ in range(n):
                    cls()
                    add_a_ticket(customers, products, orders, tickets)
            else:
                print("Command Cancelled: Add a ticket.")
                pause()
        elif admin_ticket_command == "4":
            if input("Do you want to update a ticket ? (Y/N) ").lower() in ["y", "1", "yes", "oui"]:
                update_ticket(customers, products, orders, tickets)
            else:
                print("Command Cancelled: Update a ticket.")
                pause()
        elif admin_ticket_command == "5":
            if input("Do you want to delete a ticket ? (Y/N) ").lower() in ["y", "1", "yes", "oui"]:
                delete_ticket(tickets)
            else:
                print("Command Cancelled: Delete a ticket.")
                pause()
        elif admin_ticket_command == "6":
            menu_level = "1.4.2"
            SortData(tickets, 1.4, "17", [
                2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
        elif admin_ticket_command == "7":
            menu_level = "1.4.3"
            amt_DA()
        elif admin_ticket_command == "8":
            menu_level = "1.4.4"
            amt_RG()
        elif admin_ticket_command == "9":
            menu_level = "1.4.5"
            amt_MG()


def amMsg_Search(ticket_id=None, cust=False):
    global menu_level
    df = msgs.copy()
    search_engine = CustomSearcher(df)
    qry_result = None

    def col(x):
        return msgs.columns[int(x) - 2]

    while True:
        print_menu(menu_level)
        admin_msg_search_cmd = input("Command: ")
        # Search by Msg ID
        if admin_msg_search_cmd == "1":
            qry = safe_input(f"{Fore.CYAN}Enter Query: {Fore.RESET}")
            qry_result = search_engine.by_id(qry)
            if cust:
                qry_result = qry_result if qry_result["TicketID"] == ticket_id else pd.DataFrame(
                )
        # Search by TicketID
        if admin_msg_search_cmd == "2":
            qry = safe_input(f"{Fore.CYAN}Enter Query: {Fore.RESET}")
            if qry not in tickets.index:
                throw_error('error', "ID Does not exist",
                            "Please enter an ID that exists.")
                continue
            qry_result = msgs[msgs["TicketID"] == qry]
        # Search by Strings
        elif admin_msg_search_cmd in ["3", "4"]:
            qry = input(
                f"{Fore.RED}You can use RegEX\n{Fore.CYAN}Enter Query: {Fore.RESET}")
            qry_result = search_engine.by_string(qry, col(admin_msg_search_cmd))
        elif admin_msg_search_cmd == "5":
            qry_result = search_engine.by_date(
                col(admin_msg_search_cmd), formatting=date_format, time=True)
        elif admin_msg_search_cmd == "7":
            menu_level = "1.5" if not cust else "2.5"
            break
        elif admin_msg_search_cmd == "6":
            if input(
                    f"{Fore.RED}Are you sure you want to reset \nthe dataframe for searching?\n> {Fore.RESET}").strip().lower() in "y1":
                df = msgs.copy()
                search_engine = CustomSearcher(df)
                print(f"{Fore.CYAN}DataFrame was reset.\n{Fore.RESET}")
        # Check if the user wants to use the generated df for further queries
        ops = ["1", "2", "3", "4"]
        df, search_engine = qry_df_final_func(df, admin_msg_search_cmd, ops, search_engine, qry_result)
        pause()


def message_gui(msgs_df: pd.DataFrame, customer_id=None, admin=True):
    global menu_level
    ticket_id = safe_input(Fore.LIGHTMAGENTA_EX +
                           "Enter Ticket ID: " + Fore.RESET, "Please make sure you have entered the ID as Integer")
    if ticket_id not in tickets.index or (not admin and tickets.loc[ticket_id]["CustID"] != customer_id):
        throw_error('error', "Ticket ID not found!")
        menu_level = "1.5"
        return None
    while True:
        print_menu(menu_level)
        msg_gui_cmd = input("Command: ")
        if msg_gui_cmd == "5":
            menu_level = "1.5" if admin else "2.5"
            break
        # ticket_id
        # Set the side
        side = "ADMIN" if admin else "CLIENT"
        data = msgs_df[msgs_df['TicketID'] == ticket_id]
        if msg_gui_cmd == "1":
            show_chat(data)
            pause()
        elif msg_gui_cmd == "2":
            show_chat(data)
            message = input("""
--------------------------------------------------------------------
Your Message: """)
            msgs_df.loc[msgs_df.sort_index().index[::-1][0] + 1] = [ticket_id,
                                                                    side, message, pd.to_datetime(datetime.now())]
            SaveData(msgs_df, "Messages")
            cls()
            data = msgs_df[msgs_df['TicketID'] == ticket_id]
            show_chat(data)
            pause()
        elif msg_gui_cmd == "3":
            cls()
            print(Fore.LIGHTWHITE_EX +
                  "You may find your id using our search feature" + Fore.RESET)
            ipt = safe_input(Fore.LIGHTMAGENTA_EX +
                             "Message ID: " + Fore.RESET)
            if ipt in msgs_df.index:
                msgs_df.drop(ipt, inplace=True)
            SaveData(msgs_df, "Messages")
        elif msg_gui_cmd == "4":
            menu_level = "2.5.1"
            amMsg_Search(ticket_id=ticket_id, cust=True)


def am_msg_f():
    global menu_level
    global msgs
    while True:
        print_menu(menu_level)
        admin_message_command = input("Command: ")
        if admin_message_command == "5":
            menu_level = "1"
            break
        elif admin_message_command == "1":
            cls()
            print(msgs)
            pause()
        elif admin_message_command == "2":
            menu_level = "1.5.1"
            amMsg_Search()
        elif admin_message_command == "3":
            menu_level = "1.5.2"
            SortData(msgs, 1.5, "6", [2, 3, 4, 5])
        elif admin_message_command == "4":
            menu_level = "1.5.5"
            message_gui(msgs)


# -----------------------------------------------------------------------------------------------------------------------------
def admin_menu_f():
    global menu_level
    while True:
        print_menu(menu_level)
        admin_menu_command = input("Command: ")
        if admin_menu_command == "1":
            menu_level = "1.1"
            admin_customer_main()
        elif admin_menu_command == "2":
            menu_level = "1.2"
            admin_product_main()
        elif admin_menu_command == "3":
            menu_level = "1.3"
            am_ord_f()
        elif admin_menu_command == "4":
            menu_level = "1.4"
            am_tick_f()
        elif admin_menu_command == "5":
            menu_level = "1.5"
            am_msg_f()
        elif admin_menu_command == "6":
            menu_level = "0"
            break
        else:
            print("Unknown command, please try again.")


def cust_menu_f():
    global menu_level
    while True:
        print_menu(menu_level)
        customer_menu_command = input("Command: ")
        if customer_menu_command == "1":
            customer_id = safe_input(Fore.LIGHTMAGENTA_EX +
                                     "Enter ID: " + Fore.RESET)
            password = input(Fore.LIGHTMAGENTA_EX + "Password: " + Fore.RESET)
            if customer_id in customers.index and password == customers.loc[customer_id]["password"]:
                print(Fore.LIGHTGREEN_EX + """
                                ╦  ╔═╗╔═╗╦╔╗╔  ╔═╗╦ ╦╔═╗╔═╗╔═╗╔═╗╔═╗╔═╗╦ ╦╦  
                                ║  ║ ║║ ╦║║║║  ╚═╗║ ║║  ║  ║╣ ╚═╗╚═╗╠╣ ║ ║║  
                                ╩═╝╚═╝╚═╝╩╝╚╝  ╚═╝╚═╝╚═╝╚═╝╚═╝╚═╝╚═╝╚  ╚═╝╩═╝
                """, Fore.RESET)
                pause()
                menu_level = "2.1"
                while True:
                    print_menu(menu_level)
                    search_engine = CustomSearcher(tickets)
                    qry_result = search_engine.by_single(
                        customer_id, tickets.columns[0])
                    customer_menu_command = input("Command: ")
                    if customer_menu_command == "1":
                        cls()
                        add_a_ticket(
                            customers, products, orders, tickets, custid=customer_id, register=True)
                    elif customer_menu_command == "2":
                        print(Fore.LIGHTMAGENTA_EX, qry_result, Fore.RESET)
                        pause()
                    elif customer_menu_command == "3":
                        update_ticket(
                            customers, products, orders, tickets, custid=customer_id, msg_grp=msg_grp, close=True)
                    elif customer_menu_command == "4":
                        data = customers.loc[customer_id]
                        print(Fore.CYAN,
                              f"""
                                    ╔═╗╦═╗╔═╗╔═╗╦╦  ╔═╗
                                    ╠═╝╠╦╝║ ║╠╣ ║║  ║╣ 
                                    ╩  ╩╚═╚═╝╚  ╩╩═╝╚═╝
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

        ______              ▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
       ╱      ╲              Customer ID:  {Fore.LIGHTGREEN_EX}{customer_id}{Fore.CYAN}                                    
      ╱        ╲             Name       :  {Fore.LIGHTGREEN_EX}{data['first_name'] + " " + data['last_name']}{Fore.CYAN}  
     │          │            DOB        :  {Fore.LIGHTGREEN_EX}{data['dob']}{Fore.CYAN}  
     │          │            Gender     :  {Fore.LIGHTGREEN_EX}{data['gender']}{Fore.CYAN}  
     │          │            Email      :  {Fore.LIGHTGREEN_EX}{data['email']}{Fore.CYAN}  
   _╱------------╲_          Phone      :  {Fore.LIGHTGREEN_EX}{data['phone']}{Fore.CYAN}
 _╱                ╲_       ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
╱____________________╲

░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

       ______________
      ╱              ╲
     ╱   __________   ╲
    ╱   /          \   ╲
   ╱   /            \   ╲      ▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
  |   │              │   │       Address  :   {Fore.LIGHTGREEN_EX}{data['address']}{Fore.CYAN}                                
  |   │              │   │       Country  :   {Fore.LIGHTGREEN_EX}{data['country']}{Fore.CYAN}
  |   │              │   │       State    :   {Fore.LIGHTGREEN_EX}{data['city']}{Fore.CYAN}                        
   ╲   \____________/    ╱       City     :   {Fore.LIGHTGREEN_EX}{data['state']}{Fore.CYAN}                      
    ╲                   ╱        Pincode  :   {Fore.LIGHTGREEN_EX}{data['pincode']}{Fore.CYAN}
     ╲_               _╱         Prime    :   {Fore.LIGHTGREEN_EX}{data['prime']}{Fore.CYAN}
       ╲_           _╱          ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
         ╲_       _╱
          ╲_     _╱
            ╲___╱

▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
                                                                 
   
""", Fore.RESET)
                        pause()
                    elif customer_menu_command == "5":
                        menu_level = "2.5"
                        message_gui(msgs, customer_id=customer_id, admin=False)
                    elif customer_menu_command == "6":
                        menu_level = "2"
                        break
            else:
                print(Fore.LIGHTRED_EX + "Wrong Credentials", Fore.RESET)
                forgot = input(Fore.LIGHTMAGENTA_EX +
                               "Forgot Password or Id ? (Y/N)" + Fore.RESET)
                if forgot.strip().lower() in "y1":
                    email_for_otp = input(Fore.LIGHTMAGENTA_EX +
                                          "Enter Email: " + Fore.RESET)
                    try:
                        forgot_pass_mail(customers, email_for_otp)
                        pause()
                    except Exception as e:
                        throw_error('error', "Failed to Change Password", e)
        elif customer_menu_command == "2":
            cls()
            print(Fore.LIGHTCYAN_EX +
                  """
│                        ╦═╗╔═╗╔═╗╦╔═╗╔╦╗╔═╗╦═╗                        │
│                        ╠╦╝║╣ ║ ╦║╚═╗ ║ ║╣ ╠╦╝                        │
│                        ╩╚═╚═╝╚═╝╩╚═╝ ╩ ╚═╝╩╚═                        │
╰──────────────────────────────────────────────────────────────────────╯
""" + Fore.RESET)
            add_a_Customer(customers=customers, register=True)
        elif customer_menu_command == "3":
            menu_level = "0"
            break
        else:
            print("Unknown command, please try again.")


if __name__ == "__main__":
    print(f"[{datetime.now()}] Initializing...")
    print(f"[{datetime.now()}] Loading Files...")

    # Read the Files
    # date_format = r"%Y/%m/%d %H:%M:%S"
    date_format = r"mixed"
    customers = pd.read_csv(r'Data\Customers.csv', index_col='id')
    customers["dob"] = pd.to_datetime(
        customers["dob"], format=date_format)
    orders = pd.read_csv(r'Data\Orders.csv', index_col='orderID')
    orders["dateofOrder"] = pd.to_datetime(
        orders["dateofOrder"], format=date_format)
    products = pd.read_csv(r'Data\Products.csv', index_col='id')
    tickets = pd.read_csv(r'Data\Tickets.csv', index_col='TicketID')
    tickets["DateOpened"] = pd.to_datetime(
        tickets["DateOpened"], format=date_format)
    tickets["DateClosed"] = pd.to_datetime(
        tickets["DateClosed"], format=date_format)
    msgs = pd.read_csv('Data\Messages.csv', index_col='MessageID')
    msgs["Date"] = pd.to_datetime(msgs["Date"], format=date_format)
    msg_grp = msgs.groupby(['TicketID'])
    print(f"[{datetime.now()}] Files Loaded")

    # Creating the Menu
    menu_level = "0"

    # Main Program
    while True:
        print_menu(menu_level)
        cmd = input('Command: ')

        # Handle Administrator login
        if cmd in ["Administrator", "1"]:
            menu_level = "1"
            admin_menu_f()

        # Handle Customer login
        elif cmd in ["Customer", "2"]:
            menu_level = "2"
            cust_menu_f()

        # Handle Quit Command
        elif cmd in ['quit', 'Quit', '3', 'Exit', 'exit']:
            break
        else:
            print("Unknown command, please try again.")

    # Ending Sequence
    print("Thank you for using this software.")
    print(f"[{datetime.now()}] Saving Files...")
    SaveAll()
    print(f"[{datetime.now()}] Quitting...")
    time.sleep(1)

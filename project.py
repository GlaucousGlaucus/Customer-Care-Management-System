import time
from datetime import datetime
from uuid import uuid4
import uuid
import re

import numpy as np
import pandas as pd
from matplotlib import cm

from menu_options_module import print_menu

print(f"[{datetime.now()}] Initializing...")
print(f"[{datetime.now()}] Loading Files...")

# Read the Files
customers = pd.read_csv('Data\customers.csv', index_col='id')
orders = pd.read_csv('Data\orders.csv')
products = pd.read_csv('Data\products.csv')
tickets = pd.read_csv(r'Data\tickets.csv')

print(f"[{datetime.now()}] Files Loaded")

# Creating the Menu
menu_level = "0"

def amc_Search():
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
            pass
        elif cmd_n == "13":
            menu_level = "1.1"
            break

def amc_Sort():
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
            pass
        elif cmd_n == "13":
            menu_level = "1.1"
            break

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
        if cmd == "1":
            pass
        elif cmd == "2":
            pass
        elif cmd == "3":
            pass
        elif cmd == "4":
            pass
        elif cmd == "5":
            menu_level = "1.1.3"
            break


def amcDABarGraph():
    global menu_level
    while True:
        print_menu(menu_level)
        cmd = input("Command: ")
        if cmd == "1":
            pass
        elif cmd == "2":
            menu_level = "1.1.3"
            break

def validate_email(email):
    return re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email)

def date_decoder(date):
    d, m, y = None, None, None
    if " " in date:
        date = date.split(" ")
        if str(date[1]).isdigit(): return None
        M = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        d, m, y = date[0][:2], M.index(date[1][:3]) + 1, date[2]
    elif "/" in date:
        date = date.split("/")
        d, m, y = date
    else:
        return None
    try:
        datetime(year=int(y),month=int(m),day=int(d))
        if len(y) == 2: y = "20" + y
        return f"{int(d)}/{int(m)}/{int(y)}"
    except ValueError as e:
        print("Invalid date")
        return None


def am_cust_f():
    global menu_level
    while True:
        print_menu(menu_level)
        cmd = input("Command: ")
        if cmd == "1":
            print(customers)
        elif cmd == "2":
            menu_level = "1.1.1"
            amc_Search()
        elif cmd == "3":
            print("+" + "-"*25 + "ADD A CUSTOMER" + "-"*25 + "+")
            id = input("Enter ID (Leave blank for random uuid): ")
            while id in customers.index:
                print("ERROR DUPLICATE ID")
                id = input("Enter ID (Leave blank for random uuid): ")
            if id == "": id = uuid.uuid4()
            # first_name
            first_name = input("Enter First Name: ")
            while not first_name.isalpha():
                print("First Name should only have alpha characters")
                first_name = input("Enter First Name: ")
            # last_name
            last_name = input("Enter Last Name: ")
            while not last_name.isalpha():
                print("Last Name should only have alpha characters")
                last_name = input("Enter Last Name: ")
            # DOB
            print("""Accepted Formats: 
"16th Jan 2021"
"16/01/2021"
'16 January 2021'
            """)
            dob_check = input("Enter Dob: ")
            dob = date_decoder(dob_check)
            # Gender
            gender_check = input("Enter Gender (No Abbrev): ")
            gender = gender_check if gender_check in ["Male", "Female"] else None
            # Address
            address = input("Enter Address: ")
            # Country
            country = input("Enter Country: ")
            while not country.isalpha():
                print("Country should only have alpha characters")
                country = input("Enter Country: ")
            # City
            city = input("Enter City: ")
            while not city.isalpha():
                print("City should only have alpha characters")
                city = input("Enter City: ")
            # State
            state = input("Enter State: ")
            while not state.isalpha():
                print("State should only have alpha characters")
                state = input("Enter State: ")
            # Postal code
            pincode = input("Enter Pincode: ")
            while not pincode.isdigit():
                print("Pincode must be a number.")
                pincode = input("Enter Pincode: ")
            # Phone
            phone = input("Enter Phone: ")
            while not phone.isdigit():
                print("Phone must be a valid Phone.")
                phone = input("Enter Phone: ")
            # Email
            email = input("Enter Email: ")
            while not validate_email(email):
                print("Invalid Email")
                email = input("Enter Email: ")
            # Prime
            prime = "PRIME" if input("Enter Prime: ") in ["Prime", "PRIME", "Yes", "1", "Y", "P", "p"] else "-"
            # Whole data validation
            NewData = [first_name, last_name, dob,
            gender, address, country, city, state, pincode,
            phone, email, prime]
            print("+" + "-"*50 + "+")
            if all(NewData):
                ll = max([len(x) for x in NewData])
                fac = 62 if ll <= 62 else ll
                eq = ll - 62 if ll > 62 else 0
                print(f"""
            +{"=" * (eq//2)}============================Please Confirm the Data Input======================={"=" * ((eq//2) + (1 if eq % 2 != 0 else 0))}+
            | id          :    {id        }{" " * (fac - len(str(id        )))}|
            | first_name  :    {first_name}{" " * (fac - len(str(first_name)))}|
            | last_name   :    {last_name }{" " * (fac - len(str(last_name )))}|
            | dob         :    {dob       }{" " * (fac - len(str(dob       )))}|
            | gender      :    {gender    }{" " * (fac - len(str(gender    )))}|
            | address     :    {address   }{" " * (fac - len(str(address   )))}|
            | country     :    {country   }{" " * (fac - len(str(country   )))}|
            | city        :    {city      }{" " * (fac - len(str(city      )))}|
            | state       :    {state     }{" " * (fac - len(str(state     )))}|
            | pincode     :    {pincode   }{" " * (fac - len(str(pincode   )))}|
            | phone       :    {phone     }{" " * (fac - len(str(phone     )))}|
            | email       :    {email     }{" " * (fac - len(str(email     )))}|
            | prime       :    {prime     }{" " * (fac - len(str(prime     )))}|
            +================================================================================{"=" * eq}+
            """)
                reck = input("Would you like to insert this data to Customers.csv ? (Y/N): ")
                if reck.lower() == "y": 
                    customers.loc[id] = NewData
                else:
                    print("Record Insertion Cancelled.")
            else:
                print(f"Error: Invalid Data: {NewData}")
        elif cmd == "4":
            print("Update A Customer")
        elif cmd == "5":
            print("Delete A Customer")
        elif cmd == "6":
            menu_level = "1.1.2"
            amc_Sort()
        elif cmd == "7":
            menu_level = "1.1.3"
            amc_DA()
        elif cmd == "8":
            menu_level = "1"
            break

def amp_Search():
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
            # Search By Returnable
            menu_level = "1.2.1.1"
            while True:
                print_menu(menu_level)
                cmdn = input("Command: ")
                if cmdn == "1":
                    pass
                elif cmdn == "2":
                    pass
                elif cmdn == "3":
                    pass
                elif cmdn == "4":
                    menu_level = "1.2.1"
                    break
        elif cmd == "8":
            pass
        elif cmd == "9":
            menu_level = "1.2"
            break

def amp_Sort():
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
            menu_level = "1.2"
            break

def amp_DA():
    global menu_level
    while True:
        print_menu(menu_level)
        cmd = input("Command: ")
        if cmd == "1":
            pass
        elif cmd == "2":
            menu_level = "1.2"
            break

def am_prod_f():
    global menu_level
    while True:
        print_menu(menu_level)
        cmd = input("Command: ")
        if cmd == "1":
            print("Show all Products")
        elif cmd == "2":
            menu_level = "1.2.1"
            amp_Search()
        elif cmd == "3":
            print("Add a Product")
        elif cmd == "4":
            print("Update a Product")
        elif cmd == "5":
            print("Delete a Product")
        elif cmd == "6":
            menu_level = "1.2.2"
            amp_Sort()
        elif cmd == "7":
            menu_level = "1.2.3"
            amp_DA()
        elif cmd == "8":
            menu_level = "1"
            break

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

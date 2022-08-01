from calendar import c
from re import T
import pandas as pd
import numpy as np
import time
from datetime import datetime

print(f"[{datetime.now()}] Initializing...")
print(f"[{datetime.now()}] Loading Files...")

# Read the Files
customers = pd.read_csv('Data\customers.csv')
orders = pd.read_csv('Data\orders.csv')
products = pd.read_csv('Data\products.csv')
tickets = pd.read_csv(r'Data\tickets.csv')

print(f"[{datetime.now()}] Files Loaded")

# Creating the Menu
menu_level = "0"
menu_title = """----------------------------------MENU----------------------------------"""
menu_main = \
"""
1) Login as Administrator
2) Login as Customer
3) Exit the program
"""
menu_admin = \
"""
1) Customers
2) Products
3) Orders
4) Tickets
5) Back
"""
menu_cust = \
"""
1) Login
2) Register
3) Back
"""
menu_cust_login = \
"""
1) Open a ticket
2) View ticket(s)
3) Close a ticket
4) Back
"""

# Methods related to Menus

def print_menu(menu_level):
        match menu_level:
            case "0":
                print(menu_title)
                print(menu_main)
            case "1":
                print(menu_title)
                print(menu_admin)
            case "2":
                print(menu_title)
                print(menu_cust)
            case "2.1":
                print(menu_title)
                print(menu_cust_login)

def admin_menu_f():
    global menu_level
    while True:
        print_menu(menu_level)
        cmd = input("Command: ")
        if cmd == "1":
            print("Customers")
        elif cmd == "2":
            print("Products")
        elif cmd == "3":
            print("Orders")
        elif cmd == "4":
            print("Tickets")
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
time.sleep(2)

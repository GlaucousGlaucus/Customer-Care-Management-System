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
"""
menu_cust = \
"""
1) Login
2) Register
"""
menu_cust_login = \
"""
1) Open a ticket
2) View ticket(s)
3) Close a ticket
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

while True:
    print_menu(menu_level)
    cmd = input('Command: ')
    # Handle Administrator login
    if cmd in ["Administrator", "1"]:
        print("Login as Administrator")
        menu_level = "1"
    # Handle Customer login
    elif cmd in ["Customer", "2"]:
        print("Login as Customer")
        menu_level = "2"
    # Handle Quit Command
    elif cmd in ['quit', 'Quit', '3', 'Exit', 'exit']:
        break

print("Thank you for using this software.")
print(f"[{datetime.now()}] Quitting...")
time.sleep(2)

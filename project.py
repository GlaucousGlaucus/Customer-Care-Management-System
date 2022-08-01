from calendar import c
from re import T
from menu_options_module import menu_options
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

# TODO: Replace this with better title
menu_title = lambda x=None: f"""----------------------------------{x.upper() + " " if x is not None else ""}MENU----------------------------------"""


def print_menu(menu_level):
        match menu_level:
            case "0":
                print(menu_title())
                print(menu_options[menu_level])
            case "1":
                print(menu_title("Administrator"))
                print(menu_options[menu_level])
            case "2":
                print(menu_title("Customer"))
                print(menu_options[menu_level])
            case "2.1":
                print(menu_title("Customer"))
                print(menu_options[menu_level])

def am_cust_f():
    global menu_level
    while True:
        print_menu(menu_level)
        cmd = input("Command: ")
        if cmd == "8":
            menu_level = "1"
            break

def am_prod_f():
    global menu_level
    while True:
        print_menu(menu_level)
        cmd = input("Command: ")
        if cmd == "8":
            menu_level = "1"
            break

def am_ord_f():
    global menu_level
    while True:
        print_menu(menu_level)
        cmd = input("Command: ")
        if cmd == "7":
            menu_level = "1"
            break

def am_tick_f():
    global menu_level
    while True:
        print_menu(menu_level)
        cmd = input("Command: ")
        if cmd == "10":
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

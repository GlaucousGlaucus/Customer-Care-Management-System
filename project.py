import time
from datetime import datetime
from uuid import uuid4
import uuid
import re
import actions

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
pause = actions.pause
cls = actions.cls

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

def am_cust_f():
    global menu_level
    while True:
        print_menu(menu_level)
        cmd = input("Command: ")
        if cmd == "1":
            print(customers)
            pause()
        elif cmd == "2":
            menu_level = "1.1.1"
            amc_Search()
        # Adding a Customer
        elif cmd == "3":
            actions.add_a_Customer(customers)
            pause()
        # Updating a customer
        elif cmd == "4":
            actions.update_customer(customers)
            pause()
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

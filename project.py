from calendar import c
from re import I, T
from tkinter import E

from matplotlib import cm
from menu_options_module import menu_options, print_menu
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
            print("Show all Customers")
        elif cmd == "2":
            menu_level = "1.1.1"
            print_menu(menu_level)
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
        elif cmd == "3":
            print("Add A Customer")
        elif cmd == "4":
            print("Update A Customer")
        elif cmd == "5":
            print("Delete A Customer")
        elif cmd == "6":
            menu_level = "1.1.2"
            print_menu(menu_level)
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
        elif cmd == "7":
            menu_level = "1.1.3"
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
        elif cmd == "8":
            menu_level = "1"
            break

def am_prod_f():
    global menu_level
    while True:
        print_menu(menu_level)
        cmd = input("Command: ")
        if cmd == "1":
            print("Show all Products")
        elif cmd == "2":
            print("Search")
        elif cmd == "3":
            print("Add a Product")
        elif cmd == "4":
            print("Update a Product")
        elif cmd == "5":
            print("Delete a Product")
        elif cmd == "6":
            print("Sort")
        elif cmd == "7":
            print("Data Analysis")
        elif cmd == "8":
            menu_level = "1"
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
            print_menu(menu_level)
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
        elif cmd == "3":
            print("Add an order")
        elif cmd == "4":
            print("Update an order")
        elif cmd == "5":
            print("Delete an order")
        elif cmd == "6":
            menu_level = "1.3.2"
            print_menu(menu_level)
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
        elif cmd == "7":
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

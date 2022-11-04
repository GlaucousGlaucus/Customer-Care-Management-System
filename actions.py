import time
from colorama import Fore
from datetime import datetime

import pandas as pd
import numpy as np

from helpfultools import *


# ----------------------------------------------------------------------------------------------------

def add_a_Customer(customers: pd.DataFrame, register=False):
    # TODO: Formatting
    if not register:
        print(Fore.CYAN +
              """
                    ╔═╗╔╦╗╔╦╗  ╔═╗  ╔═╗╦ ╦╔═╗╔╦╗╔═╗╔╦╗╔═╗╦═╗
                    ╠═╣ ║║ ║║  ╠═╣  ║  ║ ║╚═╗ ║ ║ ║║║║║╣ ╠╦╝
                    ╩ ╩═╩╝═╩╝  ╩ ╩  ╚═╝╚═╝╚═╝ ╩ ╚═╝╩ ╩╚═╝╩╚═
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
""" + Fore.RESET)
    id = customers.sort_index().index[::-1][0] + 1
    cls()
    # first_name
    first_name = input(Fore.LIGHTMAGENTA_EX +
                       "Enter First Name: " + Fore.RESET).capitalize()
    while not is_alpha_ws(first_name):
        throw_error('error', *data_error_msgs["first_name"](first_name))
        first_name = input("\n"*5 + Fore.LIGHTMAGENTA_EX +
                           "Enter First Name: " + Fore.RESET)
    cls()
    # last_name
    last_name = input(Fore.LIGHTMAGENTA_EX +
                      "Enter Last Name: " + Fore.RESET).capitalize()
    while not is_alpha_ws(last_name):
        throw_error('error', *data_error_msgs["last_name"](last_name))
        last_name = input("\n"*5 + Fore.LIGHTMAGENTA_EX +
                          "Enter Last Name: " + Fore.RESET)
    cls()
    # DOB
    # Print DOB GUI
    print(dateformat_info)
    dob_check = input(Fore.LIGHTMAGENTA_EX + "Enter Dob: " + Fore.RESET)
    dob = date_decoder(dob_check)
    while dob is None:  # Retake inputs for DOB till its valid
        throw_error('error', *data_error_msgs["dob"](dob_check))
        cls()
        print(dateformat_info)
        dob_check = input(Fore.LIGHTMAGENTA_EX + "Enter Dob: " + Fore.RESET)
        dob = date_decoder(dob_check)
    cls()
    # Gender
    genders = ["male", "female", "m", "f"]
    gender_check = input(Fore.LIGHTMAGENTA_EX +
                         "Enter Gender: " + Fore.RESET).strip().lower()
    gender = "Male" if gender_check in [
        "male", "m"] else "Female" if gender_check in genders else None
    # Verify Gender
    while gender is None:
        throw_error('error', *data_error_msgs["gender"](gender_check))
        gender_check = input(Fore.LIGHTMAGENTA_EX +
                             "Enter Gender: " + Fore.RESET).strip().lower()
        gender = "Male" if gender_check in [
            "male", "m"] else "Female" if gender_check in genders else None
    cls()
    # Address
    address = input(Fore.LIGHTMAGENTA_EX + "Enter Address: " +
                    Fore.RESET)
    cls()
    # Country
    country = input(Fore.LIGHTMAGENTA_EX +
                    "Enter Country: " + Fore.RESET).capitalize()
    while not is_alpha_ws(country):  # Verify country
        throw_error('error', *data_error_msgs["country"](country))
        country = input(Fore.LIGHTMAGENTA_EX +
                        "Enter Country: " + Fore.RESET).capitalize()
    cls()
    # City
    city = input(Fore.LIGHTMAGENTA_EX + "Enter City: " +
                 Fore.RESET).capitalize()
    while not is_alpha_ws(city):  # Verify City
        throw_error('error', *data_error_msgs["city"](city))
        city = input(Fore.LIGHTMAGENTA_EX + "Enter City: " +
                     Fore.RESET).capitalize()
    cls()
    # State
    state = input(Fore.LIGHTMAGENTA_EX + "Enter State: " +
                  Fore.RESET).capitalize()
    while not is_alpha_ws(state):  # Verify state
        throw_error('error', *data_error_msgs["state"](state))
        state = input(Fore.LIGHTMAGENTA_EX + "Enter State: " +
                      Fore.RESET).capitalize()
    cls()
    # Postal code
    pincode = input(Fore.LIGHTMAGENTA_EX + "Enter Pincode: " + Fore.RESET)
    while not pincode.isdigit():  # Verify pincode
        throw_error(
            'error', *data_error_msgs["pincode"](pincode))
        pincode = input(Fore.LIGHTMAGENTA_EX + "Enter Pincode: " + Fore.RESET)
    pincode = int(pincode)
    cls()
    # Phone
    print(phone_format_info)
    phone = input(Fore.LIGHTMAGENTA_EX + "Enter Phone: " + Fore.RESET)
    phone_check = phone_validator(phone)
    while not phone_check:  # Verify phone
        cls()
        throw_error('error', *data_error_msgs["phone"](phone))
        cls()
        print(phone_format_info)
        phone = input("\n"*5 + Fore.LIGHTMAGENTA_EX +
                      "Enter Phone: " + Fore.RESET)
        phone_check = phone_validator(phone)
    phone = phone_check
    cls()

    # Email
    print(email_format_info)
    email = input(Fore.LIGHTMAGENTA_EX + "Enter Email: " + Fore.RESET)
    while not validate_email(email):  # Verify email
        throw_error('error', *data_error_msgs["email"](email))
        cls()
        print(email_format_info)
        email = input("\n"*5 + Fore.LIGHTMAGENTA_EX +
                      "Enter Email: " + Fore.RESET)
    cls()
    # Prime
    prime = "PRIME" if input(Fore.LIGHTMAGENTA_EX + "Enter Prime: " + Fore.RESET).lower() in [
        "prime","yes", "p", "y", "oui"] else "NOT PRIME"
    # Password
    if register:
        password = input(Fore.LIGHTMAGENTA_EX + "Enter Password: " + Fore.RESET)
    else:
        password = np.nan
    # Data Summmarization
    NewData = [first_name, last_name, dob,
               gender, address, country, city, state, pincode,
               phone, email, prime, password]
    if all(NewData):
        print(f"""{Fore.CYAN}
                                    ╔═╗╔═╗╔╗╔╔═╗╦╦═╗╔╦╗  ╔╦╗╔═╗╔╦╗╔═╗
                                    ║  ║ ║║║║╠╣ ║╠╦╝║║║   ║║╠═╣ ║ ╠═╣
                                    ╚═╝╚═╝╝╚╝╚  ╩╩╚═╩ ╩  ═╩╝╩ ╩ ╩ ╩ ╩
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
            ID          :    {Fore.LIGHTMAGENTA_EX}{id        }{Fore.CYAN}
            First Name  :    {Fore.LIGHTMAGENTA_EX}{first_name}{Fore.CYAN}
            Last Name   :    {Fore.LIGHTMAGENTA_EX}{last_name }{Fore.CYAN}
            DOB         :    {Fore.LIGHTMAGENTA_EX}{dob       }{Fore.CYAN}
            Gender      :    {Fore.LIGHTMAGENTA_EX}{gender    }{Fore.CYAN}
            Address     :    {Fore.LIGHTMAGENTA_EX}{address   }{Fore.CYAN}
            Country     :    {Fore.LIGHTMAGENTA_EX}{country   }{Fore.CYAN}
            City        :    {Fore.LIGHTMAGENTA_EX}{city      }{Fore.CYAN}
            State       :    {Fore.LIGHTMAGENTA_EX}{state     }{Fore.CYAN}
            Pincode     :    {Fore.LIGHTMAGENTA_EX}{pincode   }{Fore.CYAN}
            Phone       :    {Fore.LIGHTMAGENTA_EX}{phone     }{Fore.CYAN}
            E-mail      :    {Fore.LIGHTMAGENTA_EX}{email     }{Fore.CYAN}
            Prime       :    {Fore.LIGHTMAGENTA_EX}{prime     }{Fore.CYAN}

▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
    """+Fore.RESET)
        if not register:
            reck = input(
                f"Would you like to insert this data to {Fore.GREEN}Customers.csv{Fore.RESET} ? (Y/N): ")
        else:
            reck = input(
                "Would you like to complete Registration ? (Y/N): ").strip().lower()
        if reck in "y1":
            customers.loc[id] = NewData
            SaveData(customers, "Customers")
            print(
                "Record inserted successfully!" if not register else "Registerd Successfully!")
        else:
            print(
                "Record Insertion Cancelled :(" if not register else "Registration Cancelled :(")
        time.sleep(1)
        pause()
    else:
        throw_error('error', f"Invalid Data",
                    'The data is invalid, please try again.')


update_customer_menu = {
    "1": "id",
    "2": "first_name",
    "3": "last_name",
    "4": "dob",
    "5": "gender",
    "6": "address",
    "7": "country",
    "8": "city",
    "9": "state",
    "10": "pincode",
    "11": "phone",
    "12": "email",
    "13": "prime"}


def update_customer(customers: pd.DataFrame):
    cls()
    id = safe_input(Fore.CYAN + "Customer ID To Update: " + Fore.RESET)
    if id not in customers.index:
        throw_error('error', "ID not found: " + str(id),
                    "Customer ID was not found in the database.\nPlease make sure you have entered a valid Customer ID.")
    else:
        sel_rec = customers.loc[id]
        print(Fore.CYAN + "This is the selected Record: \n" +
              Fore.RESET, sel_rec, sep="")
        pause()
        cls()
        while True:
            cls()
            print(Fore.CYAN +
                  f"""
                                                    ╔╦╗╔═╗╔╦╗╦╔═╗╦ ╦  ╔╦╗╔═╗╔╦╗╔═╗
                                                    ║║║║ ║ ║║║╠╣ ╚╦╝   ║║╠═╣ ║ ╠═╣
                                                    ╩ ╩╚═╝═╩╝╩╚   ╩   ═╩╝╩ ╩ ╩ ╩ ╩
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
                                
                                                 Selected ID:{Fore.RED} {id}{Fore.RESET}

                                    1) id               4) dob          7) country      10) pincode
                                    2) first_name       5) gender       8) city         11) phone  
                                    3) last_name        6) address      9) state        12) email  

                                              13) prime                       14) Back{Fore.CYAN}  

▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀                       
            """ + Fore.RESET)
            cmd = input(Fore.CYAN + "Choose To Modify: " + Fore.RESET)
            if cmd == "1":
                print(
                    Fore.CYAN + f"Updating Value of {Fore.RED}{update_customer_menu[cmd]}" + Fore.RESET)
                print(Fore.CYAN +
                      f"Old value of {update_customer_menu[cmd]}: {Fore.RED} {sel_rec.name}" + Fore.RESET)
                new_val = safe_input(
                    Fore.CYAN + "Enter your new value: " + Fore.RESET)
                if new_val not in customers.index:
                    customers.rename(
                        index={sel_rec.name: new_val}, inplace=True)
                    print("ID changed successfully")
                    id = new_val
                    sel_rec = customers.loc[id]
                else:
                    throw_error('error', f'Invalid customer ID: {new_val}', f"""Error while updating Value of id
Make sure that you have avoided any of the following errors:

    1. Invalid value for id i.e. worng format or data type.
    2. Empty value for id
    3. New Value is less than 3 characters.
    4. Not a duplicate value
                """)
            elif cmd == "14":
                break
            elif cmd in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]:
                d_type = update_customer_menu[cmd]
                print(Fore.CYAN +
                      f"Updating Value of {Fore.RED}{d_type}{Fore.CYAN}")
                print(
                    f"Old value of {d_type}: {Fore.RED}{sel_rec.loc[d_type]}{Fore.CYAN}\n\n")
                pause()
                cls()
                if cmd == "4":
                    print(dateformat_info)
                elif cmd == "11":
                    print(phone_format_info)
                elif cmd == "12":
                    print(email_format_info)
                new_val = input(f"\nEnter your new value: {Fore.RED}")
                print(f"{Fore.CYAN}Your new value for {d_type}: " +
                      Fore.RED, new_val, Fore.RESET)
                new_data = data_validator_customer(new_val, d_type)
                if new_data:
                    if input(f"{Fore.CYAN}Do you want to change the value of {Fore.RED}{d_type}?{Fore.RESET} (Y/N) ").strip().lower() in "y1":
                        customers.at[id, d_type] = new_data
                        SaveData(customers, "Customers")
                    else:
                        print("\nUpdating value cancelled.")
                        pause()
                else:
                    throw_error('error', *data_error_msgs[d_type])
                sel_rec = customers.loc[id]


def delete_customer(customers: pd.DataFrame):
    cls()
    id = safe_input(f"{Fore.CYAN}Enter the customer ID to delete: {Fore.RESET}")
    # Check if id is in the df
    if id not in customers.index:
        throw_error("error", "Customer ID is not in the Database",
                    "Please make sure if the ID you have entered is correct")
    else:
        sel_rec = customers.loc[id]
        print(
            f"{Fore.CYAN}The record to be deleted is shown below:{Fore.RESET} \n{sel_rec}")
        confirm_check = "ADMIN#" + \
            sel_rec["first_name"]+"_" + sel_rec["last_name"]
        confirm = input(
            f"{Fore.RED}Are you sure you want to delete this record ? \nThis action will not reversible!\nType {Fore.CYAN}{confirm_check}{Fore.RED} to Proceed: {Fore.RESET}")
        if confirm != confirm_check:
            print(f"{Fore.CYAN}\n\nRecord deletion cancelled{Fore.RESET}")
        else:
            customers.drop(id, inplace=True)
            print(f"{Fore.CYAN}\n\nRecord deleted successfully {Fore.RESET}")
            SaveData(customers, "Customers")
        pause()


# -----------------------------------------------------------------------------------------------------

def add_a_Product(products: pd.DataFrame):
    print(Fore.CYAN + 
        """
                       ╔═╗╔╦╗╔╦╗  ╔═╗  ╔═╗╦═╗╔═╗╔╦╗╦ ╦╔═╗╔╦╗
                       ╠═╣ ║║ ║║  ╠═╣  ╠═╝╠╦╝║ ║ ║║║ ║║   ║ 
                       ╩ ╩═╩╝═╩╝  ╩ ╩  ╩  ╩╚═╚═╝═╩╝╚═╝╚═╝ ╩ 
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
""" + Fore.RESET)
    id = products.sort_index().index[::-1][0] + 1
    cls()
    # name
    name = input(Fore.LIGHTMAGENTA_EX +
                 "Enter Product Name: " + Fore.RESET).capitalize()
    while not is_alpha_ws(name):
        throw_error('error', "Invalid Name")
        name = input("\n"*5 + Fore.LIGHTMAGENTA_EX +
                     "Enter Product Name: " + Fore.RESET)
    cls()
    # manufacturer
    manufacturer = input(Fore.LIGHTMAGENTA_EX +
                         "Enter manufacturer: " + Fore.RESET).capitalize()
    while not is_alpha_ws(manufacturer):
        throw_error('error', "Invalid manufacturer name")
        manufacturer = input("\n"*5 + Fore.LIGHTMAGENTA_EX +
                             "Enter manufacturer: " + Fore.RESET)
    cls()
    # category
    category = input(Fore.LIGHTMAGENTA_EX +
                     "Enter Category: " + Fore.RESET).capitalize()
    while not is_alpha_ws(category):
        throw_error('error', "Invalid Category")
        category = input("\n"*5 + Fore.LIGHTMAGENTA_EX +
                         "Enter Category: " + Fore.RESET)
    cls()
    # Returnable
    Returnables = ["Returnable", "Not Returnable", "Exchange-Only"]
    Returnables_check = input(Fore.LIGHTMAGENTA_EX +
                              "\nReturnable -> 1\nNot Returnable -> 2\nExchange-Only -> 3\nEnter Returnable: " + Fore.RESET).strip().lower().title()
    Returnable = None
    # Verify Returnable
    while Returnable is None:
        try:
            Returnable = Returnables[int(Returnables_check)-1]
            break
        except Exception as e:
            throw_error('error', f"Invalid Returnable: {Returnable}")
            Returnables_check = input(Fore.LIGHTMAGENTA_EX +
                                      "\nReturnable -> 1\nNot Returnable -> 2\nExchange-Only -> 3\nEnter Returnable: " + Fore.RESET).strip().lower().title()
    cls()
    # In-Stock
    stock = input(Fore.LIGHTMAGENTA_EX + "Enter In-Stock: " + Fore.RESET)
    while not stock.isdigit():
        throw_error(
            'error', f"Invalid stock number: {stock}")
        stock = input(Fore.LIGHTMAGENTA_EX + "Enter In-Stock: " + Fore.RESET)
    cls()
    # AvgRating
    avg_rating = input(Fore.LIGHTMAGENTA_EX + "Enter AvgRating: " + Fore.RESET)
    while type(avg_rating) != float:
        try:
            avg_rating = float(avg_rating)
        except Exception as e:
            throw_error(
                'error', f"Invalid Average Rating: {avg_rating}")
            avg_rating = input(Fore.LIGHTMAGENTA_EX +
                               "Enter AvgRating: " + Fore.RESET)
    cls()
    # Days to Return
    if Returnable != "Not Returnable":
        dtr = input(Fore.LIGHTMAGENTA_EX +
                    "Enter Days to Return: " + Fore.RESET)
        while type(dtr) != int:
            try:
                dtr = int(dtr)
                break
            except Exception as e:
                throw_error(
                    'error', f"Invalid Days to Return: {dtr}")
                print("Return", Returnable)
                dtr = input(Fore.LIGHTMAGENTA_EX +
                            "Enter Days to Return: " + Fore.RESET)
    else:
        dtr = "-"
    # Data Summmarization
    NewData = [name, manufacturer, category,
               Returnable, stock, avg_rating, dtr]
    if all(NewData):
        print(f"""{Fore.CYAN}
                                    ╔═╗╔═╗╔╗╔╔═╗╦╦═╗╔╦╗  ╔╦╗╔═╗╔╦╗╔═╗
                                    ║  ║ ║║║║╠╣ ║╠╦╝║║║   ║║╠═╣ ║ ╠═╣
                                    ╚═╝╚═╝╝╚╝╚  ╩╩╚═╩ ╩  ═╩╝╩ ╩ ╩ ╩ ╩
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
            ID              :    {Fore.LIGHTMAGENTA_EX}{id          }{Fore.CYAN}
            Name            :    {Fore.LIGHTMAGENTA_EX}{name        }{Fore.CYAN}
            Manufacturer    :    {Fore.LIGHTMAGENTA_EX}{manufacturer}{Fore.CYAN}
            Category        :    {Fore.LIGHTMAGENTA_EX}{category    }{Fore.CYAN}
            Returnable      :    {Fore.LIGHTMAGENTA_EX}{Returnable  }{Fore.CYAN}
            Stock           :    {Fore.LIGHTMAGENTA_EX}{stock       }{Fore.CYAN}
            Avg_rating      :    {Fore.LIGHTMAGENTA_EX}{avg_rating  }{Fore.CYAN}
            Days to Return  :    {Fore.LIGHTMAGENTA_EX}{dtr         }{Fore.CYAN}

▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
    {Fore.RESET}""")
        reck = input(
            f"Would you like to insert this data to {Fore.LIGHTCYAN_EX}Products.csv{Fore.RESET} ? (Y/N): ").strip().lower()
        if reck in "y1":
            products.loc[id] = NewData
            SaveData(products, "Products")
            print("Record inserted successfully!")
        else:
            print("Record Insertion Cancelled :(")
        time.sleep(1)
        pause()
    else:
        throw_error('error', f"Invalid Data",
                    'The data is invalid, please try again.')


def delete_product(products: pd.DataFrame):
    cls()
    id = safe_input(f"{Fore.CYAN}Enter the product ID to delete: {Fore.RESET}")
    # Check if id is in the df
    if id not in products.index:
        throw_error("error", "Product ID is not in the Database",
                    "Please make sure if the ID you have entered is correct")
    else:
        sel_rec = products.loc[id]
        print(
            f"{Fore.CYAN}The record to be deleted is shown below:{Fore.RESET} \n{sel_rec}")
        confirm_check = "ADMIN#" + id[len(id)-3:]
        confirm = input(
            f"{Fore.RED}Are you sure you want to delete this record ? \nThis action will not reversible!\nType {Fore.CYAN}{confirm_check}{Fore.RED} to Proceed: {Fore.RESET}")
        if confirm != confirm_check:
            print(f"{Fore.CYAN}\n\nRecord deletion cancelled{Fore.RESET}")
        else:
            products.drop(id, inplace=True)
            print(f"{Fore.CYAN}\n\nRecord deleted successfully {Fore.RESET}")
        SaveData(products, "Products")
        pause()


update_product_menu = {
    "1": "id",
    "2": "name",
    "3": "manufacturer",
    "4": "category",
    "5": "In-Stock",
    "6": "AvgRating",
    "7": "Returnable",
    "8": "DaysToReturn",
    "9": "Back"
}


def update_product(products: pd.DataFrame):
    cls()
    id = safe_input(Fore.CYAN + "Product ID To Update: " + Fore.RESET)
    if id not in products.index:
        throw_error('error', "ID not found: " + str(id),
                    "Product ID was not found in the database.\nPlease make sure you have entered a valid Product ID.")
        print(products.index)
    else:
        sel_rec = products.loc[id]
        print(Fore.CYAN + "This is the selected Record: \n" +
              Fore.RESET, sel_rec, sep="")
        pause()
        cls()
        while True:
            cls()
            print(Fore.CYAN +
                  f"""
                                                ╔╦╗╔═╗╔╦╗╦╔═╗╦ ╦  ╔╦╗╔═╗╔╦╗╔═╗
                                                ║║║║ ║ ║║║╠╣ ╚╦╝   ║║╠═╣ ║ ╠═╣
                                                ╩ ╩╚═╝═╩╝╩╚   ╩   ═╩╝╩ ╩ ╩ ╩ ╩
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
                                            
                                            Selected ID:{Fore.RED} {id}{Fore.RESET}

                            1) id                       4) category               7) Returnable   
                            2) name                     5) In-Stock               8) Days to Return
                            3) manufacturer             6) AvgRating              9) Back{Fore.CYAN}     
                    
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀                
            """ + Fore.RESET)
            cmd = input(Fore.CYAN + "Choose To Modify: " + Fore.RESET)
            if cmd == "1":
                print(
                    Fore.CYAN + f"Updating Value of {Fore.RED}{update_product_menu[cmd]}" + Fore.RESET)
                print(Fore.CYAN +
                      f"Old value of {update_product_menu[cmd]}: {Fore.RED} {sel_rec.name}" + Fore.RESET)
                new_val = safe_input(
                    Fore.CYAN + "Enter your new value: " + Fore.RESET)
                if new_val not in products.index:
                    products.rename(
                        index={sel_rec.name: new_val}, inplace=True)
                    print("ID changed successfully")
                    id = new_val
                    sel_rec = products.loc[id]
                else:
                    throw_error('error', f'Invalid product ID: {new_val}')
            elif cmd == "9":
                break
            elif cmd in ["2", "3", "4", "5", "6", "7", "8"]:
                d_type = update_product_menu[cmd]
                print(Fore.CYAN +
                      f"Updating Value of {Fore.RED}{d_type}{Fore.CYAN}")
                print(
                    f"Old value of {d_type}: {Fore.RED}{sel_rec.loc[d_type]}{Fore.CYAN}")
                if d_type == "Returnable":
                    print(
                        Fore.CYAN + "Use the index to fill the entries:\nReturnable -> 1\nNot Returnable -> 2\nExchange-Only -> 3" + Fore.RESET)
                new_val = input(f"Enter your new value: {Fore.RED}")
                if d_type == "Returnable":
                    try:
                        new_val = ["Returnable", "Not Returnable",
                                   "Exchange-Only"][int(new_val)-1]
                    except ValueError:
                        throw_error('error', 'Error while updating product data',
                                    "Please make sure you have entered the correct details.")
                        continue
                print(f"{Fore.CYAN}Your new value for {d_type}: " +
                      Fore.RED, new_val, Fore.RESET)
                if data_validator_product_bool(products, id, new_val, d_type):
                    if input(f"{Fore.CYAN}Do you want to change the value of {Fore.RED}{d_type}?{Fore.RESET} (Y/N) ").lower() in "y1":
                        products.at[id, d_type] = new_val
                        if d_type == "Returnable" and new_val == "Not Returnable":
                            products.at[id, "DaysToReturn"] = "-"
                        SaveData(products, "Products")
                    else:
                        print("\nUpdating value cancelled.")
                        pause()
                else:
                    throw_error('error', 'Error while updating product data',
                                "Please make sure you have entered the correct details.")
                sel_rec = products.loc[id]

# ----------------------------------------------------------------------------------------------------


def add_an_order(customers: pd.DataFrame, products: pd.DataFrame, orders: pd.DataFrame):
    print(Fore.CYAN +
          """
                          ╔═╗╔╦╗╔╦╗  ╔═╗╔╗╔  ╔═╗╦═╗╔╦╗╔═╗╦═╗
                          ╠═╣ ║║ ║║  ╠═╣║║║  ║ ║╠╦╝ ║║║╣ ╠╦╝
                          ╩ ╩═╩╝═╩╝  ╩ ╩╝╚╝  ╚═╝╩╚══╩╝╚═╝╩╚═
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
""" + Fore.RESET)
    # OrderID
    orderId = orders.sort_index().index[::-1][0] + 1
    cls()

    # CustomerID
    customerID = safe_input(Fore.LIGHTMAGENTA_EX +
                       "Enter Customer ID: " + Fore.RESET)
    while customerID not in customers.index:
        throw_error('error', "Customer ID not found!")
        customerID = safe_input(Fore.LIGHTMAGENTA_EX +
                           "Enter Customer ID: " + Fore.RESET)
    cls()
    # ProductID
    productID = safe_input(Fore.LIGHTMAGENTA_EX +
                      "Enter Product ID: " + Fore.RESET)
    while productID not in products.index:
        throw_error('error', "Product ID not found!")
        productID = safe_input(Fore.LIGHTMAGENTA_EX +
                          "Enter Product ID: " + Fore.RESET)
    cls()

    # Qty
    qty = input(Fore.LIGHTMAGENTA_EX +
                "Enter Quantity: " + Fore.RESET)
    while not qty.isdigit():
        throw_error('error', "Invalid value for quantity: " + qty)
        qty = input(Fore.LIGHTMAGENTA_EX +
                    "Enter Quantity: " + Fore.RESET)
    cls()

    # Price
    price = input(Fore.LIGHTMAGENTA_EX + "Enter Price: " + Fore.RESET)
    while type(price) != float:
        try:
            price = float(price)
        except Exception as e:
            throw_error(
                'error', "Invalid Price: %s" % price)
            price = input(Fore.LIGHTMAGENTA_EX +
                          "Enter Price: " + Fore.RESET)
    total_price = int(qty) * price
    cls()

    # DOO
    # Print DOO GUI
    print(dateformat_info)
    doo_check = input(Fore.LIGHTMAGENTA_EX +
                      "Enter Date of Order: " + Fore.RESET)
    doo = date_decoder(doo_check)
    while doo is None:  # Retake inputs for DOB till its valid
        throw_error('error', *data_error_msgs["dob"](doo_check))
        cls()
        print(dateformat_info)
        doo_check = input(Fore.LIGHTMAGENTA_EX +
                          "Enter Date of Order: " + Fore.RESET)
        doo = date_decoder(doo_check)
    cls()

    # Status
    States = ["Cancelled", "Delivered", "Pending", "Pre-Shipment", "Unshipped"]
    States_check = input(Fore.LIGHTMAGENTA_EX +
                         """==== STATUS LIST ====
1)  Cancelled
2)  Delivered
3)  Pending
4)  Pre-Shipment
5)  Unshipped
""" + Fore.RESET).strip().lower().title()
    State = None
    # Verify State
    while State is None:
        try:
            State = States[int(States_check)-1]
            break
        except Exception as e:
            throw_error('error', "Invalid State: %s" % State)
            States_check = input(Fore.LIGHTMAGENTA_EX +
                                 """==== STATUS LIST ====
1)  Cancelled
2)  Delivered
3)  Pre-Shipment
4)  Unshipped
""" + Fore.RESET).strip().lower().title()
    # Get Customer and Product data
    cust = customers.loc[customerID]
    cust_first_name = cust["first_name"]
    cust_last_name = cust["last_name"]
    cust_address = cust["address"]

    prod = products.loc[productID]
    prod_name = prod["name"]
    # Data Summmarization
    NewData = [customerID, cust_first_name, cust_last_name, productID, prod_name, qty,
               total_price, doo, State, cust_address]
    if all(NewData):
        print(f"""{Fore.CYAN}
                                    ╔═╗╔═╗╔╗╔╔═╗╦╦═╗╔╦╗  ╔╦╗╔═╗╔╦╗╔═╗
                                    ║  ║ ║║║║╠╣ ║╠╦╝║║║   ║║╠═╣ ║ ╠═╣
                                    ╚═╝╚═╝╝╚╝╚  ╩╩╚═╩ ╩  ═╩╝╩ ╩ ╩ ╩ ╩
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
            OrderID               :    {Fore.LIGHTMAGENTA_EX}{orderId           }{Fore.CYAN}
            CustomerID            :    {Fore.LIGHTMAGENTA_EX}{customerID        }{Fore.CYAN}
            Customer (First Name) :    {Fore.LIGHTMAGENTA_EX}{cust_first_name   }{Fore.CYAN}
            Customer (Last Name)  :    {Fore.LIGHTMAGENTA_EX}{cust_last_name    }{Fore.CYAN}
            ProductID             :    {Fore.LIGHTMAGENTA_EX}{productID         }{Fore.CYAN}
            Product Name          :    {Fore.LIGHTMAGENTA_EX}{prod_name         }{Fore.CYAN}
            Quantity              :    {Fore.LIGHTMAGENTA_EX}{qty               }{Fore.CYAN}
            Total Price           :    {Fore.LIGHTMAGENTA_EX}{total_price       }{Fore.CYAN}
            Date Of Order         :    {Fore.LIGHTMAGENTA_EX}{doo               }{Fore.CYAN}
            Status                :    {Fore.LIGHTMAGENTA_EX}{State             }{Fore.CYAN}
            Address               :    {Fore.LIGHTMAGENTA_EX}{cust_address      }{Fore.CYAN}

▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
    {Fore.RESET}""")
        reck = input(
            f"Would you like to insert this data to {Fore.LIGHTGREEN_EX}Orders.csv{Fore.RESET} ? (Y/N): ").strip().lower()
        if reck in "y1":
            orders.loc[orderId] = NewData
            print("Record inserted successfully!")
            SaveData(orders, "Orders")
        else:
            print("Record Insertion Cancelled :(")
        time.sleep(1)
        pause()
    else:
        throw_error('error', f"Invalid Data",
                    'The data is invalid, please try again.')


def delete_order(orders: pd.DataFrame):
    cls()
    id = safe_input(f"{Fore.CYAN}Enter the order ID to delete: {Fore.RESET}")
    # Check if id is in the df
    if id not in orders.index:
        throw_error("error", "Order ID is not in the Database",
                    "Please make sure if the ID you have entered is correct")
    else:
        sel_rec = orders.loc[id]
        print(
            f"{Fore.CYAN}The record to be deleted is shown below:{Fore.RESET} \n{sel_rec}")
        confirm_check = "ADMIN#" + id[len(id)-3:]
        confirm = input(
            f"{Fore.RED}Are you sure you want to delete this record ? \nThis action will not reversible!\nType {Fore.CYAN}{confirm_check}{Fore.RED} to Proceed: {Fore.RESET}")
        if confirm != confirm_check:
            print(f"{Fore.CYAN}\n\nRecord deletion cancelled{Fore.RESET}")
        else:
            orders.drop(id, inplace=True)
            print(f"{Fore.CYAN}\n\nRecord deleted successfully {Fore.RESET}")
        SaveData(orders, "Orders")
        pause()


update_order_menu = {
    "1": "orderId",
    "2": "customerID",
    "3": "productID",
    "4": "qty",
    "5": "total_price",
    "6": "doo",
    "7": "State",
    "8": "Back"
}


def update_order(customers: pd.DataFrame, products: pd.DataFrame, orders: pd.DataFrame):
    cls()
    id = safe_input(Fore.CYAN + "Order ID To Update: " + Fore.RESET)
    if id not in orders.index:
        throw_error('error', "ID not found: " + str(id),
                    "Order ID was not found in the database.\nPlease make sure you have entered a valid Order ID.")
        print(orders.index)
    else:
        sel_rec = orders.loc[id]
        print(Fore.CYAN + "This is the selected Record: \n" +
              Fore.RESET, sel_rec, sep="")
        pause()
        cls()
        while True:
            cls()
            print(Fore.CYAN +
                  f"""
                                                    ╔╦╗╔═╗╔╦╗╦╔═╗╦ ╦  ╔╦╗╔═╗╔╦╗╔═╗
                                                    ║║║║ ║ ║║║╠╣ ╚╦╝   ║║╠═╣ ║ ╠═╣
                                                    ╩ ╩╚═╝═╩╝╩╚   ╩   ═╩╝╩ ╩ ╩ ╩ ╩
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
                              
                                              Selected ID:{Fore.RED} {id}{Fore.RESET}

                                           1)  orderId                         4)  qty
                                           2)  customerID                      5)  total_price
                                           3)  productID                       6)  doo
                                                        
                                                    7)  State       8)  Back{Fore.CYAN}

▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
            {Fore.RESET}""")
            cmd = input(Fore.CYAN + "Choose To Modify: " + Fore.RESET)
            if cmd == "1":
                print(
                    Fore.CYAN + f"Updating Value of {Fore.RED}{update_order_menu[cmd]}" + Fore.RESET)
                print(Fore.CYAN +
                      f"Old value of {update_order_menu[cmd]}: {Fore.RED} {sel_rec.name}" + Fore.RESET)
                new_val = safe_input(
                    Fore.CYAN + "Enter your new value: " + Fore.RESET)
                if new_val not in orders.index:
                    orders.rename(
                        index={sel_rec.name: new_val}, inplace=True)
                    print("ID changed successfully")
                    id = new_val
                    sel_rec = orders.loc[id]
                else:
                    throw_error('error', f'Invalid order ID: {new_val}')
            elif cmd == "8":
                break
            elif cmd in "234567":
                d_type = update_order_menu[cmd]
                print(Fore.CYAN +
                      f"Updating Value of {Fore.RED}{d_type}{Fore.CYAN}")
                print(
                    f"Old value of {d_type}: {Fore.RED}{sel_rec[d_type]}{Fore.CYAN}")
                new_val = input(f"Enter your new value: {Fore.RED}") if d_type not in ["orderId", "customerID", "products"] else safe_input(f"Enter your new value: {Fore.RED}")
                print(f"{Fore.CYAN}Your new value for {d_type}: " +
                      Fore.RED, new_val, Fore.RESET)
                if data_validator_order_bool(customers, products,  orders, id, new_val, d_type):
                    if input(f"{Fore.CYAN}Do you want to change the value of {Fore.RED}{d_type}?{Fore.RESET} (Y/N) ").lower() in "y1":
                        orders.at[id, d_type] = new_val
                        if d_type == "customerID":
                            cust = customers.loc[new_val]
                            orders.at[id,
                                      "customerFirstName"] = cust["first_name"]
                            orders.at[id, "customerLastName"] = cust["last_name"]
                            orders.at[id, "address"] = cust["address"]
                        elif d_type == "productID":
                            prod = products.loc[new_val]
                            orders.at[id, "productName"] = prod["name"]
                            SaveData(orders, "Orders")
                    else:
                        print("\nUpdating value cancelled.")
                        pause()
                else:
                    throw_error('error', 'Error while updating order data',
                                "Please make sure you have entered the correct details.")
                sel_rec = orders.loc[id]

# ----------------------------------------------------------------------------------------------------


def add_a_ticket(customers: pd.DataFrame, products: pd.DataFrame, orders: pd.DataFrame, tickets: pd.DataFrame, custid=None, register=False):
    print(Fore.CYAN +
          """
                       ╔═╗╔╦╗╔╦╗  ╔═╗  ╔╦╗╦╔═╗╦╔═╔═╗╔╦╗
                       ╠═╣ ║║ ║║  ╠═╣   ║ ║║  ╠╩╗║╣  ║ 
                       ╩ ╩═╩╝═╩╝  ╩ ╩   ╩ ╩╚═╝╩ ╩╚═╝ ╩ 
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
""" + Fore.RESET)
    # TicketID
    ticketID = tickets.sort_index().index[::-1][0] + 1

    # CustID
    if register:
        CustID = custid
    else:
        CustID = safe_input(Fore.LIGHTMAGENTA_EX +
                       "Enter Customer ID: " + Fore.RESET)
        while CustID not in customers.index:
            throw_error('error', "Customer ID not found!")
            CustID = safe_input(Fore.LIGHTMAGENTA_EX +
                           "Enter Customer ID: " + Fore.RESET)
    cls()
    # OrderID
    OrderID = safe_input(Fore.LIGHTMAGENTA_EX +
                    "Enter Order ID: " + Fore.RESET)
    while (OrderID not in orders.index) or (orders.loc[OrderID]["customerID"] != custid):
        throw_error('error', "Order ID not found!")
        OrderID = safe_input(Fore.LIGHTMAGENTA_EX +
                        "Enter Order ID: " + Fore.RESET)
    cls()

    # Issue Category & Issue
    issueCategory = input(Fore.LIGHTMAGENTA_EX + "Enter Issue Category: " +
                          Fore.RESET)
    issue = input(Fore.LIGHTMAGENTA_EX + "Enter Issue: " +
                  Fore.RESET)

    # Date of Open
    if not register:
        print(datetimeformat_info)
        do_check = input(Fore.LIGHTMAGENTA_EX +
                         "Enter Date Opened: " + Fore.RESET)
        if do_check != "now":
            do = date_decoder(do_check, time=True)
            while do is None:  # Retake inputs for DOB till its valid
                throw_error('error', *data_error_msgs["dob"](do_check))
                cls()
                print(datetimeformat_info)
                do_check = input(Fore.LIGHTMAGENTA_EX +
                                 "Enter Date of Opened: " + Fore.RESET)
                do = date_decoder(do_check, time=True)
        else:
            do = pd.to_datetime(datetime.now())
    else:
        do = pd.to_datetime(datetime.now())
    cls()

    # Date of Closed
    if not register:
        print(datetimeformat_info)
        doc_check = input(Fore.LIGHTMAGENTA_EX +
                          "Enter Date Closed: " + Fore.RESET)
        doc = date_decoder(doc_check, time=True)
        while (doc is None and doc_check != "-"):  # Retake inputs for DOB till its valid
            throw_error('error', *data_error_msgs["dob"](doc_check))
            cls()
            print(datetimeformat_info)
            doc_check = input(Fore.LIGHTMAGENTA_EX +
                              "Enter Date Closed: " + Fore.RESET)
            doc = date_decoder(doc_check, time=True)
        if doc_check == "-":
            doc = np.NaN
        cls()

        # FRT
        frt = input(Fore.LIGHTMAGENTA_EX +
                    "Enter First Response Time: " + Fore.RESET)
        while type(frt) != float:
            try:
                frt = float(frt)
            except Exception as e:
                throw_error(
                    'error', "Invalid Price: %s" % frt)
                frt = input(Fore.LIGHTMAGENTA_EX +
                            "Enter First Response Time: " + Fore.RESET)
        cls()

        # Customer Satisfaction
        custSatis = input(Fore.LIGHTMAGENTA_EX +
                          "Enter Customer Satisfaction: " + Fore.RESET)
        while type(custSatis) != float:
            try:
                custSatis = float(custSatis)
            except Exception as e:
                throw_error(
                    'error', "Invalid Customer Satisfaction: %s" % custSatis)
                custSatis = input(Fore.LIGHTMAGENTA_EX +
                                  "Enter Customer Satisfaction: " + Fore.RESET)
        cls()

        # Replies
        replies = input(Fore.LIGHTMAGENTA_EX +
                        "Enter Replies: " + Fore.RESET)
        while not replies.isdigit():
            throw_error('error', "Invalid value for replies: " + replies)
            replies = input(Fore.LIGHTMAGENTA_EX +
                            "Enter Replies: " + Fore.RESET)
        cls()
    else:
        doc_check = "-"
        replies = custSatis = frt = doc = np.nan

    # Get Customer and Product data
    cust = customers.loc[CustID]
    cust_first_name = cust["first_name"]
    cust_phone = cust["phone"]

    order = orders.loc[OrderID]
    status = "Closed" if doc != "-" else "Open"

    # HoursTaken
    if doc_check == "-":
        hoursTaken = np.NaN
    else:
        res = doc - do
        hoursTaken = res.days * 24

    prod = products.loc[order['productID']]
    prod_name = prod["name"]
    prod_category = prod["category"]
    # Data Summmarization
    NewData = [CustID, OrderID, prod_name, prod_category,
               cust_first_name, cust_phone, status, issueCategory, issue,
               do, doc, hoursTaken, frt, replies, custSatis]
    print("+" + "-"*50 + "+")
    ll = max([len(str(x)) for x in NewData])
    fac = 62 if ll <= 62 else ll
    eq = ll - 62 if ll > 62 else 0
    print(f"""{Fore.CYAN}
                                    ╔═╗╔═╗╔╗╔╔═╗╦╦═╗╔╦╗  ╔╦╗╔═╗╔╦╗╔═╗
                                    ║  ║ ║║║║╠╣ ║╠╦╝║║║   ║║╠═╣ ║ ╠═╣
                                    ╚═╝╚═╝╝╚╝╚  ╩╩╚═╩ ╩  ═╩╝╩ ╩ ╩ ╩ ╩
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
    
                TicketID                 : {Fore.LIGHTMAGENTA_EX}{ticketID}       {Fore.CYAN}
                CustID                   : {Fore.LIGHTMAGENTA_EX}{CustID}         {Fore.CYAN}
                OrderID                  : {Fore.LIGHTMAGENTA_EX}{OrderID}        {Fore.CYAN}
                ProductName              : {Fore.LIGHTMAGENTA_EX}{prod_name}      {Fore.CYAN}
                ProductCategory          : {Fore.LIGHTMAGENTA_EX}{prod_category}  {Fore.CYAN}
                CustFirstName            : {Fore.LIGHTMAGENTA_EX}{cust_first_name}{Fore.CYAN}
                CustPhone                : {Fore.LIGHTMAGENTA_EX}{cust_phone}     {Fore.CYAN}
                Status                   : {Fore.LIGHTMAGENTA_EX}{status}         {Fore.CYAN}
                IssueCategory            : {Fore.LIGHTMAGENTA_EX}{issueCategory}  {Fore.CYAN}
                Issue                    : {Fore.LIGHTMAGENTA_EX}{issue}          {Fore.CYAN}
                DateOpened               : {Fore.LIGHTMAGENTA_EX}{do}             {Fore.CYAN}
                DateClosed               : {Fore.LIGHTMAGENTA_EX}{doc}            {Fore.CYAN}
                HoursTaken               : {Fore.LIGHTMAGENTA_EX}{hoursTaken}     {Fore.CYAN}
                FirstResponseTime        : {Fore.LIGHTMAGENTA_EX}{frt}            {Fore.CYAN}
                Replies                  : {Fore.LIGHTMAGENTA_EX}{replies}        {Fore.CYAN}
                CustomerSatisfaction(%)  : {Fore.LIGHTMAGENTA_EX}{custSatis}      {Fore.CYAN}

▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
    """ + Fore.RESET)
    reck = input(
        f"Would you like to insert this data to {Fore.LIGHTGREEN_EX}Tickets.csv{Fore.RESET} ? (Y/N): ").strip().lower()
    if reck in "y1":
        tickets.loc[ticketID] = NewData
        SaveData(tickets, "Tickets")
        print("Record inserted successfully!")
    else:
        print("Record Insertion Cancelled :(")
    time.sleep(1)
    pause()


def delete_ticket(tickets: pd.DataFrame):
    cls()
    id = safe_input(f"{Fore.CYAN}Enter the ticket ID to delete: {Fore.RESET}")
    # Check if id is in the df
    if id not in tickets.index:
        throw_error("error", "Ticket ID is not in the Database",
                    "Please make sure if the ID you have entered is correct")
    else:
        sel_rec = tickets.loc[id]
        print(
            f"{Fore.CYAN}The record to be deleted is shown below:{Fore.RESET} \n{sel_rec}")
        confirm_check = "ADMIN#" + id[len(id)-3:]
        confirm = input(
            f"{Fore.RED}Are you sure you want to delete this record ? \nThis action will not reversible!\nType {Fore.CYAN}{confirm_check}{Fore.RED} to Proceed: {Fore.RESET}")
        if confirm != confirm_check:
            print(f"{Fore.CYAN}\n\nRecord deletion cancelled{Fore.RESET}")
        else:
            tickets.drop(id, inplace=True)
            print(f"{Fore.CYAN}\n\nRecord deleted successfully {Fore.RESET}")
        SaveData(tickets, "Tickets")
        pause()


update_ticket_menu = {
    "1": "TicketId",
    "2": "CustID",
    "3": "OrderID",
    "4": "Status",
    "5": "IssueCategory",
    "6": "Issue",
    "7": "DateOpened",
    "8": "DateClosed",
    "9": "HoursTaken",
    "10": "FirstResponseTime",
    "11": "Replies",
    "12": "CustomerSatisfaction"
}


def update_ticket(customers: pd.DataFrame, products: pd.DataFrame, orders: pd.DataFrame, tickets: pd.DataFrame, close=False):
    cls()
    id = safe_input(Fore.CYAN + "Ticket ID To Update: " + Fore.RESET)
    if id not in tickets.index:
        throw_error('error', "ID not found: " + str(id),
                    "Ticket ID was not found in the database.\nPlease make sure you have entered a valid Ticket ID.")
        print(tickets.index)
    else:
        sel_rec = tickets.loc[id]
        print(Fore.CYAN + "This is the selected Record: \n" +
              Fore.RESET, sel_rec, sep="")
        pause()
        cls()
        if close:
            tickets.at[id, "Status"] = "Closed"
            tdy = pd.to_datetime(datetime.today())
            tickets.at[id, "DateClosed"] = tdy
            res = tdy - tickets.loc[id]["DateOpened"]
            tickets.at[id, "HoursTaken"] = res.days * 24
            fail_text = "Please Enter on a scale of 1-10"
            interaction = safe_input(
                Fore.LIGHTMAGENTA_EX + "Please rate your experience with us: (Rate them on a scale of 1-10) \nHow was our staff's interaction with you ?" + Fore.RESET, fail_text=fail_text)
            frtt = safe_input(Fore.LIGHTMAGENTA_EX +
                              "Did you recieve the first interaction message from our staff quick ?" + Fore.RESET, fail_text=fail_text)
            theclock = safe_input(Fore.LIGHTMAGENTA_EX +
                                  "How quickly your issue was resolved ?" + Fore.RESET, fail_text=fail_text)
            satis_deter = [interaction, frtt, theclock]
            tickets.at[id, "CustomerSatisfaction(%)"] = round(
                sum(satis_deter)/len(satis_deter)*1000) / 10
            SaveData(tickets, "Tickets")
            return None
        while True:
            cls()
            print(Fore.CYAN +
                  f"""      
                                                   ╔╦╗╔═╗╔╦╗╦╔═╗╦ ╦  ╔╦╗╔═╗╔╦╗╔═╗
                                                   ║║║║ ║ ║║║╠╣ ╚╦╝   ║║╠═╣ ║ ╠═╣
                                                   ╩ ╩╚═╝═╩╝╩╚   ╩   ═╩╝╩ ╩ ╩ ╩ ╩
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
                                            
                                                 Selected ID:{Fore.RED} {id}{Fore.RESET}
        
             1) TicketId         4) Status               7) DateOpened          10) FirstResponseTime
             2) CustID           5) IssueCategory        8) DateClosed          11) Replies
             3) OrderID          6) Issue                9) HoursTaken          12) CustomerSatisfaction
                                                            13) Back{Fore.CYAN}
        
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
            """+Fore.RESET)
            cmd = input(Fore.CYAN + "Choose To Modify: " + Fore.RESET)
            if cmd == "1":
                print(
                    Fore.CYAN + f"Updating Value of {Fore.RED}{update_ticket_menu[cmd]}" + Fore.RESET)
                print(Fore.CYAN +
                      f"Old value of {update_ticket_menu[cmd]}: {Fore.RED} {sel_rec.name}" + Fore.RESET)
                new_val = safe_input(
                    Fore.CYAN + "Enter your new value: " + Fore.RESET)
                if new_val not in tickets.index:
                    tickets.rename(
                        index={sel_rec.name: new_val}, inplace=True)
                    print("ID changed successfully")
                    id = new_val
                    sel_rec = tickets.loc[id]
                else:
                    throw_error('error', f'Invalid order ID: {new_val}')
            elif cmd == "13":
                break
            elif cmd in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]:
                d_type = update_ticket_menu[cmd]
                print(Fore.CYAN +
                      f"Updating Value of {Fore.RED}{d_type}{Fore.CYAN}")
                print(
                    f"Old value of {d_type}: {Fore.RED}{sel_rec.loc[d_type]}{Fore.CYAN}")
                new_val = input(f"Enter your new value: {Fore.RED}")
                print(f"{Fore.CYAN}Your new value for {d_type}: " +
                      Fore.RED, new_val, Fore.RESET)
                if data_validator_ticket_bool(customers, products, orders, tickets, id, new_val, d_type):
                    if input(f"{Fore.CYAN}Do you want to change the value of {Fore.RED}{d_type}?{Fore.RESET} (Y/N) ").lower() in "y1":
                        tickets.at[id, d_type] = new_val
                        if d_type == "CustID":
                            cust = customers.loc[new_val]
                            tickets.at[id,
                                       "CustFirstName"] = cust["first_name"]
                            tickets.at[id, "CustPhone"] = cust["phone"]
                        elif d_type == "OrderID":
                            order = orders.loc[new_val]
                            prod = products.loc[order["productID"]]
                            tickets.at[id, "ProductName"] = prod["name"]
                            tickets.at[id,
                                       "ProductCategory"] = prod["category"]
                    else:
                        print("\nUpdating value cancelled.")
                        pause()
                else:
                    throw_error('error', 'Error while updating order data',
                                "Please make sure you have entered the correct details.")
                sel_rec = tickets.loc[id]
        SaveData(tickets, "Tickets")

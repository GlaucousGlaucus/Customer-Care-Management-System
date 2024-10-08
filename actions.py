import difflib
import time

import numpy as np
import pandas as pd

from util_tools import *


# ----------------------------------------------------------------------------------------------------

def add_a_Customer(customers: pd.DataFrame, register=False):
    # TODO: Formatting
    if not register:
        cls()
        print(Fore.CYAN +
              """
                    ╔═╗╔╦╗╔╦╗  ╔═╗  ╔═╗╦ ╦╔═╗╔╦╗╔═╗╔╦╗╔═╗╦═╗
                    ╠═╣ ║║ ║║  ╠═╣  ║  ║ ║╚═╗ ║ ║ ║║║║║╣ ╠╦╝
                    ╩ ╩═╩╝═╩╝  ╩ ╩  ╚═╝╚═╝╚═╝ ╩ ╚═╝╩ ╩╚═╝╩╚═
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
""" + Fore.RESET)
    customer_id = customers.sort_index().index[::-1][0] + 1
    # first_name
    customer_first_name = input(Fore.LIGHTMAGENTA_EX +
                                "Enter First Name: " + Fore.RESET).capitalize()
    while not is_alpha_whitespace(customer_first_name):
        throw_error('error', *data_error_msgs["first_name"](customer_first_name))
        customer_first_name = input("\n" * 5 + Fore.LIGHTMAGENTA_EX +
                                    "Enter First Name: " + Fore.RESET)
    cls()
    # last_name
    customer_last_name = input(Fore.LIGHTMAGENTA_EX +
                               "Enter Last Name: " + Fore.RESET).capitalize()
    while not is_alpha_whitespace(customer_last_name):
        throw_error('error', *data_error_msgs["last_name"](customer_last_name))
        customer_last_name = input("\n" * 5 + Fore.LIGHTMAGENTA_EX +
                                   "Enter Last Name: " + Fore.RESET)
    cls()
    # DOB
    # Print DOB GUI
    print(dateformat_info)
    date_of_birth_check = input(Fore.LIGHTMAGENTA_EX + "Enter Dob: " + Fore.RESET)
    decoded_date = date_decoder(date_of_birth_check, dob_check=True)
    while decoded_date is None:  # Retake inputs for DOB till its valid
        throw_error('error', *data_error_msgs["dob"](date_of_birth_check))
        cls()
        print(dateformat_info)
        date_of_birth_check = input(Fore.LIGHTMAGENTA_EX + "Enter Dob: " + Fore.RESET)
        decoded_date = date_decoder(date_of_birth_check, dob_check=True)
    cls()
    # Gender
    genders = ["male", "female", "m", "f"]
    gender = None
    # Verify Gender
    while gender is None:
        gender_in = input(Fore.LIGHTMAGENTA_EX +
                          "Enter Gender: " + Fore.RESET).strip().lower()
        gender = "Male" if gender_in in [
            "male", "m"] else "Female" if gender_in in genders else None
        if gender is None:
            throw_error('error', *data_error_msgs["gender"](gender_in))
            continue
    cls()
    # Address
    address = input(Fore.LIGHTMAGENTA_EX + "Enter Address: " +
                    Fore.RESET)
    cls()
    # Country
    country_in = input(Fore.LIGHTMAGENTA_EX +
                       "Enter Country: " + Fore.RESET).capitalize()
    while not is_alpha_whitespace(country_in):  # Verify country
        throw_error('error', *data_error_msgs["country"](country_in))
        country_in = input(Fore.LIGHTMAGENTA_EX +
                           "Enter Country: " + Fore.RESET).capitalize()
    cls()
    # City
    city_in = input(Fore.LIGHTMAGENTA_EX + "Enter City: " +
                    Fore.RESET).capitalize()
    while not is_alpha_whitespace(city_in):  # Verify City
        throw_error('error', *data_error_msgs["city"](city_in))
        city_in = input(Fore.LIGHTMAGENTA_EX + "Enter City: " +
                        Fore.RESET).capitalize()
    cls()
    # State
    state_in = input(Fore.LIGHTMAGENTA_EX + "Enter State: " +
                     Fore.RESET).capitalize()
    while not is_alpha_whitespace(state_in):  # Verify state
        throw_error('error', *data_error_msgs["state"](state_in))
        state_in = input(Fore.LIGHTMAGENTA_EX + "Enter State: " +
                         Fore.RESET).capitalize()
    cls()
    # Postal code
    pincode_in = input(Fore.LIGHTMAGENTA_EX + "Enter Pincode: " + Fore.RESET)
    while not pincode_in.isdigit():  # Verify pincode
        throw_error(
            'error', *data_error_msgs["pincode"](pincode_in))
        pincode_in = input(Fore.LIGHTMAGENTA_EX + "Enter Pincode: " + Fore.RESET)
    pincode_in = int(pincode_in)
    cls()
    # Phone
    print(phone_format_info)
    phone_in = input(Fore.LIGHTMAGENTA_EX + "Enter Phone: " + Fore.RESET)
    phone_check = phone_validator(phone_in)
    while not phone_check:  # Verify phone
        cls()
        throw_error('error', *data_error_msgs["phone"](phone_in))
        cls()
        print(phone_format_info)
        phone_in = input("\n" * 5 + Fore.LIGHTMAGENTA_EX +
                         "Enter Phone: " + Fore.RESET)
        phone_check = phone_validator(phone_in)
    phone_in = phone_check
    cls()

    # Email
    print(email_format_info)
    email_in = input(Fore.LIGHTMAGENTA_EX + "Enter Email: " + Fore.RESET)
    while not validate_email(email_in):  # Verify email
        throw_error('error', *data_error_msgs["email"](email_in))
        cls()
        print(email_format_info)
        email_in = input("\n" * 5 + Fore.LIGHTMAGENTA_EX +
                         "Enter Email: " + Fore.RESET)
    cls()
    # Prime
    prime = "PRIME" if input(Fore.LIGHTMAGENTA_EX + "Enter Prime: " + Fore.RESET).lower() in [
        "prime", "yes", "p", "y", "oui"] else "NOT PRIME"
    # Password
    if register:
        password = input(Fore.LIGHTMAGENTA_EX + "Enter Password: " + Fore.RESET)
    else:
        password = np.nan
    # Data Summarization
    new_data = [customer_first_name, customer_last_name, decoded_date,
                gender, address, country_in, city_in, state_in, pincode_in,
                phone_in, email_in, prime, password]
    if all(new_data):
        print(f"""{Fore.CYAN}
                                    ╔═╗╔═╗╔╗╔╔═╗╦╦═╗╔╦╗  ╔╦╗╔═╗╔╦╗╔═╗
                                    ║  ║ ║║║║╠╣ ║╠╦╝║║║   ║║╠═╣ ║ ╠═╣
                                    ╚═╝╚═╝╝╚╝╚  ╩╩╚═╩ ╩  ═╩╝╩ ╩ ╩ ╩ ╩
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
            ID          :    {Fore.LIGHTMAGENTA_EX}{customer_id}{Fore.CYAN}
            First Name  :    {Fore.LIGHTMAGENTA_EX}{customer_first_name}{Fore.CYAN}
            Last Name   :    {Fore.LIGHTMAGENTA_EX}{customer_last_name}{Fore.CYAN}
            DOB         :    {Fore.LIGHTMAGENTA_EX}{decoded_date}{Fore.CYAN}
            Gender      :    {Fore.LIGHTMAGENTA_EX}{gender}{Fore.CYAN}
            Address     :    {Fore.LIGHTMAGENTA_EX}{address}{Fore.CYAN}
            Country     :    {Fore.LIGHTMAGENTA_EX}{country_in}{Fore.CYAN}
            City        :    {Fore.LIGHTMAGENTA_EX}{city_in}{Fore.CYAN}
            State       :    {Fore.LIGHTMAGENTA_EX}{state_in}{Fore.CYAN}
            Pincode     :    {Fore.LIGHTMAGENTA_EX}{pincode_in}{Fore.CYAN}
            Phone       :    {Fore.LIGHTMAGENTA_EX}{phone_in}{Fore.CYAN}
            E-mail      :    {Fore.LIGHTMAGENTA_EX}{email_in}{Fore.CYAN}
            Prime       :    {Fore.LIGHTMAGENTA_EX}{prime}{Fore.CYAN}

▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
    """ + Fore.RESET)
        if not register:
            insert_data_to_csv = input(
                f"Would you like to insert this data to {Fore.GREEN}Customers.csv{Fore.RESET} ? (Y/N): ")
        else:
            insert_data_to_csv = input(
                "Would you like to complete Registration ? (Y/N): ").strip().lower()
        if insert_data_to_csv in "y1":
            customers.loc[customer_id] = new_data
            SaveData(customers, "Customers")
            print(
                "Record inserted successfully!" if not register else "Registered Successfully!")
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
    customer_id = safe_input(Fore.CYAN + "Customer ID To Update: " + Fore.RESET)
    if customer_id not in customers.index:
        throw_error('error', "ID not found: " + str(customer_id),
                    "Customer ID was not found in the database.\nPlease make sure you have entered a valid Customer ID.")
    else:
        sel_rec = customers.loc[customer_id]
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
                                
                                                 Selected ID:{Fore.RED} {customer_id}{Fore.RESET}

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
                    customer_id = new_val
                    sel_rec = customers.loc[customer_id]
                else:
                    throw_error('error', f'Invalid customer ID: {new_val}', f"""Error while updating Value of id
Make sure that you have avoided any of the following errors:

    1. Invalid value for id i.e. wrong format or data type.
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
                    if input(
                            f"{Fore.CYAN}Do you want to change the value of {Fore.RED}{d_type}?{Fore.RESET} (Y/N) ").strip().lower() in "y1":
                        customers.at[customer_id, d_type] = new_data
                        SaveData(customers, "Customers")
                    else:
                        print("\nUpdating value cancelled.")
                        pause()
                else:
                    throw_error('error', *data_error_msgs[d_type])
                sel_rec = customers.loc[customer_id]


def delete_customer(customers: pd.DataFrame):
    cls()
    customer_id = safe_input(f"{Fore.CYAN}Enter the customer ID to delete: {Fore.RESET}")
    # Check if id is in the df
    if customer_id not in customers.index:
        throw_error("error", "Customer ID is not in the Database",
                    "Please make sure if the ID you have entered is correct")
    else:
        sel_rec = customers.loc[customer_id]
        print(
            f"{Fore.CYAN}The record to be deleted is shown below:{Fore.RESET} \n{sel_rec}")
        confirm_check = "ADMIN#" + \
                        sel_rec["first_name"] + "_" + sel_rec["last_name"]
        confirm = input(
            f"{Fore.RED}Are you sure you want to delete this record ? \nThis action will not reversible!\nType {Fore.CYAN}{confirm_check}{Fore.RED} to Proceed: {Fore.RESET}")
        if confirm != confirm_check:
            print(f"{Fore.CYAN}\n\nRecord deletion cancelled{Fore.RESET}")
        else:
            customers.drop(customer_id, inplace=True)
            print(f"{Fore.CYAN}\n\nRecord deleted successfully {Fore.RESET}")
            SaveData(customers, "Customers")
        pause()


# -----------------------------------------------------------------------------------------------------

def add_a_Product(products: pd.DataFrame):
    cls()
    print(Fore.CYAN +
          """
                       ╔═╗╔╦╗╔╦╗  ╔═╗  ╔═╗╦═╗╔═╗╔╦╗╦ ╦╔═╗╔╦╗
                       ╠═╣ ║║ ║║  ╠═╣  ╠═╝╠╦╝║ ║ ║║║ ║║   ║ 
                       ╩ ╩═╩╝═╩╝  ╩ ╩  ╩  ╩╚═╚═╝═╩╝╚═╝╚═╝ ╩ 
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
""" + Fore.RESET)
    product_id = products.sort_index().index[::-1][0] + 1
    # name
    name = input(Fore.LIGHTMAGENTA_EX +
                 "Enter Product Name: " + Fore.RESET).capitalize()
    while not is_alpha_whitespace(name):
        throw_error('error', "Invalid Name")
        name = input("\n" * 5 + Fore.LIGHTMAGENTA_EX +
                     "Enter Product Name: " + Fore.RESET)
    cls()
    # manufacturer
    manufacturer = input(Fore.LIGHTMAGENTA_EX +
                         "Enter manufacturer: " + Fore.RESET).capitalize()
    while not is_alpha_whitespace(manufacturer):
        throw_error('error', "Invalid manufacturer name")
        manufacturer = input("\n" * 5 + Fore.LIGHTMAGENTA_EX +
                             "Enter manufacturer: " + Fore.RESET)
    cls()
    # category
    category = input(Fore.LIGHTMAGENTA_EX +
                     "Enter Category: " + Fore.RESET).capitalize()
    while not is_alpha_whitespace(category):
        throw_error('error', "Invalid Category")
        category = input("\n" * 5 + Fore.LIGHTMAGENTA_EX +
                         "Enter Category: " + Fore.RESET)
    cls()
    # Returnable
    returnables = ["Returnable", "Not Returnable", "Exchange-Only"]
    returnables_check = input(Fore.LIGHTMAGENTA_EX +
                              "\nReturnable -> 1\nNot Returnable -> 2\nExchange-Only -> 3\nEnter Returnable: " + Fore.RESET).strip().lower().title()
    returnable = None
    # Verify Returnable
    while returnable is None:
        try:
            returnable = returnables[int(returnables_check) - 1]
            break
        except IndexError:
            throw_error('error', f"Invalid Returnable: {returnable}")
            returnables_check = input(Fore.LIGHTMAGENTA_EX +
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
    avg_rating = None
    while avg_rating is None:
        avg_rating = safe_input(Fore.LIGHTMAGENTA_EX + "Enter AvgRating: " + Fore.RESET, d_type="float")
    cls()
    # Days to Return
    if returnable != "Not Returnable":
        days_to_return = None
        while type(days_to_return) != int:
            days_to_return = safe_input(Fore.LIGHTMAGENTA_EX +
                                        "Enter Days to Return: " + Fore.RESET)
    else:
        days_to_return = "-"
    # Data Summarization
    new_data = [name, manufacturer, category,
                returnable, stock, avg_rating, days_to_return]
    if all(new_data):
        print(f"""{Fore.CYAN}
                                    ╔═╗╔═╗╔╗╔╔═╗╦╦═╗╔╦╗  ╔╦╗╔═╗╔╦╗╔═╗
                                    ║  ║ ║║║║╠╣ ║╠╦╝║║║   ║║╠═╣ ║ ╠═╣
                                    ╚═╝╚═╝╝╚╝╚  ╩╩╚═╩ ╩  ═╩╝╩ ╩ ╩ ╩ ╩
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
            ID              :    {Fore.LIGHTMAGENTA_EX}{product_id}{Fore.CYAN}
            Name            :    {Fore.LIGHTMAGENTA_EX}{name}{Fore.CYAN}
            Manufacturer    :    {Fore.LIGHTMAGENTA_EX}{manufacturer}{Fore.CYAN}
            Category        :    {Fore.LIGHTMAGENTA_EX}{category}{Fore.CYAN}
            Returnable      :    {Fore.LIGHTMAGENTA_EX}{returnable}{Fore.CYAN}
            Stock           :    {Fore.LIGHTMAGENTA_EX}{stock}{Fore.CYAN}
            Avg_rating      :    {Fore.LIGHTMAGENTA_EX}{avg_rating}{Fore.CYAN}
            Days to Return  :    {Fore.LIGHTMAGENTA_EX}{days_to_return}{Fore.CYAN}

▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
    {Fore.RESET}""")
        insert_into_csv = input(
            f"Would you like to insert this data to {Fore.LIGHTCYAN_EX}Products.csv{Fore.RESET} ? (Y/N): ").strip().lower()
        if insert_into_csv in "y1":
            products.loc[product_id] = new_data
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
    product_id = safe_input(f"{Fore.CYAN}Enter the product ID to delete: {Fore.RESET}")
    # Check if id is in the df
    if product_id not in products.index:
        throw_error("error", "Product ID is not in the Database",
                    "Please make sure if the ID you have entered is correct")
    else:
        sel_rec = products.loc[product_id]
        print(
            f"{Fore.CYAN}The record to be deleted is shown below:{Fore.RESET} \n{sel_rec}")
        confirm_check = "ADMIN#" + str(product_id)[len(str(product_id)) - 3:]
        confirm = input(
            f"{Fore.RED}Are you sure you want to delete this record ? \nThis action will not reversible!\nType {Fore.CYAN}{confirm_check}{Fore.RED} to Proceed: {Fore.RESET}")
        if confirm != confirm_check:
            print(f"{Fore.CYAN}\n\nRecord deletion cancelled{Fore.RESET}")
        else:
            products.drop(product_id, inplace=True)
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
    product_id = safe_input(Fore.CYAN + "Product ID To Update: " + Fore.RESET)
    if product_id not in products.index:
        throw_error('error', "ID not found: " + str(product_id),
                    "Product ID was not found in the database.\nPlease make sure you have entered a valid Product ID.")
        print(products.index)
    else:
        sel_rec = products.loc[product_id]
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
                                            
                                            Selected ID:{Fore.RED} {product_id}{Fore.RESET}

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
                    product_id = new_val
                    sel_rec = products.loc[product_id]
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
                                   "Exchange-Only"][int(new_val) - 1]
                    except ValueError:
                        throw_error('error', 'Error while updating product data',
                                    "Please make sure you have entered the correct details.")
                        continue
                print(f"{Fore.CYAN}Your new value for {d_type}: " +
                      Fore.RED, new_val, Fore.RESET)
                if data_validator_product_bool(products, product_id, new_val, d_type):
                    if input(
                            f"{Fore.CYAN}Do you want to change the value of {Fore.RED}{d_type}?{Fore.RESET} (Y/N) ").lower() in "y1":
                        products.at[product_id, d_type] = new_val
                        if d_type == "Returnable" and new_val == "Not Returnable":
                            products.at[product_id, "DaysToReturn"] = "-"
                        SaveData(products, "Products")
                    else:
                        print("\nUpdating value cancelled.")
                        pause()
                else:
                    throw_error('error', 'Error while updating product data',
                                "Please make sure you have entered the correct details.")
                sel_rec = products.loc[product_id]


# ----------------------------------------------------------------------------------------------------


def add_an_order(customers: pd.DataFrame, products: pd.DataFrame, orders: pd.DataFrame):
    cls()
    print(Fore.CYAN +
          """
                          ╔═╗╔╦╗╔╦╗  ╔═╗╔╗╔  ╔═╗╦═╗╔╦╗╔═╗╦═╗
                          ╠═╣ ║║ ║║  ╠═╣║║║  ║ ║╠╦╝ ║║║╣ ╠╦╝
                          ╩ ╩═╩╝═╩╝  ╩ ╩╝╚╝  ╚═╝╩╚══╩╝╚═╝╩╚═
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
""" + Fore.RESET)
    # OrderID
    orderId = orders.sort_index().index[::-1][0] + 1

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
    price = None
    total_price = None
    while price is None:
        price = safe_input(Fore.LIGHTMAGENTA_EX + "Enter Price: " + Fore.RESET, d_type='float')
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
            State = States[int(States_check) - 1]
            break
        except IndexError:
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
    # Data Summarization
    NewData = [customerID, cust_first_name, cust_last_name, productID, prod_name, qty,
               total_price, doo, State, cust_address]
    if all(NewData):
        print(f"""{Fore.CYAN}
                                    ╔═╗╔═╗╔╗╔╔═╗╦╦═╗╔╦╗  ╔╦╗╔═╗╔╦╗╔═╗
                                    ║  ║ ║║║║╠╣ ║╠╦╝║║║   ║║╠═╣ ║ ╠═╣
                                    ╚═╝╚═╝╝╚╝╚  ╩╩╚═╩ ╩  ═╩╝╩ ╩ ╩ ╩ ╩
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
            OrderID               :    {Fore.LIGHTMAGENTA_EX}{orderId}{Fore.CYAN}
            CustomerID            :    {Fore.LIGHTMAGENTA_EX}{customerID}{Fore.CYAN}
            Customer (First Name) :    {Fore.LIGHTMAGENTA_EX}{cust_first_name}{Fore.CYAN}
            Customer (Last Name)  :    {Fore.LIGHTMAGENTA_EX}{cust_last_name}{Fore.CYAN}
            ProductID             :    {Fore.LIGHTMAGENTA_EX}{productID}{Fore.CYAN}
            Product Name          :    {Fore.LIGHTMAGENTA_EX}{prod_name}{Fore.CYAN}
            Quantity              :    {Fore.LIGHTMAGENTA_EX}{qty}{Fore.CYAN}
            Total Price           :    {Fore.LIGHTMAGENTA_EX}{total_price}{Fore.CYAN}
            Date Of Order         :    {Fore.LIGHTMAGENTA_EX}{doo}{Fore.CYAN}
            Status                :    {Fore.LIGHTMAGENTA_EX}{State}{Fore.CYAN}
            Address               :    {Fore.LIGHTMAGENTA_EX}{cust_address}{Fore.CYAN}

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
    order_id = safe_input(f"{Fore.CYAN}Enter the order ID to delete: {Fore.RESET}")
    # Check if id is in the df
    if order_id not in orders.index:
        throw_error("error", "Order ID is not in the Database",
                    "Please make sure if the ID you have entered is correct")
    else:
        sel_rec = orders.loc[order_id]
        print(
            f"{Fore.CYAN}The record to be deleted is shown below:{Fore.RESET} \n{sel_rec}")
        confirm_check = "ADMIN#" + str(order_id)[len(str(order_id)) - 3:]
        confirm = input(
            f"{Fore.RED}Are you sure you want to delete this record ? \nThis action will not reversible!\nType {Fore.CYAN}{confirm_check}{Fore.RED} to Proceed: {Fore.RESET}")
        if confirm != confirm_check:
            print(f"{Fore.CYAN}\n\nRecord deletion cancelled{Fore.RESET}")
        else:
            orders.drop(order_id, inplace=True)
            print(f"{Fore.CYAN}\n\nRecord deleted successfully {Fore.RESET}")
        SaveData(orders, "Orders")
        pause()


update_order_menu = {
    "1": "orderId",
    "2": "customerID",
    "3": "productID",
    "4": "qty",
    "5": "totalPrice",
    "6": "dateofOrder",
    "7": "status",
    "8": "Back"
}


def update_order(customers: pd.DataFrame, products: pd.DataFrame, orders: pd.DataFrame):
    cls()
    order_id = safe_input(Fore.CYAN + "Order ID To Update: " + Fore.RESET)
    if order_id not in orders.index:
        throw_error('error', "ID not found: " + str(order_id),
                    "Order ID was not found in the database.\nPlease make sure you have entered a valid Order ID.")
        print(orders.index)
    else:
        sel_rec = orders.loc[order_id]
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
                              
                                              Selected ID:{Fore.RED} {order_id}{Fore.RESET}

                                           1)  orderId                         4)  qty
                                           2)  customerID                      5)  totalPrice
                                           3)  productID                       6)  Date Ordered
                                                        
                                                    7)  Status       8)  Back{Fore.CYAN}

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
                    order_id = new_val
                    sel_rec = orders.loc[order_id]
                else:
                    throw_error('error', f'Invalid order ID: {new_val}')
            elif cmd == "8":
                break
            elif cmd in "234567":
                d_type = update_order_menu[cmd]
                print(Fore.CYAN +
                      f"Updating Value of {Fore.RED}{d_type}{Fore.CYAN}")
                print(sel_rec)
                print(
                    f"Old value of {d_type}: {Fore.RED}{sel_rec[d_type]}{Fore.CYAN}")
                new_val = input(f"Enter your new value: {Fore.RED}") if d_type not in ["orderId", "customerID",
                                                                                       "productID"] else safe_input(
                    f"Enter your new value: {Fore.RED}")
                if data_validator_order_bool(customers, products, orders, new_val, d_type):
                    if d_type == "dateofOrder":
                        new_val = date_decoder(new_val)
                    print(f"{Fore.CYAN}Your new value for {d_type}: " +
                          Fore.RED, new_val, Fore.RESET)
                    if input(
                            f"{Fore.CYAN}Do you want to change the value of {Fore.RED}{d_type}?{Fore.RESET} (Y/N) ").lower() in "y1":
                        orders.at[order_id, d_type] = new_val
                        if d_type == "customerID":
                            cust = customers.loc[new_val]
                            orders.at[order_id,
                                      "customerFirstName"] = cust["first_name"]
                            orders.at[order_id, "customerLastName"] = cust["last_name"]
                            orders.at[order_id, "address"] = cust["address"]
                        elif d_type == "productID":
                            prod = products.loc[new_val]
                            orders.at[order_id, "productName"] = prod["name"]
                            SaveData(orders, "Orders")
                    else:
                        print("\nUpdating value cancelled.")
                        pause()
                else:
                    throw_error('error', 'Error while updating order data',
                                "Please make sure you have entered the correct details.")
                sel_rec = orders.loc[order_id]


# ----------------------------------------------------------------------------------------------------


def add_a_ticket(customers: pd.DataFrame, products: pd.DataFrame, orders: pd.DataFrame, tickets: pd.DataFrame,
                 custid=None, register=False):
    cls()
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
    order_id = safe_input(Fore.LIGHTMAGENTA_EX +
                          "Enter Order ID: " + Fore.RESET)
    while (order_id not in orders.index) or (orders.loc[order_id]["customerID"] != CustID):
        throw_error('error', "Order ID not found!")
        order_id = safe_input(Fore.LIGHTMAGENTA_EX +
                              "Enter Order ID: " + Fore.RESET)
    cls()

    # Issue Category & Issue
    issue_categories = ["Damaged product", "Info", "Different from product description", "Part missing",
                        "Received the wrong product", "Other"]
    issue_category = None
    while issue_category is None:
        issue_category = input(Fore.LIGHTMAGENTA_EX + "Enter Issue Category: " +
                               Fore.RESET)
        if issue_category in issue_categories:
            break
        match = difflib.get_close_matches(issue_category, issue_categories, n=1, cutoff=0.8)
        issue_category = None
        if match:
            throw_error('error', 'Error while updating order data',
                        f"Please make sure you have entered the correct details. \nDid you mean '{match[0]}' ?")
            continue

        throw_error('error', 'Error while updating order data',
                    "Please make sure you have entered the correct details.")

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
        while doc is None and doc_check != "-":  # Retake inputs for DOB till its valid
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
        first_response_time = None
        while first_response_time is None:
            first_response_time = safe_input(Fore.LIGHTMAGENTA_EX +
                                             "Enter First Response Time: " + Fore.RESET, d_type='float',
                                             can_be_nan=True)
            print(first_response_time)
        cls()

        # Customer Satisfaction
        custSatis = None
        while type(custSatis) != float:
            custSatis = safe_input(Fore.LIGHTMAGENTA_EX +
                                   "Enter Customer Satisfaction: " + Fore.RESET, d_type='float', can_be_nan=True)
        cls()

        # Replies
        replies = None
        while replies is None:
            replies = safe_input(Fore.LIGHTMAGENTA_EX +
                                 "Enter Replies: " + Fore.RESET, can_be_nan=True)
        cls()
    else:
        doc_check = "-"
        replies = custSatis = first_response_time = doc = np.nan

    # Get Customer and Product data
    cust = customers.loc[CustID]
    cust_first_name = cust["first_name"]
    cust_phone = cust["phone"]

    order = orders.loc[order_id]
    status = "Closed" if date_decoder(doc) else "Open"

    # HoursTaken
    if doc_check == "-":
        hoursTaken = np.NaN
    else:
        res = doc - do
        hoursTaken = res.days * 24

    prod = products.loc[order['productID']]
    prod_name = prod["name"]
    prod_category = prod["category"]
    # Data Summarization
    NewData = [CustID, order_id, prod_name, prod_category,
               cust_first_name, cust_phone, status, issue_category, issue,
               do, doc, hoursTaken, first_response_time, replies, custSatis]
    print(f"""{Fore.CYAN}
                                    ╔═╗╔═╗╔╗╔╔═╗╦╦═╗╔╦╗  ╔╦╗╔═╗╔╦╗╔═╗
                                    ║  ║ ║║║║╠╣ ║╠╦╝║║║   ║║╠═╣ ║ ╠═╣
                                    ╚═╝╚═╝╝╚╝╚  ╩╩╚═╩ ╩  ═╩╝╩ ╩ ╩ ╩ ╩
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
    
                TicketID                 : {Fore.LIGHTMAGENTA_EX}{ticketID}       {Fore.CYAN}
                CustID                   : {Fore.LIGHTMAGENTA_EX}{CustID}         {Fore.CYAN}
                OrderID                  : {Fore.LIGHTMAGENTA_EX}{order_id}        {Fore.CYAN}
                ProductName              : {Fore.LIGHTMAGENTA_EX}{prod_name}      {Fore.CYAN}
                ProductCategory          : {Fore.LIGHTMAGENTA_EX}{prod_category}  {Fore.CYAN}
                CustFirstName            : {Fore.LIGHTMAGENTA_EX}{cust_first_name}{Fore.CYAN}
                CustPhone                : {Fore.LIGHTMAGENTA_EX}{cust_phone}     {Fore.CYAN}
                Status                   : {Fore.LIGHTMAGENTA_EX}{status}         {Fore.CYAN}
                IssueCategory            : {Fore.LIGHTMAGENTA_EX}{issue_category}  {Fore.CYAN}
                Issue                    : {Fore.LIGHTMAGENTA_EX}{issue}          {Fore.CYAN}
                DateOpened               : {Fore.LIGHTMAGENTA_EX}{do}             {Fore.CYAN}
                DateClosed               : {Fore.LIGHTMAGENTA_EX}{doc}            {Fore.CYAN}
                HoursTaken               : {Fore.LIGHTMAGENTA_EX}{hoursTaken}     {Fore.CYAN}
                FirstResponseTime        : {Fore.LIGHTMAGENTA_EX}{first_response_time}            {Fore.CYAN}
                Replies                  : {Fore.LIGHTMAGENTA_EX}{replies}        {Fore.CYAN}
                CustomerSatisfaction(%)(%)  : {Fore.LIGHTMAGENTA_EX}{custSatis}      {Fore.CYAN}

▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
    """ + Fore.RESET)
    insert_into_csv = input(
        f"Would you like to insert this data to {Fore.LIGHTGREEN_EX}Tickets.csv{Fore.RESET} ? (Y/N): ").strip().lower()
    if insert_into_csv in "y1":
        tickets.loc[ticketID] = NewData
        SaveData(tickets, "Tickets")
        print("Record inserted successfully!")
    else:
        print("Record Insertion Cancelled :(")
    time.sleep(1)
    pause()


def delete_ticket(tickets: pd.DataFrame):
    cls()
    ticket_id = safe_input(f"{Fore.CYAN}Enter the ticket ID to delete: {Fore.RESET}")
    # Check if id is in the df
    if ticket_id not in tickets.index:
        throw_error("error", "Ticket ID is not in the Database",
                    "Please make sure if the ID you have entered is correct")
    else:
        sel_rec = tickets.loc[ticket_id]
        print(
            f"{Fore.CYAN}The record to be deleted is shown below:{Fore.RESET} \n{sel_rec}")
        confirm_check = "ADMIN#" + str(ticket_id)[len(str(ticket_id)) - 3:]
        confirm = input(
            f"{Fore.RED}Are you sure you want to delete this record ? \nThis action will not reversible!\nType {Fore.CYAN}{confirm_check}{Fore.RED} to Proceed: {Fore.RESET}")
        if confirm != confirm_check:
            print(f"{Fore.CYAN}\n\nRecord deletion cancelled{Fore.RESET}")
        else:
            tickets.drop(ticket_id, inplace=True)
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
    "12": "CustomerSatisfaction(%)"
}


def update_ticket(customers: pd.DataFrame, products: pd.DataFrame, orders: pd.DataFrame, tickets: pd.DataFrame,
                  custid=None, msg_grp=None, close=False):
    cls()
    ticket_id = safe_input(Fore.CYAN + "Ticket ID To Update: " + Fore.RESET)
    if ticket_id not in tickets.index or (close and custid != tickets.loc[ticket_id]['CustID']):
        throw_error('error', "ID not found: " + str(ticket_id),
                    "Ticket ID was not found in the database.\nPlease make sure you have entered a valid Ticket ID.")
        print(tickets.index)
    else:
        sel_rec = tickets.loc[ticket_id]
        print(Fore.CYAN + "This is the selected Record: \n" +
              Fore.RESET, sel_rec, sep="")
        pause()
        cls()
        if close:
            if msg_grp is None:
                return throw_error('error', "MSG_GRP IS NULL")
            tickets.at[ticket_id, "Status"] = "Closed"
            tdy = pd.to_datetime(datetime.today())
            tickets.at[ticket_id, "DateClosed"] = tdy
            res = tdy - tickets.loc[ticket_id]["DateOpened"]
            tickets.at[ticket_id, "HoursTaken"] = res.days * 24
            fail_text = "Please Enter on a scale of 1-10"
            interaction = safe_input(
                Fore.LIGHTMAGENTA_EX + "Please rate your experience with us: (Rate them on a scale of 1-10) \nHow was our staff's interaction with you ?" + Fore.RESET,
                fail_text=fail_text)
            frtt = safe_input(Fore.LIGHTMAGENTA_EX +
                              "Did you receive the first interaction message from our staff quick ?" + Fore.RESET,
                              fail_text=fail_text)
            theclock = safe_input(Fore.LIGHTMAGENTA_EX +
                                  "How quickly your issue was resolved ?" + Fore.RESET, fail_text=fail_text)
            satis_deter = [x * 10 for x in [interaction, frtt, theclock]]
            tickets.at[ticket_id, "CustomerSatisfaction(%)(%)"] = round(sum(satis_deter) / len(satis_deter), 2)
            tickets.at[ticket_id, "Replies"] = msg_grp.size()[ticket_id]
            q = msg_grp.get_group(ticket_id)
            Q = q[q['Side'] == "ADMIN"]['Date']
            fmdate = None
            if not Q.empty:
                fmdate = pd.to_datetime(Q.values[0])
            if fmdate is not None:
                if fmdate != 0:
                    tickets.at[ticket_id, "FirstResponseTime"] = int(
                        (fmdate - (tickets.loc[ticket_id]["DateOpened"])).seconds // 60)
                else:
                    tickets.at[ticket_id, "FirstResponseTime"] = np.nan
            else:
                tickets.at[ticket_id, "FirstResponseTime"] = np.nan
            del q
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
                                            
                                                 Selected ID:{Fore.RED} {ticket_id}{Fore.RESET}
        
             1) TicketId         4) Status               7) DateOpened          10) FirstResponseTime
             2) CustID           5) IssueCategory        8) DateClosed          11) Replies
             3) OrderID          6) Issue                9) HoursTaken          12) CustomerSatisfaction(%)
                                                            13) Back{Fore.CYAN}
        
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
            """ + Fore.RESET)
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
                    ticket_id = new_val
                    sel_rec = tickets.loc[ticket_id]
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
                if data_validator_ticket_bool(customers, orders, tickets, new_val, d_type):
                    if input(
                            f"{Fore.CYAN}Do you want to change the value of {Fore.RED}{d_type}?{Fore.RESET} (Y/N) ").lower() in "y1":
                        tickets.at[ticket_id, d_type] = new_val
                        if d_type == "CustID":
                            cust = customers.loc[new_val]
                            tickets.at[ticket_id,
                                       "CustFirstName"] = cust["first_name"]
                            tickets.at[ticket_id, "CustPhone"] = cust["phone"]
                        elif d_type == "OrderID":
                            order = orders.loc[new_val]
                            prod = products.loc[order["productID"]]
                            tickets.at[ticket_id, "ProductName"] = prod["name"]
                            tickets.at[ticket_id,
                                       "ProductCategory"] = prod["category"]
                    else:
                        print("\nUpdating value cancelled.")
                        pause()
                else:
                    if d_type in ["Status", "IssueCategory"]:
                        match_list = ['Open', 'Closed'] if d_type == "Status" else ["Damaged product", "Info",
                                                                                    "Different from product description",
                                                                                    "Part missing",
                                                                                    "Received the wrong product",
                                                                                    "Other"]
                        match = difflib.get_close_matches(new_val, match_list, n=1, cutoff=0.8)
                        if match:
                            throw_error('error', 'Error while updating order data',
                                        f"Please make sure you have entered the correct details. \nDid you mean '{match[0]}' ?")
                            continue
                    throw_error('error', 'Error while updating order data',
                                "Please make sure you have entered the correct details.")
                    continue
                sel_rec = tickets.loc[ticket_id]
        SaveData(tickets, "Tickets")

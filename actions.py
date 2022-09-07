from ast import For
import imp
from multiprocessing.spawn import import_main_path
import re
import time
from turtle import st
import uuid
from colorama import Fore, Style
from datetime import datetime
from numpy import mat

import pandas as pd

from util import text_formatting as tf


def pause(): return input('\n'*2 + "Press Any key To Contine...")
def cls(): return print("\n" * 30)


def throw_error(type, title, message):
    cls()
    if type == 'error':
        print(f"{Fore.RED} \u26A0 ERROR: {title} \u26A0")
        print(message, Fore.RESET)
    elif type == 'warning':
        print(f"! WARNING: {title} !")
        print(message)
    elif type == 'info':
        print(f"{tf.BOLD} INFO: {title}{message}")
    else:
        print(f"======================{title}======================")
        print(message)
    pause()


def phone_validator(s: str):
    org = s
    org = org.split(" ")
    if org[0][0] == "+":
        org[0] = org[0][1:]
    PatternA = re.compile("(0-91)?")
    PatternB = re.compile("[0-9]{10}")
    lhs = "".join(org[1:])
    if PatternA.match(org[0]) and PatternB.match(lhs):
        return f"+{org[0]} {lhs[:3]} {lhs[3:6]} {lhs[6:10]}"
    else:
        None


def validate_email(email):
    rem = re.fullmatch(
        r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email)
    return rem if len(email) >= 3 else None


def date_decoder(date):
    d, m, y = None, None, None
    if " " in date:
        date = date.split(" ")
        if str(date[1]).isdigit() or len(date) != 3:
            return None
        M = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
             'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        d, m, y = date[0].replace("th", "").replace("st", "").replace("rd", "").replace("nd", ""), M.index(
            str((date[1][:3]).lower()).capitalize()) + 1, date[2]
    elif "/" in date:
        date = date.split("/")
        d, m, y = date
    else:
        return None
    try:
        datetime(year=int(y), month=int(m), day=int(d))
        if len(y) == 2:
            y = "20" + y
        if y > str(datetime.today().year): raise ValueError("Invalid DOB \n year of birth cannot be greater then this year!")
        return f"{int(d)}/{int(m)}/{int(y)}"
    except ValueError as e:
        #throw_error('error', 'INVALID DATE', f'{d, m, y} \n {e}')
        return None


def data_validator_customer(data, d_type):
    if d_type in ["first_name", "last_name", "country", "city", "state"]:
        return data if data.isalpha() else None
    elif d_type == "dob":
        return date_decoder(data)
    elif d_type == "gender":
        return data if data in ["Male", "Female"] else None
    elif d_type == "address":
        return data
    elif d_type == "pincode":
        return data if data.isdigit() else None
    elif d_type == "phone":
        return phone_validator(data)
    elif d_type == "email":
        return data if validate_email(data) else None
    elif d_type == "prime":
        return "PRIME" if data in ["Yes", "PRIME", "P"] else "-"


def add_a_Customer(customers: pd.DataFrame):
    # TODO: Formatting
    print("+" + "-"*25 + "ADD A CUSTOMER" + "-"*25 + "+" + "\n\n") # GUI
    id = input(Fore.LIGHTMAGENTA_EX + "Enter ID (Leave blank for random uuid): " + Fore.RESET)
    # Verify that the customer id is not a duplicate
    while id in customers.index:
        throw_error('error', f'Duplicate ID: {id}', "\n> ID should be a unique ID.")
        id = input("\n"*5 + Fore.LIGHTMAGENTA_EX + "Enter ID (Leave blank for random uuid): " + Fore.RESET)
    if id == "": # Gen uuid if input is empty
        id = uuid.uuid4()
    cls()
    # first_name
    first_name = input(Fore.LIGHTMAGENTA_EX + "Enter First Name: " + Fore.RESET).capitalize()
    while not first_name.isalpha():
        throw_error('error', f'Invalid Firstname: {first_name}', "\n> First Name should only have alphabets and must not be blank!\n\n")
        first_name = input("\n"*5 + Fore.LIGHTMAGENTA_EX + "Enter First Name: " + Fore.RESET)
    cls()
    # last_name
    last_name = input(Fore.LIGHTMAGENTA_EX + "Enter Last Name: " + Fore.RESET).capitalize()
    while not last_name.isalpha():
        throw_error('error', f'Invalid Lastname: {last_name}', "\n> Last Name should only have alphabetsand must not be blank!\n\n")
        last_name = input("\n"*5 + Fore.LIGHTMAGENTA_EX + "Enter Last Name: " + Fore.RESET)
    cls()
    # DOB
    # Print DOB GUI
    print(f"""{Fore.LIGHTRED_EX}
+============================= FORMAT =============================+
|   > The date must not be blank                                   |
|   > The date must be on the calander                             |
|   > The date must be in any of the following Formats             |
|        "16th Jan 2021"         OR      "16 Jan 2021"             |
|        "16th January 2021"     OR      "16 January 2021"         |
|        "dd/mm/yy"              OR      "dd/mm/yyyy"              |
+==================================================================+{Fore.RESET}\n\n\n""")
    dob_check = input(Fore.LIGHTMAGENTA_EX + "Enter Dob: " + Fore.RESET)
    dob = date_decoder(dob_check)
    while dob is None: # Retake inputs for DOB till its valid
        throw_error('error', f'Invalid DOB: {dob_check}', f"""
Please make sure you have a entered a valid date.

{Fore.LIGHTRED_EX}
+============================= FORMAT =============================+
|   > The date must not be blank                                   |
|   > The date must be on the calander                             |
|   > The date must be in any of the following Formats             |
|        "16th Jan 2021"         OR      "16 Jan 2021"             |
|        "16th January 2021"     OR      "16 January 2021"         |
|        "dd/mm/yy"              OR      "dd/mm/yyyy"              |
+==================================================================+{Fore.RESET}\n\n\n""")
        dob_check = input(Fore.LIGHTMAGENTA_EX + "Enter Dob: " + Fore.RESET)
        dob = date_decoder(dob_check)
    cls()
    # Gender
    genders = ["male", "female", "m", "f"]
    gender_check = input(Fore.LIGHTMAGENTA_EX + "Enter Gender: " + Fore.RESET).strip().lower()
    gender = "Male" if gender_check in ["male", "m"] else "Female" if gender_check in genders else None
    # Verify Gender
    while gender is None:
        throw_error('error', f'Invlaid gender: {gender_check}', "Make sure you have entered a valid gender.")
        gender_check = input(Fore.LIGHTMAGENTA_EX + "Enter Gender: " + Fore.RESET)
        gender = gender_check if gender_check in genders else None
    cls()
    # Address
    address = input(Fore.LIGHTMAGENTA_EX + "Enter Address: " + Fore.RESET) #TODO Address format
    cls()
    # Country
    country = input(Fore.LIGHTMAGENTA_EX + "Enter Country: " + Fore.RESET).capitalize()
    while not all(c.isalpha() for c in country.split(" ")): # Verify country
        throw_error('error', f'Invalid Country: {country}', "\n  Country should only have alphabets.")
        country = input(Fore.LIGHTMAGENTA_EX + "Enter Country: " + Fore.RESET)
    cls()
    # City
    city = input(Fore.LIGHTMAGENTA_EX + "Enter City: " + Fore.RESET).capitalize()
    while not all(c.isalpha() for c in city.split(" ")): # Verify City
        throw_error('error', f'Invalid City: {city}', "\n  City should only have alphabets.")
        city = input(Fore.LIGHTMAGENTA_EX + "Enter City: " + Fore.RESET)
    cls()
    # State
    state = input(Fore.LIGHTMAGENTA_EX + "Enter State: " + Fore.RESET).capitalize()
    while not all(c.isalpha() for c in state.split(" ")): # Verify state
        throw_error('error', f'Invalid State: {state}', "\n  State should only have alphabets.")
        state = input(Fore.LIGHTMAGENTA_EX + "Enter State: " + Fore.RESET)
    cls()
    # Postal code
    pincode = input(Fore.LIGHTMAGENTA_EX + "Enter Pincode: " + Fore.RESET)
    while not pincode.isdigit(): # Verify pincode
        throw_error('error', f'Invalid Pincode: {pincode}', "\n  Pincdoe should only have digits.")
        pincode = input(Fore.LIGHTMAGENTA_EX + "Enter Pincode: " + Fore.RESET)
    cls()
    # Phone
    phone = input(Fore.LIGHTMAGENTA_EX + "Enter Phone: " + Fore.RESET)
    while not phone_validator(phone): # Verify phone
        cls()
        throw_error('error', f"Invalid phone number: {phone}", """Phone must be a valid Phone.

1) It should not be blank.
2) The first two digits of the phone must be between 0 and 91 (inclusive).
3) The other digits of the phone must be between 0 and 9 (inclusive).

Input Format: +XX XXX XXX XXXX OR +XX XXXXXXXXXX

Avoid the above errors and try again.
        """)
        phone = input("\n"*5 + Fore.LIGHTMAGENTA_EX + "Enter Phone: " + Fore.RESET)
    cls()

    # Email
    email = input(Fore.LIGHTMAGENTA_EX + "Enter Email: " + Fore.RESET)
    while not validate_email(email): # Verify email
            throw_error('error', f"Invalid email address: {email}", """
The email address should be:
r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
1) At least three characters long
2) Should have a valid Username: 
    a) Can have A-Z and a-z characters
    b) Can have digits and special characters (_%+-)
3) Should have the '@' character
4) Should have valid Mail server name:
    a) Can have A-Z and a-z characters
    b) Can have digits and hypen (-) no special characters
5) Should have valid top level domain name:

Avoid the above errors and try again.
        """)
            email = input("\n"*5 + Fore.LIGHTMAGENTA_EX + "Enter Email: " + Fore.RESET)
    cls()
    # Prime
    prime = "PRIME" if input(Fore.LIGHTMAGENTA_EX + "Enter Prime: " + Fore.RESET) in [
        "Prime", "PRIME", "Yes", "1", "Y", "P", "p"] else "-"
    # Data Summmarization
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
        reck = input(
            "Would you like to insert this data to Customers.csv ? (Y/N): ")
        if reck.lower() == "y":
            customers.loc[id] = NewData
            print("Record inserted successfully!")
        else:
            print("Record Insertion Cancelled :(")
        time.sleep(1)
    else:
        throw_error('error', f"Invalid Data", 'The data is invalid, please try again.')

# ----------------------------------------------------------------------------------------------------


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
    id = input("Customer ID To Update: ")
    if id in customers.index:
        sel_rec = customers.loc[id]
        print("This is the selected Record: \n", sel_rec, sep="")
        pause()
        cls()
        while True:
            cls()
            print(f"""What would you like to Modify ?  Selected ID: {id}
    1) id        
    2) first_name
    3) last_name 
    4) dob       
    5) gender    
    6) address   
    7) country   
    8) city      
    9) state     
    10) pincode   
    11) phone     
    12) email     
    13) prime
    14) Back     
            """)
            cmd = input("Command: ")
            if cmd == "1":
                print(f"Updating Value of {update_customer_menu[cmd]}")
                print(
                    f"Old value of {update_customer_menu[cmd]}: {sel_rec.name}")
                new_val = input("Enter your new value: ")
                if new_val not in customers.index and new_val != "" and len(new_val) >= 3:
                    customers.rename(
                        index={sel_rec.name: new_val}, inplace=True)
                    break
                else:
                    throw_error('error', 'Invalid customer ID', f"""Error while updating Value of id
Make sure that you have avoided any of the following errors:
1. Invalid value for id i.e. worng format or data type.
2. Empty value for id
3. New Value is less than 3 characters.
                """)
                pause()
            elif cmd == "14" or cmd == "":
                break
            else:
                d_type = update_customer_menu[cmd]
                print(f"Updating Value of {d_type}")
                print(f"Old value of {d_type}: {sel_rec.loc[d_type]}")
                new_val = input("Enter your new value: ")
                print(new_val)
                new_data = data_validator_customer(new_val, d_type)
                if new_data:
                    customers.at[id, d_type] = new_data
                else:
                    throw_error('error', 'Error while updating customer data', f"""Error while updating Value of {d_type} with value {new_data}
Make sure that you have avoided any of the following errors:
1. Empty value for {d_type}

2. Invalid value for {d_type} i.e. worng format or data type.
    a. For (first_name, last_name, country, city, state),
        Data should have only alphabetical characters
    b. For Geneder, either Male/Female, Abbreviations NOT Allowed
    c. For pincode, the data should have only digits
    d. For phone numbers, '+AB Yxx xxx xxxx',
        AB -> 0-91 ; Y -> 7-9 ; X -> 0-9
    e. For email addresses,
        i. The Recipient's name can have: 
            Either case letters, digits from 1-9, Special characters.)
        ii. The @ symbol
        iii. Domain name and Top-level domain eg. abc@yahoo.com
    f. For Prime, either yes, PRIME or P will be valid
                """)
                pause()
    else:
        print("ID DOES NOT EXIST:", id)

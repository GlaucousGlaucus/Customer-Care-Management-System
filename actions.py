import re
import time
import uuid
from datetime import datetime
from operator import ne

import pandas as pd

from util import text_formatting as tf


def pause(): return input('\n'*2 + "Press Any key To Contine...")
def cls(): return print("\n" * 30)


def phone_validator(s):
    org = s
    org = org.split(" ")
    if org[0][0] == "+":
        org[0] = org[0][1:]
    PatternA = re.compile("(0-91)?")
    PatternB = re.compile("[7-9][0-9]{9}")
    if PatternA.match(org[0]) and PatternB.match("".join(org[1:])):
        return s
    else:
        None


def validate_email(email):
    print("Validating email", email)
    rem = re.fullmatch(
        r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email)
    print(email if email else None)
    return rem


def date_decoder(date):
    d, m, y = None, None, None
    if " " in date:
        date = date.split(" ")
        if str(date[1]).isdigit():
            return None
        M = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
             'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        d, m, y = date[0].replace("th", ""), M.index(
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
        return f"{int(d)}/{int(m)}/{int(y)}"
    except ValueError as e:
        print("Invalid date: ", d, m, y)
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


def add_a_Customer(customers):
    print("+" + "-"*25 + "ADD A CUSTOMER" + "-"*25 + "+")
    id = input("Enter ID (Leave blank for random uuid): ")
    while id in customers.index:
        print("ERROR DUPLICATE ID")
        id = input("Enter ID (Leave blank for random uuid): ")
    if id == "":
        id = uuid.uuid4()
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
    print("""
                    Accepted Formats: 
"16th Jan 2021"     OR      "16/01/2021"        OR  '16 January 2021'
    """)
    dob_check = input("Enter Dob: ")
    dob = date_decoder(dob_check)
    while dob is None:
        print("Invlaid Dob")
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
    prime = "PRIME" if input("Enter Prime: ") in [
        "Prime", "PRIME", "Yes", "1", "Y", "P", "p"] else "-"
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
        reck = input(
            "Would you like to insert this data to Customers.csv ? (Y/N): ")
        if reck.lower() == "y":
            customers.loc[id] = NewData
            print("Record inserted successfully!")
        else:
            print("Record Insertion Cancelled :(")
            time.sleep(1)
    else:
        print(f"Error: Invalid Data: {NewData}")

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
                    print(f"""Error while updating Value of id
Make sure that you have avoided any of the following errors:
1. Invalid value for id i.e. worng format or data type.
2. Empty value for id
3. New Value is less than 3 characters.
                """)
                pause()
            elif cmd == "14":
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
                    print(f"""Error while updating Value of {d_type} with value {new_data}
Make sure that you have avoided any of the following errors:
1. Invalid value for {d_type} i.e. worng format or data type.
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

2. Empty value for {d_type}
                """)
                pause()
    else:
        print("ID DOES NOT EXIST:", id)

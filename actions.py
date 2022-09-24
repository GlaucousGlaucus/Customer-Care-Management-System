from logging.handlers import DatagramHandler
import re
from telnetlib import STATUS
import time
import uuid
from colorama import Fore
from datetime import datetime

import pandas as pd

from util import text_formatting as tf


def pause(): return input('\n'*2 + "Press Any key To Contine...")
def cls(): return print("\n" * 30)


def throw_error(type: str, title: str, message=""):
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
        if y > str(datetime.today().year):
            raise ValueError(
                "Invalid DOB \n year of birth cannot be greater then this year!")
        return pd.to_datetime(f"{int(y)}-{int(m)}-{int(d)}")
    except ValueError as e:
        #throw_error('error', 'INVALID DATE', f'{d, m, y} \n {e}')
        return None


def data_validator_customer(data, d_type):
    if d_type in ["first_name", "last_name", "country", "city", "state"]:
        return data if all(c.isalpha() for c in data.split(" ")) else None
    elif d_type == "dob":
        return date_decoder(data)
    elif d_type == "gender":
        gc = data.strip().lower()
        return "Male" if gc in ["male", "m"] else "Female" if gc in ["male", "female", "m", "f"] else None
    elif d_type == "address":
        return data
    elif d_type == "pincode":
        return data if data.isdigit() else None
    elif d_type == "phone":
        return phone_validator(data)
    elif d_type == "email":
        return data if validate_email(data) else None
    elif d_type == "prime":
        return "PRIME" if data.strip().lower() in ["prime", "yes", "1", "y", "p"] else "-"


data_error_msgs = {
    "id": lambda id: (f'Duplicate ID: {id}', "\n> ID should be a unique ID."),
    "first_name": lambda first_name: (f'Invalid Firstname: {first_name}',
                                      "\n> First Name should only have alphabets and must not be blank!\n\n"),
    "last_name": lambda last_name: (f'Invalid Lastname: {last_name}',
                                    "\n> Last Name should only have alphabets and must not be blank!\n\n"),
    "dob": lambda dob_check: (f'Invalid Date: {dob_check}', f"""Please make sure you have a entered a valid date."""),
    "gender": lambda gender_check: (f'Invlaid gender: {gender_check}',
                                    "Make sure you have entered a valid gender."),
    "address": 0,
    "country": lambda country: (f'Invalid Country: {country}', "\n  Country should only have alphabets."),
    "city": lambda city: (f'Invalid City: {city}', "\n  City should only have alphabets."),
    "state": lambda state: (f'Invalid State: {state}', "\n  State should only have alphabets."),
    "pincode": lambda pincode: (f'Invalid Pincode: {pincode}', "\n  Pincdoe should only have digits."),
    "phone": lambda phone: (f"Invalid phone number: {phone}", """Phone must be a valid Phone.

1) It should not be blank.
2) The first two digits of the phone must be between 0 and 91 (inclusive).
3) The other digits of the phone must be between 0 and 9 (inclusive).

Input Format: +XX XXX XXX XXXX OR +XX XXXXXXXXXX

Avoid the above errors and try again.
        """),
    "email": lambda email: (f"Invalid email address: {email}", """
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
        """),
    "prime": 0,
}


def add_a_Customer(customers: pd.DataFrame):
    # TODO: Formatting
    print("+" + "-"*25 + "ADD A CUSTOMER" + "-"*25 + "+" + "\n\n")  # GUI
    id = input(Fore.LIGHTMAGENTA_EX +
               "Enter ID (Leave blank for random uuid): " + Fore.RESET)
    # Verify that the customer id is not a duplicate
    while id in customers.index:
        throw_error('error', *data_error_msgs["id"](id))
        id = input("\n"*5 + Fore.LIGHTMAGENTA_EX +
                   "Enter ID (Leave blank for random uuid): " + Fore.RESET)
    if id == "":  # Gen uuid if input is empty
        id = str(uuid.uuid4())
    cls()
    # first_name
    first_name = input(Fore.LIGHTMAGENTA_EX +
                       "Enter First Name: " + Fore.RESET).capitalize()
    while not first_name.isalpha():
        throw_error('error', *data_error_msgs["first_name"](first_name))
        first_name = input("\n"*5 + Fore.LIGHTMAGENTA_EX +
                           "Enter First Name: " + Fore.RESET)
    cls()
    # last_name
    last_name = input(Fore.LIGHTMAGENTA_EX +
                      "Enter Last Name: " + Fore.RESET).capitalize()
    while not last_name.isalpha():
        throw_error('error', *data_error_msgs["last_name"](last_name))
        last_name = input("\n"*5 + Fore.LIGHTMAGENTA_EX +
                          "Enter Last Name: " + Fore.RESET)
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
    while dob is None:  # Retake inputs for DOB till its valid
        throw_error('error', *data_error_msgs["dob"](dob_check))
        cls()
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
                    Fore.RESET)  # TODO Address format
    cls()
    # Country
    country = input(Fore.LIGHTMAGENTA_EX +
                    "Enter Country: " + Fore.RESET).capitalize()
    while not all(c.isalpha() for c in country.split(" ")):  # Verify country
        throw_error('error', *data_error_msgs["country"](country))
        country = input(Fore.LIGHTMAGENTA_EX +
                        "Enter Country: " + Fore.RESET).capitalize()
    cls()
    # City
    city = input(Fore.LIGHTMAGENTA_EX + "Enter City: " +
                 Fore.RESET).capitalize()
    while not all(c.isalpha() for c in city.split(" ")):  # Verify City
        throw_error('error', *data_error_msgs["city"](city))
        city = input(Fore.LIGHTMAGENTA_EX + "Enter City: " +
                     Fore.RESET).capitalize()
    cls()
    # State
    state = input(Fore.LIGHTMAGENTA_EX + "Enter State: " +
                  Fore.RESET).capitalize()
    while not all(c.isalpha() for c in state.split(" ")):  # Verify state
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
    phone = input(Fore.LIGHTMAGENTA_EX + "Enter Phone: " + Fore.RESET)
    phone_check = phone_validator(phone)
    while not phone_check:  # Verify phone
        cls()
        throw_error('error', *data_error_msgs["phone"](phone))
        phone = input("\n"*5 + Fore.LIGHTMAGENTA_EX +
                      "Enter Phone: " + Fore.RESET)
        phone_check = phone_validator(phone)
    phone = phone_check
    cls()

    # Email
    email = input(Fore.LIGHTMAGENTA_EX + "Enter Email: " + Fore.RESET)
    while not validate_email(email):  # Verify email
        throw_error('error', *data_error_msgs["email"](email))
        email = input("\n"*5 + Fore.LIGHTMAGENTA_EX +
                      "Enter Email: " + Fore.RESET)
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
        ll = max([len(str(x)) for x in NewData])
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
        pause()
    else:
        throw_error('error', f"Invalid Data",
                    'The data is invalid, please try again.')

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


# TODO: Fix update_customer() not updating customer record
def update_customer(customers: pd.DataFrame):
    cls()
    id = input(Fore.CYAN + "Customer ID To Update: " + Fore.RESET).strip()
    if id not in customers.index:
        throw_error('error', "ID not found: " + id,
                    "Customer ID was not found in the database.\nPlease make sure you have entered a valid Customer ID.")
    else:
        sel_rec = customers.loc[id]
        print(Fore.CYAN + "This is the selected Record: \n" +
              Fore.RESET, sel_rec, sep="")
        pause()
        cls()
        while True:
            cls()
            print(Fore.CYAN + f"""What would you like to Modify ?  Selected ID:{Fore.RED} {id}{Fore.RESET}
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
            cmd = input(Fore.CYAN + "Choose To Modify: " + Fore.RESET)
            if cmd == "1":
                print(
                    Fore.CYAN + f"Updating Value of {Fore.RED}{update_customer_menu[cmd]}" + Fore.RESET)
                print(Fore.CYAN +
                      f"Old value of {update_customer_menu[cmd]}: {Fore.RED} {sel_rec.name}" + Fore.RESET)
                new_val = input(
                    Fore.CYAN + "Enter your new value: " + Fore.RESET)
                if new_val not in customers.index and new_val != "" and len(new_val) >= 3:
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
            elif cmd == "14" or cmd == "":
                break
            else:
                d_type = update_customer_menu[cmd]
                print(Fore.CYAN +
                      f"Updating Value of {Fore.RED}{d_type}{Fore.CYAN}")
                print(
                    f"Old value of {d_type}: {Fore.RED}{sel_rec.loc[d_type]}{Fore.CYAN}")
                new_val = input(f"Enter your new value: {Fore.RED}")
                print(f"{Fore.CYAN}Your new value for {d_type}: " +
                      Fore.RED, new_val, Fore.RESET)
                new_data = data_validator_customer(new_val, d_type)
                if new_data:
                    if input(f"{Fore.CYAN}Do you want to change the value of {Fore.RED}{d_type}?{Fore.RESET} (Y/N) ").lower() in "y1":
                        customers.at[id, d_type] = new_data
                    else:
                        print("\nUpdating value cancelled.")
                        pause()
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
                sel_rec = customers.loc[id]


def delete_customer(customers: pd.DataFrame):
    cls()
    id = input(f"{Fore.CYAN}Enter the customer ID to delete: {Fore.RESET}")
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
        pause()


# -----------------------------------------------------------------------------------------------------
def data_validator_product_bool(products, id, data, d_type):
    product = products.loc[id]
    if d_type == "id":
        return not (data in products.index)
    elif d_type in ["name", "manufacturer", "category"]:
        return data.isalpha()
    elif d_type == "Returnable":
        return data in ["Returnable", "Not Returnable", "Exchange-Only"]
    elif d_type == "In-Stock":
        return data.isdigit()
    elif d_type == "AvgRating":
        return re.fullmatch(r"[0-9]+\.?[0-9]*", data)
    elif d_type == "DaysToReturn":
        return (data == "-" and product["Returnable"] == "Not Returnable") or (type(data) == int and product["Returnable"] != "Not Returnable")


def add_a_Product(products: pd.DataFrame):
    print("+" + "-"*25 + "ADD A PRODUCT" + "-"*25 + "+" + "\n\n")  # GUI
    id = input(Fore.LIGHTMAGENTA_EX +
               "Enter ID (Leave blank for random uuid): " + Fore.RESET)
    # Verify that the product id is not a duplicate
    while id in products.index:
        throw_error('error', "Duplicate ID")
        id = input("\n"*5 + Fore.LIGHTMAGENTA_EX +
                   "Enter ID (Leave blank for random uuid): " + Fore.RESET)
    if id == "":  # Gen uuid if input is empty
        id = str(uuid.uuid4())
    cls()
    # name
    name = input(Fore.LIGHTMAGENTA_EX +
                 "Enter Product Name: " + Fore.RESET).capitalize()
    while not name.isalpha():
        throw_error('error', "Invalid Name")
        name = input("\n"*5 + Fore.LIGHTMAGENTA_EX +
                     "Enter Product Name: " + Fore.RESET)
    cls()
    # manufacturer
    manufacturer = input(Fore.LIGHTMAGENTA_EX +
                         "Enter manufacturer: " + Fore.RESET).capitalize()
    while not manufacturer.isalpha():
        throw_error('error', "Invalid manufacturer name")
        manufacturer = input("\n"*5 + Fore.LIGHTMAGENTA_EX +
                             "Enter manufacturer: " + Fore.RESET)
    cls()
    # category
    category = input(Fore.LIGHTMAGENTA_EX +
                     "Enter Category: " + Fore.RESET).capitalize()
    while not category.isalpha():
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
            throw_error('error', "Invalid Returnable: %s" % Returnable)
            Returnables_check = input(Fore.LIGHTMAGENTA_EX +
                                      "\nReturnable -> 1\nNot Returnable -> 2\nExchange-Only -> 3\nEnter Returnable: " + Fore.RESET).strip().lower().title()
    cls()
    # In-Stock
    stock = input(Fore.LIGHTMAGENTA_EX + "Enter In-Stock: " + Fore.RESET)
    while not stock.isdigit():
        throw_error(
            'error', "Invalid stock number: %s" % stock)
        stock = input(Fore.LIGHTMAGENTA_EX + "Enter In-Stock: " + Fore.RESET)
    cls()
    # AvgRating
    avg_rating = input(Fore.LIGHTMAGENTA_EX + "Enter AvgRating: " + Fore.RESET)
    while type(avg_rating) != float:
        try:
            avg_rating = float(avg_rating)
        except Exception as e:
            throw_error(
                'error', "Invalid Average Rating: %s" % avg_rating)
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
                    'error', "Invalid Days to Return: %s" % dtr)
                print("Return", Returnable)
                dtr = input(Fore.LIGHTMAGENTA_EX +
                            "Enter Days to Return: " + Fore.RESET)
    else:
        dtr = "-"
    # Data Summmarization
    NewData = [name, manufacturer, category,
               Returnable, stock, avg_rating, dtr]
    print("+" + "-"*50 + "+")
    if all(NewData):
        ll = max([len(str(x)) for x in NewData])
        fac = 62 if ll <= 62 else ll
        eq = ll - 62 if ll > 62 else 0
        print(f"""
    +{"=" * (eq//2)}============================Please Confirm the Data Input======================={"=" * ((eq//2) + (1 if eq % 2 != 0 else 0))}+
    | id           :    {id          }{" " * (fac - len(str(id          )))}|
    | name         :    {name        }{" " * (fac - len(str(name        )))}|
    | manufacturer  :    {manufacturer }{" " * (fac - len(str(manufacturer )))}|
    | category     :    {category    }{" " * (fac - len(str(category    )))}|
    | Returnable   :    {Returnable  }{" " * (fac - len(str(Returnable  )))}|
    | stock        :    {stock       }{" " * (fac - len(str(stock       )))}|
    | avg_rating   :    {avg_rating  }{" " * (fac - len(str(avg_rating  )))}|
    | dtr          :    {dtr         }{" " * (fac - len(str(dtr         )))}|
    +================================================================================{"=" * eq}+
    """)
        reck = input(
            "Would you like to insert this data to Products.csv ? (Y/N): ")
        if reck.lower() == "y":
            products.loc[id] = NewData
            print("Record inserted successfully!")
        else:
            print("Record Insertion Cancelled :(")
        time.sleep(1)
        pause()
    else:
        throw_error('error', f"Invalid Data",
                    'The data is invalid, please try again.')

# ----------------------------------------------------------------------------------------------------


def delete_product(products: pd.DataFrame):
    cls()
    id = input(f"{Fore.CYAN}Enter the product ID to delete: {Fore.RESET}")
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
        pause()


update_order_menu = {
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
    id = input(Fore.CYAN + "Product ID To Update: " + Fore.RESET).strip()
    if id not in products.index:
        throw_error('error', "ID not found: " + id,
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
            print(Fore.CYAN + f"""What would you like to Modify ?  Selected ID:{Fore.RED} {id}{Fore.RESET}
    1) id        
    2) name
    3) manufacturer 
    4) category       
    5) In-Stock    
    6) AvgRating   
    7) Returnable   
    8) Days to Return      
    9) Back     
            """)
            cmd = input(Fore.CYAN + "Choose To Modify: " + Fore.RESET)
            if cmd == "1":
                print(
                    Fore.CYAN + f"Updating Value of {Fore.RED}{update_order_menu[cmd]}" + Fore.RESET)
                print(Fore.CYAN +
                      f"Old value of {update_order_menu[cmd]}: {Fore.RED} {sel_rec.name}" + Fore.RESET)
                new_val = input(
                    Fore.CYAN + "Enter your new value: " + Fore.RESET)
                if new_val not in products.index and new_val != "" and len(new_val) >= 3:
                    products.rename(
                        index={sel_rec.name: new_val}, inplace=True)
                    print("ID changed successfully")
                    id = new_val
                    sel_rec = products.loc[id]
                else:
                    throw_error('error', f'Invalid product ID: {new_val}')
            elif cmd == "9" or cmd == "":
                break
            else:
                d_type = update_order_menu[cmd]
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
                    else:
                        print("\nUpdating value cancelled.")
                        pause()
                else:
                    throw_error('error', 'Error while updating product data',
                                "Please make sure you have entered the correct details.")
                sel_rec = products.loc[id]

# ----------------------------------------------------------------------------------------------------

def add_an_order(customers: pd.DataFrame, products: pd.DataFrame, orders: pd.DataFrame):
    print("+" + "-"*25 + "ADD AN ORDER" + "-"*25 + "+" + "\n\n")  # GUI
    # OrderID
    orderId = input(Fore.LIGHTMAGENTA_EX +
               "Enter ID (Leave blank for random uuid): " + Fore.RESET)
    while orderId in orders.index:
        throw_error('error', "Duplicate ID")
        orderId = input("\n"*5 + Fore.LIGHTMAGENTA_EX +
                   "Enter ID (Leave blank for random uuid): " + Fore.RESET)
    if orderId == "":  # Gen uuid if input is empty
        orderId = str(uuid.uuid4())
    cls()

    # CustomerID
    customerID = input(Fore.LIGHTMAGENTA_EX +
               "Enter Customer ID: " + Fore.RESET)
    while customerID not in customers.index:
        throw_error('error', "Customer ID not found!")
        customerID = input(Fore.LIGHTMAGENTA_EX +
               "Enter Customer ID: " + Fore.RESET)
    cls()
    # ProductID
    productID = input(Fore.LIGHTMAGENTA_EX +
               "Enter Product ID: " + Fore.RESET)
    while productID not in products.index:
        throw_error('error', "Product ID not found!")
        productID = input(Fore.LIGHTMAGENTA_EX +
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
    print(f"""{Fore.LIGHTRED_EX}
+============================= FORMAT =============================+
|   > The date must not be blank                                   |
|   > The date must be on the calander                             |
|   > The date must be in any of the following Formats             |
|        "16th Jan 2021"         OR      "16 Jan 2021"             |
|        "16th January 2021"     OR      "16 January 2021"         |
|        "dd/mm/yy"              OR      "dd/mm/yyyy"              |
+==================================================================+{Fore.RESET}\n\n\n""")
    doo_check = input(Fore.LIGHTMAGENTA_EX + "Enter Date of Order: " + Fore.RESET)
    doo = date_decoder(doo_check)
    while doo is None:  # Retake inputs for DOB till its valid
        throw_error('error', *data_error_msgs["dob"](doo_check))
        cls()
        print(f"""{Fore.LIGHTRED_EX}
+============================= FORMAT =============================+
|   > The date must not be blank                                   |
|   > The date must be on the calander                             |
|   > The date must be in any of the following Formats             |
|        "16th Jan 2021"         OR      "16 Jan 2021"             |
|        "16th January 2021"     OR      "16 January 2021"         |
|        "dd/mm/yy"              OR      "dd/mm/yyyy"              |
+==================================================================+{Fore.RESET}\n\n\n""")
        doo_check = input(Fore.LIGHTMAGENTA_EX + "Enter Date of Order: " + Fore.RESET)
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
    print("+" + "-"*50 + "+")
    if all(NewData):
        ll = max([len(str(x)) for x in NewData])
        fac = 62 if ll <= 62 else ll
        eq = ll - 62 if ll > 62 else 0
        print(f"""
    +{"=" * (eq//2)}=================================Please Confirm the Data Input============================{"=" * ((eq//2) + (1 if eq % 2 != 0 else 0))}+
    | OrderID               :    {orderId           }{" " * (fac - len(str(orderId           )))}|
    | CustomerID            :    {customerID        }{" " * (fac - len(str(customerID        )))}|
    | Customer (First Name) :    {cust_first_name   }{" " * (fac - len(str(cust_first_name   )))}|
    | Customer (Last Name)  :    {cust_last_name    }{" " * (fac - len(str(cust_last_name    )))}|
    | ProductID             :    {productID         }{" " * (fac - len(str(productID         )))}|
    | Product Name          :    {prod_name         }{" " * (fac - len(str(prod_name         )))}|
    | Quantity              :    {qty               }{" " * (fac - len(str(qty               )))}|
    | Total Price           :    {total_price       }{" " * (fac - len(str(total_price       )))}|
    | Date Of Order         :    {doo               }{" " * (fac - len(str(doo               )))}|
    | Status                :    {State             }{" " * (fac - len(str(State             )))}|
    | Address               :    {cust_address      }{" " * (fac - len(str(cust_address      )))}|
    +=========================================================================================={"=" * eq}+
    """)
        reck = input(
            "Would you like to insert this data to Orders.csv ? (Y/N): ")
        if reck.lower() == "y":
            orders.loc[orderId] = NewData
            print("Record inserted successfully!")
        else:
            print("Record Insertion Cancelled :(")
        time.sleep(1)
        pause()
    else:
        throw_error('error', f"Invalid Data",
                    'The data is invalid, please try again.')

def delete_order(orders: pd.DataFrame):
    cls()
    id = input(f"{Fore.CYAN}Enter the order ID to delete: {Fore.RESET}")
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
        pause()


update_order_menu = {
    "1" : "orderId",
    "2" : "customerID",
    "3" : "productID",
    "4" : "qty",
    "5" : "total_price",
    "6" : "doo",
    "7" : "State",
    "8": "Back"
}

def data_validator_order_bool(customers, products, orders, id, data, d_type):
    order = orders.loc[id]
    if d_type == "orderId":
        return not (data in orders.index)
    elif d_type in "customerID":
        return data in customers.index
    elif d_type in "products":
        return data in products.index
    elif d_type == "State":
        return data in ["Cancelled", "Delivered", "Pending", "Pre-Shipment", "Unshipped"]
    elif d_type == "qty":
        return data.isdigit()
    elif d_type == "total_price":
        return re.fullmatch(r"[0-9]+\.?[0-9]*", data)
    elif d_type == "doo":
        if date_decoder(data):
            return True
        else:
            return False


def update_order(customers: pd.DataFrame, products: pd.DataFrame, orders: pd.DataFrame):
    cls()
    id = input(Fore.CYAN + "Order ID To Update: " + Fore.RESET).strip()
    if id not in orders.index:
        throw_error('error', "ID not found: " + id,
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
            print(Fore.CYAN + f"""What would you like to Modify ?  Selected ID:{Fore.RED} {id}{Fore.RESET}
        1)  orderId
        2)  customerID
        3)  productID
        4)  qty
        5)  total_price
        6)  doo
        7)  State
        8)  Back
            """)
            cmd = input(Fore.CYAN + "Choose To Modify: " + Fore.RESET)
            if cmd == "1":
                print(
                    Fore.CYAN + f"Updating Value of {Fore.RED}{update_order_menu[cmd]}" + Fore.RESET)
                print(Fore.CYAN +
                      f"Old value of {update_order_menu[cmd]}: {Fore.RED} {sel_rec.name}" + Fore.RESET)
                new_val = input(
                    Fore.CYAN + "Enter your new value: " + Fore.RESET)
                if new_val not in orders.index and new_val != "" and len(new_val) >= 3:
                    orders.rename(
                        index={sel_rec.name: new_val}, inplace=True)
                    print("ID changed successfully")
                    id = new_val
                    sel_rec = orders.loc[id]
                else:
                    throw_error('error', f'Invalid order ID: {new_val}')
            elif cmd == "8" or cmd == "":
                break
            else:
                d_type = update_order_menu[cmd]
                print(Fore.CYAN +
                      f"Updating Value of {Fore.RED}{d_type}{Fore.CYAN}")
                print(
                    f"Old value of {d_type}: {Fore.RED}{sel_rec.loc[d_type]}{Fore.CYAN}")
                new_val = input(f"Enter your new value: {Fore.RED}")
                print(f"{Fore.CYAN}Your new value for {d_type}: " +
                      Fore.RED, new_val, Fore.RESET)
                if data_validator_order_bool(customers, products,  orders, id, new_val, d_type):
                    if input(f"{Fore.CYAN}Do you want to change the value of {Fore.RED}{d_type}?{Fore.RESET} (Y/N) ").lower() in "y1":
                        orders.at[id, d_type] = new_val
                        if d_type == "customerID":
                            cust = customers.loc[new_val]
                            orders.at[id, "customerFirstName"] = cust["first_name"]
                            orders.at[id, "customerLastName"] = cust["last_name"]
                            orders.at[id, "address"] = cust["address"]
                        elif d_type == "productID":
                            prod = products.loc[new_val]
                            orders.at[id, "productName"] = prod["name"]
                    else:
                        print("\nUpdating value cancelled.")
                        pause()
                else:
                    throw_error('error', 'Error while updating order data',
                                "Please make sure you have entered the correct details.")
                sel_rec = orders.loc[id]

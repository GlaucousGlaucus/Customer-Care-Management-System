import pandas as pd
from colorama import Fore
from datetime import datetime
import re

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


def print_text(Color, *text):
    print(f"{Color}{text}{Fore.RESET}")


class Searchy:

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def by_id(self, qry):
        qry_result = self.df.loc[qry] if qry in self.df.index else pd.DataFrame(
        )
        return qry_result

    def by_string(self, qry, col):
        qry_df = self.df[col]
        qry_result = self.df.loc[qry_df.str.contains(qry)]
        return qry_result

    def by_num(self, col: str):
        qry_df = self.df[col].replace("-", "0").astype(float)
        min, max = input(f"{Fore.LIGHTMAGENTA_EX}Enter Min: {Fore.RESET}"), input(
            f"{Fore.LIGHTMAGENTA_EX}Enter Max: {Fore.RESET}")
        if min == "":
            min = "0"
        if max == "":
            max = str(qry_df.max())
        try:
            min, max = float(min), float(max)
            qry_result = self.df.loc[(qry_df >= min) & (qry_df <= max)]
        except Exception as e:
            print(f"{Fore.RED}\nPlease enter a valid range!\n{Fore.RESET}")
            qry_result = pd.DataFrame()
        return qry_result

    def by_options(self, qry, col: str, options: dict, like=False):
        qry_df = self.df[col]
        if like:
            qry_result = self.df.loc[qry_df.str.contains(options[qry])]
        else:
            qry_result = self.df.loc[qry_df == options[qry]]
        return qry_result

    def by_date(self, col, format=r"%Y-%m-%d", time=False):
        qry_start = input(
            f"{Fore.RED}You can use RegEX\n{Fore.CYAN}Enter range for date \nStart: {Fore.RESET}")
        qry_end = input(f"{Fore.CYAN}End: {Fore.RESET}")
        qry_start, qry_end = pd.to_datetime(date_decoder(
            qry_start, time=time), format=format), pd.to_datetime(date_decoder(qry_end, time=time), format=format)
        if qry_start is None:
            return self.df
        if qry_end is not None:
            qry_df = (self.df[col] < qry_end) & (
                self.df[col] > qry_start)
            qry_result = self.df[qry_df]
        else:
            qry_df = self.df[col] > qry_start
            qry_result = self.df[qry_df]
        return qry_result


def pause(): return input('\n'*2 + "Press Any key To Contine...")
def cls(): return print("\n" * 49)


def throw_error(err_type: str, title: str, message=""):
    cls()
    if err_type == 'error':
        print(f"{Fore.RED} \u26A0 ERROR: {title} \u26A0")
        print(message, Fore.RESET)
    elif err_type == 'warning':
        print(f"! WARNING: {title} !")
        print(message)
    elif err_type == 'info':
        print(f"INFO: {title}{message}")
    else:
        print(f"======================{title}======================")
        print(message)
    pause()


def phone_validator(original: str):
    original = original.split(" ")
    if original[0][0] == "+":
        original[0] = original[0][1:]
    PatternA = re.compile("(0-91)?")
    PatternB = re.compile("[0-9]{10}")
    lhs = "".join(original[1:])
    if PatternA.match(original[0]) and PatternB.match(lhs):
        return f"+{original[0]} {lhs[:3]} {lhs[3:6]} {lhs[6:10]}"
    else:
        None


def validate_email(email):
    reg_email = re.fullmatch(
        r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email)
    return reg_email if len(email) >= 3 else None


def date_decoder(date, time=False, dob_chck=False):
    d, m, y, hrs, min, sec = None, None, None, None, None, None
    M = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
         'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    try:
        if time:
            date = date.split(' ')
            time, date = date[-1], " ".join(date[:len(date)-1])
            time = time.split(':')
            hrs, min, sec = time[0], time[1], time[2]
        if " " in date:
            date = date.split(" ")
            if str(date[1]).isdigit() or len(date) != 3:
                return None
            d, m, y = date[0].replace("th", "").replace("st", "").replace("rd", "").replace("nd", ""), M.index(
                str((date[1][:3]).lower()).capitalize()) + 1, date[2]
        elif "/" in date:
            date = date.split("/")
            d, m, y = date
        else:
            return None
        if time:
            datetime(year=int(y), month=int(m), day=int(d),
                     hour=int(hrs), minute=int(min), second=int(sec))
        else:
            datetime(year=int(y), month=int(m), day=int(d))
        if len(y) == 2:
            y = "20" + y
        if dob_chck and y > str(datetime.today().year):
            raise ValueError(
                "Invalid DOB \n year of birth cannot be greater then this year!")
        if time:
            return pd.to_datetime(f"{int(y)}-{int(m)}-{int(d)} {hrs}:{min}:{sec}")
        else:
            return pd.to_datetime(f"{int(y)}-{int(m)}-{int(d)}")
    except Exception as e:
        #throw_error('error', 'INVALID DATE', f'{d, m, y} \n {e}')
        return None


def data_validator_customer(data, d_type):
    if d_type in ["first_name", "last_name", "country", "city", "state"]:
        return data if all(c.isalpha() for c in data.split(" ")) else None
    elif d_type == "dob":
        return date_decoder(data, dob_chck=True)
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


def data_validator_product_bool(products: pd.DataFrame, id, data, d_type):
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


def data_validator_order_bool(customers: pd.DataFrame, products: pd.DataFrame, orders: pd.DataFrame, id, data, d_type):
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


def data_validator_ticket_bool(customers: pd.DataFrame, products: pd.DataFrame, orders: pd.DataFrame, tickets: pd.DataFrame, id, data, d_type):
    ticket = tickets.loc[id]
    if d_type == "TicketID":
        return not (data in tickets.index)
    elif d_type in "CustID":
        return data in customers.index
    elif d_type in "OrderID":
        return data in orders.index
    elif d_type == "Status":
        return data in ["Open", "Closed"]
    elif d_type in ["IssueCategory", "Issue"]:
        return True
    elif d_type == "Replies":
        return data.isdigit()
    elif d_type in ["HoursTaken", "FirstResponseTime", "CustomerSatisfaction"]:
        return re.fullmatch(r"[0-9]+\.?[0-9]*", data)
    elif d_type in ["DateOpened", "DateClosed"]:
        if date_decoder(data, time=True):
            return True
        else:
            return False


def safe_input(text:str, fail_text:str=None, dtype:str="int"):
    fail_text = f"Please Enter Data as {dtype}" if fail_text is None else fail_text
    try:
        match dtype:
            case "int":
                return int(input(text))
            case "float":
                return float(input(text))
    except ValueError as e:
        throw_error(err_type="error", title="Wrong Value", message=fail_text)
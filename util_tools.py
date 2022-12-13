import numpy as np
import pandas as pd
from colorama import Fore
from datetime import datetime
import re
import smtplib
import os
import random
from email.message import EmailMessage

# Constants
lemon_constants = {
    'affirmative-confirmation': "y1"
}

# -------------------

email_format_info = f"""{Fore.LIGHTRED_EX}
                              ╔═╗╔═╗╦═╗╔╦╗╔═╗╔╦╗
                              ╠╣ ║ ║╠╦╝║║║╠═╣ ║ 
                              ╚  ╚═╝╩╚═╩ ╩╩ ╩ ╩ 
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
The email address:
> Should at least three characters long
> Should have a valid Username: 
    a) Can have A-Z and a-z characters
    b) Can have digits and special characters (_%+-)
> Should have the '@' separator
> Should have valid domain name:
    a) Can have A-Z and a-z characters
    b) Can have digits and hyphen (-) no special characters
> Should have valid top level domain name:
    a) Can have A-Z and a-z characters
    b) Can have digits and hyphen (-) no special characters

▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
{Fore.RESET}\n\n\n"""

phone_format_info = f"""{Fore.LIGHTRED_EX}
                              ╔═╗╔═╗╦═╗╔╦╗╔═╗╔╦╗
                              ╠╣ ║ ║╠╦╝║║║╠═╣ ║ 
                              ╚  ╚═╝╩╚═╩ ╩╩ ╩ ╩ 
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
Please make sure that you enter the correct format for phone.

    > It should not be blank.
    > The first two digits of the phone must be between 0 and 91 (inclusive).
    > There must be a space after the first two digits of the phone.
    > The other digits of the phone must be between 0 and 9 (inclusive).

You can enter the phone number in either of the formats given below:

                    +XX XXX XXX XXXX OR +XX XXXXXXXXXX

▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
{Fore.RESET}\n\n\n"""

dateformat_info = f"""{Fore.LIGHTRED_EX}
                              ╔═╗╔═╗╦═╗╔╦╗╔═╗╔╦╗
                              ╠╣ ║ ║╠╦╝║║║╠═╣ ║ 
                              ╚  ╚═╝╩╚═╩ ╩╩ ╩ ╩ 
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
   > The date must not be blank                                   
   > The date must be on the calender      
   > The date must not be in the future                  
   > The date must be in any of the following Formats             
        
            "16th Jan 2021"         OR          "16th January 2021"
            "16 Jan 2021"           OR          "16 January 2021"  
            "dd/mm/yy"              OR          "dd/mm/yyyy" 

▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
{Fore.RESET}\n\n\n"""

datetimeformat_info = f"""{Fore.LIGHTRED_EX}
                              ╔═╗╔═╗╦═╗╔╦╗╔═╗╔╦╗
                              ╠╣ ║ ║╠╦╝║║║╠═╣ ║ 
                              ╚  ╚═╝╩╚═╩ ╩╩ ╩ ╩ 
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
   > The date must not be blank                                   
   > The date must be on the calender      
   > The date must not be in the future       
   > The time must be in the format {Fore.LIGHTCYAN_EX}hh:mm:ss{Fore.LIGHTRED_EX}
   > The time must be in 24-hr time format
   > Do to give a space between the date and the time{Fore.LIGHTGREEN_EX}
        Correct       -->  "16th Jan 2021 12:42:35" {Fore.LIGHTYELLOW_EX}   
        InCorrect     -->  "16th Jan 2021  12:42:35" 
                                          ↑
                                Should be exactly One Space {Fore.LIGHTRED_EX}           
   > The date must be in any of the following Formats             
        
    "16th Jan 2021 {Fore.LIGHTCYAN_EX}12:42:35"{Fore.LIGHTRED_EX}       OR    
    "16 Jan 2021 {Fore.LIGHTCYAN_EX}12:42:35"{Fore.LIGHTRED_EX}         OR
    "16th January 2021 {Fore.LIGHTCYAN_EX}12:42:35"{Fore.LIGHTRED_EX}   OR        
    "16 January 2021 {Fore.LIGHTCYAN_EX}12:42:35{Fore.LIGHTRED_EX}      OR    
    "dd/mm/yy {Fore.LIGHTCYAN_EX}hh:mm:ss"{Fore.LIGHTRED_EX}            OR
    "dd/mm/yyyy {Fore.LIGHTCYAN_EX}hh:mm:ss"{Fore.LIGHTRED_EX}          

▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
{Fore.RESET}\n\n\n"""

data_error_msgs = {
    "id": lambda df_id: (f'Duplicate ID: {df_id}', "\n> ID should be a unique ID."),
    "first_name": lambda first_name: (f'Invalid Firstname: {first_name}',
                                      "\n> First Name should only have alphabets and must not be blank!\n\n"),
    "last_name": lambda last_name: (f'Invalid Lastname: {last_name}',
                                    "\n> Last Name should only have alphabets and must not be blank!\n\n"),
    "dob": lambda dob_check: (f'Invalid Date: {dob_check}', f"""Please make sure you have a entered a valid date."""),
    "gender": lambda gender_check: (f'Invalid gender: {gender_check}',
                                    "Make sure you have entered a valid gender."),
    "address": 0,
    "country": lambda country: (f'Invalid Country: {country}', "\n  Country should only have alphabets."),
    "city": lambda city: (f'Invalid City: {city}', "\n  City should only have alphabets."),
    "state": lambda state: (f'Invalid State: {state}', "\n  State should only have alphabets."),
    "pincode": lambda pincode: (f'Invalid Pincode: {pincode}', "\n  Pincode should only have digits."),
    "phone": lambda phone: (f"Invalid phone number: {phone}", """Phone must be a valid Phone.

1) It should not be blank.
2) The first two digits of the phone must be between 0 and 91 (inclusive).
3) The other digits of the phone must be between 0 and 9 (inclusive).

Input Format: +XX XXX XXX XXXX OR +XX XXXXXXXXXX

Avoid the above errors and try again.
        """),
    "email": lambda email: (f"Invalid email address: {email}", """
The email address should be:

1) At least three characters long
2) Should have a valid Username: 
    a) Can have A-Z and a-z characters
    b) Can have digits and special characters (_%+-)
3) Should have the '@' character
4) Should have valid Mail server name:
    a) Can have A-Z and a-z characters
    b) Can have digits and hyphen (-) no special characters
5) Should have valid top level domain name:

Avoid the above errors and try again.
        """),
    "prime": 0,
}


# Methods to save files


def SaveData(df: pd.DataFrame, filename: str): return df.to_csv(
    f'Data\\{filename}.csv')


def print_text(color, *text):
    print(f"{color}{text}{Fore.RESET}")


class CustomSearcher:

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def by_id(self, qry):
        qry_result = self.df.loc[qry] if qry in self.df.index else pd.DataFrame(
        )
        return qry_result

    def by_single(self, qry, col):
        qry_df = self.df[col]
        qry_result = self.df.loc[qry_df == qry]
        return qry_result

    def by_string(self, qry, col):
        qry_df = self.df[col]
        qry_result = self.df.loc[qry_df.str.contains(qry)]
        return qry_result

    def by_num(self, col: str):
        qry_df = self.df[col].replace("-", "0").astype(float)
        range_min, range_max = input(f"{Fore.LIGHTMAGENTA_EX}Enter Min: {Fore.RESET}"), input(
            f"{Fore.LIGHTMAGENTA_EX}Enter Max: {Fore.RESET}")
        if range_min == "":
            range_min = "0"
        if range_max == "":
            range_max = str(qry_df.max())
        try:
            range_min, range_max = float(range_min), float(range_max)
            qry_result = self.df.loc[(qry_df >= range_min) & (qry_df <= range_max)]
        except ValueError:
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

    def by_date(self, col, formatting=r"%Y-%m-%d", time=False):
        if time:
            print(datetimeformat_info)
        else:
            print(dateformat_info)
        qry_start = input(
            f"{Fore.RED}You can use RegEX\n{Fore.CYAN}Enter range for date \nStart: {Fore.RESET}")
        qry_end = input(f"{Fore.CYAN}End: {Fore.RESET}")
        qry_start, qry_end = pd.to_datetime(date_decoder(
            qry_start, time=time), format=formatting), pd.to_datetime(date_decoder(qry_end, time=time),
                                                                      format=formatting)
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


def pause(): return input('\n' * 2 + "Press ENTER To Continue...")


def cls(): return print("\n" * 2)


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
    pattern = '\\+?([0-9]{1,2})?(\\s*)?[0-9]{3}(\\s*)?[0-9]{3}(\\s*)?[0-9]{4}'
    if re.fullmatch(pattern, original):
        if original[0] == "+":
            original = original[1:]
        original = "".join(original.split(" "))
        print(original)
        n = len(original) - 10
        return f"+{original[:n]} {original[n:n + 3]} {original[n + 3:n + 6]} {original[n + 6:]}"


def validate_email(email):
    reg_email = re.fullmatch(
        r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]+', email)
    return reg_email if len(email) >= 3 else None


def date_decoder(date, time=False, dob_check=False):
    d, m, y, hrs, minutes, sec = None, None, None, None, None, None
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    try:
        if time:
            date = date.split(' ')
            time, date = date[-1], " ".join(date[:len(date) - 1])
            time = time.split(':')
            hrs, minutes, sec = time[0], time[1], time[2]
        if " " in date:
            date = date.split(" ")
            if str(date[1]).isdigit() or len(date) != 3:
                return None
            d, m, y = date[0].replace("th", "").replace("st", "").replace("rd", "").replace("nd", ""), months.index(
                str((date[1][:3]).lower()).capitalize()) + 1, date[2]
        elif "/" in date:
            date = date.split("/")
            d, m, y = date
        else:
            return None
        if time:
            datetime(year=int(y), month=int(m), day=int(d),
                     hour=int(hrs), minute=int(minutes), second=int(sec))
        else:
            datetime(year=int(y), month=int(m), day=int(d))
        if len(y) == 2:
            y = "20" + y
        if dob_check and y > str(datetime.today().year):
            raise ValueError(
                "Invalid DOB \n year of birth cannot be greater then this year!")
        if time:
            return pd.to_datetime(f"{int(y)}-{int(m)}-{int(d)} {hrs}:{minutes}:{sec}")
        else:
            return pd.to_datetime(f"{int(y)}-{int(m)}-{int(d)}")
    except Exception:
        # throw_error('error', 'INVALID DATE', f'{d, m, y} \n {e}')
        return None


def data_validator_customer(data, d_type):
    if d_type in ["first_name", "last_name", "country", "city", "state"]:
        return data if all(c.isalpha() for c in data.split(" ")) else None
    elif d_type == "dob":
        return date_decoder(data, dob_check=True)
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
        return "PRIME" if data.strip().lower() in ["prime", "yes", "1", "y", "p"] else "NOT PRIME"


def data_validator_product_bool(products: pd.DataFrame, product_id, data, d_type):
    product = products.loc[product_id]
    if d_type == "id":
        return not (data in products.index)
    elif d_type in ["name", "manufacturer", "category"]:
        return is_alpha_whitespace(data)
    elif d_type == "Returnable":
        return data in ["Returnable", "Not Returnable", "Exchange-Only"]
    elif d_type == "In-Stock":
        return data.isdigit()
    elif d_type == "AvgRating":
        return re.fullmatch(r"[0-9]+\.?[0-9]*", data)
    elif d_type == "DaysToReturn":
        return (data == "-" and product["Returnable"] == "Not Returnable") or (
                    type(data) == int and product["Returnable"] != "Not Returnable")


def data_validator_order_bool(customers: pd.DataFrame, products: pd.DataFrame, orders: pd.DataFrame, data, d_type):
    if d_type == "orderId":
        return not (data in orders.index)
    elif d_type in "customerID":
        return data in customers.index
    elif d_type in "productID":
        return data in products.index
    elif d_type == "status":
        return data in ["Cancelled", "Delivered", "Pending", "Pre-Shipment", "Unshipped"]
    elif d_type == "qty":
        return data.isdigit()
    elif d_type == "totalPrice":
        return re.fullmatch(r"[0-9]+\.?[0-9]*", data)
    elif d_type == "dateofOrder":
        if date_decoder(data):
            return True
        else:
            return False


def data_validator_ticket_bool(customers: pd.DataFrame, orders: pd.DataFrame,
                               tickets: pd.DataFrame, data, d_type):
    if d_type in ["TicketID", "CustID", "OrderID"] and data.isdigit():
        data = int(data)
    if d_type == "TicketID":
        return not (data in tickets.index)
    elif d_type in "CustID":
        return data in customers.index
    elif d_type in "OrderID":
        return data in orders.index
    elif d_type == "Status":
        return data in ["Open", "Closed"]
    elif d_type == "IssueCategory":
        return data in ["Damaged product", "Info", "Different from product description", "Part missing",
                        "Received the wrong product", "Other"]
    elif d_type == "Issue":
        return True
    elif d_type == "Replies":
        return data.isdigit()
    elif d_type in ["HoursTaken", "FirstResponseTime", "CustomerSatisfaction(%)"]:
        return re.fullmatch(r"[0-9]+\.?[0-9]*", data)
    elif d_type in ["DateOpened", "DateClosed"]:
        if date_decoder(data, time=True):
            return True
        else:
            return False


def safe_input(text: str, fail_text: str = None, d_type: str = "int", can_be_nan=False):
    fail_text = f"Please Enter Data as {d_type}" if fail_text is None else fail_text
    inpt = input(text).strip()
    try:
        match d_type:
            case "int":
                return int(inpt)
            case "float":
                return float(inpt)
    except ValueError:
        if inpt == "-" and can_be_nan:
            return np.nan
        throw_error(err_type="error", title="Wrong Value", message=fail_text)


def show_chat(data: pd.DataFrame):
    cls()
    data.sort_values(['Date'])
    for _, row in data.iterrows():
        color = Fore.LIGHTGREEN_EX if row['Side'] == 'ADMIN' else Fore.LIGHTCYAN_EX
        print(
            color, f"[{row['Side']} @ {Fore.YELLOW}{row['Date']}{color}]:\n\t {row['Message']}", Fore.RESET)


def is_alpha_whitespace(s): return all(x.isalpha() for x in s.split(" "))


def forgot_pass_mail(customers: pd.DataFrame, receiver: str):
    qry_df = customers[customers["email"] == receiver]
    if len(qry_df) == 0:
        raise Exception(f"Customer with email {receiver} does not exist")
    if len(qry_df) != 1:
        raise Exception(f"Multiple customers with email {receiver} exist")

    passs, sender = None, None
    try:
        passs = os.environ['EMAIL_PASS']
        sender = os.environ['EMAIL_EMAIL']
    except KeyError:
        throw_error('error', 'Environ variable not found', f"""
        
        You must set the {Fore.LIGHTGREEN_EX}EMAIL_PASS{Fore.RED} and {Fore.LIGHTGREEN_EX}EMAIL_EMAIL{Fore.RED} environment variables.
        where {Fore.LIGHTGREEN_EX}EMAIL_PASS{Fore.RED} is your APP PASSWORD 
        and {Fore.LIGHTGREEN_EX}EMAIL_EMAIL{Fore.RED} is your email address

        You can get your APP PASSWORD from here: https://myaccount.google.com/apppasswords
        and set the environment variables:
        {Fore.LIGHTGREEN_EX}EMAIL_PASS : YOUR APP PASSWORD{Fore.RED} 
        {Fore.LIGHTGREEN_EX}EMAIL_EMAIL: YOUR EMAIL ADDRESS{Fore.RED}

        NOTE: You must have 2 Factor authentication enabled on your google account as a sender.
        
        """)

    # receiver = sender

    # Generate the email
    msg = EmailMessage()
    msg['Subject'] = 'Forgot Password/ID'
    msg['From'] = sender
    msg['To'] = receiver

    # Setup otp, id and timer
    otp = random.randint(10000, 99999)
    customer_id = qry_df.index.values[0]

    # Generate email message
    msg.set_content("""
    <!DOCTYPE html>
    <html>
    <head>
    <style> 
    .div1 {
      width: 300px;
      height: 300px;
      border-style: ridge none none ridge;
      padding: 50px;
      background-color:#264653
    }
    </style>
    </head>
    <body>
        <h1 style="background-color:#2A9D8F;font-family:verdana;color:#E9C46A;text-align:center;">LEMON BEE</h1>
        <hr>
        <div class="div1">
            <h3 style="font-family:verdana;color:#FFFFFF">Forgot Password/ID</h3>
            <p style="color:#E76F51">
            Hello, <br>
            Your ID is """ + str(customer_id) + """<br><br>
            To change your password please enter the otp given below in our software:
            <br><br>
            OTP: """ + str(otp) + """
            </p>
        </div>
        <br>
    </body>
    </html>
    """, subtype='html')

    # Send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender, passs)
        smtp.send_message(msg)

    # Check and action
    time_sent = datetime.now()
    cls()
    otp_in = safe_input(
        Fore.LIGHTMAGENTA_EX + "We have sent you an OTP on your mail \nplease enter it it proceed.\n\nEnter OTP: " + Fore.RESET)
    if otp_in != otp:
        raise Exception(f"Otp is not valid. Please try again.")
    if (datetime.now() - time_sent).seconds > 5 * 60:
        raise Exception("OTP has expired. Please try again.")
    while True:
        cls()
        new_pass = input(Fore.LIGHTMAGENTA_EX + "New Password: " + Fore.RESET).strip()
        if new_pass == passs:
            throw_error('error', 'Invalid password', "Password cannot be your Old Password. Please try again.")
            continue
        if new_pass in customers['password'].values:
            throw_error('error', 'Invalid password', "Password is already in use. Please try again.")
            continue
        customers.at[customer_id, 'password'] = new_pass
        SaveData(customers, "Customers")
        break
    print("Password successfully changed!")


def qry_df_final_func(df: pd.DataFrame, cmd: str, options: list, search_engine: CustomSearcher,
                      qry_result: pd.DataFrame):
    if cmd in options:
        print(f"\n\n{Fore.CYAN}Your Query Result: {Fore.RESET}\n")
        if not qry_result.empty:
            print(qry_result)
            if cmd != "1":
                udf = input(
                    f"{Fore.CYAN}Do you want to use the above dataframe for rest of the queries?\n(Y/N): {Fore.RESET}")
                if udf.strip().lower() in lemon_constants['affirmative-confirmation']:
                    return qry_result.copy(), CustomSearcher(qry_result.copy())
        else:
            print(f"\nEmpty dataframe\n")
    return df, search_engine

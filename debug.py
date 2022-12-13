import pandas as pd
from colorama import Fore
from datetime import datetime
import re
import smtplib
import os
import random
from email.message import EmailMessage

passs, sender = None, None

try:
    passs = os.environ['EMAIL_PASS']
    sender = os.environ['EMAIL_EMAIL']
except KeyError as e:
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

reciever = "arpitbenjamin20055@gmail.com"

# Generate the email
msg = EmailMessage()
msg['Subject'] = 'Forgot Password/ID'
msg['From'] = sender
msg['To'] = reciever

# Setup otp, id and timer
otp = random.randint(10000, 99999)
Id = 1

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
        Your ID is """ + str(Id) + """<br><br>
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

import pandas as pd
import smtplib
import os
import random
from email.message import EmailMessage

customers = pd.read_csv('Data\Customers.csv', index_col='id')

passs = os.environ['EMAIL_PASS']
sender = os.environ['EMAIL_EMAIL']
reciever = 'ashishbenjamin38@gmail.com'
reciever = sender

msg = EmailMessage()
msg['Subject'] = 'Forgot Password/ID'
msg['From'] = sender
msg['To'] = reciever
otp = random.randint(10000, 99999)
Id = random.randint(1, 1000)
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


#with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
#with smtplib.SMTP('localhost', 1025) as smtp:
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    #smtp.ehlo()
    #smtp.starttls()
    #smtp.ehlo()

    smtp.login(sender, passs)

##    subject = 'Ttest'
##    body = """
##Hello, This email was sent using python
##"""
##    msg = f"Subject: {subject}\n\n{body}"

    smtp.send_message(msg)


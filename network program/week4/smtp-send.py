from email import message
import smtplib

message = """Hello world
From : Nari | window os"""

try:
    smtp = smtplib.SMTP("10.4.15.22")
    smtp.sendmail('heart','eiei',message)
    print("Email sent successfully")
except Exception as err:
    print(str(err))
##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)




import datetime as dt
import pandas as pd
import random
import smtplib
from email.message import EmailMessage
email = "chilakamanikanta5@gmail.com"
password = "ldocbnmrlhjvbmes"  
email_to = "manikantasonny@gmail.com"

target_word = "[NAME]"
second_target = "Angela"

now = dt.datetime.now()
month_date = (now.month, now.day)
print(month_date)
print(type(month_date))

df = pd.read_csv(r"D:\Python Code\Day_32_ABW\006 birthday-wisher-hard-start\birthdays.csv")
birthday_dicts = {(newkey["month"], newkey["day"]) : newkey.to_dict() for index, newkey in df.iterrows()}
# print(birthday_dicts)
if month_date in birthday_dicts:
    num = random.randint(1,3)
    with open(f"D:/Python Code/Day_32_ABW/006 birthday-wisher-hard-start/letter_templates/letter_{num}.txt", "r") as data_file:
        data = data_file.read()
        # print(data)
        updated_content = data.replace(target_word, birthday_dicts[month_date]["name"])
        updated_content = updated_content.replace(second_target, "Manikanta Chilaka")
        print(updated_content)
        msg = EmailMessage()
        msg.set_content(updated_content)
        msg['Subject'] = "Happy Birthday"
        msg["From"] = email
        msg["To"] = email_to

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(email, password)
            smtp.send_message(msg)
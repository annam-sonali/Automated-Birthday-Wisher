# 🎉 Automated Birthday Wisher

Never forget a birthday again!  
This project automatically sends birthday wishes to your friends, family, or team members on their special day — completely hands-free. 🥳  

You can configure it to send messages via **email**, **WhatsApp**, or **SMS**, and even schedule it to run every day using **cron jobs** or **Windows Task Scheduler**.

---

## 🚀 Features

- 🗓️ Automatically checks today’s date against a stored list of birthdays  
- 💌 Sends a personalized birthday message (via Email, WhatsApp, or SMS)  
- 🧠 Remembers past birthdays (to avoid duplicate wishes)  
- 💬 Customizable messages for each person  
- 🕐 Can run daily automatically (via `cron` or `schedule` library)

---

## 🧰 Tech Stack

- **Python 3.9+**
- [**pandas**](https://pandas.pydata.org/) – manage birthday data  
- [**smtplib**](https://docs.python.org/3/library/smtplib.html) – send emails  
- [**pywhatkit**](https://pypi.org/project/pywhatkit/) – send WhatsApp messages  
- [**schedule**](https://pypi.org/project/schedule/) – automate daily runs  

---

## 🗂️ Project Structure


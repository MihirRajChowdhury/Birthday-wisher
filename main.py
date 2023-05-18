import datetime as dt
import smtplib
import pandas
import random

now = dt.datetime.now()
today_day = now.day
today_month = now.month
today = (today_day, today_month)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if (today_month, today_day) in birthdays_dict:
    birthdays_peron = birthdays_dict[(today_month, today_day)]

    letter_no = random.randint(1, 3)
    with open(file=f"letter_templates/letter_{letter_no}.txt") as letter_file:
        letter_data = letter_file.read()
        new_letter = letter_data.replace("[NAME]",birthdays_peron["name"])

        my_email = "tcode8449@gmail.com"
        my_password = "yrrnixwdwdcdqkox"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=birthdays_peron["email"],
                                msg=f"Subject:Happy Birthday \n\n {new_letter}")

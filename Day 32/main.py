import api_keys
import random
import smtplib
import pandas
import datetime

PLACEHOLDER = "[NAME]"
now = datetime.datetime.now()
data = pandas.read_csv("birthdays.csv")

for index, row in data.iterrows():
    if row["month"] == now.month:
        if row["day"] == now.day:
            random_number = random.randint(1, 3)
            with open(f"letter_{random_number}.txt", mode = "r") as letter_file:
                x = letter_file.read()
                letter_to_send = x.replace(PLACEHOLDER, row["name"])
                final_to_send = letter_to_send.replace("Angela", "Daniel")
            with smtplib.SMTP(host="smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=api_keys.my_email, password=api_keys.password)
                connection.sendmail(
                    from_addr=api_keys.my_email,
                    to_addrs=row["email"],
                    msg=f"Happy birthday\n\n{final_to_send}"
                )

        else:
            print("It is not birthday day")
    else:
        print("it is not birthday month")

import smtplib
import random
import datetime as dt
import api_keys


# with smtplib.SMTP(host="smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="dani.ghebrat@gmail.com",
#         msg="Subject:Yooo\n\nThis is the body"
#     )




now = dt.datetime.now()
print(now.weekday())
if now.weekday() == 4:
    with open("quotes.txt") as file:
        x = file.readlines()
        random_quote = random.choice(x)
        print(random_quote)
    with smtplib.SMTP(host="smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=api_keys.my_email, password=api_keys.password)
        connection.sendmail(
            from_addr=api_keys.my_email,
            to_addrs=api_keys.password,
            msg=f"Subject:Motivational\n\n{random_quote}"
        )

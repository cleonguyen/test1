from datetime import date

wallet = 41
print(wallet)

wallet = 32
print(wallet)

day = "16th Jan 2025"
print(day)

date = date.today() #Initially did not import date from datetime (required for date format)
print(date)
# Correct the date assignment
date_today = date.fromisocalendar(2025,1,5).weekday()
print(date_today)
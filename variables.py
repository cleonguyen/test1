from datetime import date

wallet = 41
print(wallet)

wallet = 32
print(wallet)

day = "16th Jan 2025"
print(day)

date = date.today() #Initially did not import date from datetime (required for date format)
print(date)

date_today = date.fromisocalendar(2025,1,5).weekday()
print(date_today)

day = 21
temp =-15
weight = 190.468 #decimal called float (+/-)
print(weight*2)

flour = 250
dad_weight = 76.5

shirt = "blue" #text called string, needs "" or ''
print(shirt)

store = "Nick's Pizza Shop, the 'best' there is" #if quoting can use \ to indicate e.g. "Nick\'s 
store = 'Nick\'s Pizza Shop, the "best" there is' # or using apostrophes
print(store)
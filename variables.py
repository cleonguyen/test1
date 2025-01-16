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

day = 16
month = "January"
temp = -15 

print(f"Today is {month} {day} and it is {temp} degrees outside") #f-string at the front of text to insert variables into string

light_is_on = True #boolean, doens't need quotes, because it will become a string (True or False only)
if light_is_on:
    print("The light is on!") #needs the tab or | to indicate it is part of the if statement
else:
    print("We're in the dark!") #if var light_is_on is False, will run else statement

dad_weight = 76.5
if dad_weight < 100: #condition if ____ : , == exactly != not equal to
    print("You're not overweight, probably...")
else:
    print("You gotta exercise more!")


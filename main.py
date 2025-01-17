fav_movies = ["Heretic", "Godzilla vs Kong", "The Matrix"]
print(fav_movies[0])

# Lists uses 0 based counting, i.e. 0 = Heretic, 1 = Godzilla vs Kong, 2 = The Matrix...

fav_numbers = [7, 13, 21]
print(fav_numbers[0])

# Find out no. of items in list
print(len(fav_movies))  # len for length

fav_movies.append("Iron Man")
print(len(fav_movies))
print(fav_movies)

# How to place new list item in specific location
fav_movies.insert(1, "Batman")  # add in 2nd position
print(fav_movies)

del (fav_movies[2])  # delete 3rd item
print(fav_movies)

# For loop
for number in range(10):  # Go through 10 times, print Hello
    print("Hello")
    # Prints 0-9, reminder that starts from 0, remember to name variables well to be easily understood
    print(number)

fav_movies = ["Heretic", "Godzilla vs Kong", "The Matrix"]
for movie in fav_movies:
    print(movie)

for number in range(40):  # since counter is from 0, remember to add variable + 1 to get 1-40
    print((number + 1) * 2)

# lists - key value pairs
# dictionaries have curly brackets {}

cats = {"Bubbles": 6, "Tom": 3, "Jinxy": 8}
print(cats)

# print value of key Tom, NB: case sensitive - can only use the 'key' to get the value (age)
print(cats["Tom"])

cats["Willow"] = 1
print(cats)

# note cannot use insert for dictionaries, only append


# creating functions
def bark():  # colon tabbed over, belongs to thing above it
    print("Woof woof!")
    print("I'm a dog!")


bark()  # calling the function

for x in range(20):
    bark()


def hello():
    print("Hello Dad :D")


hello()

# parameters can go inside the ()


def hello(name):
    print(f"Hello {name}!")


hello("Dad")


def add_numbers(num1, num2):
    print(num1 + num2)


add_numbers(4, 5)


def doginfo(name, age):  # parameters
    print(f"Hi my name is {name} and I am {age} years old")


doginfo("Minnie", 4)  # put in the user input into function


def double(number):
    return number * 2  # return is used to give back a value to the caller


# new_number is the variable that will store the value of the function - just enter value into function
new_number = double(5)
print(new_number)


def uppercase(text):
    return text.upper()


print(uppercase("nick"))

names = ["Nick", "Bob", "Sue"]

for name in names:
    print(uppercase(name))

wallet = 40
wallet -= 8  # I bought some food
wallet += 40  # I got paid

# comments to code to explain what is happening


user_text = input("Enter some text: ")
print(user_text.upper())

# input from the console comes through as a string, so need to convert to number if want to do maths
user_number = input("Enter a number you want to double: ")
print(int(user_number) * 2)  # convert to integer

# upper or lowercase
user_text = input("Enter some text: ")

upper_or_lower = input("Enter 1 to uppercase or 2 to lowercase: ")
if upper_or_lower == "1":
    print(user_text.upper())
else:
    upper_or_lower == "2"
    print(user_text.lower())
print("FINITO :D")

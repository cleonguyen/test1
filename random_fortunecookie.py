import random

# Generate a random integer between 1 and 10
random_number = random.randint(1, 10)
print(random_number)


print(random.random())  # random float between 0 and 1pi

answer = random.randint(1, 3)
if answer == 1:  # comparing things need ==
    print("Yes")
if answer == 2:
    print("No")
if answer == 3:
    print("Maybe")

lucky_number = random.randint(1, 100)

fortune_number = random.randint(1, 3)

fortune_text = ""
if fortune_number == 1:
    fortune_text = "You will have a great day!"
if fortune_number == 2:
    fortune_text = "Today will be tough but worth it"
if fortune_number == 3:
    fortune_text = "You will get $$$ this year!"

# remember need f string and need {} to insert variable
print(f"{fortune_text} Your lucky number is: {lucky_number}!")

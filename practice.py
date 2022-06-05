birthdays = {'Janeta':'18th Sept','Amelia' : '20th June','Milly' : '10 May'}
print(birthdays.keys())
print(list(birthdays.keys()))
print(list(birthdays.values()))
print(list(birthdays.items()))

string = input("Enter your name and profession: ")
characters = {}
for character in string:
    characters.setdefault(character,0)
    characters[character] = characters[character] + 1
print(characters)


#Magic 8 ball game
import random
user_input = input("Enter your question here: ")
random_number = random.randint(1,9)
if random_number == 0:
    print("You have a bright future")
elif random_number == 1:
    print("You are optimistic")
elif random_number == 3:
    print("You have a successful future")
elif random_number == 4:
    print("You have a shiny future")
elif random_number == 5:
    print("You have a leadership role in future")
elif random_number == 6:
    print("You have a successful team collaboration in future")
elif random_number == 7:
    print("You have a compassionate future")
elif random_number == 8:
    print("God hass blessed me abundantly")
elif random_number == 9:
    print("Wow, look at you ! You are living your best life everyday")
else:
    print("Nobody really cares if you don't take care of yourself!!")


#FizzBuzz Game
for num in range(0,100):
    if num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 15 == 0:
        print("FizzBuzz")
    else:
        pass
print(num)

#Reversing a string in Python
name = "Sexy Aklisiya is my baby gyaldem."[::-1]
print(name)
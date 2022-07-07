"""age = int(input("Please provide your age: "))
if age > 18:
    print(f"As your age is {age}, you can watch Thor Love & Thunder") #if you dont want to fill a space- use pass, example below
else:
        print(f"As your age is {age}, you can't watch Thor Love & Thunder")"""

"""age = int(input("Please provide your age: "))
if age > 18:
    pass
else:
        print(f"As your age is {age}, you can't watch Thor Love & Thunder")"""


"""answer = 89
user_answer = int(input ("Enter a number between 1 and 100: "))
if user_answer == answer:
    print("Correct answer!!")
else:
    if user_answer<answer:
        print("Number is greater than this")
    else:
        print("Number is smaller than this")
"""



"""
THE GAME


from random import seed
from random import randint
answer = randint(0,100)
user_answer = int(input ("Enter a number between 1 and 100: "))
if user_answer == answer:
    print("Correct answer!!")
else:
    if user_answer<answer:
        print("Number is greater than this")
    else:
        print("Number is smaller than this")
print("The answer was ",answer)
if answer==user_answer:
    print("You win the game")"""


"""name, age = input ("Your name and age: ").split(",")
newage=int(age)
name = name.lower()
if (newage>=18 and name[0]=="a"):
    print("You can watch the movie")
else:
    print("You cant watch the movie")"""



#age 0 to 5 free ticket, 5 to 60 200/-, 60+ 100/-
"""age = input("Enter age: ")
newage = int(age)
if newage<=5:
    print("Free ticket!")
elif (newage<=60 and newage>=5):
    print("200/- fare")
    elif newage==0 and newage<0:
    print("Are you serious?")
else:
    print("100/- fare")"""


# in and check for empty string

fname = "Thor"

if fname:
    if "a" in fname:
        print("'a' is present in your name")
    else:
        print("Not present")
else:
    ("Try to enter again FULLY, idiot")
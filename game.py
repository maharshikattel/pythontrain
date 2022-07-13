import random
number = int(random.randint(0,100))
i = 0
while i < 100:

    guessed = int(input("Enter a number 1-100: "))

    if (guessed == number):
        print("Correct!")
        print(f"You got it correct in {i+1}th turn")
        break
    while guessed is not number:
        if (guessed < number):
            i += 1
            print("The number is greater")
            break
        elif (guessed > number):
            i += 1
            print("Number is smaller")
            break
















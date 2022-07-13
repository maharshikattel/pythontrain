# function defines with parameter
"""def function_name(eutavalue):
    print(f"I was summoned {eutavalue}")

#function calling with argument 
print(function_name(", Hello"))"""

"""def fun(sloppy,seconds):
    print(f"Your name is {sloppy} and your age is {seconds}")

name, age = input("ENter your name and age (comma sep): ").split(",")
print(fun(name,age))

"""
"""def fun(sloppy):
    mod = sloppy % 2
    if mod == 0:
        result = "even"
    else:
        result = "odd"
    return f"Your number is {sloppy} and it is {result}"

num = int(input("ENter your number: "))
state = fun(num)
print(state)"""




"""def odd_even(anyNum):
    if anyNum % 2 == 0:
        return True
    else:
        return False"""


"""def odd_even(anyNum):
    return anyNum % 2 == 0

userdincha = int(input("Dear user please enter a number: "))
functionledeko = odd_even(userdincha)
print(functionledeko)"""

"""def palindrome(anyNum):
    rev = anyNum[::-1]
    print(rev)
    return 

userdincha = input("Dear user please enter anything: ")
rever = palindrome(userdincha)
print(rever)"""



"""def greater(one, two):
    if one > two:
        return one,two
    else:
        buffer = one
        one = two
        two = buffer
        return one,two

first = int(input("Dear user please enter anything: "))
second = int(input("Dear user please enter anything: "))
new,newer = greater(first,second)
print(f"{new} is greater than {newer}")"""


def greater(one, two, three):
    if one > two and one > three:
        return f"{one} > {two} and {three}"
    elif two > one and two > three:
        return f"{two} > {one} and {three}"
    else:
        return f"{three} > {two} and {one}"
    

first = int(input("Dear user please enter anything: "))
second = int(input("Dear user please enter anything: "))
third = int(input("Dear user please enter anything: "))

print(greater(first,second,third))
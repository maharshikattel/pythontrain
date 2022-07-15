"""list_of_numbers=[1,2,3,4,5]
list_of_nepali_names=["समय,आर्यमा,कृतिका,महर्षि"]
list_of_even_numbers=[2,4,6]
list_of_odd_numbers=[1,3,5]

mixed =["one",2,3.0,"four",False]

for i in mixed:
    print(f"{type(i)}\n")

for i in list_of_even_numbers:
    print(f"{i}\n")

list_of_odd_numbers[2]=False
print(list_of_odd_numbers[0:2])"""



#2) add data to list --> append() and insert() method

"""list_of_numbers=[1,2,3,4,5]
list_of_numbers.append(6)
list_of_numbers.insert(2,11) #position= 2 value= 11
print(list_of_numbers)



fruits1 = ["apple","mango","banana"]
fruits2 = ["apricot","watermelon","guava"]


#fruits1.pop() ---> pops out the last element of the array/list
fruits1.pop(0) #pops acc to position

#pop not only deletes but momentarily stores the data so we can use it like this
popped_entity = fruits1.pop()
print(fruits1)
print(popped_entity)"""


# del fruits1[1]
# print(fruits1)



# in keyword in list

"""if "apple" in fruits1:
    print("present")
else:
    print("absent")"""

"""
list methods
--> count()
--> sort() method 
--> sorted() function
--> clear() and copy() method
--> reverse() method
"""

"""print(fruits2.count("grapes"))
fruits2.sort()
print(fruits2)
fruits2.reverse()
fruits3 = fruits2.copy()
print(fruits2)
fruits2.clear()
print(fruits3)"""



#sort and sorted
"""
sort changes the original thing and never goes back
sorted changed the original thing temporarily and doesnt change it over all, it is used to save in another variable type ko situation ma
"""

# is vs equal --> comparison
"""fruits5 = ["apple","banana","mango"]
fruits6 = ["apple","banana","mango"]

print(fruits5 == fruits6) #compares values 
print(fruits5 is fruits6) #compares memory address in RAM


#making a list

def give_me_list(num):
    my_list=[]
    for i in range(0,num+1):
        my_list.append(i)
    return my_list

mero_list = give_me_list(10)
print(mero_list)"""

num = int(input("Enter number: "))
def list1(num):
    global square
    square=[]
    for i in range(1,num+1):
        square.append(i**2)
    return square

sq = list1(num)
print (sq)

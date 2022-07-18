days=("sunday","monday","tuesday")


# tuple unpacking (js object de-structuring) same value
day1,day2,day3 = days
print(day2)

#function returning two values

def calculator(num1,num2):
    sum = num1 + num2
    multiply = num1 * num2
    return sum,multiply
    
    
returned_value = calculator(4,5)
print(f"The returned value is: {returned_value}")
print(f"The type of returned value is: {type(returned_value)}")

multiply_only = returned_value[1]
print(f"The returned value is: {multiply_only}")


#list inside tuple
"""
searched_value = "sth"
left_pointer = 0
right_pointer = len(tuple_a)-1
mid_pointer = (left_pointer+right_pointer)/2
if value<mid_pointer:
    right_pointer = mid_pointer


""" 
 
 
 
 
"""
tuple_a = (1,2,3,[4,5,6],7,8,9)
print(tuple_a[3])
print(tuple_a[3][1]) # --> to get the value inside the list in the tuple
tuple_a[3][1] = "Maharshi"""



tuple_a = (1,2,3,4,5,6,7,8,9)
print(tuple_a)
print(min(tuple_a))
print(max(tuple_a))
print(sum(tuple_a))

# MOre about tuples
# creating new tuple from range function like list
new_tuples = tuple(range(1,11))
print(new_tuples)





create_list_from_tuples = list(new_tuples)
print(f"The list is: {create_list_from_tuples} and its type is: {type(create_list_from_tuples)}")
create_string_from_tuples = str(new_tuples)
print(f"The string is: {create_string_from_tuples} and its type is: {type(create_string_from_tuples)}")





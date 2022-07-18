#sets dont support indexing
# It is used to remove duplicacy
# It is faster than dictionaries

sets_any = {"sunday","monday","tuesday"}
any_list = [1,2,3,4,5,6,7,8,9]
sets_convert = set(any_list)
print(sets_convert)

#again convert to list
list_convert = list(sets_convert)
print(list_convert)
one_lint_list_set = list(sets_convert)
print(list_convert)


"""
sets support in keyword for conditional and looping statements
it is also used 
"""

set1 = {"k","r","i","t","i","k","a"}
print(set1)

if "r" in set1:
    print("Present")
else:
    print("Absent")



for i in set1:
    print(f"{i}-->0")


set2 = {"m","a","h","a","r","h","i"}
union_set = set1 | set2
intersection_set = set1 & set2

print(f"The union of two sets are: ---> {union_set}")
print(f"The intersection of two sets are: ---> {intersection_set}")


# ! string
# string = "   hello world     "
# print(string.lstrip()) #remove whitespace
# print(string.join(["1","helo","jsadasd"]))
# print(string.split("o"))

# ? casting
# int("21")
# str(21)

# * dictionary
# grades = {"anas":100,"ahmad":"90","khalid":23}
# print(grades.keys())

# ! sets are lists {} with no duplicates
# numbers = [1, 2, 3, 4, 4, 4, 5, 5, 6]
# first_set = set(numbers)
# second_set = {1, 2, 3, 4, 5, 6, 7, 9}
# print(first_set | second_set)  # union of sets (all of items)
# print(first_set & second_set)  # intersection of sets (in both of sets)
# print(first_set - second_set)  # difference of sets (in both of sets)
# print(first_set ^ second_set)  # either in one set but not both

# ? loops

# x = list(range(10)) # list of number from 0 to 9
# print(x)

# x = ["anas","ahmad","Abd"]
# for i in x:
#     print(i)

# i = 5
# while i < 10:
#     print(i)
#     i +=1

# * functions
# def double_numbers(*numbers, times=1):  # "*" this makes the parameter as a tuple
#     for number in numbers:
#         print(number*times)

# double_numbers(1, 2, 3, 4, 5, 6, times=2)

# def double_numbers(**numbers, times=1):  # "**" this makes the parameter as a dictionary
#     for number in numbers:
#         print(number*times)

# double_numbers(1, 2, 3, 4, 5, 6, times=2)

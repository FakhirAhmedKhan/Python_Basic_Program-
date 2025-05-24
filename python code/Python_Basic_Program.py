# # Task_1
# # write a program to print Twinkle twinkle little star poem in python
# print(
#     """Twinkle, twinkle, little star,
#  How I wonder what you are!
#  Up above the world so high,
#  Like a diamond in the sky.

#  When the blazing sun is gone,
#  When he nothing shines upon,
#  Then you show your little light,
#  Twinkle, twinkle, all the night.

#  Then the traveler in the dark
#  Thanks you for your tiny spark,
#  How could he see where to go,
#  If you did not twinkle so?

#  In the dark blue sky you keep,
#  Often through my curtains peep.
#  For you never shut your eye,
#  Till the sun is in the sky.

#  As your bright and tiny spark
#  Lights the traveler in the dark,
#  Though I know not what you are,
#  Twinkle, twinkle, little star.
# """
# )

# # Task_2
# # Use a repl and print table of 5 using it
# # DONE BY USIING CMD

# # Task_3
# # Install an external module and use it to perform an operation of your interest
# import pyjokes

# print(pyjokes.get_joke())

# # Task_4
# # Write a python program to print the content of a directory using the os module. Search online for the function which does that
# import os

# directory_path = "."

# try:
#     contents = os.listdir(directory_path)
#     print(f"Contents of '{directory_path}':")
#     for item in contents:
#         print(item)
# except FileNotFoundError:
#     print("The specified directory was not found.")
# except PermissionError:
#     print("Permission denied to access the directory.")

# # Task_5
# # Label the python program written in problem 4 with comments
# # This is commite


# # Task_6
# # Write a program to add two numbers
# A = 1
# B = 1
# print(A + B)  # Output value is 2

# # Task_7
# # Write a python program to find remainder when a number is divided by x
# A = int(input("Enter the First num: "))
# B = int(input("Enter the Second num: "))
# C = A % B
# print(
#     f"The remainder whhen{A} is divided by {B} is: {C}"
# )  # Output value is 2 beacuse 17 % 5 = 2

# # Task_8
# # Check the type of variable assigned using input () function
# A = float(input("Enter the "))
# print(type(A))  # Output value is float beacuse we add already in a varuble

# # Task_9
# # use comparison operator to find out whether a given variable a is greater then "b" or not. Take "a" = 34 and b=80
# A = 34
# B = 80
# C = A < B
# print(C)  # The out put is True

# # Task_10
# # write a python program to find an average of two numbers entered by the user
# A = int(input("Enter the num: "))
# B = int(input("Enter the num: "))
# C = A / B
# D = print(f"The remainder whhen{A} is average number by {B} is: {C}")
# E = print(
#     type(D)
# )  # The output is 33 / 33 = 1 but the (typeof()) is Nonetype because of pass the value by using print mathad it will be shown Nonetype because the output is a message does not return a value

# name = "Fakhir"
# age = 17
# print(f"My name is {name} and I am {age} years old.")

# # Task_11
# # Write a python program to calculate the square of a number entered by user
# A = int(input("Enter the num: "))
# B = int(input("Enter the num: "))
# C = A**B
# print(C)

# # Task_12
# # Write a python program to display a user entered name followed by Good afternoon using input () function
# A = input("Enter your name: ")
# print(f"Good eveing {A}")

# # Task_13
# # Write a program to fill in a letter template given below with name and date
# letter = """Dear <|Name|>,
# You are selected!
# <|Date|>"""
# print(letter.replace("<|Name|>", "Fakhir").replace("<|Date|>", "25 may"))

# # Task_14
# # write a python program to detect double space in a string

# A = "hi my name  is fakir"
# print(A.find(""))

# # Task_15
# # replace the double space form  problem 3 with single space
# A = "hi my name  is fakir"
# print(A.replace("", " a"))

# # Task_16
# # Write a program to format the following letter using escape sequence characters
# letter = "Dear Harry,\n\tThis python course is nice.\nThank"
# print(letter)

# # Task_17
# # write a python program to store seven name in a list entered by the user
# mark = []
# f1 = input("Enter the number: ")
# mark.append(f1)
# f2 = input("Enter the number: ")
# mark.append(f2)
# f3 = input("Enter the number: ")
# mark.append(f3)
# f4 = input("Enter the number: ")
# mark.append(f4)
# f5 = input("Enter the number: ")
# mark.append(f5)
# f6 = input("Enter the number: ")
# mark.append(f6)
# f7 = input("Enter the number: ")
# mark.append(f7)
# print(mark)

# # Task_18
# # write a python program to accept mark of 6 student and display them in a sorted manner
# mark = []
# f1 = int(input("Enter the number: "))
# mark.append(f1)
# f2 = int(input("Enter the number: "))
# mark.append(f2)
# f3 = int(input("Enter the number: "))
# mark.append(f3)
# f4 = int(input("Enter the number: "))
# mark.append(f4)
# f5 = int(input("Enter the number: "))
# mark.append(f5)
# f6 = int(input("Enter the number: "))
# mark.append(f6)
# mark.sort()
# print(mark)

# # Task_19
# # check that a type cannot be changed in python program
# # ANS
# # tuple is object it does not support assigment

# # Task_20
# # write a python program to sum a list with four number
# num = [23, 32, 45, 545, 545]
# print(sum(num))

# # Task_21
# # write a python program to count the number of zeros in the following tuple
# num = [23, 23, 45, 545, 545]
# n = num.count(23)
# print(n)

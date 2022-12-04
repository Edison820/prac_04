"""
CP1404 Practical
list exercises
"""

numbers = []
for i in range(5):
    number = int(input("Enter a number: "))
    numbers.append(number)
print("Number: ",numbers[0])
print("Number: ",numbers[1])
print("Number: ",numbers[2])
print("Number: ",numbers[3])
print("Number: ",numbers[4])
print("The first number is", numbers[0])
print("The last number is", numbers[4])
print("The smallest number is", min(numbers))
print("The largest number is", max(numbers))
print("The average of the numbers", sum(numbers) / len(numbers))






usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
users_name = input("Username: ")
if  users_name in usernames:
    print("Access granted")
else:
    print("Access denied")
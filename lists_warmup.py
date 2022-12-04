numbers = [3, 1, 4, 1, 5, 9, 2]

numbers[0]
#3

numbers[-1]
#2

numbers[3]
#1

numbers[:-1]
#[3, 1, 4, 1, 5, 9]

numbers[3:4]
#[1]

5 in numbers
#Ture

7 in numbers
#False

"3" in numbers
#False

numbers + [6, 5, 3]
#[3, 1, 4, 1, 5, 9, 2, 6, 5, 3]


numbers = [3, 1, 4, 1, 5, 9, 2]

# 1.Change the first element of numbers to "ten"
numbers[0] = "ten"

# 2.Change the last element of numbers to 1
numbers[-1] = 1

# 3.Print all the elements from numbers except the first two
print(numbers[2:])

# 4.Print whether 9 is an element of numbers
print(9 in numbers)



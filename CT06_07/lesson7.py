## Recap 1: Debugging Average Score Program

### There is a total of 3 bugs in the following program.
### Identify and fix the bugs:

# score_one = 80
# score_two = 90
# score_three = 75

# total = score_one + score_two + score_three

# average_score = total / 3

# student_name = "Alex"

# print("Average score for " + student_name + " is: " + str(average_score) + ".")

# f - string >> formatted string
# print(f"Average score for {student_name} is: {average_score}") << to insert variable no need +, just curly bracket

# Task 1
# for i in range (1, 11, 1): >> (1, 10 + 1) OR 1, 11
#     print(i)

#  Task 2
# for i in range (2, 21, 2):
#     print(i)

# Task 3 
# for i in range (10, 0, -1):
#     print(i)

# Task 4
# word = input("Enter a word ") << rmb add spacing
# n = int(input("Enter a number "))

# for i in range(n): 
#     print(word)

# Task 5
# name = input("Enter your name: ")
# n = int(input("Enter a number: "))
# for i in range(n):
#     print(f"Nice to meet you {name}.")

# Task 6
# total = 0 << variable , used to store total sum

# working

# total = 0
# for i in range (5):
#     number = int(input(f"What is number #{i + 1}? ")) 
#     total = total + number

# print(f"Sum of the 5 numbers is {total}.")

# Task 7 
# number = int(input("Enter a number: "))
# for i in range (1, 13):
#     print(f"{number} x {i} = {number * i}")
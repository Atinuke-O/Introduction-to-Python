    #----------Conditionals and Mathematics-----------#

# add 2 numbers from input using a cast to integer and display the answer 

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
print(num1, " + ", num2, " = ", int(num1) + int(num2))

#---------------------------------#

# Multiply 2 numbers from input using cast and save the answer as part of a string "the answer is..."
# display the string using print

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

answer = (int(num1) * int(num2))
print("The answer is,", answer)

#---------------------------------#

# get input of 2 numbers and display the average: (num1 + num2) divided by 2

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

answer = ((int(num1) + int(num2))/2)
print("The answer is,", answer)

#---------------------------------#

# get input of 2 numbers and subtract the largest from the smallest (use an if statement to see which is larger)
# show the answer

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

if int(num1) > int(num2):
    answer = (int(num1) - int(num2))
    print("Subtraction of smallest from largest =", answer)
    
if  int(num2) > int(num1):
    answer = (int(num2) - int(num1))
    print("Subtraction of smallest from largest =", answer)
    
else:
    pass
    
#---------------------------------#
    
# Divide a larger number by a smaller number and print the integer part of the result
# don't divide by zero! if a zero is input make the result zero
# cast the answer to an integer to cut off the decimals and print the result

num1 = input("Enter large number: ")
num2 = input("Enter small number: ")

answer = (int(num1) / int(num2))
print(answer)

whole_answer = int(answer)
print(whole_answer)

    #-----------If Else Conditional logic-----------#

# input a variable: age as digit and cast to int
# if age greater than or equal to 12 then print message on age in 10 years 
# or else print message "It is good to be" age

age = int(input(""))
if age >= 12:
    print("Your age in 10 years will be", age + 10)
else:
    print("It is good to be", age)
    
#--------------------------#

# input a number 
# if number IS a digit string then cast to int
# print number "greater than 100 is" True/False
# if number is NOT a digit string then message the user that "only int is accepted"

number = input("Enter a number: ")
if number.isdigit():
    print (int(number), "greater than 100 is", int(number) > 100)
else:
    print ("only int is accepted")
# It appears that there must always be a variable involved and the int() and str() doesn't work well with input() alone

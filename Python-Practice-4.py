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

#-------Pet Conversation-------#

#**ask the user for a sentence about a pet and then reply**  
#- get user input in variable: about_pet
#- using a series of **if** statements respond with appropriate conversation
  #- check if "dog" is in the string about_pet (sample reply "Ah, a dog")
  #- check if "cat" is in the string about_pet
  #- check if 1 or more animal is in string about_pet
#- finish with thanking for the story


about_pet = (input ("Start a conversation about a pet: "))

if "dog" in about_pet:
    print ("Ah, a dog. how wonderful! Dogs are amazing")
if "cat" in about_pet:
    print ("Cats are very sassy creatures. But they are good cuddlers ^-^")
if "dog, cat, hamster, guinea pig, turtle, goldfish, bunny" in animals:
    print ("It's so great to have lots of animal company!")

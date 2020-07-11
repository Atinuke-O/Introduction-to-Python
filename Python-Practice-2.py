        #------Getting User Input------#
# get user input for a variable named remind_me
remind_me=input("What do you want to be reminded about? ")

# print the value of the variable remind_me
print(remind_me)

# use string addition to print "remember: " before the remind_me input string
print("remember:", remind_me)

# get user input for 2 variables: meeting_subject and meeting_time
meeting_subject=input("what is the meeting subject?: ")
meeting_time=input("what is the meeting time?: ")

#use string addition to print meeting subject and time with labels
print("Meeting Subject:", meeting_subject)
print("Meeting Time:", meeting_time)



        #------Print Formatting------#
# print the combined strings "Wednesday is" and "in the middle of the week" 
print("Wednesday is", "in the middle of the week")

# print combined string "Remember to" and the string variable remind_me from input above
print("Remember to", remind_me)

# Combine 3 variables from above with multiple strings
print(remind_me, "by", meeting_time, "and", meeting_subject)



        #------Print Quotation Marks------#
# print a string sentence that will display an Apostrophe (')
print("She told me that 'I' was being sarcastic")

# print a string sentence that will display a quote(") or quotes
print('She told me that "I" was being sarcastic')



        #------Boolean String Tests------#
# creating a vehicle test
vehicle=input()
print("All alpha?:", vehicle.isalpha())
print("All alpha & num?:", vehicle.isalnum())
print("Capitalized?:", vehicle.isupper())
print("Lowercase?:", vehicle.islower())



        #------String Formatting------#
# print the string variable capital_this Capitalizing only the first letter
capitalize_this = "the TIME is Noon."
print(capitalize_this.capitalize())

# print the string variable swap_this in swapped case
swap_this = "wHO writes LIKE tHIS?"
print(swap_this.swapcase())

# print the string variable whisper_this in all lowercase
whisper_this = "Can you hear me?"
print(whisper_this.lower())

# print the string variable yell_this in all UPPERCASE
yell_this = "Can you hear me Now!?"
print(yell_this.upper())

# format input using .upper(), .lower(), .swapcase, .capitalize()
format_input = input('enter a string to reformat: ')
print(format_input.upper(), format_input.lower(), format_input.swapcase(), format_input.capitalize())



        #------Input Formatting------#
# get user input for a variable named color
# modify color to be all lowercase and print
color=input()
print(color.lower())

# get user input using variable remind_me and format to all **lowercase** and print
# test using input with mixed upper and lower cases
remind_me = input().lower()
print(remind_me)

# get user input for the variable yell_this and format as a "YELL" to ALL CAPS
yell_this=input().upper()
print(yell_this)



        #------"In" Keyword------#
# get user input for the name of some animals in the variable animals_input

animals_input =input()
# print true or false if 'cat' is in the string variable animals_input
print("cat" in animals_input)
# get user input for color

color=input()
# print True or False for starts with "b"
print(color.startswith("b"))
print(color)

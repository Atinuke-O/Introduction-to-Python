    #------while() loops and increments------#
    
##### use a "forever" while loop to get user input of integers to add to sum, 
# until a non-digit is entered, then break the loop and print sum
sum = 0

while sum >= 0:
    add = input("Enter an integer: ")
    if add.isdigit():
        sum = sum + int(add)
    else:
        break
    
print(sum)

#--------------------------#

# use a while True loop (forever loop) to give 4 chances for input of a correct color in a rainbow
# rainbow = "red orange yellow green blue indigo violet"

rainbow = "red orange yellow green blue indigo violet"
color_choice = 0

while color_choice < 4:
    color_z = input("Enter a color of choice: ")
    if color_z.lower() in rainbow:
        print ("You are correct!")
        break
    else:
        color_choice += 1
        print("try again")
        print()
        
if color_choice == 4:
    print("out of tries")
        

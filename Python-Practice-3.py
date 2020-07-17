    #------Functions, Arguments and Parameters------#

# define and call a function short_rhyme() that prints a 2 line rhyme

def short_rhyme(line1, line2):
    lyric1=(line1.title())
    lyric2=(line2.title())
    return lyric1 + lyric2
rhyme = short_rhyme ("one two three.", " play with me")
print(rhyme)

#-----------------------------------------#

# define (def) a simple function: title_it() and call the function
#--has a string parameter: msg
#--prints msg in Title Case

def title_it(msg):
    print(msg.title())
    
title_it("Nothing works until you do")

#-----------------------------------------#

# get user input with prompt "what is the title?" 
# call title_it() using input for the string argument

title_input=input("what is the title? ")
title_it(title_input)

#-----------------------------------------#

# define title_it_rtn() which returns a titled string instead of printing
# call title_it_rtn() using input for the string argumetnt and print the result

def title_it_rtn(string):
    titled_string=(string.title())
    return titled_string

title=input()
title2=title_it_rtn(title)
print(title2)

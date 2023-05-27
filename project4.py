"""
Project 4 - Wait, wait, don't tell me
Author: Tulika Basu 
Date: 03/02/2023

Enhancements in this release:
- allowing the use of any symbol to create each shape 
- returning the shape as a single string return value
- create main function
"""

# GuessLimerick() Function
def GuessLimerick():
    limerick = "there was a young fellow of Crete \nwho was so exceedingly neat \nwhen he got out of be \nhe stood on his head \nto make sure of not soiling his  _ _ _ _ "
    secret = str("feet")
    max_tries = 5
    tries = 0
    cont = True
    print(limerick)
    print("**input missing word in all lowercase letters**")
    while (cont and tries < max_tries):
        guess = str(input("your guess :"))
        tries += 1
        if(guess == secret):
            print("congratulations!")
            cont = False
        else:
            print("please try again")
    if (cont):
         print("Game over, out of tries")
                         

# Menu() Function
def menu():
    while (True):
        print("choose an option : ")
        print("PLAY")
        print("CHEAT") 
        print("EXIT")
        choice = input().upper()
        if (choice == "PLAY"):
            return GuessLimerick()
        elif (choice == "CHEAT"):
            print("there was a young fellow of Crete \nwho was so exceedingly neat \nwhen he got out of be \nhe stood on his head \nto make sure of not soiling his FEET")
        elif (choice == "EXIT"):
            print ("goodbye!")
            break
        else:
            print("invalid choice, please try again")
     


#main program 
menu()

"""
###output for guessing correctly 
choose an option : 
PLAY
CHEAT
EXIT

there was a young fellow of Crete 
who was so exceedingly neat 
when he got out of be 
he stood on his head 
to make sure of not soiling his  _ _ _ _ 
**input missing word in all lowercase letters**
your guess : feet #user input

congratulations!

###output for guessing incorrectly all 5 times 

choose an option : 
PLAY
CHEAT
EXIT

there was a young fellow of Crete 
who was so exceedingly neat 
when he got out of be 
he stood on his head 
to make sure of not soiling his  _ _ _ _ 
**input missing word in all lowercase letters**

your guess :blah #user input
please try again
your guess :blah #user input
please try again
your guess :blah #user input
please try again
your guess :blah #user input
please try again
your guess :blah #user input
please try again
Game over, out of tries


###output for CHEAT 

there was a young fellow of Crete 
who was so exceedingly neat 
when he got out of be 
he stood on his head 
to make sure of not soiling his FEET
choose an option : 
PLAY
CHEAT
EXIT

###output for EXIT
choose an option : 
PLAY
CHEAT
EXIT

goodbye!
"""
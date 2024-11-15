## Bryan Xaysanavongphet 11/14/2024


import random

#Creating the random coin flip function to return heads or tails.
def flip_coin():
    return random.choice(["Heads", "Tails"])

#Making a heads or tails function for the user to guess.
def hot():
    while True:
        #Creating an option for the user to choose either heads or tails.
        print("Welcome to the guessing game!")
        print("1. For Heads")
        print("2. For Tails")
        print("3. Quit")
        guess = input("Please enter your guess (1 for Heads, 2 for Tails): ")
        
        #result of the coinflip
        result = flip_coin()
        
        #if statement for when the coin is either heads or tails and letting the user know.
        if result == "Heads" and guess == "1":
            print("Congrats! It was heads!")
        elif result == "Tails" and guess == "2":
            print("Congrats! It was tails!")
        elif guess == "3":
            return
        else:
            print(f"Sorry, it was {result.lower()}.")

    
    

#function for the user to clip the coin.
def coin():
    #Making a while loop for when the user is wanting to flip the coin.
    while True:
        start = input("We're going to flip the coin now! \nPress 1 to start or press 2 to quit.")
        print("--------------------------------------")
        
        #if statement to show the result of the coin toss
        if(start == "1"):
            result = flip_coin()
            print(f"\nThe coin landed on {result}")
        elif (start == "2"):
            return
        else:
            print("Invalid selection")


#Main function loop.
if __name__ == "__main__":
    
    while True:
        print("\nWelcome to the coin flip game!")
        print("---------------------------------")
        print("Please select an option below:")
        print("1. Flip a coin.")
        print("2. Choose if it's heads or tails.")
        print("3. Quit.")
        print("----------------------------------")
        
        menu = input("Please select an option: ")
        
        #menu
        if menu == "1":
            coin()
        elif menu == "2":
            hot()
        elif menu == "3":
            print("Thank you for playing! Goodbye!")
            break
        else:
            print("Invalid selection. Please try again.")
        
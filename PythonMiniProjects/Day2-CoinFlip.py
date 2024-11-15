import random

#Creating the random coin flip function to return heads or tails.
def flip_coin():
    return random.choice(["Heads", "Tails"])

#Making a heads or tails function for the user to guess.
def hot():
    print("Welcome to")

#function for the user to clip the coin.
def coin():
    start = input("We're going to flip the coin now! Press 1 to start or press 2 to quit.")
    if(start == "1"):
        flip_coin()
    elif (start == "2"):
        break
    else:
        print("Invalid selection")


#Main function loop.
if __name__ == "__main__":
    
    print("Welcome to the coin flip game!")
    print("---------------------------------")
    print("Please select an option below:")
    print("1. Flip a coin.")
    print("2. Choose if it's heads or tails.")
    print("3. Quit.")
    print("----------------------------------")
    menu = input("Please select an option: ")
    
    if(menu == "1"):
        coin()
    elif (menu == "2"):
        hot()
    elif (menu == "3"):
        break
    else:
        print("Invalid selection. Please try again.")
        
    #choice = input("Please choose how many times you would like to flip the coin.")
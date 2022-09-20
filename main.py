# Rock paper scissors
# User vs Computer

import random, time 

def main():

    L = ["rock","paper","scissors"] 
    computer = random.choice(L)
    user = input("À vous de jouer : ")
    win = False

    # User says rock 
    if user.lower() == "rock" and computer.lower() == "scissors":
        win = True

    # User says paper
    if user.lower() == "paper" and computer.lower() == "rock":
        win = True
    
    #User says scissors
    if user.lower() == "scissors" and computer.lower() == "paper":
        win = True


    time.sleep(1)
    print(computer)
    time.sleep(1)
    
    if win == True:
        print("You win")
    else: 
        print("You lost")




if __name__ == '__main__':
    main()
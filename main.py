
#* Rock paper scissors
#* User vs Computer

import random


def main():

    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r','p','s'])
    print(f"Computer chooses : {computer}")
    
    if user == computer:
        return 'Its a tie'
    
    if is_win(user, computer):
        return 'You won!'

    return 'You lost!'


def is_win(user, computer):
    
    if (user == 'r' and computer == 's') or (user == 'p' and computer == 'r') \
        or (user == 's' and computer == 'p'):
        return True




if __name__ == '__main__':
    print(main())
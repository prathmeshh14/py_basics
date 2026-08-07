import random 
choices=['heads','tails']

def flip():
    return random.choice(choices)
def play():
    while True:
        user_flip=input("Enter heads or tails: ").lower()
        if user_flip not in choices:
            print("invalid choice! Please choose heads or tails.")
            continue
        computer_flip=flip()
        print(f"You flipped: {user_flip}")
        print(f"Computer flipped: {computer_flip}")
        if user_flip==computer_flip:
            print("It's a tie!")
        else:
            print("You lose!")

        play_again=input("Do you want to flip again? (y/n): ").lower()
        if play_again!='y':
            print("Thanks for playing!")
            break
result=play()
print(result)
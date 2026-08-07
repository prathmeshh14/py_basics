import random 

def roll():
    return random.randint(1,6)
def play():
    while True:
        player_roll=roll()
        computer_roll=roll()

        print(f"You rolled: {player_roll}")
        print(f"Computer rolled: {computer_roll}")

        if player_roll>computer_roll:
            print("You win!")
        elif player_roll<computer_roll:
            print("Computer wins!")
        else:
            print("It's a tie!")
    
        play_again=input("you want to roll the dice? (y/n): ").lower()

        if play_again!='y':
            print("Thanks for playing!")
            break

result=play()
print(result)
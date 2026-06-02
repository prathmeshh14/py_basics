import random 
choices = ["rock", "paper", "scissors"]
def play(user):
    computer = random.choice(choices)
    print(f"Computer chose: {computer}")
    if user not in choices:
        return "Invalid choice! Please choose rock, paper, or scissors."
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "Computer wins!"
    
user_input = input("Enter rock, paper, or scissors: ")
result = play(user_input)
print(result)
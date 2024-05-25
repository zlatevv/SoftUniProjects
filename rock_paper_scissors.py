import random

computer_commands = ["rock", "paper", "scissors"]
text = input("Rock, paper, or scissors? ")
if text.lower() == "rock":
    computer_choice = random.choice(computer_commands)
    if computer_choice == "rock":
        print("Computer also chose rock!")
        print("Tie!")
    elif computer_choice == "paper":
        print("Computer chose paper!")
        print("You lose!")
    elif computer_choice == "scissors":
        print("Computer chose scissors!")
        print("You win!")
elif text.lower() == "paper":
    computer_choice = random.choice(computer_commands)
    if computer_choice == "rock":
        print("Computer chose rock!")
        print("You win!")
    elif computer_choice == "paper":
        print("Computer also chose paper!")
        print("Tie!")
    elif computer_choice == "scissors":
        print("Computer chose scissors!")
        print("You lose!")
elif text.lower() == "scissors":
    computer_choice = random.choice(computer_commands)
    if computer_choice == "rock":
        print("Computer chose rock!")
        print("You lose!")
    elif computer_choice == "paper":
        print("Computer chose paper!")
        print("You win!")
    elif computer_choice == "scissors":
        print("Computer also chose scissors!")
        print("Tie!")
else:
    print("Invalid input")
    exit(1)
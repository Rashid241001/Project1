import random

choices = ["rock", "paper", "scissors"]

def determine_winner(user_choice, computer_choice):

    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "paper" and computer_choice == "rock") or \
            (user_choice == "scissors" and computer_choice == "paper"):
        return "win"
    else:
        return "loss"

for i in range(3):
    print(f" Round {i + 1} ")

    computer_choice = random.choice(choices)

    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_choice in choices:
            break
        print("Invalid choice. Please try again.")

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")


    result = determine_winner(user_choice, computer_choice)

    if result == "tie":
        print("It's a tie")
    elif result == "win":
        print("You win!")
    else: # result == "loss"
        print("Computer wins!")

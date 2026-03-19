import random

print("========================================")
print("------ ROCK PAPER SCISSORS GAME ------")

user_score = 0
computer_score = 0
tie_score = 0

while True:
    print("========================================")
    print("Choose one:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    print("========================================")

    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    # Game logic
    if user_choice == computer_choice:
        print("Result: It's a Tie!")
        tie_score += 1

    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):

        print("Result: You Win!")
        user_score += 1

    elif user_choice in choices:
        print("Result: Computer Wins!")
        computer_score += 1

    else:
        print("Invalid choice!")

    print("Score -> You:", user_score, "Computer:", computer_score, "Ties:", tie_score)

    again = input("Do you want to play again? (y/n): ").lower()
    if again != "y":
        break

print("\n========================================")
print("Final Score -> You:", user_score, "Computer:", computer_score, "Ties:", tie_score)
print("Thanks for playing!")
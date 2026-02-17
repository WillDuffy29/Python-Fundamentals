# Rock Paper Scissors

import random

print("================================")
print("Welcome to Rock, Paper Scissors!")
print("================================")

player = 0
computer = 0
rock = 0
paper = 0
scissors = 0

print("Your options are:")
print("  1. Rock")
print("  2. Paper")
print("  3. Scissors")

player = int(input("Please enter your selection (1, 2 or 3): "))

if player == 1:
    print("You chose: Rock!")
    rock += 1
elif player == 2:
    print("You chose: Paper!")
    paper += 1
else:
    player == 3
    print("You chose: Scissors!")
    scissors += 1

computer = random.randint(1, 3)

if computer == 1:
    print("The computer chose: Rock!")
    rock += 1
elif computer == 2:
    print("The computer chose: Paper!")
    paper += 1
else:
    computer == 3
    print("The computer chose: Scissors!")
    scissors += 1

if player == computer:
    print("You have tied...")
elif player > computer:
    print("Congrats! You win!")
else:
    print("You Lose... Better luck next time!")
import random
rock = "Rock"
paper = "Paper"
scissors = "Scissors"

player_move = input("Choose [r]ock, [p]aper or [s]cissors: ")

if player_move == "r":
    player_move = rock
elif player_move == "p":
    player_move = paper
elif player_move == "s":
    player_move = scissors
else:
    raise SystemExit("Invalid Input. Try again...")

computer_random_number = random.randint(1, 3)
computer_move = ""

your_won_games = 0
computer_won_games = 0

if computer_random_number == 1:
    computer_move = rock
elif computer_random_number == 2:
    computer_move = paper
else:
    computer_move = scissors

print(f"The computer chose {computer_move}.")

while True:

    if (player_move == rock and computer_move == scissors) or \
            (player_move == scissors and computer_move == paper) or \
            (player_move == paper and computer_move == rock):
        your_won_games += 1
        print("You win this hand!")
    elif player_move == computer_move:
        print("Draw!")
    else:
        computer_won_games += 1
        print("You lose this hand!")

    if your_won_games == 5:
        print("You win this game!")
    elif computer_won_games == 5:
        print("You lose this game!")
    break

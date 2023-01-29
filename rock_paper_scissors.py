import random
rock = "Rock"
paper = "Paper"
scissors = "Scissors"
your_won_games, computer_won_games = 0, 0

while True:
    player_move = input("Choose [r]ock, [p]aper or [s]cissors: ")

    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    else:
        print("Invalid Input. Try again...")
        continue

    computer_random_number = random.randint(1, 3)
    computer_move = ""

    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    else:
        computer_move = scissors

    print(f"The computer chose {computer_move}.")

    if (player_move == rock and computer_move == scissors) or (player_move == scissors and computer_move == paper) or \
            (player_move == paper and computer_move == rock):
        your_won_games += 1
        print(f"You win this hand! You: {your_won_games} / Comp: {computer_won_games}")

    elif player_move == computer_move:
        print("Draw!")
    else:
        computer_won_games += 1
        print(f"The computer wins this hand! You: {your_won_games} / Comp: {computer_won_games}")

    if your_won_games == 5:
        print("You win this game!")
        break
    elif computer_won_games == 5:
        print("You lose this game!")
        break

print("Thank you for playing!")

import random


player_1 = int(input("choose a rock , paper or scissors: 1 represent scissors, 2 represents rock and 3 represents paper: "))
player_2 = random.randint(1,3)

if player_1 > 3 or player_1 < 0:
    print("you entered an invalid number")
else:
    print(f"computer choice: {player_2}")
    print(f"player's choice: {player_1}")




if player_1 >= 3 or player_1 < 0:
    print("you entered an invalid number, you lose")
elif player_1 == 1 and player_2 == 3:
    print("you win")
elif player_1 == 3 and player_2 == 1:
    print("you lose")
elif player_1 > player_2:
    print("you win")
elif player_1 < player_2:
    print("you lose")
elif player_1 == player_2:
    print("it's a draw")


    # play_again = input("Play again? (y/n): ")
    # if play_again.lower() != "y":
    #     break

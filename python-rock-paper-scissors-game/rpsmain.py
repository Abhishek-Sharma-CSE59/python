import random
import numpy as np
user_wins = 0 
computer_wins = 0
options = np.array(["rock" , "paper","scissors"])
while True:
    user_input = input("Type Rock/Paper/Scissors or q to quit.").lower()
    if(user_input== 'q' or user_input =='quit'):
        break

    if user_input not in options :
        continue
     
    random_number = random.randint(0,2)
    computer_choice = options[random_number]

    print("computer picked :",computer_choice + ".")

    if (user_input == "rock" and computer_choice=="scissors"):
        print("You won!!")
        user_wins +=1
        continue
    elif (user_input== "paper" and computer_choice=="rock"):
        print("You won!!")
        user_wins +=1
        continue
    elif (user_input == "rock" and computer_choice=="scissors"):
        print("You won!!")
        user_wins +=1
        continue        
    else:
        print("Computer won")
        computer_wins +=1

print(f"You won {user_wins} times")
print(f"You won {computer_wins} times")
print("Goodbye")
    
name = input("Enter your name :")
print(f"Welcome {name} to this adventure!")

answer = input("You are on a dirty road, it has come to an end and you can go left or right. which way whould you go? :").lower()
if answer =="left":
    answer = input("You come to a river, you can walk around it or swim across? type swim to swim across and walk to walk around :").lower()
    if answer == "swim":
        print("You got eaten by an aligator, You lose!!")
    elif answer == "walk":
        print("You walked kilometers and ran out of water , You lose!!")
    else:
        print("Not a valid option. You Lose")
elif answer == 'right':
    answer = input('You came to a bridge, it looks wobbly, Do you want to cross it or go back :').lower()
    if answer == 'back':
        print("You go back and you lose!!")
    elif answer =='cross':
        answer = input('You crossed the bridge and meet a stranger. Do you talk to them (yes/no)? :').lower()
        if answer =='yes':
            print("You talked to the stranger and they gave you gold. You WIN!")
        elif answer =='no':
            print('you ignored the stranger and they are offended and you lose.')
        else:
            print("Not a valid option. You lose.")
    else:
        print("Not a valid option. You lose.")

else:
    print('Not a valid option. You lose.')
print(f"thank you for trying {name}")
        
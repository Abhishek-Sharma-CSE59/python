import random as rn
guesses = 0

limit = input("Type a number : ")

# this is a check code for number is int or not
if limit.isdigit():

    limit = int(limit)

    if limit <= 0:

        print("Please type a number greater then 0 Next time!"),quit()

else:

     print("Please type a digit next time!"),quit()
random = rn.randint(0,limit)
# print(random)

while True:
    guesses +=1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a digit next time!")
        continue

    if user_guess == random:
        print("You got it right!")
        break
    else:
        if user_guess > random:
            print("Your guess is greater than the number!")
        elif user_guess < random:
            print("Your guess is smaller than the number!")
        continue
    break

print(f"You got it in {guesses} guesses")


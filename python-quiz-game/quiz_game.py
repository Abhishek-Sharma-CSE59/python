print("Welcome to my computer quiz")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

score = 0

print("Okay! Let's play :)")
# QUESTION 1
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('correct!')
    score+=1
else:
    print('Incorrect!')

# QUESTION 2

answer = input("What does GPU stand for? ")
if answer.lower() == "graphic processing unit":
    print('correct!')
    score+=1

else:
    print('Incorrect!')

# QUESTION 3

answer = input("What does RAM stand for? ")
if answer.lower() == "random acess memory":
    print('correct!')
    score+=1

else:
    print('Incorrect!')

# QUESTION 4

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('correct!')
    score+=1

else:
    print('Incorrect!')

print(f"You got : {score} Questions corret")
print(f"You got {(score/4)*100} %")

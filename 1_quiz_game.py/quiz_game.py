print("Welcome to my computer quiz!")

playing = input("Do you want to play?      (yes/no): ")

if playing.lower() !="yes":
    quit()

print("Okay! Let's play :)")
score = 0




#FIRST QUESTION
answer = input("What is the capital of Romania? ")
if answer.lower() == "bucharest":
    print('Correct!')
    score += 1
else:
    print('Incorecct!')


#SECOND QUESTION
answer = input("What covers about 71% of the Earth's surface: land or water? ")
if answer.lower() == "water":
    print('Correct!')
    score += 1
else:
    print('Incorecct!')


#THIRD QUESTION
answer = input("How many planets are there in our solar system? ")
if answer.lower() == "eight":
    print('Correct!')
    score += 1
else:
    print('Incorecct!')


#FOURTH QUESTION
answer = input("Which planet is closest to the Sun? ")
if answer.lower() == "mercur":
    print('Correct!')
    score += 1
else:
    print('Incorecct!')



print("You got " + str(score)  + " questions correct!")
print("You got " + str((score / 4) * 100)  + "%.")
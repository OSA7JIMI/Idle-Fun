x=range(101)
import random
answer=random.choice(x)
tries=1
again =0

while again!="no":
    guess=int(input("Guess a number between 1 and 100:"))
    while guess != answer:
        if guess < answer:
            print("The number is higher!")
        else:
            print("The number is lower!")
        guess=int(input("Guess a number between 1 and 100:"))
        tries+=1
        if tries ==5:
            break

    if guess == answer:
        print("CONGRATULATIONS!!! You guessed it in", tries, "tries!")
    else:
        print("YOU SUCK! The number is", answer)

    again = input("Would you like to play again?")



          

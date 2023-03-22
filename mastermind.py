x = range(1, 9)
import random
code = [random.choice(x), random.choice(x), random.choice(x), random.choice(x)]
guess = [1, 2, 3, 4]
tries = 1
again = 0
red = 0
white = 0
win = 0
lose = 0
print("Welcome to Mastermind! The objective of the game is to guess the secret code.")
print("For each digit you guess in the right position, the red counter increases by 1.")
print("For each digit in the code but in the wrong position, the white counter increases by 1.")

while again != "no":
    for i in range(0, 4):
        guess[i] = int(input("Guess a number between 1 and 8: "))
        while guess[i] not in x:
            guess[i] = int(input("Guess a number between 1 and 8: "))
    for i in range(0, 4):
        if code[i] == guess[i]:
            red += 1
        for j in range(0, 4):
            if guess[j] == code[i]:
                white += 1
                break
    print("Red: ", red, "; White: ", white - red)
    
    if red == 4:
        print("Congratulations! You have beaten the mastermind in", tries, "tries!")
        again = input("Would you like to play again? Enter no to end: ")
        code = [random.choice(x), random.choice(x), random.choice(x), random.choice(x)]
        tries = 0
        win += 1
        break
    
    if tries == 12:
        print("You suck! The mastermind has beaten you!")
        print("The code was: ", code)
        again = input("Would you like to play again? Enter no to end: ")
        code = [random.choice(x), random.choice(x), random.choice(x), random.choice(x)]
        tries = 0
        lose += 1
        break

    print(12 - tries, "tries left")    
    red = 0
    white = 0
    tries +=1

print("You won", win, "games and lost", lose)

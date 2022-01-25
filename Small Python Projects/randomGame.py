# generate a number 1~10
# input from user?
# check that input is a number from 1~10
# check if number is right guess
# ask for input from user again

from random import randint
# random number generated
answer = randint(1, 10)
# check the input
while True:
    try:
        # user input
        guess = int(input("guess a number (1~10): "))
        if 0 < guess < 11:
            if guess == answer:
                print('You guessed right!!')
                break
        else:
            print("Hey! I asked for a number 1~10. ")
    except ValueError:
        print("Please enter a number!")
        continue








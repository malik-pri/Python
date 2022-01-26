# generate a number 1~10
# input from user?
# check that input is a number from 1~10
# check if number is right guess
# ask for input from user again

from random import randint


# random number generated
ans = randint(1, 10)


# define a function
def run_guess(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print('You guessed right!!')
            return True
    else:
        print("Hey! I asked for a number 1~10. ")
        return False


if __name__ == '__main__':
    # check the input
    while True:
        try:
            # user input
            guess_ans = int(input("guess a number (1~10): "))
            if run_guess(guess_ans, ans):
                break
        except ValueError:
            print("Please enter a number!")
            continue

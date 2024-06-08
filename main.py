import random

def main():
    lower_bound = int(input("Enter the lower bound: "))
    upper_bound = int(input("Enter the upper bound: "))
    print()
    random_int = random.randint(lower_bound, upper_bound)
    maximum_guesses = 3

    while maximum_guesses > 0:
        if maximum_guesses == 3:
            guess = int(input(f'Now guess a number between, {lower_bound} and {upper_bound}, you have {maximum_guesses} guesses: '))
        elif maximum_guesses > 1:
            print()
            guess = int(input(f"Try again, you have {maximum_guesses} guesses left: "))
        else:
            print()
            guess = int(input("Last chance! Try again: "))
        if guess == random_int:
            print("You got it!")
            return True
        elif guess > random_int:
            print("Your number is too high")
            maximum_guesses -= 1
        elif guess < random_int:
            print("Guess is too low!")
            maximum_guesses -= 1
        else:
            print("Invalid input")
            maximum_guesses -= 1
    print("You ran out of guesses")
    return False

main()

#testing
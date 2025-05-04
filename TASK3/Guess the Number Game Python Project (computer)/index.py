import random

secret_number = random.randint(1, 5)
print("🎯 I have selected a number between 1 and 20 Can you guess it? ")

while True:
    try:
        guess = int(input("🔢 Enter your guess: "))

        if guess < secret_number:
            print("Too low! Try again🔄")
        elif guess > secret_number:
            print("Too high! Try again🔄")
        else:
            print(f"🎉 Correct! The number was {secret_number}. You guessed it!🏆")
            break
    except ValueError:
        print("Please enter a valid number!🚫")
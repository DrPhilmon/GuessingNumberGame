import random

number = random.randint(1, 100)

print("I'm thinking of a number between 1 and 100.")
print("You have 7 chances to guess it!")

for chance in range(1, 8):
    guess = int(input(f"Chance {chance}: Enter your guess: "))

    if guess == number:
        print("🎉 Correct! You guessed the number!")
        break
    elif guess < number:
        print("Too low!")
    else:
        print("Too high!")

else:
    print(f"Sorry! You used all 7 chances. The number was {number}.")
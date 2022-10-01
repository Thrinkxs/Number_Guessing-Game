import random
number = random.randint(0, 100)
guess_count = 0
guess = 0
while guess != "exit" and guess != number:
    guess = int(input("Guess the number:\n"))
    guess_count += 1
    if guess == "exit":
        print("Game Over")
        break
    elif guess > number:
        print('Lower number please')
    elif guess < number:
        print('Higher number please')
    elif guess == number:
        print(f"Nice!!!, you guessed correctly after {guess_count} tries")
    else:
        print("What did you input?, I\'m lost")
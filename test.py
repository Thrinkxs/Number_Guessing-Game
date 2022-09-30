import random
number = random.randint(0, 100)
guess = int(input('Guess the number:\n'))
while guess != number:
    guess = int(input('Guess the number:\n'))
    if guess < number:
        print('Higher number please')
    elif guess > number:
        print('Lower number please')
    elif guess == number:
        print(f"Nice!!!, you guessed {number} correctly")
    else:
        print('What the hell did you guess uh?!')
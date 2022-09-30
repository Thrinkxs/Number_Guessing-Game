import random
number = random.randint(0, 100)
guess = int(input('Guess the number:\n'))
for i in number:
    if guess < i:
        print('Higher number please')
    elif guess > i:
        print('Lower number please')
    elif guess == i:
        print(f"Nice!!!, you guessed {i} correctly")
    else:
        print('What the hell did you guess uh?!')
import random
number = random.randint(0, 100)
guess = int(input('Guess the number:\n'))
attempt = 0
while guess != number:
    while attempt <= 5:
        attempt += 1
        guess = int(input('Guess the number:\n'))
        print(f"you have {attempt - 1} tries")
        if guess < number:
            print('Higher number please')
        elif guess > number:
            print('Lower number please')
        
        elif guess == number:
            print(f"Nice!!!, you guessed {number} correctly")
        else:
            print('What the hell did you guess uh?!')
    break
print('you have exhausted your tries')

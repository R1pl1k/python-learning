import random

secret: int = random.randint(1, 100)
attempts: int = 0

while True:
    guess: int = int(input("Какое число? "))
    attempts += 1

    if guess < secret:
        print("Больше!")
    elif guess > secret:                   
        print("Меньше!")
    else:
        print(f"Угадали за {attempts} попыток! Мое число было {guess}" )
        break
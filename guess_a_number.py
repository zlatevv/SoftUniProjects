import random
a = random.randint(1, 100)
while True:
    number = int(input("Guess a number from 1 to 100: "))
    if number == a:
        print(f"You guessed the number: {a}!")
        break
    else:
        print(f"{number} is not correct!")
        if number < a:
            if a - number <= 10:
                print("A little higher!")
            else:
                print("Higher!")
        else:
            if number - a <= 10:
                print("A little lower!")
            else:
                print("Lower!")
    print()
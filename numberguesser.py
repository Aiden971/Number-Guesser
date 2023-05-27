import random

number = input("Enter your highest range: ") #number is the highest range

if number.isdigit() == True:
    number = int(number)
    r = random.randint(0, number)

else:
    print("Print a number next time")
    quit()

while True:
    guess = input("Guess a number\n")
    if guess.isdigit() == False:
        print("Type a number, not a character")
        continue
    else:
        guess = int(guess)
        if guess > number:
            print("You need to enter a number lower than the highest range")
        if guess == r:
            print("You got it!")
            break
        elif guess > r:
            print("Just a bit lower")
        else:
            print("Just a bit higher")

    
import random
secret = random.randint(1, 50)
attempts = 0
while attempts <7:
    number = input("pick up a number between 1 and 50 (you have 7 attempts): ")
    try:
        number = int(number)
    except ValueError:
        print("Please enter an integer")
        continue
    if number < 1 or number > 50:
        print("Number must be between 1 and 50")
        continue
    if number == secret:
        print("You win")
        break
    elif number >secret:
        print("Too high")
        continue
    elif number<secret:
        print("Too low")
        continue
    elif abs(number - secret) <= 3:
        print("Very close")
        continue
    attempts += 1
print("Your attempts are done")
print("The secret number is : ", secret)



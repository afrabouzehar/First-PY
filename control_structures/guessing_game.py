import random
secret = random.randint(1, 50)
attempts = 0
while attempts <=7:
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
        attempts += 1
        print("Too high")
        continue
    elif number<secret:
        attempts += 1
        print("Too low")
        continue
    elif abs(number-secret)>1:
        attempts += 1
        print("Very close")
        continue
while attempts >= 7:
    print("Your attempts are done")
    print("The secret number is : ", secret)
    break


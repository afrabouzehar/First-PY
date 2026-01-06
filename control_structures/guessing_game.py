import random
secret = random.randint(1, 50)
attempts = 0
try:
while attempts <=7 and secret <=50 :
    number = input("pick up a number between 1 and 50 (you have 7 attempts): ")
    if number != int:
        print("It must be an integer")
        continue
    if number < 1 or number > 50:
        print("Number must be between 1 and 50")
        continue
    if number == secret:
        print("you win")
        break
    elif number >secret:
        attempts += 1
        print("too high")
        continue
    elif number<secret:
        attempts += 1
        print("too low")
        continue
    elif abs(number-secret)>1:
        attempts += 1
        print("very close")
        continue
    if attempts >= 7:
        print("Your attempts are done")
        print("The secret number is : ", secret)
        break


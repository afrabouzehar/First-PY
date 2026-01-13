import random
# Generate a secret number between 1 and 50
secret = random.randint(1, 50)
# Counter for attempts
attempts = 0
# The player has 7 attempts → loop runs while attempts < 7
while attempts <7:
    # Ask the user for input (always a string)
    number = input("pick up a number between 1 and 50 (you have 7 attempts): ")
    # Try to convert the input to an integer
    try:
        number = int(number)
    # If conversion fails → not an integer
    except ValueError:
        print("Please enter an integer")
        continue # invalid → do NOT count attempt
        # Check if the number is within the valid range
    if number < 1 or number > 50:
        print("Number must be between 1 and 50")
        continue # invalid → do NOT count attempt
    # Check if the user guessed correctly
    if number == secret:
        print("You win")
        break
    # Check if the guess is very close (difference of 3 or less)
    if abs(number - secret) <= 3:
        print("Very close")
    # If not close, check if it's too high or too low
    elif number > secret:
        print("Too high")
    else:
        print("Too low")
    # Count this as a valid attempt
    attempts += 1
# If the loop ended because attempts ran out (not because of break)
if attempts == 7 and number != secret:
    print("Your attempts are done.")
    print("The secret number was:",secret)



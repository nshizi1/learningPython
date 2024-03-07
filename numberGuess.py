import random

# Generate a random number between 1 and 10
correct_number = random.randint(1, 10)

# Use a while loop to keep prompting the user until they guess the correct number
while True:
    # Take user input for the guess
    user_guess_str = input("Guess a number between 1 and 10: ")

    # Check if the input is empty
    if not user_guess_str:
        print("You must enter a number!")
        continue

    try:
        # Try to convert the input to an integer
        user_guess = int(user_guess_str)

        # Check if the guess is within the valid range
        if user_guess > 10 or user_guess < 1:
            print("Invalid input. Please enter a number between 1 and 10.")
            continue

        # Check if the guess is correct
        if user_guess == correct_number:
            print("Congratulations! You guessed the correct number:", correct_number)
            break  # Exit the loop when the correct number is guessed
        else:
            print("Try again!")

    except ValueError:
        # Handle the case where the input is not a valid integer
        print("Invalid input. Please enter a valid number.")
        continue

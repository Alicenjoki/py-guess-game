import random
# print("I am thinking of a number between 1 to 10")

# compGuess = random.randint(1, 10)
# for i in range(1,6):
#     print("Take a guess")
#     guess = int(input())
    
#     if guess < compGuess:
#         print("Guess higher")
#     elif guess > compGuess:
#         print("Guess lower")
#     else:
#         break

# if guess == compGuess:
#     print("Yaaay! You guessed it write")
# else:
#     print("Failed!! The number was " + str(compGuess))

print("Enter a number between 1 and 20")
compGuess = random.randint(1, 20)
while True:
    for i in range(1,6):
        print("Take a guess")
        guess = int(input())
        if guess < compGuess:
            print("Guess higher")
        elif guess > compGuess:
            print("Guess lower")
        else:
            break

    if guess == compGuess:
        print("Yaaay!!! you guessed the number right in " + str(i) + " guesses")
    else:
        print("Failed to guess.The number is " + str(compGuess))

    play_again = input("Do you wih to play again? (y/n):")
    if play_again != "y":
        break
print("Bye!!Thank you for playing")
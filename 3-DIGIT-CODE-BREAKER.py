###########################
### --- Simple Game --- ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--##
###########################

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match, the game will report "CODE CRACKED"!


import random

def get_guess():
    return list(input("\nEnter your guess: "))

def generate_code():
    digits = [str(num) for num in range(10)]
    random.shuffle(digits)
    return digits[:3]

def generate_clues(code,userGuess):
    if userGuess == code:
        return ["CODE CRACKED"]

    clues = []
    for ind,num in enumerate(userGuess):
        if num == code[ind]:
            clues.append("Match")
        elif num in code:
            clues.append("Close")
    if clues == []:
        return ["Nope"]
    else:
        return clues

print("Welcome Code Breaker! Let's see if you can guess my 3 digit number!")

secretCode = generate_code()
print("Code has been generated, please guess a 3 digit number")

clueReport = []

count = 0
while clueReport != ["CODE CRACKED"]:
    count += 1
    guess = get_guess()
    clueReport = generate_clues(secretCode, guess)
    print("Result of your guess: ", end="")
    for clue in clueReport:
        print(clue, end=", ")
print('You guessed number in {} attempts!'.format(count))
print()

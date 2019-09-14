import urllib.request
import random

"""
    Author: Nkem Ohanenye
    Date: 11/26/18
    Purpose: Create a Wheel of Fortune program.
"""

'list of guessable words taken from hangman game'
animals = urllib.request.urlopen('http://davidbau.com/data/animals').read().split()

'random generator of word from the hangman game'
secret = random.choice(animals)

'decodes the code in bytes to human language, from  hangman game'
secret = secret.decode('utf-8')

'variables'
turns = 5
amount = 0
miss = 0
x = 0
found = False
'the letters that can be guessed'
consonants = ['b', 'c', 'd', 'f', 'g',
              'h', 'j', 'k', 'l', 'm',
              'n', 'p', 'q', 'r', 's',
              't', 'v', 'w', 'x', 'y',
              'z']
'the letters that were guessed'
guesses = []
'the letters that can be bought'
vowels = ['a','e','i','o','u']

"The user's hand"
hold = []

'The wheel'
wheel = [0, 5000, 500, 900, 700, 300,
         800, 550, 400, 500, 600,
         350, 500, 900, 0, 650, 'Free Play',
         700, -1, 800, 500, 450, 500, 300]

'The function that prints the secret line'
def key():
    'unknown used to check if you won, taken from hangman game'
    global unknown
    unknown = 0
    'used to check the letter in the secret number, taken from hangman game'
    for letter in secret:
        if letter in guesses:
            print(letter, end="")
        else:
            print('_', end=" ",)
            unknown += 1

'The function to make the wheel spin'
def spin():
    'randomizes the values in the list'
    random.shuffle(wheel)
    global amount
    global turns
    global guesses
    global x
    for x in wheel:
        print("\nYou spun: " + str(x))
        print("")

        'The list values on the wheel'
        if x == 0:
            print("Uh oh, you just became bankrupt")
            amount = 0
            turns -= 1
            print("\nYou are on turn: " + str(turns))
            break
        elif x == -1:
            print("Uh oh, you lost a turn")
            turns -= 1
            print("\nYou are on turn: " + str(turns))
        elif x == 'Free Play':
            print("You Won a Free Play")
            hold.append('Free Play')
            print("You currently have " + str(len(hold)) + " Free Plays")
        if turns == 0:
            break
        else:
            'used to make the shuffle truly random'
            break

'The function that asks the user for a letter'
def question():
    'lets the language know all uses in the code are the same to avoid an error'
    global turns
    global amount
    global miss
    global found
    'loop to keep the user in if they give a random answer'
    while True:
        'reprints the key'
        if miss >= 1:
            key()
            print("")
        'prints guesses in list if there is an item inside'
        if len(guesses) >= 1:
            print("\nYou already guessed: ")
            for guessed in guesses:
                print(guessed, end=", ")
        'gives choice of consonants'
        print("\nChoose between: ")
        for con in consonants:
            print(con, end=", ")
        'Asks the user for input and adds the guess to guesses, taken from hangman game'
        guess = input('\n\nGuess a letter: ')

        'checks if the guess is in the secret word, taken from hangman game'
        if guess in consonants:
            if guess not in secret:
                print("\nI'm sorry, but that letter is not here.")
                'adds the guess to guesses and removes the guess from the constants'
                guesses.append(guess)
                consonants.remove(guess)
                turns -= 1
                print("\nYou are on turn: " + str(turns))
                miss = 0
                answer()
                break
            elif guess in guesses:
                'stays in case of unseeable bug'
                print("\nYou already guessed that letter")
                print("\nYou are on turn: " + str(turns))
                miss = 0
                answer()
            elif secret.count(guess) >= 3:
                'Checks if the player got more than 3 letters'
                print("You found " + str(secret.count(guess)) + " letters")
                print("\nYour award is tripled!")
                guesses.append(guess)
                consonants.remove(guess)
                amount += (x * 3)
                key()
                'checks for win'
                if unknown == 0:
                    found = True
                    break
                else:
                    print("\nYour current amount is: " + "$" + str(amount))
                    buy_vowel()
                    print("\nYou are on turn: " + str(turns))
                miss = 0
                if found is not True:
                    answer()
                else:
                    break
                'in case of unforeseen error'
                break
            else:
                print("\nCongratulations, you answered correctly!")
                guesses.append(guess)
                consonants.remove(guess)
                amount += x
                key()
                if unknown == 0:
                    found = True
                    break
                else:
                    print("\nYour current amount is: " + "$" + str(amount))
                    buy_vowel()
                    print("\nYou are on turn: " + str(turns))
                miss = 0
                if found is not True:
                    answer()
                else:
                    break
                'in case of unforeseen error'
                break
        else:
            'to not crash from random answers'
            print("\nI'm sorry, please try again.\n")
            miss += 1

'The function to buy the vowels'
def buy_vowel():
    global player
    global turns
    global amount
    global found
    if amount > 250:
        while True:
            'asks the player if they want to buy a vowel'
            player = input("\nWould you like to buy a vowel? (y/yes or n/no): ")
            print("")
            if (player == "yes") or (player == "y"):
                for vow in vowels:
                    print(vow, end=", ")
                'checks what vowel you wish to buy'
                buy = input("\nWhich vowel would you like to buy?: ")
                if buy in vowels:
                    print("\nYou have bought: " + buy)
                    amount -= 250
                    if buy not in secret:
                        'if the letter is not present in the secret word'
                        print("\nI'm sorry, but that letter is not here.")
                        'adds the bought vowel to the guesses and removes the vowel from the vowels list'
                        guesses.append(buy)
                        vowels.remove(buy)
                        turns -= 1
                        break
                    elif buy in guesses:
                        'stays in case of unseeable bug'
                        print("\nYou already guessed that letter")
                        print("\nYou are on turn: " + str(turns))
                    else:
                        'You get a letter'
                        print("\nCongratulations, you answered correctly!")
                        guesses.append(buy)
                        vowels.remove(buy)
                        key()
                        if unknown == 0:
                            found = True
                            break
                        else:
                            break
                else:
                    'to not crash from random answers'
                    print("Sorry, once more.")

            elif (player == "no") or (player == "n"):
                print("\nAlright, then spin again...\n")
                break
            else:
                print("Sorry, once more.")

'The function to figure out the secret word'
def answer():
    global turns
    global word
    global found
    'checks if you know the secret answer'
    while True:
        player = input("\nDo you know the secret word? (y/yes or n/no): ")
        if (player == "yes") or (player == "y"):
            'if you dont know the word you lose a turn'
            word = input("\nWhat is the word?: ")
            if str(word) == secret:
                found = True
                break
            else:
                print("\nI'm sorry, you are incorrect.")
                turns -= 1
                break
        elif (player == "no") or (player == "n"):
            print("\nAlright, spin again\n")
            break
        else:
            print("Sorry, once more.")

'Game Start'
player = input("Would you like to play Wheel of Fortune? (y/yes): ")
if (player == "yes") or (player == "y"):
    'welcomes player to the game'
    print("Welcome to The Wheel Of Fortune!")
    print("The category is......animals!")
    print("\nYou are on turn: " + str(turns))
    while True:
        'prints the key you will be going off of'
        key()
        if unknown == 0:
            found = True
            break
        elif turns != 0:
            'initiates the spin function'
            spin()
            for x in wheel:
                if x != -1 and x != 0 and x != 'Free Play':
                    question()
                    'breaks out of loop'
                    break
                else:
                    break
            if found is True:
                break
        elif (turns == 0) and (len(hold) >= 1):
            print("You use a Free Play")
            turns += 1
            print("You are on turn: " + str(turns))
            hold.pop(0)
        else:
            'breaks out of else'
            break
    if found is False:
        'you lose'
        print("You ran out of rounds, your final score is: " + str(amount))
        print("\nThe correct answer was: " + secret)
        print("Game Over")
    else:
        'you win'
        print("\n\nCongratulations! You won the Wheel Of Fortune!")
        print("You won: " + "$" + str(amount))
else:
    'you quit'
    print("I guess you didn't want to play...")
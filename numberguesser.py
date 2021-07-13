import random
number = random.randint(1, 10)


player_name = input('What is your name? ')
number_of_guesses = 0
print('''Hello! ''' + player_name + " Let's start the game, Press W for instructions. " )
instructions = input('')

if instructions.upper() == 'W':
    print(''' You have to guess a random number between 1 to 10 
 You only have 5 number of guesses! ''')
else:
    print("I did not understand that, sorry ")
    quit()

while number_of_guesses <= 4:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('The guess is low. ')
    if guess > number:
        print('The guess is high. ')
    if guess == number:
        break
if guess == number:
    print('You guessed the number in ' + str(number_of_guesses) + ' tries! ')
else:
    print('Alas you lost! The number was ' + str(number) + '. ')

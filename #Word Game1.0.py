#Word Game


#random word generator
import random

word_bank = []
missplaced = []
incorrect = []
guess_number = 0

with open("words.txt") as word_file:
	for line in word_file:
		word_bank.append(line.rstrip().upper())

rando_word = random.choice(word_bank)


#guessing system

print('Welcome to word guesser.\n Your job is to guess a 5 letter word in 5 tries or less.\n')
print('For the record, there are adult words on the list of possible options.')



while guess_number < 5:
	index = 0
	guess = input('What is your guess?: ').upper()

	if len(guess) != len(rando_word) or not guess.isalpha():
		print('Please enter a five letter word')
		continue


	for i in guess:
		if i == rando_word[index]:
			print(i, end=' ')
			if i in missplaced:
				missplaced.remove(i)



		elif i in rando_word:
			if i not in missplaced:
				missplaced.append(i)
			print('_', end=' ')
		
		if i not in rando_word:
			if i not in incorrect:
				incorrect.append(i)
			print('_', end=' ')

		index += 1


	print('\n')
	print('Missplaced Guesses: ', missplaced)
	print('Incorrect Guesses: ', incorrect)
	guess_number += 1
	print('Turns remaining: ', 5 - guess_number)

	if guess == rando_word:
		print('Congradulations, you have guessed correctly.')
		break
	
	if guess_number == 5:
		print('You have taken too many turns.')
		print('You lose. Better luck next time.')
		print('The word you are looking for is ', rando_word)
		break
exit


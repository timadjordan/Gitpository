import random

def init():
	printChoices()
	main(0, '?')

#a function for using other functions
def main(invOptCounter, prevUserChoice):
	invOptCounter = invOptCounter
	userChoice = input('Input a command to execute a function. ')
	if userChoice == 'r':
		userChoice = prevUserChoice
	if userChoice == 'a':
		autoTyper('', 0) # 0 means use type0 words 
	elif userChoice == 'a1':
		autoTyper('', 1) # with type1 words
	elif userChoice == 'a2': # Uses words created with
		autoTyper('', 2)	 # the weighted alphabet.(type2)
	elif userChoice == 'c':
		wordList()
#     elif userChoice == 'd':
#         proceduralGrammerizerA()
	elif userChoice == '?':
		init()
	elif userChoice == 'q':
		print('OK')
	elif invOptCounter == 3:
		print("You aren't very good at this.")
		print("To see the options again type '?'")
		invOptCounter = 0
		main(0, userChoice)
	else:
		print(str(userChoice) + ' is not a valid option.')
		invOptCounter += 1
		main(invOptCounter, userChoice)
		
#types a sentence
def autoTyper(randSentence, wType):
	sentenceLength = random.randint(1,8)
	while sentenceLength > 0:
		if wType == 0:
			randSentence += wordMaker()
		elif wType == 1:
			randSentence += wordMakerPlus()
		else:
			randSentence += wordMakerWeighted()
		if sentenceLength != 1:
			randSentence += ' '
		sentenceLength -= 1
	punctuation = punctuationSelector()
	randSentence += punctuation
	if punctuation == '.' or punctuation == '!' or punctuation == '?':
		print(randSentence)
		if wType == 0:
			main(0, 'b')
		elif wType == 1:
			main(0, 'b1')
		else:
			main(0, 'b2')
	else:
		randSentence += ' '
		autoTyper(randSentence, wType)

# creates a word
def wordMaker():
	wordLength = random.randint(1,6)
	word = ''
	while wordLength > 0:
		word += random.choice(alphabet)
		wordLength -= 1
	return word

#returns pronouncable words
def wordMakerPlus():
	wordLength = random.randint(1,6)
	startsVowel = random.randint(0,1)
	word = ''
	if startsVowel == 0:
		word += random.choice(unVowels + uVSCombos + uVRCombos + uVOtherCombos)
	else:
		word += random.choice(vowels)
	while wordLength > 0:
		if isVowel(word):
			word += random.choice(unVowels + uVSCombos + uVRCombos + uVOtherCombos)
		else:
			word += random.choice(vowels)
		wordLength -= 1
	return word

#returns a word with the letters chosen from a weighted list
def wordMakerWeighted():
	wordLength = random.randint(1,6)
	word = ''
	while wordLength > 0:
		word += random.choice(weightedAlphabet)
		wordLength -= 1
	return word

#returns a punctuaton mark
def punctuationSelector():
	return random.choice(['.','!','?',',',';',':'])

#checks if the last character in a string is a vowel and returns a bool
def isVowel(word):
	prevWord = word[-1]
	if prevWord == 'a' or prevWord == 'e' or prevWord == 'i' or prevWord == 'o' or prevWord == 'u' or prevWord == 'y':
		return True
	else:
		return False
		
def wordList():
	sentenceLength = 10
	typeOhWords = "Type0 words: "
	typeOneWords = "Type1 words: "
	typeTwoWords = "Type2 words: "
	while sentenceLength > 0:
		typeOhWords += wordMaker() + ' '
		typeOneWords += wordMakerPlus() + ' '
		typeTwoWords += wordMakerWeighted() + ' '
		sentenceLength -= 1
	print(typeOhWords)
	print(typeOneWords)
	print(typeTwoWords)
	main(0, 'c')
	
#part of init
def printChoices():
	print('a: autoTyper')
	print('a1: autoTyperPlus')
	print('a2: autoTyperPlusOne')
	print('c: sampler')
#	 print('d: proceduralGrammarizerA')
	print('r: repeat last command')
	print('q: quit')
	print('?: display options')
	print()

# Global Variables
vowels = ['a','e','i','o','u','y']
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']
weightedAlphabet = (['e'] * 15 + ['t'] * 12 + ['a'] * 11 + ['o'] * 10
	+ ['i', 'n', 's', 'h', 'r'] * 9 + ['d', 'l'] * 7 
	+ ['c', 'u', 'm', 'w', 'f', 'g', 'y', 'p'] * 5
	+ ['b', 'v', 'k'] * 3 + ['j', 'x', 'q', 'z'])
unVowels = ['b','c','d','f','g','h','j','k','l','m','n','p','q','qu,','r','s','t','v','x','y','z']
uVSCombos = ['bs','cs','ds','fs','gs','hs','js','ks','ls','ms','ns','ps','qs','rs','ss','ts','vs','ys']
uVRCombos = ['br','cr','dr','fr','gr','pr','rr','tr']
uVOtherCombos = ['ph','tt','sh','ll','sw','ch','ck','sm','sn','sk']

init()
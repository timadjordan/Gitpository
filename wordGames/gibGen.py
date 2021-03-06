def init():
	printChoices()
	main(0, '?')

#a function for using other functions
def main(invOptCounter, prevUserChoice):
    invOptCounter = invOptCounter
	userChoice = input('Input a command to execute a function. ')
    if userChoice == 'r':
        userChoice = prevUserChoice
#     if userChoice == 'a':
#         typeOne()
    elif userChoice == 'b':
        autoTyper('', False)
    elif userChoice == 'b1':
        autoTyper('', True)
#     elif userChoice == 'c':
#         printPattern()
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
def autoTyper(randSentence, speakable):
    sentenceLength = random.randint(1,8)
    while sentenceLength > 0:
        if speakable != True:
            randSentence += wordMaker()
        else:
            randSentence += wordMakerPlus()
        if sentenceLength != 1:
            randSentence += ' '
        sentenceLength -= 1
    punctuation = punctuationSelector()
    randSentence += punctuation
    if punctuation == '.' or punctuation == '!' or punctuation == '?':
        print(randSentence)
        if speakable:
            main(0, 'b1')
        else:
            main(0, 'b')
    else:
        randSentence += ' '
        autoTyper(randSentence, speakable)

# creates a word
def wordMaker():
    wordLength = random.randint(1,6)
    word = ''
    while wordLength > 0:
        word += random.choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z'])
        wordLength -= 1
    return word

#returns pronouncable words
def wordMakerPlus():
    wordLength = random.randint(1,4)
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

#returns a punctuaton mark
def punctuationSelector():
    return random.choice(['.','!','?',',',';',':'])

#checks if the preceeding character in a string is a vowel and returns a bool
def isVowel(word):
    if word[-1] == 'a' or word[-1] == 'e' or word[-1] == 'i' or word[-1] == 'o' or word[-1] == 'u' or word[-1] == 'y':
        return True
    else:
        return False
	
#part of init
def printChoices():
#    print('a: typeOne')
    print('b: autoTyper')
    print('b1: autoTyperPlus')
#    print('c: printPattern')
#     print('d: proceduralGrammarizerA')
    print('r: repeat last command')
    print('q: quit')
    print('?: display options')
    print()

# Global Variables
vowels = ['a','e','i','o','u','y']
# There must be a way to use weighted random to select vowels and unVowels.
# Math, maybe.
weightedAlphabet = (['e'] * 15 + ['t'] * 12 + ['a'] * 11 + ['o'] * 10
	+ ['i', 'n', 's', 'h', 'r'] * 9 + ['d', 'l'] * 7 
	+ ['c', 'u', 'm', 'w', 'f', 'g', 'y', 'p'] * 5
	+ ['b', 'v', 'k'] * 3 + ['j', 'x', 'q', 'z'])
unVowels = ['b','c','d','f','g','h','j','k','l','m','n','p','q','qu,','r','s','t','v','x','y','z']
uVSCombos = ['bs','cs','ds','fs','gs','hs','js','ks','ls','ms','ns','ps','qs','rs','ss','ts','vs','ys']
uVRCombos = ['br','cr','dr','fr','gr','pr','rr','tr']
uVOtherCombos = ['ph','tt','sh','ll','sw','ch','ck','sm','sn','sk']

init()

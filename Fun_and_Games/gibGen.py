def init():
	print(weightedAlphabet)

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

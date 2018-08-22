import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open('data.json'))

def translate(word):
	word = word.lower()
	if word in data:
		return data[word]
	elif len(get_close_matches(word, data.keys())) > 0:
		yn = input('Did you mean %s instead? Enter Y if yes or N if no:' % get_close_matches(word, data.keys())[0])
		if yn == 'Y'or 'y':
			return data[get_close_matches(word, data.keys())[0]]
		elif yn == 'N' or 'n':
			return 'The word doesn\'t exist'
		else:
			return 'We didn\'t understand the word' 
	else:
		return 'The word does not exist in the dictionary. Please check again...'

word = input('Enter a word: ')
print(translate(word))
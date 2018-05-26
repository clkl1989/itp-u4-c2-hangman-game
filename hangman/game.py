from .exceptions import *
import random
# Complete with your own, just for fun :)
LIST_OF_WORDS = []


def _get_random_word(list_of_words):
    #1. pick an integer from the len(list_of_words)
    #2. return word in the list at the position of the integer
    number_of_words = len(list_of_words)
    if number_of_words == 0:
        raise InvalidListOfWordsException
    random_int = random.randint(0,number_of_words)
    return list_of_words[random_int-1]

def _mask_word(answer_word):
    #1. count length of word
    #2. for loop of the length of word to add one asterisk until length of maskedWord = length of word
    if (answer_word == None or answer_word == ''):
        raise InvalidWordException

    word_length = len(answer_word)
    masked_word = ""
    for i in range(word_length):
        masked_word = masked_word + "*"
    print(masked_word)
    return masked_word

def _uncover_word(answer_word, masked_word, guessed_letter):
    #1. make answer_word into a list A
    #2. make masked_word into a list B
    #3. check if guessed_letter is in list A
    #4. if guessed_letter is in list A, find all the positions of the guesseed_letter in list A
    #5. replace the asterisks in these positions in list B with the guessed_letter
    #6. join list B back into a string
    #7. return string for list B
    if (answer_word == None or answer_word == ''):
        raise InvalidWordException
    if (masked_word == None or masked_word == ''):
        raise InvalidWordException
    if (guessed_letter == None or guessed_letter == ''):
        raise InvalidWordException
    if (len(guessed_letter) > 1):
        raise InvalidGuessedLetterException
    if (len(answer_word)!=len(masked_word)):
        raise InvalidWordException
    
    list_A = list(answer_word)
    list_B = list(masked_word)
    for i in range(len(list_A)):
        if list_A[i].lower() == guessed_letter.lower():
            list_B[i] = guessed_letter.lower()
    return "".join(list_B)



def guess_letter(game, guessed_letter):
    #1. Return _uncover_word to modify variables inside game
    #2. Replace masked_word with result from #1
    if game['remaining_misses'] == 0 or game['masked_word'] == game['answer_word']:
        raise GameFinishedException
    guessed_letter = guessed_letter.lower()
    new_masked_word = _uncover_word(game['answer_word'],game['masked_word'],guessed_letter)
    if game['masked_word'] == new_masked_word:
        game['remaining_misses'] = game['remaining_misses'] - 1
    if game['remaining_misses'] == 0:
        raise GameLostException
        
    game['masked_word'] = new_masked_word
    game['previous_guesses'].append(guessed_letter)

    if game['masked_word'] == game['answer_word']:
        raise GameWonException

    pass
    
def start_new_game(list_of_words=None, number_of_guesses=5):
    if list_of_words is None:
        list_of_words = LIST_OF_WORDS

    word_to_guess = _get_random_word(list_of_words)
    masked_word = _mask_word(word_to_guess)
    game = {
        'answer_word': word_to_guess,
        'masked_word': masked_word,
        'previous_guesses': [],
        'remaining_misses': number_of_guesses,
    }

    return game
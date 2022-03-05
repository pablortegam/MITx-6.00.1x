def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
#     if set(secretWord).intersection(lettersGuessed)==set(secretWord):
#         return True
#     else:
#         return False
    return True if set(secretWord).intersection(lettersGuessed)==set(secretWord) else False
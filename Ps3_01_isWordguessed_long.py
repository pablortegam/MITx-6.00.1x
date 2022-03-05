def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    countnot=0
    for letter in secretWord:
        if letter not in lettersGuessed:
            countnot+=1
    if countnot>0:
        return False
    else:
        return True
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alpha='abcdefghijklmnopqrstuvwxyz'
    availableletters=''
    for letter in alpha:
        if letter not in lettersGuessed:
            availableletters+=letter
    return availableletters
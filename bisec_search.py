print('Please think of a number between 0 and 100!')
while llim != hlim:
    number=(llim+hlim)//2
    print('Is your secret number '+str(number)+'?')
    letter=input("Enter 'h' to indicate the guess is too high.Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly: ")
    if letter=='c':
        print('Game over. Your secret number was: '+str(number))
        break
    elif letter == 'h':
        hlim=number
    elif letter == 'l':
        llim=number
    else:
        print('Sorry, I did not understand your input.')

from random import randint

def roll2dice():
    '''simulates rolling 2 dice and returns the sum of the dice'''
    die1 = randint(1,6)
    die2 = randint(1,6)
    dicesum = die1+die2
    print("you rolled a", die1, "and",die2)
    return dicesum
    
def play1game():
    ''' simulates one game of craps and returns True if user wins, false if they lose
        and it prints out all of the rolls of the dice.
        
    '''
    roll1 = roll2dice()
    if roll1 == 2 or roll1 == 3 or roll1 == 12:
        print("you lose!")
        return False
    elif roll1 == 7 or roll1 == 11:
        print("you win!")
        return True
    else:
        print(f"you have to roll a {roll1} before a 7 to win")
        result = play_rest_game(roll1)
        return result
    
def play_rest_game(point):
    ''' returns True if they roll the point before a 7, False otherwise '''
    roll = roll2dice()
    while roll != point and roll!=7:
        roll=roll2dice()
    if roll==point:
        print('you win!')
        return True
    else:
        print("you lose")
        return False
    
def play_craps(state):
    ''' repeatedly asks the user if they want to play
        if so, it calls play1game()
        and continues until they don't want to play anymore
    '''
    balance=100
    print('you have',balance,'dollars')
    playvar = input("Do you want to play a game of craps? (y/n) ")
    while playvar == "y":
        bet = int(input(f"how much would you like to bet? (out of {balance})"))
        if bet > balance:
            print("Sorry, you can't bet more than your balance!")
            continue
        user_won = play1game()
        if user_won:
            print('good job, you won')
            balance += bet
        else:
            print('sorry you lost')
            balance -= bet
        print('you have',balance,'dollars')
        playvar = input("Do you want to play again? (y/n)")
    print('Goodbye')


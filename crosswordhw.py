
def valid_pattern(pattern):
    ''' returns true or false if the entered pattern is valid '''
    for c in pattern:
        if c != 'C' and c != 'V' and c != '.' and not c.islower():
            print(c,"not allowed in patterns")
            return False
    return True

def matches(word, pattern):
    ''' returns true if the word matches the pattern '''
    V = "aeiou"
    C = "bcdfghjklmnpqrstvwxyz"

    if len(word) != len(pattern):
        return False

    for n in range(len(word)):
        if pattern[n] == 'C' and word[n] not in C:
            return False
        elif pattern[n] == 'V' and word[n] not in V:
            return False
        elif pattern[n] == '.' and not word[n].islower():
            return False
        elif pattern[n].islower() and pattern[n] != word[n]:
            return False
    return True


def search_for_words():
    ''' asks the user for a pattern and then prints out its matching words '''
    count = 0
    pattern = input("enter a pattern with . for unknown lowercase letters C for consonants, and V for vowels \n > ")
    while not valid_pattern(pattern):
        print("the pattern must only contain lowercase letters or C or V or periods (.)")
        pattern = input("give another pattern: ")
        
    wordfile = open('wlist_match8.txt', 'r')
    wordstring = wordfile.read()
    words = wordstring.split()
    for word in words:
        if matches(word, pattern):
            print(word)
            count+=1
    print(count,"matches were found")

        


def word_search_loop():
    ''' asks user if they want to continue searching for words and calls search_for_words() if yes '''
    cont = input("Want to search for words? (y or n): ")
    while cont == 'y':
        print("----------------------------------------")
        search_for_words()
        cont = input("more? (y or n): ")

word_search_loop()

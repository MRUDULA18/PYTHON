def countLetters(word):
    letterdict={}
    for letter in word:
        letterdict[letter] = 0
    for letter in word:
        letterdict[letter] += 1
    return letterdict
 print countLetters("yahoo.in")

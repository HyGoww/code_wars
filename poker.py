# Determine if the poker hand is flush, meaning if the five cards are of the same suit.

# Your function will be passed a list/array of 5 strings, each representing a poker card in the format "5H" (5 of hearts), meaning the value of the card followed by the initial of its suit (Hearts, Spades, Diamonds or Clubs). No jokers included.

# Your function should return true if the hand is a flush, false otherwise.

# The possible card values are 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A

realFlush = ["AS", "3S", "9S", "KS", "4S"]
fakeFlush = ["AD", "4S", "7H", "KS", "10S"]

def all_letters_are_same(string):
    # fonction all qui permet en fonction du premier caractère voir si les autres sont pareils
    return all(s == string[0] for s in string)

def flush(suite):
    letters = ""
    for card in suite:
        letters += card[-1]
    if(all_letters_are_same(letters)):
        print("Flush !")
    else:
        print("Not flush looser booooouuuuuuh le gros naze t'as tout perdu")
        

flush(fakeFlush)

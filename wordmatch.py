
import re

def main():
    # want to randomly print out a word.
    print "Insert random word here.\n"

    while True:
        user_word = raw_input("Your turn: ").upper()
        if (not check(user_word)):
            print "Try again? Word is: " + next_word + "\n"
        else:
            # add the word to known words..
            said_words.append(user_word)

            next_word = find_next(user_word)
            if (len(next_word) < 4):
                print "No more words can be found. You're da wordmaster!\n"
                break

            # otherwise, good! print that thing
            print "\n" + next_word + "\n"
            said_words.append(next_word)

def check_said(new):
    # If it's already been said, then that's bad too!
    for word in said_words:
        if (new == word):
            return False
    return True

def check_dict(new):
    f = open('4words.txt', 'r')
    # I guess just linear search through for the word in the total list..
    for line in f:
        if (new == line[:-1]):
            f.close()
            return True
    f.close()
    return False

def check_related(new):
    if (len(said_words) == 0):
        return True

    # can only be one character off from the previously added word.
    regex = '[A-Z]'
    patterns = []
    patterns.append(new.replace(new[0], regex))
    patterns.append(new.replace(new[1], regex))
    patterns.append(new.replace(new[2], regex))
    patterns.append(new.replace(new[3], regex))

    for p in patterns:
        m = re.search(p, said_words[-1])
        if (m):
            return True

    return False


def check(new):
    if (len(new) != 4):
        return False

    if (not check_dict(new)):
        print "Not a valid word! "
        return False

    if (not check_said(new)):
        print "Already been said! "
        return False

    # already know hasn't been said, just check character off
    if (not check_related(new)):
        print "Too many characters off! "
        return False

    return True

def find_next(new):
    # painfully stupid...just switch out each possible letter and then call
    # check?

    regex = '[A-Z]'
    patterns = []
    patterns.append(new.replace(new[0], regex))
    patterns.append(new.replace(new[1], regex))
    patterns.append(new.replace(new[2], regex))
    patterns.append(new.replace(new[3], regex))

    f = open('4words.txt', 'r')

    for p in patterns:
        for line in f:
            m = re.search(p, line)
            if (m):
                next_word = line[m.start():m.end()]
                if (check_said(next_word)):
                    f.close()
                    return next_word

    f.close()
    return "no"


# create a list of the words that have been said.
said_words = []

main()

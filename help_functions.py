#!

import itertools

def UniqueEverseen(iterable, key=None):
    seen = set()
    seen_add = seen.add
    if key is None:
        for element in ifilterfalse(seen.__contains__, iterable):
            seen_add(element)
            yield element

def GetRawInput(question, type):
    save = 2
    try:
        if type == int:
            save = int(raw_input(question))
            print save
        else:
            save = list(raw_input(question))
            print save
    except (TypeError, ValueError):
            print "is not an integer"
            save = GetRawInput(question, type)

#       while not ((save == 0) or (save == 1)):
#               print "please choose a 0 or a 1"
#               save = GetRawInput(question, type)
    return save

#def GetRawInput(question):
#       save = 2
#       try:
#               save = int(raw_input(question))
#               print save
#       except (TypeError, ValueError)
#               print "is not an integer"
#               save = GetRawInput(question)
#
#       while not ((save == 0) or (save == 1)):
#               print "please choose a 0 or a 1"
#               save = GetRawInput(question)
#       return save

#def GetInput():
#       save = 2
#       try:
#               save = int(raw_input("Do you want to save any dice? 0 = No, 1 = Yes "))
#       except (TypeError, ValueError):
#               print "is not an integer"
#               save = GetInput()

#       while not ((save == 0) or (save == 1)):
#               print "please choose a 0 or a 1"
#               save = GetInput()
#               return save

def Zeroize(score_class):
    score_class.totalsDict['Ones'] = 0
    score_class.totalsDict['Twos'] = 0
    score_class.totalsDict['Threes'] = 0
    score_class.totalsDict['Fours']= 0
    score_class.totalsDict['Fives'] = 0
    score_class.totalsDict['Sixes'] = 0

def CountDice(listOfDice, score_class):
    Ones = 0
    Twos = 0
    Threes = 0
    Fours = 0
    Fives = 0
    Sixes = 0

    for j in range(len(listOfDice)):
        if listOfDice[j] == 1:
            score_class.totalsDict['Ones'] += 1
        elif listOfDice[j] == 2:
            score_class.totalsDict['Twos'] += 1
        elif listOfDice[j] == 3:
            score_class.totalsDict['Threes'] += 1
        elif listOfDice[j] == 4:
            score_class.totalsDict['Fours'] += 1
        elif listOfDice[j] == 5:
            score_class.totalsDict['Fives'] += 1
        else:
            score_class.totalsDict['Sixes'] += 1
    return score_class

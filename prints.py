#!

def PrintUsedList(score_class):
    for q in score_class.usedScoresDict:
        if (len(q) < 7):
            print q, '\t\t\t', score_class.usedScoresDict[q]
        elif (len(q) >= 7) and (len(q) <= 14):
            print q, '\t\t', score_class.usedScoresDict[q]
        else:
            print q, '\t', score_class.usedScoresDict[q]

def PrintScoreList():
    print('''
  Yahtzee:              50 points       Ones:           Total of Ones
  Small straight:       30 points       Twos:           Total of Twos
  Large straight:       30 points       Threes:         Total of Threes
  Full House:           25 points       Fours:          Total of Fours
  Three of a kind:      Dice Total      Fives:          Total of Fives
  Four of a kind:       Dice Total      Sixes:          Total of Sixes
  Chance:               Dice Total
        ''')

def PrintTitle():
    print('''

You ready for 

 _________   _________   _  _  __   _  _  ____  ____  ____  ____
|         | |         | ( \/ )/ _\ / )( \(_  _)(__  )(  __)(  __)
|  o   o  | |  o   o  |  )  //    \) __ (  )(   / _/  ) _)  ) _)
|  o   o  | |    o    | (__/ \_/\_/\_)(_/ (__) (____)(____)(____)
|  o   o  | |  o   o  |
|_________| |_________|

                         _________   _________
                        |         | |         |
                        |  o   o  | |  o      |
                        |         | |    o    |
                        |  o   o  | |      o  |
                        |_________| |_________|

                                                  _________   _________
                                                 |         | |         |
                                                 |  o      | |         |
                                                 |         | |    o    |
                                                 |      o  | |         |
                                                 |_________| |_________|
little fella?
''')



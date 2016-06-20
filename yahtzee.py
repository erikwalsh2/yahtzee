#!

#Yahtzee

import random
from collections import OrderedDict
from collections import Counter
from itertools import groupby
from help_functions import UniqueEverseen
from help_functions import GetRawInput
from help_functions import Zeroize
from help_functions import CountDice
from prints import PrintUsedList
from prints import PrintScoreList
from prints import PrintTitle
import itertools

def Game():

    #create player class
    class player:
        diceList = []
        totalScore = 0
        diceToRoll = 5
        diceTotal = 0
        name = raw_input("\n\nWhat is your name? ")
        loopCounter = 0
        tempList = [0,0,0,0,0]

    #create score class
    class score_class:
        turnScore = 0
        bonus = 0
        un = 'unused'
        total = 0
        count = 0
        singles_counter = 0
        totalsDict = OrderedDict([('Ones', 0), ('Twos', 0), ('Threes', 0), ('Fours', 0), ('Fives', 0), ('Sixes', 0)])
        scoresDict = {'Yahtzee':50, 'Chance': total, 'Full House':25, 'Three of a kind': total, 'Four of a kind':total, 'Small straight':30, 'Large straight':35, 'Ones':total, 'Twos':total, 'Threes':total, 'Fours':total, 'Fives':total, 'Sixes':total}
        usedScoresDict = OrderedDict([('Yahtzee',un),('Chance',un),('Full House',un), ('Three of a kind',un), ('Four of a kind',un), ('Small straight',un), ('Large straight',un), ('Ones',un), ('Twos',un), ('Threes',un), ('Fours',un), ('Fives',un), ('Sixes',un)])

#    PrintTitle()
    player1 = player()
    score = score_class()

    Turn (player1, score)

    score.bonus = Bonus(score)
    if score.bonus == 1:
        print '\nYou scored over 63 points on the singles!  You receive a bonus of 35 points!'
        player1.totalScore = player1.totalScore + 35
    else:
        print '\nYou did not receive the bonus'
    print '*****$$$$$*****$$$$$*****$$$$$*****'
    print "\n\nNice game", player1.name, ".  Your final score was: ", player1.totalScore, '\n'
    if (player1.name == 'Mitch') or (player1.name == 'Mitchell') or (player1.name == 'mitch') or (player1.name == 'mitchell'):
        print "\n That is a terrible name for really reals"

#TODO -- extra yahtzees, discard other score
#TODO -- score checking for large straight
#TODO -- score checking for four of a kind
#TODO -- functions to list scores on command
#TODO -- score checking for large straight, wont let me use it sometimes
#	 (EX. - 1, 3, 4, 5, 6)
#TODO -- adapt for 2 players
#TODO -- if all dice are saved, don't roll again
#TODO -- implement a save all dice option
#TODO -- don't ask which one to keep if there is only 1 die

#       PlayAgain(player1)

def Turn (current_player, score_class):

    roll_count = 0
    turn_count = 0

    #amount of turns
    for i in range(13):
        print "\nTURN ", i+1, "\n"

        #amount of rolls per turn
        for j in range(3):
            current_player.tempList = Roll(current_player)
            roll_count = roll_count + 1
            #need to split list and calculate total below - in save function?
            current_player.diceTotal = sum(current_player.diceList)
            print '\ncalculated total of dies: ', current_player.diceTotal
            print "the roll count is ", roll_count
            current_player.diceToRoll = current_player.diceToRoll - (len(current_player.tempList))
            current_player.diceList.extend(current_player.tempList)
            current_player.loopCounter = current_player.loopCounter + 1
        roll_count = 0
        current_player.diceToRoll = 5
        current_player.loopCounter = 0
        scoreDict = Totals(current_player.diceTotal, current_player.diceList, 
                    score_class)
        raw_input('\n\nPress \'enter\' key to continue to scoring ')
        Scoring (score_class,current_player.diceTotal, current_player.diceList)
        print "\nthe turn count is: ", turn_count +1
        current_player.diceList[:] = []
        turn_count = turn_count + 1
        current_player.totalScore = current_player.totalScore + score_class.turnScore
        print '\n Your total score is: ', current_player.totalScore
        Zeroize(score_class)
    return score_class

def Roll(player1):
    num_dice = 5
    sides = 6
    total = 0
    hold_list = [0,0,0,0,0]
    listNew = []
    print "\n *** dice to roll *** ----> ", player1.diceToRoll
    for r in range(player1.diceToRoll):
        x = random.randint(1,sides)
        print 'For die #', r, 'you rolled a', x
        total += x
        hold_list[r] = x

    if player1.loopCounter < 2:
        text = "Do you want to save any dice? 0 = No, 1 = Yes  "
        saveany = GetRawInput(text, int)
        while not ((saveany == 0) or (saveany == 1)):
            print "please choose a 0 or a 1"
            saveany = GetRawInput(text,int)
        if saveany == 0:
            print "No dice saved "
        else:
            listNew = Save(hold_list)
            list_length = len(listNew)
            print "The number of dice saved is ", list_length
    else:
        SaveList(player1,hold_list)

    return listNew

#TODO -- check bounds of dice
#TODO -- error handling

#TODO -- all messed up, revert to commented out version of Save?
#TODO -- fix bug that lets you select multiples of dice ex -> saving 00000 will save 5 copies of the first die.
#     -- needs to be one digit
def Save(hold_list):
        text = "which ones? - Enter space separated values "
        temp_list = GetRawInput(text, list)
        x = len(temp_list)
        for i in range(x):
            if i == x:
                break
            if temp_list[i] == ' ':
                x = x - 1
                temp_list.pop(i)
        for i in range(len(temp_list)):
            temp_list[i] = int(temp_list[i])
        new_list = list(hold_list[i] for i in temp_list)
        print new_list
        list_length = len(new_list)
        return new_list

#def Save(hold_list):
#    print "which ones? - Enter space separated values "
#    temp_list = map(int, raw_input().split())
#    new_list = list(hold_list[i] for i in temp_list)
#    print new_list
#    list_length = len(new_list)
#    return new_list

def SaveList(player1,hold_list):
    list_length = len(hold_list)
    for i in range(list_length -1, -1, -1):
        if hold_list[i] == 0:
            del hold_list[i]
    player1.diceList.extend(hold_list)
    print 'DL post:', player1.diceList

def Totals(totalOfDice, listOfDice, score_class):
    CountDice(listOfDice, score_class)
    score_class.totalsDict['Twos'] = score_class.totalsDict['Twos'] * 2
    score_class.totalsDict['Threes'] = score_class.totalsDict['Threes'] * 3
    score_class.totalsDict['Fours'] = score_class.totalsDict['Fours'] * 4
    score_class.totalsDict['Fives'] = score_class.totalsDict['Fives'] * 5
    score_class.totalsDict['Sixes'] = score_class.totalsDict['Sixes'] * 6

    score_class.scoresDict['Chance'] = totalOfDice
    score_class.scoresDict['Three of a kind'] = totalOfDice
    score_class.scoresDict['Four of a kind'] = totalOfDice
    score_class.scoresDict['Ones'] = score_class.totalsDict['Ones']
    score_class.scoresDict['Twos'] = score_class.totalsDict['Twos']
    score_class.scoresDict['Threes'] = score_class.totalsDict['Threes']
    score_class.scoresDict['Fours'] = score_class.totalsDict['Fours']
    score_class.scoresDict['Fives'] = score_class.totalsDict['Fives']
    score_class.scoresDict['Sixes'] = score_class.totalsDict['Sixes']

    return score_class

def choose(score_class):
    choice = raw_input('Type the name of the score you\'d like: ')
    if choice in score_class.usedScoresDict:
        return choice
    else:
        choice = -1
        return choice

def Scoring(score_class, totalOfDice, listOfDice):
    valid = 0
    listOfDice.sort()
    while valid == 0:
        print '\nHere is the final state of the dice: ', listOfDice, '\n'
        PrintScoreList()

        #//// print out used list ////
        PrintUsedList(score_class)

        choice = choose(score_class)
        while (choice == -1):
            print '\nInvalid choice '
            choice = choose(score_class)

        choice = CheckScoreUsed(choice, score_class)
        valid = CheckScoreValid(choice, score_class, listOfDice)

    print '\nscore class turn score: ', score_class.turnScore
    print '\nchoice: ', choice
    print '\nscore class scores dict ', score_class.scoresDict[choice]
    #if valid = 1 - do scoring stuff
    #else (valid = 2) make score 0, print saying such
    if valid == 1:
        score_class.turnScore = score_class.scoresDict[choice]
    else:
        score_class.turnScore = 0

    print 'You scored ', score_class.turnScore, ' points!\n'
    score_class.count = score_class.count +1 
    score_class.usedScoresDict[choice] = 'used'

    print "\nchoice: ",choice
    if (choice == 'Ones') or (choice == 'Twos') or (choice == 'Threes') or (choice == 'Fours') or (choice == 'Fives') or (choice == 'Sixes'):
        score_class.singles_counter = score_class.singles_counter + score_class.turnScore

    #print '\nthe singles total is: ', singles_total, '\n'
    return score_class

#def save_score(score_class,score_choice):
#    score_class.turnScore = scoresDict[score_choice]

def CheckScoreUsed(score_choice,scoreClass):
    print "score choice: ", score_choice
    flag = 0
    while flag == 0:
        if scoreClass.usedScoresDict[score_choice] == 'used':
            score_choice = raw_input('\n\nSelection used, please choose another.\n')
	    #TODO -- Error checking
            print score_choice
        else:
            flag = 1
    return score_choice

def TakeNone():
    choice_zero = raw_input("Would you like to take 0 points for this turn? No = Re-enter choice, Yes = Take 0 points for this choice ")
    if choice_zero == 'No':
        return 0
    else:
        return 2

def CheckScoreValid(score_choice, score_class, listOfDice):
    flag = 0
    list_copy = listOfDice
    list_copy = list(set(list_copy))

    print listOfDice
    print list_copy
    if (score_choice == 'Ones') or (score_choice == 'Twos') or (score_choice == 'Threes') or (score_choice == 'Fours') or (score_choice == 'Fives') or (score_choice == 'Sixes') or (score_choice == 'Chance'):
        return 1
    elif score_choice == 'Yahtzee':
        print "\nin yahtzee stmt"
        print 'list of dice[4]: ', listOfDice[4], 'and list of dice[0]: ', listOfDice[0]
        if listOfDice[4] == listOfDice[0]:
            return 1
        else:
            return (TakeNone())
    elif score_choice == 'Large straight':
        if listOfDice[4] - listOfDice[0] == 4:
            return 1
        else:
            return (TakeNone())
    elif score_choice == 'Small straight':
        for i in range(len(list_copy)):
            if list_copy[i] == (list_copy[i+1] - 1):
                return 1
            return (TakeNone())
    elif score_choice == 'Three of a kind':
        dict_copy = dict(Counter(listOfDice))
        print 'dict_copy: ', dict_copy
        for item in dict_copy:
            print 'this is it ', dict_copy[item], '\n'
            if dict_copy[item] >= 3:
                return 1
        return (TakeNone())
    elif score_choice == 'Four of a kind':
        dict_copy = dict(Counter(listOfDice))
        print 'dict_copy: ',dict_copy
        for item in dict_copy:
            print 'this is it ', dict_copy[item], '\n'
            if dict_copy[item] >= 4:
                print "\n I'm going to return one"
                return 1
        return (TakeNone())
    elif score_choice == 'Full House':
        if listOfDice[0] == listOfDice[1]:
            if (listOfDice[0] == listOfDice[1]) and (listOfDice[3] == listOfDice[4]):
                print 'first 3 are the same'
                return 1
            elif (listOfDice[2] == listOfDice[3]) and (listOfDice[3] == listOfDice[4]):
                print 'last 3 are the same'
                return 1
            return (TakeNone())
    else:
        print 'we didn\'t find your selection'

def Bonus(score_class):
    bonus = 0
    if score_class.singles_counter >= 63:
        bonus = 1
    return bonus

def PlayAgain (player1):
    again = int(raw_input("Would you like to play again? 0 = No, 1 = Yes "))
    if again < 0:
        again = 0
        print 'not an option'
        Playagain()
    elif again ==1:
        Turn(player1)
    elif again == 0:
        print 'Thanks for playing,',player1.name,'!'
    else:
        again = 0
        print 'not an option'
        PlayAgain()

Game()



from art import logo,vs
from GameData import data
from random import randint
from os import system, name
clear=lambda:system('cls' if name=='nt' else 'clear')

""" MARK DOWN 
        'name': 'Selena Gomez',
        'follower_count': 174,
        'description': 'Musician and actress',
        'country': 'United States'
""" 
NUM_ANSWER=0
COMPARISON=0
ALL_COMPARISON=data.copy()
LENGTH_ALL_DATA=len(ALL_COMPARISON)
questionMap={}
def selectTheGuess():
    global LENGTH_ALL_DATA,COMPARISON,ALL_COMPARISON
    index=randint(COMPARISON,LENGTH_ALL_DATA)
    needToGuess=ALL_COMPARISON[index]
    ALL_COMPARISON[index]=ALL_COMPARISON[COMPARISON]
    ALL_COMPARISON[COMPARISON]=needToGuess
    COMPARISON+=1
    return needToGuess

def answer():
    global questionMap
    firstACount=questionMap['a']['follower_count']
    secondACount=questionMap['b']['follower_count']
    if firstACount > secondACount:
        return questionMap['a']
    else:
        return questionMap['b']
def printAcountStatus(account):
    return (f"{account['name']}, a {account['description']} from {account['country']}")
def setUpGame():
    global questionMap
    print('guest how have more follower ?')
    questionMap['a']=selectTheGuess()
    questionMap['b']=selectTheGuess()
    print(f"{printAcountStatus(questionMap['a'])}\n{vs}\n{printAcountStatus(questionMap['b'])}")
def playerRightPrint(rightAnswer):
    global NUM_ANSWER
    NUM_ANSWER+=1
    print(logo)
    print(f"you right {rightAnswer['name']} have more follower\nyou have {NUM_ANSWER} point")
    if input('next question y or no ') =='y':
        playGame() 

def playerWrongPrint(rightAnswer):
    global NUM_ANSWER
    NUM_ANSWER=0
    print(logo)
    print(f"you wrong, {rightAnswer['name']} have more follower")
    if input('do you wont play again y or no') =='y':
        playGame() 
def playGame():
    global questionMap
    setUpGame()
    rightAnswer=answer()
    playerAnswer=questionMap[input('How has more followers type A or B ').lower()] 
    clear()
    if playerAnswer['name'] == rightAnswer['name']:
        playerRightPrint(rightAnswer)
    else:
        playerWrongPrint(rightAnswer)
playGame()



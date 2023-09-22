# print('hallo')
from random import randint
from hangman_words import word_list
from hangmanArt import logo, stages
latterNeedToGus=word_list[randint(0,len(word_list)-1)]
def fillBlank(latter:str) ->int:
    num=0
    for idx,car in enumerate(latterNeedToGus):
        if latter == car:
            blank[idx]=car
            num+=1
    return num

# generate blank
blank=list()
for num in latterNeedToGus: blank.append('_')
count=len(blank) -1
lives=0
display=f"welcome to hangman we have {count} words{logo}\nGuess the words :"
while count >= 0:
    print(display)
    if lives == 6 and count !=0:
        print(f"GAME OVER\nthe words is: {latterNeedToGus}")
        break
    elif lives < 6 and count==0:
        print(f"you right :{blank}\nGOOD JOB")
        break
    latterGuess=input("Guess a latter ").lower()
    if lives >= 0:display+=f"\n{stages[lives]}\n{blank}"
    answerStatus=fillBlank(latterGuess)
    if answerStatus:
        count+=answerStatus
        lives-=1
    else:
        lives+=1



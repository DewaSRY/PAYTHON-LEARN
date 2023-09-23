from question_model import Question

class QuestionBrain:
    def __init__(self, listQuestion:list[Question]):
        self.listQuestion:list[Question]=listQuestion
        self.userState=0
        self.currentQuiz:str=''
        self.currentAnswer:bool
        self.userAnswer:bool
        self.userCorrect=0
    
    def quizStart(self):
        if self.userState==0:
            self._greetingQuiz()
        elif self.userState < len(self.listQuestion):
            self.runQuiz()
        elif self.userState == len(self.listQuestion):
            self._resultQuiz()
        
    def runQuiz(self):
        
        self._getQuestion()\
            ._printQuiz()\
            ._printUserResult()\
            ._compareAnswer()\
            .quizStart()


    
    def _getQuestion(self):
        self.currentQuiz=self.listQuestion[self.userState].q
        self.currentAnswer=self.listQuestion[self.userState].a
        self.userState+=1
        return self
    
    def _printQuiz(self):
        print(f'Q({self.userState}): {self.currentQuiz}.\n(True/False)')
        self.userAnswer=input('type t for true and f for false ') =='f'
        return self
    
    def _rightAnswer(self):
        print(f'right answer for: {self.currentQuiz}\nis {self.userAnswer}')

    def _printUserResult(self):
        print("\033c", end='')
        self._rightAnswer()

        return self
    def _compareAnswer(self):
        if self.currentAnswer == self.userAnswer:
            self.userCorrect+=1
        return self
    
    def _resultQuiz(self):
        print(f"user result is {self.userCorrect}")
        if input('do you wont play again ? ') =='y':
            print("\033c", end='')
            self.userState=0
            self.runQuiz()
    def _greetingQuiz(self):

        print(f'WELCOME TO QUIZ\nwe have {len(self.listQuestion)} question ready to play')
        if input('Type y to start !') =='y':
            print("\033c", end='')
            self.runQuiz()

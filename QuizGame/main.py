from data import question_data
from question_model import Question
from quiz_brain import QuestionBrain

questionBank:list[Question]=[]
for quest in question_data:
    questionText=quest['text']
    questionAnswer=quest['answer']
    newQuestion=Question(question=questionText,answer=questionAnswer)
    questionBank.append(newQuestion)


play=QuestionBrain(questionBank)
play.quizStart()
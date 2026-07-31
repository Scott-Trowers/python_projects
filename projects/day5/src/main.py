from projects.day5.src.quiz_brain import QuizBrain
from projects.day5.src.data import question_data

quiz_master = QuizBrain(question_data, question_key="question", answer_key="correct_answer")
quiz_master.start_quiz()

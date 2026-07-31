class Question:
    def __init__(self, question_number, question_data):
        self.question_number = question_number
        self.question_entry = question_data[question_number]
        self.question_text = self.question_entry["text"]
        self.answer = self.question_entry["answer"].lower()

    def ask_question(self):
        # adjust question number from 0-indexed
        print(f"Q{self.question_number + 1}) {self.question_text}...")

        user_answer = ''
        while user_answer not in ['true', 'false']:
            # use strings rather than bool, otherwise an empty answer evaluates to True
            # and the answer is stored in the dictionary as a string
            user_answer = str(input("True or False? ")).lower()

        return user_answer

    def check_answer(self, user_answer):
        if user_answer == self.answer:
            return True
        else:
            return False

class Quiz_Brain:
    def __init__(self, question_data: list):
        self.question_number = 0
        self.score = 0
        self.score_pct = 0.00
        self.question_data = question_data
        self.num_questions = len(question_data)

    def initialise_question(self):
        question = Question(self.question_number, self.question_data)
        self.question_number += 1
        user_answer = question.ask_question()
        user_was_correct = question.check_answer(user_answer)
        return user_was_correct

    def evaluate_answer(self, user_was_correct):
        if user_was_correct:
            self.score += 1
            response = "Correct"
        else:
            response = "Incorrect"

        if self.question_number == self.num_questions:
            message_modifier = "final "
        else:
            message_modifier = ""

        self.score_pct = 100 * self.score / self.question_number
        print(f"{response}! Your {message_modifier}score is: {self.score}/{self.question_number} ({self.score_pct:.2f}%)\n")

    def start_quiz(self):
        while self.question_number < self.num_questions:
            user_was_correct = self.initialise_question()
            self.evaluate_answer(user_was_correct)

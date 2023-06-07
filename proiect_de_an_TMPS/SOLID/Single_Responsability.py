class Question:
    def __init__(self, question_text, correct_answer):
        self.question_text = question_text
        self.correct_answer = correct_answer

    def display_question(self):
        print(self.question_text)

    def check_answer(self, user_answer):
        return user_answer == self.correct_answer


class ScoreManager:
    def __init__(self):
        self.score = 0

    def update_score(self, points):
        self.score += points

    def display_score(self):
        print("Current score:", self.score)

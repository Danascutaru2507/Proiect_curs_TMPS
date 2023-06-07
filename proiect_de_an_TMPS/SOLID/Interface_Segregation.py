from SOLID.Single_Responsability import ScoreManager


def display_question(question):
    question.display_question()


def get_user_answer():
    user_answer = input("Raspunsul tau: ")
    return user_answer


class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score_manager = ScoreManager()

    def play_game(self):
        for question in self.questions:
            self.display_question(question)
            user_answer = get_user_answer()
            if question.check_answer(user_answer):
                self.score_manager.update_score(1)
                print("Raspuns corect!")
            else:
                print("Raspuns gresit!")

        self.score_manager.display_score()

    def display_question(self, question):
        pass

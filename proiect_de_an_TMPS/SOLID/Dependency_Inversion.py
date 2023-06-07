from abc import ABC, abstractmethod


class GameQuestion(ABC):
    def __init__(self, question_text, correct_answer):
        self.question_text = question_text
        self.correct_answer = correct_answer

    @abstractmethod
    def display_question(self):
        pass

    @abstractmethod
    def check_answer(self, user_answer):
        pass


class TrueFalseQuestion(GameQuestion):
    def display_question(self):
        print(self.question_text)
        print("1. Adevarat")
        print("2. Fals")

    def check_answer(self, user_answer):
        return str(user_answer) == str(self.correct_answer)


class MultipleChoiceQuestion(GameQuestion):
    def __init__(self, question_text, options, correct_answer):
        super().__init__(question_text, correct_answer)
        self.options = options

    def display_question(self):
        print(self.question_text)
        for i, option in enumerate(self.options):
            print(f"{i + 1}. {option}")

    def check_answer(self, user_answer):
        return str(user_answer) == str(self.correct_answer)


class ScoreManager:
    def __init__(self):
        self.score = 0

    def update_score(self, points):
        self.score += points

    def display_score(self):
        print("Scor:", self.score)


class QuizGame:
    def __init__(self, questions, score_manager):
        self.questions = questions
        self.score_manager = score_manager

    def play_game(self):
        for question in self.questions:
            question.display_question()
            user_answer = input("Raspunsul tau: ")
            if question.check_answer(user_answer):
                print("Raspuns corect!")
                self.score_manager.update_score(1)
            else:
                print("Raspuns gresit!")

        self.score_manager.display_score()


# Exemplu de utilizare:
true_false_question = TrueFalseQuestion("Is the sky blue?", "1")
multiple_choice_question = MultipleChoiceQuestion("What is the capital of France?",
                                                  ["1. Paris", "2. London", "3. Rome"], "1")

questions = [true_false_question, multiple_choice_question]

score_manager = ScoreManager()
game = QuizGame(questions, score_manager)
game.play_game()

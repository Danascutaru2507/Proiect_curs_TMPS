from abc import ABC, abstractmethod


class GameQuestion(ABC):
    @abstractmethod
    def display_question(self):
        pass

    @abstractmethod
    def check_answer(self, user_answer):
        pass


class TrueFalseQuestion(GameQuestion):
    def __init__(self, question_text, correct_answer):
        self.question_text = question_text
        self.correct_answer = correct_answer

    def display_question(self):
        print(self.question_text)
        print("1. Adevarat")
        print("2. Fals")

    def check_answer(self, user_answer):
        return str(user_answer) == str(self.correct_answer)


class MultipleChoiceQuestion1(GameQuestion):
    def __init__(self, question_text, options, correct_answer):
        self.question_text = question_text
        self.options = options
        self.correct_answer = correct_answer

    class MultipleChoiceQuestion2(GameQuestion, ABC):
        def display_question(self):
            pass

        def __init__(self, question_text, options, correct_answer):
            self.question_text = question_text
            self.options = options
            self.correct_answer = correct_answer

    def display_question(self):
        print(self.question_text)
        for i, option in enumerate(self.options):
            print(f"{i + 1}. {option}")

    def check_answer(self, user_answer):
        return str(user_answer) == str(self.correct_answer)

class Question:
    def __init__(self, question_text, correct_answer):
        self.question_text = question_text
        self.correct_answer = correct_answer

    def display_question(self):
        raise NotImplementedError

    def check_answer(self, user_answer):
        raise NotImplementedError


class TrueFalseQuestion(Question):
    def display_question(self):
        print(self.question_text)

    def check_answer(self, user_answer):
        return user_answer.lower() == self.correct_answer.lower()


class MultipleChoiceQuestion(Question):
    def __init__(self, question_text, choices, correct_answer):
        super().__init__(question_text, correct_answer)
        self.choices = choices

    def display_question(self):
        print(self.question_text)
        for choice in self.choices:
            print(choice)

    def check_answer(self, user_answer):
        return user_answer.lower() == self.correct_answer.lower()


class QuestionDecorator(Question):
    def __init__(self, decorated_question, question_text, correct_answer):
        super().__init__(question_text, correct_answer)
        self.decorated_question = decorated_question

    def display_question(self):
        self.decorated_question.display_question()

    def check_answer(self, user_answer):
        return self.decorated_question.check_answer(user_answer)


class CountingQuestionDecorator(QuestionDecorator):
    def __init__(self, decorated_question, question_number):
        super().__init__(decorated_question, None, None)
        self.question_number = question_number

    def display_question(self):
        print(f"Intrebarea {self.question_number}:")
        self.decorated_question.display_question()


class SymbolAdding(QuestionDecorator):
    def __init__(self, decorated_question, symbol):
        super().__init__(decorated_question, None, None)
        self.symbol = symbol

    def display_question(self):
        question_text = self.decorated_question.question_text
        decorated_question_text = f"{self.symbol} {question_text}"
        print(decorated_question_text)

    def display_choices(self):
        choices = self.decorated_question.choices
        decorated_choices = [f"{self.symbol} {choice}" for choice in choices]
        for choice in decorated_choices:
            print(choice)


class NumberedQuestionDecorator(QuestionDecorator):
    def __init__(self, decorated_question, question_text, correct_answer):
        super().__init__(decorated_question, question_text, correct_answer)

    def display_question(self):
        print(self.question_text)
        self.decorated_question.display_question()

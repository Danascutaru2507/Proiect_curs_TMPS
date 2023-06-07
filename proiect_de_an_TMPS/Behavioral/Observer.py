from Creational.Factory_Method import MultipleChoiceQuestion


class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self)


class Observer:
    def update(self, subject):
        pass


class ScoreManagerSubject(Subject):
    def __init__(self):
        super().__init__()
        self.score = 0

    def notify(self, correct):
        for observer in self.observers:
            observer.update(correct)

    def update_score(self, correct):
        if correct:
            self.score += 1

        self.notify(correct)

    def get_score(self):
        return self.score


class QuizGameObserver(Observer):
    def update(self, correct):
        if correct:
            print("Răspuns corect!")
        else:
            print("Răspuns greșit!")


class CustomQuestionFactoryObserver(Observer):
    def update(self, correct):
        if correct:
            print("Felicitări!")
        else:
            print("Întrebarea personalizată creată nu este corectă.")


class QuestionDecorator:
    def __init__(self, decorated_question):
        self.decorated_question = decorated_question

    def display_question(self):
        self.decorated_question.display_question()

    def check_answer(self, user_answer):
        return self.decorated_question.check_answer(user_answer)


class CountingQuestionDecorator(QuestionDecorator):
    def __init__(self, decorated_question, question_number):
        super().__init__(decorated_question)
        self.question_number = question_number

    def display_question(self):
        print(f"Intrebare {self.question_number}:")
        self.decorated_question.display_question()


class SymbolAdding(QuestionDecorator):
    def __init__(self, decorated_question, symbol):
        super().__init__(decorated_question)
        self.symbol = symbol

    def display_question(self):
        question_text = self.decorated_question.question_text
        decorated_question_text = f"{self.symbol} {question_text}"
        print(decorated_question_text)

        if isinstance(self.decorated_question, MultipleChoiceQuestion):
            self.display_choices()

    def display_choices(self):
        choices = self.decorated_question.choices
        decorated_choices = [f"{self.symbol} {choice}" for choice in choices]
        for choice in decorated_choices:
            print(choice)

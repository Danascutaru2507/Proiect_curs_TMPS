class Question:
    def __init__(self, text):
        self.text = text

    def display(self):
        print(self.text)


class QuestionFactory:
    def create_question(self):
        pass


class MultipleChoiceQuestion(Question):
    def __init__(self, text, options):
        super().__init__(text)
        self.options = options

    def display(self):
        super().display()
        print("Raspuns:", self.options)


class FillInTheBlankQuestion(Question):
    def __init__(self, text, answer):
        super().__init__(text)
        self.answer = answer

    def display(self):
        super().display()
        print("Raspunsul tau:", self.answer)


class CustomQuestionFactory(QuestionFactory):
    def create_question(self):
        text = input("Scrie aici intrebarea ta: ")
        question_type = input("Scrie tipul intrebarii tale: (cu optiuni mulptiple/ cu un singur raspuns): ")

        if question_type == "optiuni multiple":
            options = input("Scrie optiunile (separate prin virgula): ").split(",")
            return MultipleChoiceQuestion(text, options)
        elif question_type == "un raspuns":
            answer = input("Scrie raspunsul: ")
            return FillInTheBlankQuestion(text, answer)
        else:
            raise ValueError("Tipul intrebarii este incorect.")

class CustomQuestion(Question):
    def __init__(self, question_text, correct_answer, display_mode):
        super().__init__(question_text, correct_answer, display_mode)

    def display_question(self):
        print(f"Intrebare personalizata: {self.question_text}")

    def check_answer(self, user_answer):
        return user_answer.lower() == self.correct_answer.lower()



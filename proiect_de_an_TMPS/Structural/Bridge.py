# Ierarhia pentru tipurile de întrebări
class Question:
    def __init__(self, question_text, correct_answer, display_mode):
        self.question_text = question_text
        self.correct_answer = correct_answer
        self.display_mode = display_mode

    def display_question(self):
        self.display_mode.display_question(self.question_text)

    def check_answer(self, user_answer):
        return user_answer.lower() == self.correct_answer.lower()


# Subclasa pentru întrebările cu răspuns adevărat/fals
class TrueFalseQuestion(Question):
    def __init__(self, question_text, correct_answer, display_mode):
        super().__init__(question_text, correct_answer, display_mode)

    def display_question(self):
        self.display_mode.display_question(self.question_text)


# Subclasa pentru întrebările cu opțiuni multiple
class MultipleChoiceQuestion(Question):
    def __init__(self, question_text, choices, correct_answer, display_mode):
        super().__init__(question_text, correct_answer, display_mode)
        self.choices = choices

    def display_question(self):
        self.display_mode.display_question(self.question_text, self.choices)


# Ierarhia pentru modurile de afișare a întrebărilor
class DisplayMode:
    def display_question(self, question_text, choices=None):
        raise NotImplementedError("Metoda trebuie implementată în subclase.")


# Subclasa pentru modul de afișare text simplu
class TextDisplayMode(DisplayMode):
    def display_question(self, question_text, choices=None):
        print(question_text)
        if choices:
            for choice in choices:
                print(choice)


# Subclasa pentru modul de afișare grafică
class GraphicDisplayMode(DisplayMode):
    def display_question(self, question_text, choices=None):
        # Implementați afișarea grafică a întrebării
        pass

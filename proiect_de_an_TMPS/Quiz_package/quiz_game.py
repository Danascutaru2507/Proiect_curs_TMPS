from Behavioral.Observer import ScoreManagerSubject

class Question:
    def __init__(self, question_text, correct_answer, display_mode):
        self.question_text = question_text
        self.correct_answer = correct_answer
        self.display_mode = display_mode

    def display_question(self):
        self.display_mode.display(self.question_text)

    def check_answer(self, user_answer):
        return user_answer.lower() == self.correct_answer.lower()



class TrueFalseQuestion(Question):
    def __init__(self, question_text, correct_answer, display_mode):
        super().__init__(question_text, correct_answer, display_mode)

    def display(self):
        self.display_mode.display(self.question_text)




class MultipleChoiceQuestion(Question):
    def __init__(self, question_text, choices, correct_answer, display_mode):
        super().__init__(question_text, correct_answer, display_mode)
        self.choices = choices

    def display_question(self):
        print(f"Intrebare: {self.question_text}")
        self.display_choices()

    def display_choices(self):
        for choice in self.choices:
            print(choice)

class CustomMultipleChoiceQuestion(Question):
    def __init__(self, question_text, choices, correct_answer, display_mode):
        super().__init__(question_text, correct_answer, display_mode)
        self.choices = choices

    def display(self):
        print(f"Intrebare: {self.question_text}")
        for choice in self.choices:
            print(choice)

    def check_answer(self, user_answer):
        return user_answer == self.correct_answer


class ScoreManager:
    def __init__(self):
        self.score = 0

    def increment_score(self):
        self.score += 1

    def get_score(self):
        return self.score


class ScoreManagerSubject:
    def __init__(self):
        self.observers = []
        self.score = 0

    def attach(self, observer):
        self.observers.append(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self)

    def increment_score(self):
        self.score += 1
        self.notify_observers()

    def get_score(self):
        return self.score


class QuizGame:
    def __init__(self, questions, score_manager):
        self.questions = questions
        self.score_manager = score_manager
        self.current_question_index = 0

    def display_current_question(self):
        current_question = self.questions[self.current_question_index]
        current_question.display_question()

    def get_user_answer(self):
        return input("Raspunsul tau: ")

    def check_user_answer(self, user_answer):
        current_question = self.questions[self.current_question_index]
        return current_question.check_answer(user_answer)

    def play_game(self):
        for _ in range(len(self.questions)):
            self.display_current_question()
            user_answer = self.get_user_answer()
            if self.check_user_answer(user_answer):
                print("Raspuns corect!")
                self.score_manager.increment_score()
            else:
                print("Raspuns gresit!")
            self.current_question_index += 1

        final_score = self.score_manager.get_score()
        print(f"Scor final: {final_score}")

class FillInTheBlankQuestion:
    pass

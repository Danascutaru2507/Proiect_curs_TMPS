from Quiz_package.quiz_game import TrueFalseQuestion, MultipleChoiceQuestion, ScoreManager, QuizGame, Question, \
    FillInTheBlankQuestion, CustomMultipleChoiceQuestion
from Creational.Singleton import GameManager
from Creational.Factory_Method import CustomQuestionFactory
from Structural.Bridge import TextDisplayMode
from Behavioral.Observer import ScoreManagerSubject, QuizGameObserver, CustomQuestionFactoryObserver, \
    CountingQuestionDecorator, SymbolAdding
from Quiz_package.quiz_game import TrueFalseQuestion, MultipleChoiceQuestion, ScoreManagerSubject, QuizGame, Question, FillInTheBlankQuestion


class QuestionDecorator:
    def __init__(self, decorated_question):
        self.decorated_question = decorated_question

    def display_question(self):
        self.decorated_question.display()

    def check_answer(self, user_answer):
        return self.decorated_question.check_answer(user_answer)


class CountingQuestionDecorator(QuestionDecorator):
    def __init__(self, decorated_question, question_count):
        super().__init__(decorated_question)
        self.question_count = question_count

    @property
    def options(self):
        return self.decorated_question.options

    def display_question(self):
        super().display_question()
        print(f"Question {self.question_count}")

    def get_choices(self):
        return self.decorated_question.get_choices()

class CustomQuestionFactory:
    def create_question(self, question_text):
        return CustomQuestion(question_text)


class CustomQuestion(Question):
    def __init__(self, question_text):
        super().__init__(question_text, None, TextDisplayMode())

    def check_answer(self, user_answer):
        return True


class SymbolAdding(QuestionDecorator):
    def __init__(self, decorated_question, symbol):
        super().__init__(decorated_question)
        self.symbol = symbol

    def display(self):
        self.decorated_question.display()

        if isinstance(self.decorated_question, FillInTheBlankQuestion):
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


class FillInTheBlankQuestion(Question):
    def __init__(self, question_text, correct_answer, display_mode):
        super().__init__(question_text, correct_answer, display_mode)

    def display_question(self):
        print(f"Intrebare: {self.question_text}")

    def check_answer(self, user_answer):
        return user_answer.lower() == self.correct_answer.lower()


def display_menu():
    title = "Bun venit in Quiz_Game!"
    add_question_button = "1. Adauga o intrebare personalizata"
    start_game_button = "2. Incepe jocul"

    # Afisam meniul intr-o rama
    print("═" * 60)
    print("║" + " " * 58 + "║")
    print("║" + title.center(58) + "║")
    print("║" + " " * 58 + "║")
    print("║" + " " * 58 + "║")
    print("║" + add_question_button.center(58) + "║")
    print("║" + " " * 58 + "║")
    print("║" + start_game_button.center(58) + "║")
    print("║" + " " * 58 + "║")
    print("═" * 60)

class TextDisplayMode:
    def display(self, question_text):
        # Afișează întrebarea text într-un mod specific acestui mod de afișare
        print(question_text)

def main():
    custom_question_factory = CustomQuestionFactory()

    # Crearea unei instanțe a GameManager utilizând Singleton
    game_manager = GameManager()

    # Crearea gestionarului de scor
    score_manager_subject = ScoreManagerSubject()

    # Crearea obiectului ScoreManager
    score_manager = ScoreManagerSubject()

    # Crearea întrebărilor și jocului de quiz
    questions = []

    true_false_question1 = TrueFalseQuestion(
        "Este adevărat că alfabetul limbii engleze are 26 litere?", "da", TextDisplayMode()
    )
    questions.append(CountingQuestionDecorator(SymbolAdding(true_false_question1, "➤"), 1))

    true_false_question2 = TrueFalseQuestion(
        "O persoană adultă are 32 de dinți?", "da", TextDisplayMode()
    )
    questions.append(CountingQuestionDecorator(SymbolAdding(true_false_question2, "➤"), 2))

    multiple_choice_question1 = MultipleChoiceQuestion(
        "Cine a scris piesa de teatru: HAMLET?",
        ["1. Charles Dickens", "2. Johann Wolfgang von Goethe", "3. William Shakespeare", "4. Moliere"],
        "3", TextDisplayMode()
    )
    questions.append(multiple_choice_question1)  # Adăugați direct întrebarea fără decoratori

    multiple_choice_question2 = MultipleChoiceQuestion(
        "Ce planetă se află între Marte și Jupiter?",
        ["1. Venus", "2. Neptun", "3. Jupiter", "4. Saturn"],
        "3", TextDisplayMode()
    )
    questions.append(multiple_choice_question2)  # Adăugați direct întrebarea fără decoratori

    while True:
        display_menu()
        choice = input("Alege o opțiune: ")

        if choice == "1":
            # Logica pentru adăugarea întrebării personalizate
            print("Adaugă o întrebare personalizată.")
            question_text = input("Introduceti intrebarea: ")
            question_type = input("Este o întrebare cu variante multiple de răspuns? (da/nu): ")
            if question_type.lower() == "da":
                choices = []
                while True:
                    choice = input("Introduceti varianta de raspuns (sau 'stop' pentru a opri): ")
                    if choice == "stop":
                        break
                    choices.append(choice)
                correct_answer = input("Introduceti raspunsul corect: ")
                custom_question = CustomMultipleChoiceQuestion(question_text, choices, correct_answer, TextDisplayMode())
            else:
                correct_answer = input("Introduceti raspunsul corect: ")
                custom_question = CustomQuestion(question_text)


            questions.append(CountingQuestionDecorator(SymbolAdding(custom_question, "⌖"), len(questions) + 1))

        elif choice == "2":
            # Logica pentru începerea jocului
            print("Incepe jocul.")
            game = QuizGame(questions, score_manager)
            game.play_game()
            break

        else:
            print("Optiune invalida. Te rog sa selectezi o optiune valida.")


if __name__ == "__main__":
    main()

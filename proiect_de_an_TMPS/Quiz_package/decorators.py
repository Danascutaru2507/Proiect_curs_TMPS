# decorators.py

class DecoratedQuestion:
    def __init__(self, decorated_question):
        self.decorated_question = decorated_question

    def display_question(self):
        self.decorated_question.display_question()

    def get_question_text(self):
        return self.decorated_question.get_question_text()

def register_custom_question(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("Notificare: Intrebarea personalizată a fost înregistrată cu succes.")
        return result
    return wrapper

def display_score(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        score = result["score"]
        print(f"Scor actualizat: {score}")
        return result
    return wrapper

def display_notification(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        notification = result["notification"]
        print(notification)
        return result
    return wrapper

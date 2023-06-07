from Behavioral.Observer import ScoreManagerSubject

class ScoreManager(ScoreManagerSubject):
    def __init__(self):
        super().__init__()
        self.score = 0

    def increase_score(self):
        self.score += 1
        self.notify_observers(self.score)

    def increment_correct(self):
        self.correct_count += 1

    def increment_wrong(self):
        self.wrong_count += 1

    def get_score(self):
        total_questions = self.correct_count + self.wrong_count
        if total_questions == 0:
            return 0
        score_percent = (self.correct_count / total_questions) * 100
        return score_percent

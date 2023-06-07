class ScoreManagerSubject:
    def __init__(self):
        self.score = 0

    def update_score(self, correct):
        if correct:
            self.score += 1

    def get_score(self):
        return self.score

    def increment_score(self):
        self.score += 1

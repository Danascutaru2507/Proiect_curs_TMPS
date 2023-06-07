class GameManager:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.score = 0
        self.level = 1
        self.time_remaining = 60

    def update_score(self, points):
        self.score += points

    def increase_level(self):
        self.level += 1

    def update_time(self, delta):
        self.time_remaining -= delta

    def get_score(self):
        return self.score

    def get_level(self):
        return self.level

    def get_time_remaining(self):
        return self.time_remaining

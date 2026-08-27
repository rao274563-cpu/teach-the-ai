class LearnerModel:

    def __init__(self):
        self.mastery = 0
        self.attempts = 0

    def update_mastery(self, score):
        self.attempts += 1
        self.mastery = score

    def get_level(self):
        if self.mastery < 50:
            return "Needs Guidance"
        elif self.mastery < 75:
            return "Developing"
        elif self.mastery < 90:
            return "Proficient"
        else:
            return "Mastered"
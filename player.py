from random import uniform


class Player:
    def __init__(self, probability):
        self.probability = probability
        self.count_blue = 0
        self.count_red = 0
        self.score = 0
        self.average = 0

    def get_choice(self):
        return int(uniform(0, 1) > self.probability)

    def reinforcement(self, color, value):
        if color:
            self.count_blue += value
        else:
            self.count_red += value
        self.probability = self.count_red / (self.count_red + self.count_blue)

    def punishment(self, color, value):
        if color:
            self.count_blue -= value
        else:
            self.count_red -= value
        self.count_blue = max(self.count_blue, 0)
        self.count_red = max(self.count_red, 0)
        self.probability = self.count_red / (self.count_red + self.count_blue)
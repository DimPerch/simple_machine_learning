from math import sqrt


class Statiscic:
    def __init__(self, player_A, player_B):
        self.player_A = player_A
        self.player_B = player_B
        self.choice_history = []
        self.expectation = 0
        self.deviation = 0
        self.square_expectation = 0
        self.dispersion = 0
        self.theoretical_deviation = 0

    def add_history(self, choice_A, choice_B):
        self.choice_history.append((choice_A, choice_B))

    def change_score(self, element):
        self.player_A.score += element
        self.player_B.score -= element

    def average_score(self):
        self.player_A.average = self.player_A.score / 100
        self.player_B.average = self.player_B.score / 100

    def set_expectation(self, matrix):
        self.expectation = (matrix[0][0] * self.player_A.probability * self.player_B.probability +
                            matrix[0][1] * self.player_A.probability * (1 - self.player_B.probability) +
                            matrix[1][0] * (1 - self.player_A.probability) * self.player_B.probability +
                            matrix[1][1] * (1 - self.player_A.probability) * (1 - self.player_B.probability))

    def set_standard_deviation(self, matrix):
        self.deviation = sqrt((pow(matrix[0][0] - self.player_A.average, 2) +
                               pow(matrix[0][1] - self.player_A.average, 2) +
                               pow(matrix[1][0] - self.player_A.average, 2) +
                               pow(matrix[1][1] - self.player_A.average, 2)) / 3)

    def set_square_expectation(self, matrix):
        self.square_expectation = (pow(matrix[0][0], 2) * self.player_A.probability * self.player_B.probability +
                                   pow(matrix[0][1], 2) * self.player_A.probability * (1 - self.player_B.probability) +
                                   pow(matrix[1][0], 2) * (1 - self.player_A.probability) * self.player_B.probability +
                                   pow(matrix[1][1], 2) * (1 - self.player_A.probability) * (1 - self.player_B.probability))

    def set_dispersion(self):
        self.dispersion = self.square_expectation - pow(self.expectation, 2)

    def set_theoretical_deviation(self):
        self.theoretical_deviation = sqrt(self.dispersion)

    def __str__(self):
        string = f'Вероятности выбора игроков: A = {self.player_A.probability}, B = {self.player_B.probability}\n'
        string += f'Счёт игроков: А = {self.player_A.score}, B = {self.player_B.score}\n'
        string += f'Среднее игроков: А =  {self.player_A.average}, B = {self.player_B.average}\n'
        string += f'Математическое ожидание: {self.expectation}\n'
        string += f'Среднее квадратичное отклонение: {self.deviation}\n'
        string += f'Дисперсия: {self.dispersion}\n'
        string += f'Теоретическое среднее квадратичное отклонение: {self.theoretical_deviation}\n'
        return string
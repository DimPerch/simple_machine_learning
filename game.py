from player import Player
from statistic import Statiscic


class GameSimulator:
    def __init__(self, probability_A, probability_B):
        self.matrix = ((2, -3),
                       (-1,  2))
        self.player_A = Player(probability_A)
        self.player_B = Player(probability_B)
        self.statistic = Statiscic(self.player_A, self.player_B)

    def get_statistic(self):
        for _ in range(100):
            choice_A = self.player_A.get_choice()
            choice_B = self.player_B.get_choice()
            self.statistic.add_history(choice_A, choice_B)
            element = self.matrix[choice_A][choice_B]
            self.statistic.change_score(element)

        self.statistic.average_score()
        self.statistic.set_expectation(self.matrix)
        self.statistic.set_standard_deviation(self.matrix)
        self.statistic.set_square_expectation(self.matrix)
        self.statistic.set_dispersion()
        self.statistic.set_theoretical_deviation()

    def learn(self, model):
        if model == '1':
            self.player_A.count_blue = self.player_A.count_red = 10
            for _ in range(100):
                choice_A = self.player_A.get_choice()
                choice_B = self.player_B.get_choice()
                element = self.matrix[choice_A][choice_B]
                if element > 0:
                    self.player_A.reinforcement(choice_A, element)

        elif model == '2':
            self.player_A.count_blue = self.player_A.count_red = 100
            for _ in range(100):
                choice_A = self.player_A.get_choice()
                choice_B = self.player_B.get_choice()
                element = self.matrix[choice_A][choice_B]
                if element < 0:
                    self.player_A.punishment(choice_A, abs(element))

        elif model == '3':
            self.player_A.count_blue = self.player_A.count_red = 10
            self.player_B.count_blue = self.player_B.count_red = 10
            for _ in range(100):
                choice_A = self.player_A.get_choice()
                choice_B = self.player_B.get_choice()
                element = self.matrix[choice_A][choice_B]
                if element > 0:
                    self.player_A.reinforcement(choice_A, element)
                else:
                    self.player_B.reinforcement(choice_B, abs(element))
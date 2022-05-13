from game import GameSimulator


if __name__ == '__main__':
    print('Сценарий: A = 0.5, B = 0.5')
    game = GameSimulator(.5, .5)
    game.get_statistic()
    print(game.statistic)

    print('Сценарий: A = 0.5, B = 0.25')
    game = GameSimulator(.5, .25)
    game.get_statistic()
    print(game.statistic)

    print('Сценарий: A = reinforcement, B = 0.25')
    game = GameSimulator(.5, .25)
    game.learn('1')
    game.get_statistic()
    print(game.statistic)

    print('Сценарий: A = punishment, B = 0.25')
    game = GameSimulator(.5, .25)
    game.learn('2')
    game.get_statistic()
    print(game.statistic)

    print('Сценарий: A = reinforcement, B = reinforcement')
    game = GameSimulator(.5, .25)
    game.learn('3')
    game.get_statistic()
    print(game.statistic)
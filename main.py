# Нормальная ELO система
from rating_system_warchest_base import RatingSystemWarchest

# Система рейтинга полностью как на Warchest
#from rating_system_warchest_full import RatingSystemWarchest


from matplotlib import animation, pyplot
from player import Player
import random

# Количество игроков
PLAYER_COUNT = 100

# Количество игр за один слайд
GAMES_COUNT_PER_SLIDE = 1000

ladder = RatingSystemWarchest()
players = [
    Player(4000 / PLAYER_COUNT * i, ladder.default_rating())
    for i in range(PLAYER_COUNT)
]


def play_game():
    p1, p2 = None, None
    while p1 == p2:
        p1, p2 = random.choices(players, k=2)

    ladder.play_game(p1, p2)


def animate_func(num):
    # Рейтинг игроков
    pyplot.clf()
    values = [p.rating for p in players]
    pyplot.plot(values)

    # Реальная сила игроков
    values = [p.power for p in players]
    pyplot.plot(values)

    # Линия сверху
    values = [5500] * PLAYER_COUNT
    pyplot.plot(values)

    # Линия снизу
    values = [-500] * PLAYER_COUNT
    pyplot.plot(values)

    for i in range(GAMES_COUNT_PER_SLIDE):
        play_game()


fig = pyplot.figure()
line_ani = animation.FuncAnimation(fig, animate_func, interval=10, frames=100)
pyplot.show()


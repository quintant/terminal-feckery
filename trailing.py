from time import sleep
from string import printable
from random import choice, randint, uniform
from colors import COLORS


class TrailParticle:
    def __init__(self, x: int, y: int, term_size: tuple) -> None:
        self.x = x
        self.y = y
        self.term_size = term_size
        self.direction = (1, 0)
        self.char = choice(printable)
        self.dead = False
        self.trail = []
        self.t_lim = randint(3, 15)
        self.gen = True
        self.color = choice(["r", "g", "b", "y", "m", "c"])

        self._draw()

    def play(self):
        self._clear()
        self._move()
        self._draw()

    def _move(self):
        kill = []
        if len(self.trail) < self.t_lim and self.gen:
            self.trail.append((self.x, self.y))
        else:
            self.gen = False
            for i in range(len(self.trail)):
                self.trail[i] = (
                    self.trail[i][0] + self.direction[0],
                    self.trail[i][1] + self.direction[1],
                )
                if not (0 <= self.trail[i][0] < self.term_size[1]):
                    kill.append(self.trail[i])
                if not (0 <= self.trail[i][1] < self.term_size[0]):
                    kill.append(self.trail[i])
        for i in kill:
            try:
                self.trail.remove(i)
            except Exception:
                pass
        if len(self.trail) < 1:
            self.dead = True
        self.x += self.direction[0]
        self.y += self.direction[1]

    def _draw(self):
        if not self.dead:
            print(COLORS[self.color], end="", flush=False)
            for x, y in self.trail:
                if x < self.term_size[1] and y <= self.term_size[0]:
                    move_to = f"\u001b[{int(x)};{int(y)}H"
                    print(move_to, end="", flush=False)
                    print(choice(printable), end="", flush=False)
            print(COLORS["reset"], end="", flush=False)

    def _clear(self):
        if not self.dead:
            for x, y in self.trail:
                if x < self.term_size[1] and y < self.term_size[0]:
                    move_to = f"\u001b[{int(x)};{int(y)}H"
                    print(move_to, end="", flush=False)
                    print(" ", end="", flush=False)

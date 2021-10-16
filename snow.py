from time import sleep
from string import printable
from random import choice, randint, uniform


class SnowParticle:
    def __init__(self, x: int, y: int, term_size: tuple) -> None:
        self.x = x
        self.y = y
        self.term_size = term_size
        self.direction = (1, 0)
        self.mod = uniform(0.4, 1.5)
        self.char = choice(printable)
        self.dead = False
        self.wind = randint(-1, 1)
        self.TIF = uniform(0, 0.2)

        self._draw()

    def play(self):
        self._clear()
        self._move()
        self._draw()

    def _move(self):
        self.x += self.direction[0] * self.mod  # + self.TIF
        self.y += self.direction[1] * self.mod + self.TIF * self.wind
        if not (0 <= self.x < self.term_size[1]):
            self.dead = True
        if not (0 <= self.y < self.term_size[0]):
            self.dead = True

    def _draw(self):
        if not self.dead:
            move_to = f"\u001b[{int(self.x)};{int(self.y)}H"
            print(move_to, end="", flush=False)
            print(self.char, end="", flush=False)

    def _clear(self):
        if not self.dead:
            base = "\u001b[{r};{c}H"
            move_to = base.format(r=int(self.x), c=int(self.y))
            print(move_to, end="", flush=False)
            print(" ", end="", flush=False)

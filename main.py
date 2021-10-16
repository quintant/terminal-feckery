#!/bin/python
from random import expovariate, randint
from typing import List, Set
import sys
import shutil
from time import sleep

PARTICLE_MULTIPLIER = 1
if len(sys.argv) == 2:
    TXY = sys.argv[1]
    if TXY == "matrix":
        from trailing import TrailParticle as Particle

        SLEEP = 0.05
    elif TXY == "rev":
        from rev_trailing import RevMatrixParticle as Particle

        SLEEP = 0.05
    elif TXY == "jump":
        from jump import JumpParticle as Particle

        PARTICLE_MULTIPLIER = 2
        SLEEP = 0.0
    else:
        from snow import SnowParticle as Particle

        SLEEP = 0.02
else:
    from snow import SnowParticle as Particle

    SLEEP = 0.02


TERM = shutil.get_terminal_size((80, 20))
PARTICLES: Set[Particle] = set()
DEAD: List[Particle] = []

H, W = TERM

# Clear the screen
print("\u001b[2J", end="", flush=True)

while True:
    DEAD = []
    x = expovariate(1)
    if x > 0.0001:
        for _ in range(PARTICLE_MULTIPLIER):
            PARTICLES.add(Particle(0, randint(0, H), TERM))

    for particle in PARTICLES:
        particle.play()
        if particle.dead:
            DEAD.append(particle)

    for particle in DEAD:
        PARTICLES.remove(particle)

    # Move cursor away
    print("\u001b[0;0H", end="", flush=True)
    sleep(SLEEP)

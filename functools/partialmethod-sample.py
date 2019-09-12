from functools import partialmethod

class Cell:
    def __init__(self):
        self._alive = False
    @property
    def alive(self):
        return self._alive
    def set_state(self, state):
        self._alive = bool(state)

    set_alive = partialmethod(set_state, True)
    set_dead = partialmethod(set_state, False)

c = Cell()
print(c.alive)
c.set_alive()
print(c.alive)
c.set_dead()
print(c.alive)

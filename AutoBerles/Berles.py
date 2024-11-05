
class Berles:
    def __init__(self, datum, auto):
        self._datum = datum
        self._auto = auto

    @property
    def datum(self):
        return self._datum

    @property
    def auto(self):
        return self._auto

    def __str__(self):
        return f"{self._datum}, {self._auto}"

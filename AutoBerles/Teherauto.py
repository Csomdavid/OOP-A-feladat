from Auto import Auto

class Teherauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij, marka, rakter, platos):
        super().__init__(rendszam, tipus, berleti_dij, marka)

        self._rakter = rakter
        self._platos = platos

    @property
    def rakter(self):
        return self._rakter

    @rakter.setter
    def rakter(self, rakter):
        self._rakter = rakter

    @property
    def platos(self):
        return self._platos

    @platos.setter
    def platos(self, platos):
        self._platos = platos

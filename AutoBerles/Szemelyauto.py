from Auto import Auto

class Szemelyauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij, marka, csomagtarto_terfogat, csaladi):
        super().__init__(rendszam, tipus, berleti_dij, marka)

        self._csomagtarto = csomagtarto_terfogat
        self._csaladi = csaladi

    @property
    def csomagtarto(self):
        return self._csomagtarto

    @csomagtarto.setter
    def csomagtarto(self, csomagtarto):
        self._csomagtarto = csomagtarto

    @property
    def csaladi(self):
        return self._csaladi

    @csaladi.setter
    def csaladi(self, csaladi):
        self._csaladi = csaladi
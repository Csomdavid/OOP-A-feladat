from abc import ABC

class Auto(ABC):
    def __init__(self, rendszam, tipus, berleti_dij, marka):
        self._rendszam = rendszam
        self._tipus = tipus
        self._berleti_dij = berleti_dij
        self._marka = marka

    @property
    def rendszam(self):
        return self._rendszam

    @rendszam.setter
    def rendszam(self, rendszam):
        self._rendszam = rendszam

    @property
    def tipus(self):
        return self._tipus

    @tipus.setter
    def tipus(self, tipus):
        self._tipus = tipus

    @property
    def berleti_dij(self):
        return self._berleti_dij

    @berleti_dij.setter
    def berleti_dij(self, berleti_dij):
        self._berleti_dij = berleti_dij

    @property
    def marka(self):
        return self._marka

    @marka.setter
    def marka(self, marka):
        self._marka = marka

    def __str__(self):
        return f"{self._rendszam}, {self._tipus}, {self._berleti_dij}, {self._marka}"

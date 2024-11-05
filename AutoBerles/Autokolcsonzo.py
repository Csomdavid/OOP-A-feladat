from datetime import date
from Berles import Berles
from Auto import Auto

class Autokolcsonzo:
    def __init__(self, kolcsonzo_nev, telefonszam):
        self._kolcsonzo_nev = kolcsonzo_nev
        self._telefonszam = telefonszam
        self._autok = []
        self._berlesek = []


    @property
    def kolcsonzo_nev(self):
        return self._kolcsonzo_nev

    @kolcsonzo_nev.setter
    def kolcsonzo_nev(self, value):
        self._kolcsonzo_nev = value

    @property
    def telefonszam(self):
        return self._telefonszam

    @telefonszam.setter
    def telefonszam(self, value):
        self._telefonszam = value


    def autok_listazasa(self):
        for i in range (len(self._autok)):
            print(self._autok[i])


    def auto_berlese(self, datum, rendszam):
        auto = self.auto_keresese(rendszam, self._autok)
        if auto and datum >= date.today():
            berles = self.berles_keresese(datum, auto)
            if not berles:
                self._berlesek.append(Berles(datum, auto))
                print(f"Sikeres az autóbérlés!")
                return
        print(f"Sikertelen az autóbérlés!")


    def auto_hozzaadasa(self, hozzaadando_auto):
        auto = self.auto_keresese(hozzaadando_auto.rendszam, self._autok)
        if not auto:
            self._autok.append(hozzaadando_auto)
        else:
            print("Nem egyedi az autó rendszáma!")


    def auto_keresese(self, rendszam, auto_lista):
        keresett_auto = None
        for auto in auto_lista:
            if auto.rendszam == rendszam:
                keresett_auto = auto
                break
        return keresett_auto


    def datum_megvan(self, datum):
        tartalmaz = False
        for berles in self._berlesek:
            if berles.datum.equals(datum):
                tartalmaz = True
                break
        return tartalmaz


    def berles_lemondasa(self, datum, rendszam):
        auto = self.auto_keresese(rendszam, self._autok)
        if auto:
            berles = self.berles_keresese(datum, auto)
            if berles:
                print(f"Sikeres a bérlés lemondása!")
                self._berlesek.remove(self.berles_keresese(datum, auto))
                return
        print(f"Sikertelen a bérlés lemondása!")


    def berlesek_listazasa(self):
        for berles in self._berlesek:
            print(berles)


    def berles_keresese(self, datum, auto):
        keresett_berles = None
        for berles in self._berlesek:
            if berles.datum == datum and berles.auto == auto:
                keresett_berles = berles
                break
        return keresett_berles
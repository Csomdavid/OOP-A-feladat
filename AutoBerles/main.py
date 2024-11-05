from datetime import datetime
from Szemelyauto import Szemelyauto
from Teherauto import Teherauto
from Autokolcsonzo import Autokolcsonzo


szemelyauto1 = Szemelyauto('ABEC-223', 'SuperB', 30000, 'Skoda', 600, True)
szemelyauto2 = Szemelyauto('AGFL-452', 'LS', 60000,'Lexus', 700, True)
teherauto = Teherauto('BACD-157', 'Cybertruck', 80000, 'Tesla', 3400, True)


autokolcsonzo = Autokolcsonzo("Kölcsönző", '06307779999')
autokolcsonzo.auto_hozzaadasa(szemelyauto1)
autokolcsonzo.auto_hozzaadasa(szemelyauto2)
autokolcsonzo.auto_hozzaadasa(teherauto)

autokolcsonzo.auto_berlese(datetime.strptime("2024-11-04", "%Y-%m-%d").date(), 'AGFL-452')
autokolcsonzo.auto_berlese(datetime.strptime("2024-11-09", "%Y-%m-%d").date(), 'ABEC-223')
autokolcsonzo.auto_berlese(datetime.strptime("2024-11-12", "%Y-%m-%d").date(), 'BACD-157')
autokolcsonzo.auto_berlese(datetime.strptime("2024-11-23", "%Y-%m-%d").date(), 'ABEC-223')


def felhazsnalo_kezelese():
    print(f"\nÜdvözöljük nálunk! \nTel.: {autokolcsonzo.telefonszam} \n")
    print("Autóink:")
    autokolcsonzo.autok_listazasa()
    while True:
        print("\nVálassza ki a kívánt számot!")

        lehetoseg = input("1-es az autó bérlése, 2-es az bérlés lemondása, 3-as a bérelt autók listázása, bármi más beírása esetén a program leáll!\n")

        match lehetoseg:
            case "1":
                rendszam = input("Adja meg a listából kiválasztott autó rendszámát:")
                datum = input("Mikorra szeretne autót bérelni? YYYY-MM-DD ")
                if datum_ellenorzese(datum):
                    autokolcsonzo.auto_berlese(datetime.strptime(datum, "%Y-%m-%d").date(), rendszam)
                pass

            case "2":
                rendszam = input("Adja meg a listából kiválasztott autó rendszámát:")
                datum = input("Melyik napon lévő foglalást szeretné lemondani? YYYY-MM-DD ")
                if datum_ellenorzese(datum):
                    autokolcsonzo.berles_lemondasa(datetime.strptime(datum, "%Y-%m-%d").date(), rendszam)
                pass

            case "3":
                print("Bérelt autók:")
                autokolcsonzo.berlesek_listazasa()
                pass

            case _:
                print("Kilépés")
                return

def datum_ellenorzese(ellenorizendo_datum):
    try:
        datum = datetime.strptime(ellenorizendo_datum, "%Y-%m-%d").date()
        return True
    except ValueError:
        print("A formátum hibás!")
        return False


felhazsnalo_kezelese()
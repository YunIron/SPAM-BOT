from color import *
import pyautogui
import time

class spambot:
    def __init__(self):
        try:
            print(f"{yellow}\t\t\t\t\tHosgeldiniz! Bu bir spam botudur.")
            print(f"{red}\t\t\t\t\t\t\tir0n")
            print(normal)
            self.text = str(input("Istediginiz yaziyi yazin sonra nereye yazmak istiyorsaniz oraya tiklayiniz:    "))
            self.count = int(input("Miktar: "))
            self.hiz = float(input("Ne kadar surede atsin?: "))
            self.secim = str(input("Baslatilsin mi?(E/H):    ")).lower()
            self.menu(self.text, self.count, self.secim)
        except Exception:
            print('Yanlis deger!')
            secim = str(input(f"{red}[ - ]Yeniden baslatilsin mi ? ya da kapatilsin mi? {yellow}(Y = Yeniden Baslat, K = Kapat):\t\t")).lower()
            if secim == "y":
                spambot()
            elif secim == "k":
                exit()
            else:
                print("Yanlis Deger!")
                exit()

    def menu(self, text, count, secim):
        try:
            if self.secim == "e":
                sure = 5
                for x in range(5):
                    print(f"{cyan}",sure)
                    time.sleep(1)
                    sure -=1
                    if sure == 0:
                        print(f"{green}Baslatildi!")
                        self.spam(self.text, self.count, self.hiz)

            elif secim == "h" or secim == "H":
                print('Cikis yapiliyor')
                exit()

        except Exception:
            print("Yanlis Deger!")
            (menu)

    def spam(self, text, count, hiz):
        for x in range(self.count):
            pyautogui.typewrite(self.text)
            pyautogui.press('enter')
            time.sleep(self.hiz)

spambot()

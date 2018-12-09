import random
import time

class Kumanda():
    def __init__(self, tv_durum="Kapalı", tv_ses=0, kanal_listesi=["Trt"],kanal="Trt"):
        self.tv_durum=tv_durum
        self.tv_ses=tv_ses
        self.kanal_listesi=kanal_listesi
        self.kanal=kanal
    def tv_ac(self):
        if (self.tv_durum =="Açık"):
            print("TV zaten açık...")
            time.sleep(1)

        else:
            print("TV açılıyor...")

            self.tv_durum="Açık"
            time.sleep(1)
            print("TV Açıldı")

    def tv_kapat(self):
        if (self.tv_durum=="Kapalı"):
            print("TV zaten kapalı...")
            time.sleep(1)

        else:
            print("TV kapanıyor...")
            self.tv_durum="Kapalı"
            time.sleep(1)
            print("TV kapandı...")

    def kanal_ekle(self,yeni_kanal):
        self.yeni_kanal=yeni_kanal
        self.kanal_listesi.append(yeni_kanal)


    def ses_ayarlari(self):

        while True:
            cevap = input("Sesi Azalt:'-'\nSesi Artır:'+'\nÇıkış: 'x'\n")

            if (cevap == "-" and self.tv_ses == 0):
                print("Ses Düzeyi: {} Minimum Ses".format(self.tv_ses))

            elif (cevap == "-" and self.tv_ses != 0):
                self.tv_ses -= 1
                print("Ses Düzeyi: {}".format(self.tv_ses))

            elif (cevap=="+" and self.tv_ses < 32):
                self.tv_ses+=1
                print("Ses Düzeyi:{}".format(self.tv_ses))

            elif (cevap=="+" and self.tv_ses == 32):
                print("Ses Düzeyi:{} Maksimum Ses".format(self.tv_ses))
            
            elif (cevap=="x"):
                print("Ses ayarlarından çıkıldı...")
                time.sleep(2)
                break
            else:
                print("Geçersiz seçim...")

    def rastgele_kanal(self):
        print("Rastgele kanala geçiliyor...")
        rastgele = random.randint(0,len(self.kanal_listesi)-1)
        self.kanal = self.kanal_listesi[rastgele]
        time.sleep(2)
        print("Kanal:",self.kanal)

    def mute(self):
        self.tv_ses = 0
        print("Ses Kapalı")

    def kanala_git(self):
        print("1- {} arası bir kanal seçin...".format(len(kumanda)))
        istek = int(input("Kanal:"))

        if istek <= len(kumanda):
            kumanda.kanal = kumanda.kanal_listesi[istek - 1]
            print("Kanal:", self.kanal)
        else:
            print("Böyle bir kanal bulunmamaktadır!")

    def __len__(self):
        return len(self.kanal_listesi)

    def __str__(self):
        return "TV Durumu:{}\nSes Düzeyi:{}\nKanal Listesi:{}\nŞu Anki Kanal: {}".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)

kumanda = Kumanda()

print("""
    *****************************************
            TELEVİZYON UYGULAMASI
                GİRİŞ EKRANI
    *****************************************
    İŞLEMLER;
    
    1. TV AÇ
    2. TV KAPAT
    3. SES AYARLARI
    4. KANAL EKLEME
    5. KANAL SAYISINI ÖĞRENME
    6. RASTGELE KANALA GEÇME
    7. TELEVİZYON BİLGİLERİ
    8. SESİ KAPAT
    9. KANALA GİT
    
    ****************************************
    ÇIKMAK İÇİN "q" GİRİNİZ...
    ****************************************
    BY BAHADIR YILMAZ 06.12.2018
    ****************************************
""")

while True:

        islem = input("İşlem Seçiniz:")

        if islem == "q":
            print("Program Sonlandırılıyor...")
            break
        else:

            if islem == "1":
                kumanda.tv_ac()

            elif islem == "2":
                kumanda.tv_kapat()

            elif islem == "3":
                if kumanda.tv_durum=="Kapalı":
                    print("TV şuan kapalı...")

                else:
                    kumanda.ses_ayarlari()

            elif islem == "4":
                if (kumanda.tv_durum) == "Kapalı":
                    print("TV şuan kapalı...")
                else:
                    kanal_isimleri = input("Eklemek istediğiniz kanalların arasına ',' koyarak giriş yapın:")
                    kanal_listesi = kanal_isimleri.split(",")
                    for eklenecekler in kanal_listesi:
                        kumanda.kanal_ekle(eklenecekler)
                    print("{} adet kanal eklendi...".format(len(kanal_listesi)))

            elif islem == "5":
                if kumanda.tv_durum == "Kapalı":
                    print("TV şuan kapalı...")
                else:
                    print("KANAL SAYISI: ",len(kumanda))

            elif islem == "6":
                if kumanda.tv_durum =="Kapalı":
                    print("TV şuan kapalı...")
                else:
                    kumanda.rastgele_kanal()


            elif islem == "7":
                print(kumanda)

            elif islem == "8":
                if kumanda.tv_durum =="Kapalı":
                    print("TV şuan kapalı...")

                else:
                    kumanda.mute()

            elif islem == "9":
                if kumanda.tv_durum =="Kapalı":
                    print("TV şuan kapalı...")

                else:
                    kumanda.kanala_git()


            else:
                print("Geçersiz İşlem...")








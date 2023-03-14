#class kavrami ile bir market uygulamasi

"06.02.23 tarihinde tamamlanmıştır"

import os   

"""
uygulamada bulunan os kütüphanesinin system('cls') fonksiyonu sebebi
ıle bir çok print fonksiyonu çalışmamaktadır

kütüphanenin bu fonksiyonu konsolu her defasında temizlemeye yarar
"""

class urun():
    sayi = 1 # ürünleri otomatik numaralandırmak 
             # için bu değişkeni kullandık
    def __init__(self,adi = str,stok_sayisi = int,fiyat = int):
        self.isim = adi
        self.stok_no = urun.sayi
        self.stok_sayi = stok_sayisi
        self.fiyat = fiyat
        urun.sayi += 1 #her defasında stok sayısını arttırdık
        urunler.append(self) # self ile her ürünün
                             # listeye kayıt edilmesini sağladık

urunler = []
# ********ürünler*********
"buraya daha fazlasını ekleyebilirsiniz"

cikolata = urun("çikolata",20,5)
seker = urun("seker",15,10.5)
sakiz = urun("sakiz",10,0.50)
kahve = urun("kahve",20,30)
un = urun("un",10,50)
muz = urun("muz",10,5)
badem = urun("badem",5,15)
cilek = urun("çilek",10,30)
findik = urun("fındık",20,60)
yulaf = urun("yulaf",20,20)
kursun = urun("kursun kalem",20,10)

def urunleri_gor(): # urunleri yazazdiran fonksiyon
    for u in urunler:
        print(f"[{u.stok_no}] {u.isim}" )
def urun_bilgi(numara = int):#urun var mı yok mu kontrolunu saglayan fonksiyon
    if numara > len(urunler) or numara < 1:
        return "var olan bir numara girin"
    else:
        return f"isim = {urunler[numara-1].isim}\nfiyat = {urunler[numara-1].fiyat}\nnumara = {urunler[numara-1].stok_no}\nadet = {urunler[numara-1].stok_sayi}"
def islemler(): #musterinin yapabilecegi islemleri yazdiran fonksiyon
    if ekranimiz == "musteri":
        islemler = ["urun al","urun iade et","urun degistir"] 
        sayi = 1
        for u in islemler:
            print(f"{[sayi]} {u}")
            sayi += 1
    if ekranimiz == "yonetici":
        islemler = ["urun fiyati degistir","urun stogunu degistir"]
        sayi = 1
        for u in islemler:
            print(f"{[sayi]} {u}")
            sayi += 1
musteriler = []
class musteri():#müşterinin kendisidir
    def __init__(self,isim,para,urun_hak): #burada bulunanlar müşterinin 
                                           #özellikleridir
        self.musteri_para = para
        self.hak = urun_hak
        self.sepet = []
        self.isim = isim
        musteriler.append(self)
    def musteri_bilgiler(self): # müşteri bilgilerini kolayca yazdırmak için
        return f"Müşteri isimi = {self.isim} \nParası = {self.musteri_para} \nsepet hacmi = {self.hak}"
    def urun_al(self): # bu ise müşterinin ürün alabileceği bir fonksiyondur
        os.system("cls")
        urunleri_gor()
        haci =True
        while haci:#burada devamlı kullanıcı 
            #sayı dışı bir şey girmiş mi kontrolünü yapıyoruz
            try:    
                self.urun_no = int(input("lutfen almak istediginiz urun numarasini yazin = "))
                haci = False
            except:
                haci = True    
        if urun_bilgi(self.urun_no) == "var olan bir numara girin" or len(self.sepet)>= self.hak or self.musteri_para == 0 :
            #buranın asıl amacı herhangi bir hata varsa ona göre bir mesaj vermektir 
            if urun_bilgi(self.urun_no) == "var olan bir numara girin":
                #kullanıcı ürünlerin stok numarasından büyük bir numara girmişse
                print(urun_bilgi(self.urun_no))
            if self.musteri_para <= 0:
                #parası 0 yada küçükse
                print("paraniz bitmistir")
            if len(self.sepet) == self.hak:
                print("sepet hakkiniz bitmistir")
        else:
            os.system("cls")
            print(urun_bilgi(self.urun_no))
            #kullanıcın seçtiği ürünün bilgileri
            haci = True
            while haci: # sayımı harf mi kontrolü
                try:
                    self.adet = int(input("kac adet almak istersiniz = "))
                    haci = False
                except:
                    haci = True
            print("paraniz = {}\nalmak istediğize eminmisiniz E/H ".format(self.musteri_para))
            evet = input().upper()
            if evet == "E":
                if urunler[self.urun_no-1].fiyat > self.musteri_para:
                    print("paraniz yetersiz") 
                    # burada musterinin parası yeterlimi kontrolü yapıyoruz
                else:
                    for u in range(self.adet):
                        if self.musteri_para <= 0 or self.musteri_para-urunler[self.urun_no-1].fiyat < 0:
                            print("daha fazla alacak paraniz yok")
                            break
                        if self.hak == 0 :
                            print("hakkiniz kalmamistir")
                            break
                        if urunler[self.urun_no-1].stok_sayi == 0 :
                            print("urun tukenmistir")
                            break
                        else:
                            # ürünü aldığında sepete ürünü yazan 
                            # ürünün stoğunu azaltan ve paradan fiyatı düşen bölüm
                            self.musteri_para = self.musteri_para-urunler[self.urun_no-1].fiyat
                            self.sepet.append(urunler[self.urun_no-1].isim)
                            urunler[self.urun_no-1].stok_sayi -= 1
                            self.hak -= 1       
            if evet == "H":
                pass
        
    def urun_iade(self):
        if len(self.sepet) == 0: # kullanıcı sepeti boş ise
            os.system("cls")
            print("sepetinizde iade edilecek urun yok")
        else:
            os.system("cls")
            print("iade ettiginiz urunun fiyatinin %50 sini geri alirsiniz kabul ediyorumusunuz E/H")
            evet = input().upper()
            if evet == "E":
                print(self.sepet)
                iade = input("lutfen urunun isimini yada sirasini girin = ")
                # urunun ismini mi sirasini mi girmis kontorlu
                try:
                    iade = int(iade) # burada ismini girmis ise hata cikacak 
                                     # except kod bloguna gececek
                    haci = True
                    while iade > len(self.sepet): 
                        # sepet disinda bir urun girmis ise
                        while haci:
                            try:
                                iade = int(input("lutfen urunun isimini yada sirasini girin = "))
                                haci = False
                            except:
                                haci = True
                        break                        
                    iade_urun = self.sepet[iade-1] 
                    #sepette iade edilecek urun isimi
                    self.sepet.pop(iade-1)
                    #sepetten urunu sira numarasina gore silme
                    for u in urunler:
                        if u.isim == iade_urun:
                            self.musteri_para += u.fiyat/2 
                            # urunler listesinden isimi iade olacak olan isime esitse
                            # musteri parasini o urunun yarisi kadar arttirdik
                except:
                    iade = iade.lower()
                    #burada tum urunlerin isiminin tamami kuck harf oldugu icin
                    #urunu kolay bulabilmek amaci ile
                    #tum harflerini kuculttuk
                    if iade in self.sepet:
                        self.sepet.remove(iade)# urun sepette ise urunu sepetten siliyoruz
                    else:
                        print("bu urun mevcut degil")
                for u in urunler:
                    if u.isim == iade: 
                    #urunler listesini acip tum urunlerin isimi
                    # bizim vedigimiz urune esitse o urunun fiyatinin yarisini veriyoruz 
                    
                        self.musteri_para += u.fiyat/2
    def urun_degisim(self):
        os.system("cls")
        if len(self.sepet) == 0:
            print("sepetinizde urun bulunmamakta")
        else:
            dogru = True
            deneg = True
            # kullanici devamli olarak sayi girmis mi
            # diye kontrol etmek icin olusturdugumuz bool veri tipi 
            print(self.sepet)
            degistirilmek_istenen = input("degistirmek istediginiz urunun sirasini yada ismini yazin = ")
            while deneg:
                try:
                    degistirilmek_istenen = int(degistirilmek_istenen)
                    while degistirilmek_istenen > len(self.sepet):
                        print("sepetin disina ciktiniz")    
                        while dogru:#int veri tipi sorunsuz giriliyor mu kontorlu
                            try:
                                degistirilmek_istenen = int(input("urun numarasini yazin = "))
                                dogru = False
                            except:#hata cikarsa sonsuz donug devam eder
                                dogru = True
                    secilen_urun = self.sepet[degistirilmek_istenen-1]
                    #bu kisim bize urun classinin isim degerini verir
                    for u in urunler:    
                        if u.isim == secilen_urun:
                            secilen_urun_fiyat = u.fiyat
                            break
                    urunleri_gor()
                    istenilen_urun = input("lutfen istediginiz urunun numarasini yada isimini yazin = ")
                    try:
                        istenilen_urun = int(istenilen_urun)
                        while istenilen_urun > urun.sayi or istenilen_urun < 1:
                            #urun urunler listesinde var mi kontorlu
                            istenilen_urun = int(input("lutfen istediginiz urunun numarasini yada isimini yazin = "))
                        for a in urunler:
                            if a.stok_no == istenilen_urun:
                                istenilen_urun_fiyati = a.fiyat
                                istenilen_urun_isim = a.isim
                                break
                    except:
                        for a in urunler:
                            if istenilen_urun == a.isim:
                                for u in urunler:
                                    if u.isim == istenilen_urun:
                                        istenilen_urun_fiyati = u.fiyat
                                        istenilen_urun_isim = u.isim
                                        break
                    #musterinin sepetindeki ve parasindaki degisimi ayarlayan kisim
                    fiyat_farki = istenilen_urun_fiyati - secilen_urun_fiyat
                    fiyat = self.musteri_para - fiyat_farki
                    self.musteri_para = fiyat
                    self.sepet[degistirilmek_istenen-1] = istenilen_urun_isim
                    deneg = False
                except:
                    deneg = True
def musterileri_yazdir():
    sayi = 1
    for u in musteriler:
        print(f"[{sayi}]{u.musteri_bilgiler()}")
        sayi += 1
yoneticiler = []
class yonetici():
    def __init__(self,isim,rutbe):
        self.isim = isim
        self.rutbe = rutbe
        yoneticiler.append(self)
    def yonetici_bilgi(self):
        return f"isim = {self.isim}\nrutbe = {self.rutbe}"
    def urun_fiyat_degistir(self): 
        # urun fiyati degistirmek icin kullanilan fonksiyon
        if self.rutbe == "kidemli":
            sayi = 1
            for u in urunler:
                print(f"[{sayi}]  {u.isim}")
                sayi += 1
            degisecek_urun = int(input("degisecek urunun numarasini yazin = "))
            degisecek_urun_isim = urunler[degisecek_urun-1]
            os.system("cls")
            print(urun_bilgi(degisecek_urun))
            kontrol = True
            while kontrol:
                try:
                    yeni_fiyat = int(input("yeni fiyat ne olsun = "))
                    kontrol = False
                except:
                    kontrol = True
            degisecek_urun_isim.fiyat = yeni_fiyat
        else:
            print("buna yetkiniz yok")
    def urun_stok_ayarla(self):
        # urunler ustunde stok degisimi yapabilmek icin kullanilan fonksiyon
        urunleri_gor()
        urunumuz_no = int(input("stok sayisi degisecek urunun numarasini yazin = "))
        urunumuz = urunler[urunumuz_no-1]
        os.system("cls")
        print(urun_bilgi(urunumuz_no))
        yeni_stok = int(input("yeni stok ne olsun"))      
        urunumuz.stok_sayi = yeni_stok
    def kullanici_sepet_hakki_ayarla(self):
        #kullanici ustunde sepet degisimi yapmak icin kullanilan fonksiyon
        musterileri_yazdir()
        musteri_sec = int(input("sepet hakki ayarlamak istediginiz kullanici numarasi nedir = "))
        os.system("cls")
        print(musteriler[musteri_sec-1].musteri_bilgiler())
        yeni_hak = int(input("yeni sepet hakki ne olsun = "))
        musteriler[musteri_sec-1].hak =  yeni_hak
    def kullanici_para_ayarla(self):
        #kullanici ustunde kullanicinin parasini ayarlayabilecegimiz fonksiyon
        musterileri_yazdir()
        musteri_sec = int(input("parasini ayarlamak istediginiz musterinin numarasi nedir = "))
        os.system("cls")
        print(musteriler[musteri_sec-1].musteri_bilgiler())
        yeni_para = int(input("musterinin yeni parasi ne olsun = "))
        musteriler[musteri_sec-1].musteri_para = yeni_para
os.system("cls")
####################  kişiler  ##############################
yonetici_ahmet = yonetici("ahmet","kidemli")
musterimiz = musteri("mehmet",200,15)
musterimiz2 = musteri("ali",800,20)
musterimiz3 = musteri("veli",1300,10)
musteri9 = musteri("efe",2300,25)
def ekran():
    global aktif_musteri
    global yoneticimiz
    sayi = 1
    girisler = ["musteri","yonetici"]
    os.system("cls")
    for u in girisler:
        print(f"[{sayi}] {u}")
        sayi +=1
    sayi = 1
    haci = True
    while haci:
        try:
            giris = int(input("lutfen giris yontemini secin = "))
            haci = False
        except:
            haci = True
    os.system("cls")
    if giris == 2 :
        sayi = 1
        for u in yoneticiler:#yoneticiler listesindeki elemanları yazdırıyoruz
            print(f"[{sayi}] {u.yonetici_bilgi()}")
            print("**************************************")
            sayi += 1
        yonetici_giris_no = int(input("hangi yonetici olamak istersiniz = "))
        yoneticimiz = yoneticiler[yonetici_giris_no-1]
        return "yonetici"
    #kullanıcının belirlediği işleme gore o işleme ait 
    #elemanı donduruyoruz
    if giris == 1:
        os.system("cls")
        for u in musteriler:
            print(f"[{sayi}] {u.musteri_bilgiler()}")
            print("****************************************")
            sayi += 1
        musteri_sec = int(input("hangi musteriyi sececeksiniz = "))
        try:
            aktif_musteri = musteriler[musteri_sec-1]
        except:
            print("gecerli bir numara girin")
        return "musteri"
ekranimiz = ekran()
os.system("cls")
while True:
    while ekranimiz == "musteri":
        #dödürülen değer musteri ise
        os.system("cls")
        print(f"PARA = {aktif_musteri.musteri_para}\nSEPET = {aktif_musteri.sepet}\nsepet limiti = {aktif_musteri.hak}\n\ncikmak icin 9 a basin")
        islemler()
        belirgec = True
        while belirgec:
            try:#devamlı olarak sayı mı giriyor yoksa yazımı kontrolü
                islem = int(input("hangi islemi yapmak istersiniz = "))
                belirgec = False
            except:
                belirgec = True
        if islem == 9:
            ekranimiz = ekran()
        if islem == 1:
            print("9 a basarak ilk ekrana donebilirsin")
            aktif_musteri.urun_al()
        if islem == 2:
            print("9 a basarak ilk ekrana donebilirsin")
            aktif_musteri.urun_iade()
        if islem == 3:
            print("9 a basarak ilk ekrana donebilirsin")
            aktif_musteri.urun_degisim()
    while ekranimiz == "yonetici":
        islemler_liste = ["musteri islemleri","market islemleri\n\ncikmak icin 9 a basin"]
        sayi = 1
        for u in islemler_liste:
            print(f"[{sayi}] {u}")
            sayi += 1
        islem_sec = int(input("hangi islemi yapmak isterisiniz = "))
        while islem_sec > len(islemler_liste):
            if islem_sec == 9:
                ekranimiz = ekran()
                break
            else:
                print("var olan bir islem secin")
                islem_sec = int(input("hangi islemi yapmak isterisiniz = "))   
        if islem_sec == 1:
            sayi = 1
            musteri_islemler = ["musteri para ayarla","musteri sepet hakki ayarla\n\ncikmak icin 9 a basin"]
            os.system("cls")
            for u in musteri_islemler:
                print(f"[{sayi}] {u}")
                sayi += 1 
            musteri_islem_sec = int(input("hangi islemi yapmak isterisiniz = "))    
            if musteri_islem_sec == 1:
                yoneticimiz.kullanici_para_ayarla()
            if musteri_islem_sec == 2:
                yoneticimiz.kullanici_sepet_hakki_ayarla()
            if musteri_islem_sec == 9:
                ekranimiz = ekran()
        if islem_sec == 2:
            sayi = 1
            islemler_liste = ["stok sayisi ayarla","fiyat ayarla"]
            os.system("cls")
            for u in islemler_liste:
                print(f"[{sayi}] {u}")
                sayi += 1
            market_islem_sec = int(input("hangi islemi yapmak isterisiniz = "))
            if market_islem_sec == 2:
                yoneticimiz.urun_fiyat_degistir()
            if market_islem_sec == 1:
                yoneticimiz.urun_stok_ayarla()
            if market_islem_sec == 9 :
                ekranimiz = ekran()

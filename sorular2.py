# 🧍‍♂️ Üst sınıf (Base Class)
class Insan:
    def __init__(self, ad, yas):
        self.ad = ad
        self.yas = yas

    def konus(self):
        print(f"Benim adım {self.ad}, {self.yas} yaşındayım.")

# 👨‍🏫 Hoca sınıfı (Insan'dan miras alır)
class Hoca(Insan):
    def __init__(self, ad, yas, sicil_no):
        super().__init__(ad, yas)  # Üst sınıftaki özellikleri al
        self.sicil_no = sicil_no

    # konus metodunu ezme (override)
    def konus(self):
        print(f"Ben Hoca {self.ad}, öğrencilerime bilgi aktarmayı severim.")

    def ders_ver(self):
        print(f"Hoca {self.ad} şu anda ders veriyor. (Sicil No: {self.sicil_no})")

# 👩‍💼 Sekreter sınıfı
class Sekreter(Insan):
    def __init__(self, ad, yas, ofis_no):
        super().__init__(ad, yas)
        self.ofis_no = ofis_no

    def konus(self):
        print(f"Ben Sekreter {self.ad}, ofis numaram {self.ofis_no}.")

    def toplantiyi_duzenle(self):
        print(f"Sekreter {self.ad}, toplantıyı düzenliyor...")

# 👨‍🎓 Öğrenci sınıfı
class Ogrenci(Insan):
    def __init__(self, ad, yas, ogr_no):
        super().__init__(ad, yas)
        self.ogr_no = ogr_no

    def konus(self):
        print(f"Ben Öğrenci {self.ad}, öğrenmeyi çok seviyorum!")

    def ders_calis(self):
        print(f"Öğrenci {self.ad} şu anda ders çalışıyor. (Öğrenci No: {self.ogr_no})")

# 🧩 Kullanım örnekleri
hoca1 = Hoca("Ahmet", 40, "H123")
sekreter1 = Sekreter("Elif", 30, "A12")
ogrenci1 = Ogrenci("Mert", 20, "O456")

# Metotları çağırma
hoca1.konus()
hoca1.ders_ver()

sekreter1.konus()
sekreter1.toplantiyi_duzenle()

ogrenci1.konus()
ogrenci1.ders_calis()

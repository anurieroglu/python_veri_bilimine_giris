# Python Ödevi - Temel Kavramlar

# 1️⃣ print ve sep örneği
print("Merhaba", "Dünya", sep=" - ")
print("Python", "öğrenmek", "çok", "güzel!", sep=" 💻 ")

# 2️⃣ Değişken tanımlama ve basit işlem
a = 5
b = 10
print("a:", a, "b:", b)
print("Toplam:", a + b)

# 3️⃣ Koşul (if - elif - else) örneği
if a < b:
    print("a, b'den küçüktür")
elif a == b:
    print("a ve b eşittir")
else:
    print("a, b'den büyüktür")

# 4️⃣ Döngü (for) örneği
print("\n1'den 5'e kadar sayılar:")
for i in range(1, 6):
    print(i)

# 5️⃣ Döngü (while) örneği
print("\nWhile döngüsü ile sayaç:")
sayac = 0
while sayac < 3:
    print("Sayaç:", sayac)
    sayac += 1

# 6️⃣ Basit fonksiyon (function) örneği
def selamla(isim):
    print("Merhaba,", isim)

# Fonksiyonu çağırma
selamla("Ahmet")

# 7️⃣ Parametreli ve geri dönen fonksiyon
def topla(x, y):
    return x + y

sonuc = topla(7, 3)
print("\nToplam sonucu:", sonuc)

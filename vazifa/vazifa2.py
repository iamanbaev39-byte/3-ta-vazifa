e_bozor = {
    "olma": 5000,
    "non": 3000,
    "sut": 12000
}

buyurtmalar = []

while True:
    mahsulot = input("Sotib olmoqchi bo'lgan mahsulotingiz: ")
    if mahsulot.lower() == 'stop':
        break
    buyurtmalar.append(mahsulot.lower())
print("--- Buyurtma tekshirilmoqda ---")
for mahsulot in buyurtmalar:
    if mahsulot in e_bozor:
        print(f"{mahsulot.capitalize()} - {e_bozor[mahsulot]} so'm")
    else:
        print(f"{mahsulot.capitalize()} - Bizda bu mahsulot yo'q")

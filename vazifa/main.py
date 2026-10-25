buyurtmalar = []

while True:
    mahsulot = input("Mahsulot kiriting (tugatish uchun stop): ")
    if mahsulot == "stop":
        break
    buyurtmalar.append(mahsulot)

print("Buyurtmalar:", buyurtmalar)
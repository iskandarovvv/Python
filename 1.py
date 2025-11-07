# Davlatlar ro'yxatini tuzamiz
davlatlar = ["O'zbekiston", "Qozog'iston", "Tojikiston", "Qirg'iziston", "Turkmaniston", "Rossiya", "Xitoy", "AQSH", "Yaponiya", "Fransiya"]

# 1. Ro'yxatni konsolga chiqarish
print("Asl ro'yxat:")
print(davlatlar)

# 2. Ro'yxatning uzunligini chiqarish
print("\nRo'yxat uzunligi:", len(davlatlar))

# 3. sorted() yordamida tartiblangan ro'yxat
print("\nAlifbo bo'yicha tartiblangan ro'yxat (sorted() yordamida):")
print(sorted(davlatlar))

# 4. sorted() yordamida teskari tartibda
print("\nTeskari tartibda tartiblangan ro'yxat (sorted(reverse=True)):")
print(sorted(davlatlar, reverse=True))

# 5. Asl ro'yxatni yana chiqarish (o'zgarmagan holatda)
print("\nAsl ro'yxat (o'zgarmagan):")
print(davlatlar)

# 6. reverse() yordamida ro'yxatni teskari chiqarish
davlatlar.reverse()
print("\nreverse() yordamida teskari chiqarilgan ro'yxat:")
print(davlatlar)

# 7. sort() yordamida ro'yxatni alifbo bo'yicha tartiblash
davlatlar.sort()
print("\nsort() yordamida alifbo bo'yicha tartiblangan ro'yxat:")
print(davlatlar)

# 8. sort() yordamida teskari alifbo tartibida
davlatlar.sort(reverse=True)
print("\nsort() yordamida teskari alifbo tartibida:")
print(davlatlar)

#Juft sonlar ro'yxatini yaratamiz
even_numbers = list(range(120, 1201, 2))
n = len(even_numbers)
head = even_numbers[:20]
mid_start = max(0, n//2 - 10)
mid_end = min(n, n//2 + 10)
middle = even_numbers[mid_start:mid_end]
tail = even_numbers[-20:]
print("Boshi:", head)
print("O'rtasi:", middle)
print("Oxiri:", tail)






























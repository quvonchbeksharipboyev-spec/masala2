#1
def add_left_digit(son, raqam):
    # Sonni satrga o'girib, chapiga raqamni qo'shib, yana songa aylantiramiz
    yangi_son = int(str(raqam) + str(son))
    return yangi_son

# Ishlatib ko'rish
K = 45
R = 7
K = add_left_digit(K, R)
print(f"Natija: {K}")  # 745
#2
def swap(x, y):
    return y, x

# Berilgan: A, B va D, C juftliklarini almashtirish
A, B, C, D = 1, 2, 3, 4

A, B = swap(A, B)
D, C = swap(D, C)

print(f"A: {A}, B: {B}") # A: 2, B: 1
print(f"D: {D}, C: {C}") # D: 3, C: 4
#3
def minmax(x, y):
    if x > y:
        return y, x
    return x, y

# a, b, c, d ichidan min va max ni topish
a, b, c, d = 10, 5, 20, 2

a, b = minmax(a, b)
c, d = minmax(c, d)
a, c = minmax(a, c) # Eng kichigi 'a' da qoladi
b, d = minmax(b, d) # Eng kattasi 'd' da qoladi

print(f"Eng kichigi: {a}, Eng kattasi: {d}")
#4
def sort_inc3(a, b, c):
    # Tartiblab ro'yxat ko'rinishida qaytaramiz
    elementlar = sorted([a, b, c])
    return elementlar[0], elementlar[1], elementlar[2]

# (A1, B1, C1) va (A2, B2, C2) ni tartiblash
a1, b1, c1 = 10, 2, 5
a2, b2, c2 = 30, 15, 40

a1, b1, c1 = sort_inc3(a1, b1, c1)
a2, b2, c2 = sort_inc3(a2, b2, c2)

print(f"1-guruh: {a1}, {b1}, {c1}")
print(f"2-guruh: {a2}, {b2}, {c2}")
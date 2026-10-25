def read(text, kind, a, b):
    while True:
        try:
            x = kind(input(text))
            if a <= x <= b:
                return x
            print(f"Введите число от {a} до {b}.")
        except ValueError:
            print("Ошибка: введите число.")


print("1 — цилиндрическая\n2 — коническая\n3 — червячная")
choice = read("Выберите тип: ", int, 1, 3)

match choice:
    case 1:
        name, eta = "цилиндрическая", 0.97
    case 2:
        name, eta = "коническая", 0.95
    case 3:
        name, eta = "червячная", 0.80

z1 = read("z1: ", int, 10, 100)

while True:
    z2 = read("z2: ", int, 10, 200)
    if z2 > z1:
        break
    print("z2 должно быть больше z1.")

P = read("P, кВт: ", float, 0.1, 100)
n1 = read("n1, об/мин: ", float, 100, 3000)

u = z2 / z1
n2 = n1 / u
T1 = 9550 * P / n1
T2 = T1 * u * eta

if u < 2:
    level = "малое"
elif u <= 8:
    level = "нормальное"
else:
    level = "большое"

print("\nТип передачи:", name)
print(f"u = {u:.2f}")
print(f"n2 = {n2:.2f} об/мин")
print(f"T1 = {T1:.2f} Н·м")
print(f"T2 = {T2:.2f} Н·м")
print("Класс:", level)
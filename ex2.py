import random

n = int(input("Введіть кількість рядків: "))
m = int(input("Введіть кількість стовбців: "))

matrix = [[random.randint(-5, 5) for z in range(m)] for i in range(n)]

print("-" * 5, "Матриця", "-" * 5)

for z in matrix:
    print(z)

for rd in matrix:
    for i in rd:
        if rd.count(i) > 1:
            print("Однакові елементи є в рядку: ", matrix.index(rd) + 1)
            break
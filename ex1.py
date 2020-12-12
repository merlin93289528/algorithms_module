growth = []

while True:
    n = float(input("Введіть зріст: "))
    if n == 0:
        break
    growth.append(n)

print(sum(growth) / len(growth))
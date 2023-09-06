n = int(input ("Введіть число N: "))
while (n < 1 and n > 9):
    n = int(input ("Введіть Число N: "))

print("Рисунок з заданий числом N:")
for j in range(1, n+1):
    for i in range((n+1)-j):
        print("5", end=" ")
    print(" ")
for j in range(n+1):
    for i in range(j):
        print("5", end=" ")
    print(" ")

a = int(input ("Введіть а: "))
while (a < 1):
    a = int(input ("Введіть а: "))
b = int(input ("Введіть b: "))
while (b < 1):
    b = int(input ("Введіть b: "))
if a > b:
    x = b * a + 1
elif a == b:
    x = -10
else:
    x = (a - 5) / b
print("Результат: " , x)

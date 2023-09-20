import math

# Функція для обчислення z = exp(x) + √x
def calculate_z(x):
    z = math.exp(x) + math.sqrt(x)
    return z

# Функція для знаходження суми цифр числа n
def sum_of_digits(n):
    digit_sum = 0
    while n > 0:
        digit = n % 10
        digit_sum += digit
        n //= 10
    return digit_sum

# Зчитуємо число x від користувача
x = float(input("Введіть число x: "))

# Викликаємо функцію calculate_z
z = calculate_z(x)

# Виводимо результат
print(f"Результат обчислення z = exp(x) + √x: {z}")

# Зчитуємо число n від користувача
n = int(input("Введіть число n: "))

# Викликаємо функцію sum_of_digits
digit_sum = sum_of_digits(n)

# Виводимо результат
print(f"Сума цифр числа n: {digit_sum}")

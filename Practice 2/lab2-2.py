from mod import sum_of_digits

# Зчитуємо число n від користувача
n = int(input("Введіть число n: "))

# Викликаємо функцію sum_of_digits
digit_sum = sum_of_digits(n)

# Виводимо результат
print(f"Сума цифр числа n: {digit_sum}")

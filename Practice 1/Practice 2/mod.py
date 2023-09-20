# Функція для знаходження суми цифр числа n
def sum_of_digits(n):
    digit_sum = 0
    while n > 0:
        digit = n % 10
        digit_sum += digit
        n //= 10
    return digit_sum
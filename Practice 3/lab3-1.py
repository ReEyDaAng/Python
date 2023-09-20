# Зчитуємо рядок з клавіатури
my_string = input("Введіть рядок: ")

# Отримуємо кожний 3-й символ від 4-го символа з початку до 20-го символа (20-й символ не включається)
start_index = 3  # Індекс 4-го символа
end_index = 20   # Індекс 20-го символа (не включається)
step = 3         # Крок - отримуємо кожен 3-й символ

# Перевірка на випадок, якщо введений рядок коротший, ніж end_index
if end_index > len(my_string):
    end_index = len(my_string)

result_slice = my_string[start_index:end_index:step]

# Виводимо результат
print(result_slice)

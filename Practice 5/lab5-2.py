# Ініціалізуємо двовимірний масив розміром 7x7 зі значеннями 0
array = [[0] * 7 for _ in range(7)]

# Заповнюємо масив почергово одиницями і нулями
for i in range(7):
    for j in range(7):
        # Перевіряємо, чи сума індексів парна або непарна
        if (i + j) % 2 == 0:
            array[i][j] = 1
        else:
            array[i][j] = 0

# Виводимо масив на екран
for row in array:
    print(' '.join(map(str, row)))

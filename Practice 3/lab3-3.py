# Зчитуємо речення від користувача
sentence = input("Введіть речення: ")

# Розділяємо речення на слова за пробілами
words = sentence.split()

# Ініціалізуємо змінну для зберігання довжини найкоротшого слова
shortest_word_length = float('inf')  # Встановлюємо початкове значення як дуже велике число

# Перебираємо слова та знаходимо довжину найкоротшого
for word in words:
    word_length = len(word)
    if word_length < shortest_word_length:
        shortest_word_length = word_length

# Виводимо результат
print(f"Довжина найкоротшого слова в реченні: {shortest_word_length}")

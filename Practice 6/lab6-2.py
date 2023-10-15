def search_word(word, word_list):
  if word in word_list:
      return True
  else:
      return False

# Запит користувача на введення списку слів
word_list = input("Введіть список слів, розділених пробілами: ").split()

# Запит користувача на введення слова для пошуку
search_word_input = input("Введіть слово для пошуку: ")

search_word_result = search_word(search_word_input, word_list)

if search_word_result:
  print(f"Слово '{search_word_input}' знайдено в списку.")
else:
  print(f"Слово '{search_word_input}' не знайдено в списку.")

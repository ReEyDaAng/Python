def split_list(input_list, split_value):
  # Ініціалізуємо два порожніх списки для розбитих даних
  list1 = []
  list2 = []

  # Проходимо по кожному елементу вхідного списку
  for item in input_list:
      # Перевіряємо значення інформаційного атрибуту елемента
      if item == split_value:
          list2.append(item)
      else:
          list1.append(item)

  return list1, list2

# Запит користувача на введення списку
input_list = input("Введіть список елементів (розділені пробілами): ").split()

# Запит користувача на введення значення для розбиття списку
split_value = input("Введіть значення для розбиття списку: ")

# Викликаємо функцію та отримуємо розбиті списки
result_list1, result_list2 = split_list(input_list, split_value)

# Виводимо результат
print("Список 1:", result_list1)
print("Список 2:", result_list2)

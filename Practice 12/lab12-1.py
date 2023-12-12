import json

# Функція для виведення вмісту JSON файлу
def display_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        print(json.dumps(data, indent=4))

# Функція для додавання нового запису у JSON файл
def add_record(filename, record):
    with open(filename, 'r') as file:
        data = json.load(file)
        data.append(record)
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

# Функція для видалення запису з JSON файлу
def remove_record(filename, index):
    with open(filename, 'r') as file:
        data = json.load(file)
        if 0 <= index < len(data):
            del data[index]
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

# Функція для пошуку даних за полем
def search_by_field(filename, field, value):
    with open(filename, 'r') as file:
        data = json.load(file)
        result = [record for record in data if record.get(field) == value]
        print(json.dumps(result, indent=4))

# Функція для розв'язання завдання за варіантом
def solve_task(input_filename, output_filename):
    with open(input_filename, 'r') as file:
        data = json.load(file)

    total_height_girls = sum(record['height'] for record in data if record['gender'] == 'girl')
    total_height_boys = sum(record['height'] for record in data if record['gender'] == 'boy')

    if total_height_girls > total_height_boys:
        result = {'result': 'The total height of girls exceeds the total height of boys.'}
    else:
        result = {'result': 'The total height of girls does not exceed the total height of boys.'}

    with open(output_filename, 'w') as file:
        json.dump(result, file, indent=4)

# Запис початкових даних у JSON файл
initial_data = [
    {'name': 'Kate', 'gender': 'girl', 'height': 180},
    {'name': 'Alice', 'gender': 'girl', 'height': 160},
    {'name': 'Rey', 'gender': 'boy', 'height': 175},
    {'name': 'Robin', 'gender': 'boy', 'height': 158},
    {'name': 'Jane', 'gender': 'girl', 'height': 156},
    {'name': 'Alex', 'gender': 'boy', 'height': 187},
    {'name': 'Bob', 'gender': 'boy', 'height': 178},
    {'name': 'Mishel', 'gender': 'girl', 'height': 162},
    {'name': 'Mitchel', 'gender': 'boy', 'height': 182},
    {'name': 'Maya', 'gender': 'girl', 'height': 174},
  
    # Додайте інші дані про учнів
]

with open('students.json', 'w') as file:
    json.dump(initial_data, file, indent=4)

# Демонстрація роботи функцій
display_json('students.json')

new_record = {'name': 'Bob', 'gender': 'boy', 'height': 175}
add_record('students.json', new_record)
display_json('students.json')

remove_record('students.json', 1)
display_json('students.json')

search_by_field('students.json', 'name', 'Alice')

solve_task('students.json', 'task_result.json')
display_json('task_result.json')

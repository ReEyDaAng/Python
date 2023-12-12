import pandas as pd

def find_students(students, new_student_height):
    students_below_new_student = [student for student in students.values() if student['height'] < new_student_height]

    for student_id, student in students.items():
        if student['height'] < new_student_height:
            index_to_insert = student_id
            break

    closest_height_student = min(students.values(), key=lambda x: abs(x['height'] - new_student_height))

    return students_below_new_student, index_to_insert, closest_height_student['name']

def print_all_students(students):
    print("Список усіх учнів:")
    for student_id, student in students.items():
        print(f"Ім'я: {student['name']}, Зріст: {student['height']}")

# Задані імена та зрости учнів впорядковані за зменшенням (припустимо, що вони вже відомі)
students = {
    1: {'name': 'Андрій', 'height': 175},
    2: {'name': 'Василь', 'height': 170},
    3: {'name': 'Григорій', 'height': 168},
    4: {'name': 'Денис', 'height': 165},
    5: {'name': 'Євген', 'height': 163},
    6: {'name': 'Зенон', 'height': 160},
    7: {'name': 'Ігор', 'height': 157},
    8: {'name': 'Костянтин', 'height': 155},
    9: {'name': 'Леонід', 'height': 152},
    10: {'name': 'Максим', 'height': 150}
}

# Створюємо датафрейм зі словника
df_students = pd.DataFrame.from_dict(students, orient='index')

while True:
    print("\nМеню вибору:")
    print("1. Вивести список усіх учнів")
    print("2. Знайти інформацію про новенького учня")
    print("3. Вийти")

    choice = input("Виберіть опцію (1/2/3): ")

    if choice == '1':
        # Виводимо датафрейм
        print(df_students)
    elif choice == '2':
        # Зчитуємо зріст "новенького" з клавіатури
        new_student_height = int(input("Введіть зріст новенького учня: "))
        result_a, result_b, result_c = find_students(students, new_student_height)

        print("a) Прізвища всіх учнів, зріст яких менше росту «новенького»:")
        for student in result_a:
            print(student['name'])

        print("б) Прізвище учня, після якого слід записати прізвище «новенького», щоб впорядкованість не порушилася:",
              students[result_b]['name'] if result_b < 10 else "Кінець списку")

        print("в) Прізвище учня, зріст якого найменше відрізняється від росту «новенького»:", result_c)
    elif choice == '3':
        print("Дякую за використання програми. Завершення роботи.")
        break
    else:
        print("Некоректний вибір. Спробуйте ще раз.")

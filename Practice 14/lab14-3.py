import matplotlib.pyplot as plt
import json

def plot_gender_distribution(data):
    # Отримання кількості хлопців та дівчат
    total_boys = sum(1 for record in data if record['gender'] == 'boy')
    total_girls = sum(1 for record in data if record['gender'] == 'girl')

    # Створення списку значень та підписів
    values = [total_boys, total_girls]
    labels = ['Boys', 'Girls']

    # Розфарбовування секторів кругової діаграми
    colors = ['blue', 'pink']

    # Побудова кругової діаграми
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
    plt.title('Gender Distribution in the Class')

    # Відображення діаграми
    plt.show()

# Завантаження даних з файлу JSON
with open('students.json', 'r') as file:
    student_data = json.load(file)

# Побудова кругової діаграми
plot_gender_distribution(student_data)

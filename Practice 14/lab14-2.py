import pandas as pd
import matplotlib.pyplot as plt

# Локальний шлях до CSV-файлу 
file_path = "P_Data_Extract_From_Health_Nutrition_and_Population_Statistics (1)/ed8dbcf1-c53f-4ca3-b26e-4670f34fe850_Data.csv"

# Завантаження та обробка даних
df = pd.read_csv(file_path, header=None)

# Визначення рядків для років, України та США
years = df.iloc[0, 4:].values
ukraine_data = df.iloc[1, 4:].values
usa_data = df.iloc[2, 4:].values

# 2.1 Графік динаміки показників для обраних країн
plt.figure(figsize=(10, 5))
plt.plot(years, ukraine_data, label='Ukraine', color="purple")
plt.plot(years, usa_data, label='USA', color="yellow")

# Налаштування графіка
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('Population, ages 7-11, total')
plt.legend()
plt.grid(True)

# Введення назви країни 
selected_country = input("Введіть назву країни для стовпчастої діаграми (Ukraine або USA): ")

# Вибір даних для обраної країни
if selected_country.lower() == 'ukraine':
    selected_data = ukraine_data
    selected_color = 'purple'
elif selected_country.lower() == 'usa':
    selected_data = usa_data
    selected_color = 'yellow'
else:
    print("Непідтримувана країна. Оберіть Ukraine або USA.")
    exit()

# Побудова стовпчастої діаграми
plt.show()  # Графік показаний

# Продовження виконання коду для побудови стовпчастої діаграми
plt.figure(figsize=(6, 4))
plt.bar(years, selected_data, color=selected_color)
plt.xlabel('Year')
plt.ylabel('Population')
plt.title(f'Population, ages 7-11, total - {selected_country}')
plt.show()

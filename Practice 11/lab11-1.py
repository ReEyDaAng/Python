import csv
import locale

def read_csv(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        return None

def write_csv(data, file_path):
    try:
        with open(file_path, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        print(f"Дані записано у файл: {file_path}")
    except Exception as e:
        print(f"Помилка при записі файлу: {e}")

def find_min_max(data, start_year, end_year):
    try:
        values = []

        for year in range(start_year, end_year + 1):
            year_column = f'{year} [YR{year}]'

            for row in data:
                value = row.get(year_column, '').strip()

                if value:  # Check if the value is not empty
                    try:
                        # Set the locale for proper number formatting
                        locale.setlocale(locale.LC_NUMERIC, '')
                        numeric_value = locale.atof(value)
                        values.append(numeric_value)
                    except ValueError:
                        pass  # Ignore values that cannot be converted to numbers

        if values:
            min_value = min(values)
            max_value = max(values)
            return min_value, max_value
        else:
            return None, None
    except Exception as e:
        print(f"Помилка при пошуку мінімального та максимального значень: {e}")
        return None, None

# File path
file_path = 'P_Data_Extract_From_Health_Nutrition_and_Population_Statistics (1)/73d89c9e-67aa-4bad-a44c-d544a523361c_Data.csv'

# Read data from the CSV file
data = read_csv(file_path)

if data:
    # Display the content of the CSV file
    for row in data:
        print(row)

    # Print the keys for one row to check the actual format
    for key in data[0].keys():
        print(key)


    # Find the minimum and maximum values for Urban population for the years 1991-2019
    start_year = 1991
    end_year = 2019
    min_population, max_population = find_min_max(data, start_year, end_year)

    if min_population is not None and max_population is not None:
        print(f"Мінімальне значення Urban population: {min_population}")
        print(f"Максимальне значення Urban population: {max_population}")

        # Write the results to a new CSV file
        result_data = [['Statistic', 'Value'], ['Min Urban Population', min_population], ['Max Urban Population', max_population]]
        result_file_path = 'результати.csv'
        write_csv(result_data, result_file_path)
    else:
        print("Не вдалося знайти мінімальне та максимальне значення.")

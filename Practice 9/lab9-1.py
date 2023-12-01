# a) Створення текстового файлу TF12_1 із символьних рядків різної довжини
with open('TF12_1.txt', 'w') as file1:
    lines = ["abcd", "efghij", "klmnopqr", "stuvwxyz", "12345", "67890", "!@#$%^", "&*()_+", "-=[]{}|;", ":',.<>?/"]
    for line in lines:
        file1.write(line + '\n')

# b) Читання вмісту файла TF12_1 і запис у файл TF12_2
with open('TF12_1.txt', 'r') as file1, open('TF12_2.txt', 'w') as file2:
    for line in file1:
        line = line.strip()
        for i in range(1, len(line) + 1):
            file2.write(line[:i] + '\n')

# c) Читання вмісту файла TF12_2 і друк на екран
with open('TF12_2.txt', 'r') as file2:
    for line in file2:
        print(line.strip())

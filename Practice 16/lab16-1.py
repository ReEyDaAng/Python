import nltk
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
import string

# Завантаження необхідних ресурсів
nltk.download('stopwords')
nltk.download('punkt')  # Якщо цього не було завантажено раніше

# Зчитування тексту з файлу
file_path = 'chesterton-ball.txt'  # Замініть 'шлях_до_вашого_файлу.txt' на шлях до вашого файлу
with open(file_path, 'r', encoding='latin-1') as file:
    text = file.read()

# Токенізація тексту
words = nltk.word_tokenize(text)

# Визначення кількості слів у тексті
num_words = len(words)
print(f"Кількість слів у тексті: {num_words}")

# Обчислення частоти кожного слова
fdist = FreqDist(words)

# Отримання топ-10 слів
top_words = fdist.most_common(10)
print("Топ-10 слів у тексті:", top_words)

# Побудова стовпчастої діаграми
fdist.plot(10, cumulative=False)
plt.show()

# Видалення стоп-слів та пунктуації
stop_words = set(stopwords.words('english'))
filtered_words = [word.lower() for word in words if word.isalpha() and word.lower() not in stop_words]

# Обчислення частоти кожного слова після видалення стоп-слів
fdist_filtered = FreqDist(filtered_words)

# Отримання топ-10 слів після видалення стоп-слів
top_words_filtered = fdist_filtered.most_common(10)
print("Топ-10 слів у тексті після видалення стоп-слів:", top_words_filtered)

# Побудова стовпчастої діаграми після видалення стоп-слів
fdist_filtered.plot(10, cumulative=False)
plt.show()

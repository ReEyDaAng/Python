import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Завантаження ресурсів NLTK
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Читання тексту з файлу
with open('input.txt', 'r', encoding='utf-8') as file:
    input_text = file.read()

# Токенізація
words = word_tokenize(input_text)

# Лемматизація та стеммінг
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]

# Видалення стоп-слів
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in lemmatized_words if word.lower() not in stop_words]

# Видалення пунктуації
filtered_words = [word for word in filtered_words if word.isalnum()]

# Запис обробленого тексту у файл
output_text = ' '.join(filtered_words)
with open('processed_text.txt', 'w', encoding='utf-8') as file:
    file.write(output_text)

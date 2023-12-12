import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def generate_wordcloud(text):
    # Токенізація слів
    words = word_tokenize(text)

    # Видалення стоп-слів
    stop_words = set(stopwords.words('english'))  # Використовуйте 'ukrainian' для української мови
    filtered_words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]

    # Побудова хмари слів
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(filtered_words))

    # Відображення хмари слів
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    # Приклад введеного тексту
    sample_text = "Example of using libraries to create a word cloud"

    # Генерація хмари слів
    generate_wordcloud(sample_text)

import string
from textblob import TextBlob
import nltk
from nltk.corpus import stopwords

# Download stopwords jika belum
nltk.download('stopwords')

# Fungsi untuk membersihkan teks
def clean_text(text):
    # Mengubah teks menjadi lowercase
    text = text.lower()
    # Menghapus tanda baca
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Menghapus stopwords
    stop_words = set(stopwords.words('english'))
    text = ' '.join([word for word in text.split() if word not in stop_words])
    return text

# Fungsi untuk menentukan sentimen
def get_sentiment(text):
    analysis = TextBlob(text)
    # Sentimen: positif (>0), negatif (<0), netral (0)
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity < 0:
        return 'negative'
    else:
        return 'neutral'

# Input dari pengguna
user_input = input("Masukkan ulasan produk: ")

# Bersihkan dan analisis sentimen
cleaned_input = clean_text(user_input)
sentiment = get_sentiment(cleaned_input)

# Tampilkan hasil
print(f"Sentimen ulasan: {sentiment}")

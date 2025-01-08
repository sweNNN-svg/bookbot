def count_words(text):
    """Metindeki kelime sayısını hesaplar."""
    words = text.split()  # Metni kelimelere böler
    return len(words)  # Kelime sayısını döndürür

# Dosyayı aç ve içeriği oku
with open("/home/haci/workspace/github.com/sweNNN-svg/bookbot/books/frankenstein.txt") as f:
    book_text = f.read()  # Kitap metnini oku

# Kelime sayısını hesapla
word_count = count_words(book_text)

# Sonucu ekrana yazdır
print(f"The book contains {word_count} words.")


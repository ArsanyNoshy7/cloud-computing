import nltk
from collections import Counter


nltk.download('stopwords')


with open("paragraphs.txt", "r") as file:
    text = file.read()

# Preprocess the text
text = text.lower()  # Convert to lowercase
text = "".join([char for char in text if char.isalnum() or char.isspace()])  # Remove punctuation

# Remove stop words using NLTK
stop_words = nltk.corpus.stopwords.words('english')
tokens = [word for word in text.split() if word not in stop_words]

# Count word frequency
word_counts = Counter(tokens)

# Display word frequency count
print("Word Frequency Count:")
for word, count in word_counts.items():
    print(f"{word}: {count}")
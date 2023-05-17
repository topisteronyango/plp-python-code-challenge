import re
from collections import Counter

def count_words(filename):
    with open(filename, 'r') as file:
        text = file.read()

    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = Counter(words)
    top_words = word_counts.most_common(10)

    return top_words

# Set the filename of the text file to process
filename = "file.txt"

# Call the count_words function with the filename
top_words = count_words(filename)

# Print the header
print("Top 10 Most Frequent Words:")

# Iterate over each word and count in top_words, and print them
for word, count in top_words:
    print(f"{word}: {count}")

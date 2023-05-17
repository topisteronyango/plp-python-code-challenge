# importing modules
import re
from collections import Counter

# Defining a function
def count_words(filename):

    # Reading the contents of the text file
    with open(filename, 'r') as file:
        text = file.read()

    # Extracting individual words from the text using regular expressions and convert them to lowercase for case-insensitive counting
    words = re.findall(r'\b\w+\b', text.lower())

    # Counting the frequency of each word using the Counter class from the collections module
    word_counts = Counter(words)

    # Getting the top 10 most frequent words from the word_counts dictionary
    top_words = word_counts.most_common(10)

    # Return the list of top 10 most frequent words and their counts
    return top_words

# Main program

# Setting the filename of the text file to process
filename = "file.txt"

# Calling the count_words function with the filename
top_words = count_words(filename)

# Printting the header
print("Top 10 Most Frequent Words:")

# Iterating over each word and count in top_words, and print them
for word, count in top_words:
    print(f"{word}: {count}")

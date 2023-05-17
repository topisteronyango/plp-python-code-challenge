# SOLUTION STEPS

    STEP 1: The code begins by importing the necessary modules, re and Counter, which are used for regular expressions and counting frequencies, respectively.

    STEP2: The count_words function is defined, which takes a filename as input.

    STEP3: Inside the function, the file with the given filename is opened in read mode, and its contents are read and stored in the text variable.

    STEP4: Using a regular expression pattern (r'\b\w+\b'), the re.findall function extracts all individual words from the text in a case-insensitive manner. The resulting list of words is stored in the words variable.

    STEP5: The Counter class from the collections module is used to count the frequency of each word in the words list. The Counter object is stored in the word_counts variable.

    STEP6: The most_common method of the Counter object is called with the argument 10 to retrieve the top 10 most frequent words. The resulting list of tuples (word, count) is stored in the top_words variable.

    STEP7: The top_words list is returned by the count_words function.

    STEP8: In the main part of the program, the filename of the text file to process is set.

    STEP9: The count_words function is called with the filename, and the resulting list of top words and their counts is stored in the top_words variable.

    STEP10: The program prints the header "Top 10 Most Frequent Words:".

    STEP11: The program iterates over each tuple (word, count) in the top_words list and prints them one by one, with the word and its count separated by a colon.

# Assumptions
    The code assumes that the text file exists and is accessible at the provided file path or name. If the file is not found or cannot be opened, an error may occur.

    The code considers words as consecutive sequences of alphanumeric characters, ignoring punctuation and special characters. It uses the regular expression pattern r'\b\w+\b' to match and extract words. Therefore, words with hyphens or other non-alphanumeric characters within them may be treated as separate words.







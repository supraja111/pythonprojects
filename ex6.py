# "I am a teacher and I love to inspire and teach people".
# Finding how many unique words have been used in the above given sentence.
sentence = "I am a teacher and I love to inspire and teach people"
words = sentence.split()
unique_words = set(words)
unique_words_length = len(unique_words)
print("The unique words are :", unique_words_length)
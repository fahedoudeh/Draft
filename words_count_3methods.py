txt = """
I love you you!
"""

# make the string lower case
txt = txt.lower()
# split the string into a list of words
words = txt.split()
# ### method 1 ####
# create an empty dictionary to store the words
word_count = {}
# loop through the list of words
for word in words:
# get the value of the word from the dictionary
# if the word is not in the dictionary set the value to 0then add 1

    word_count[word] = word_count.get(word, 0) + 1
for word, count in word_count.items():
    print(f"{word}: {count}")

################
# ### method 2 ####
# create an empty dictionary to store the words
word_count = {}
# loop through the list of words
for word in words:
# check if the word is not in the dictionary
    if word not in word_count:
# if the word is not in the dictionary add it and setthe value to 1
        word_count[word] = 1

    else:
# if the word is in the dictionary add 1 to the value
        word_count[word] += 1
# print the dictionary
for word, count in word_count.items():
    print(f"{word}: {count}")
#############################
# ### method 3 ####
# create an empty dictionary to store the words
word_count = {}
# loop through the list of words
for word in words:
# set the value of the word to 0 if it is not in the dictionary
    word_count.setdefault(word, 0)
# add 1 to the value of the word
    word_count[word] += 1
for word, count in word_count.items():
    print(f"{word}: {count}")

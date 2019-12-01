#!/home/tushar/anaconda3/bin/python
# Hadoop Streaming : Program to count the non-English words in a file.
# mapper.py

import re
import sys
import os

# Function to read the file containing all the english words.
def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())
    return valid_words

# Loaded all english words as dictionary in the variable.
WordList = load_words()

# Fetching filename on which the mapper is working.
filepath = os.environ["map_input_file"] 
filename = os.path.split(filepath)[-1]

flag = 0
word_list = []

# Looping over every line which is input to mapper.
for line in sys.stdin:
    # Regex to find 'Text:' keyword in the file. 
    # Only lines after keyword 'Text:' will be consider for operation.
    if re.match('^text:$', line.lower()):
        flag = 1
    elif flag == 1:
        # Keeping only alphanumeric characters only.
        line = re.sub(r'[^0-9a-zA-Z]',' ',line)
        # Splitting the line.
        words = line.strip().split()
        # Looping over all the words.
        for word in words:
            # Checking if the word is an english word or not.
            if word.lower() not in WordList:
                word_list.append(word.lower())
            else:
                pass
# Mapper output is filename on which mapper is executing and the list of non english words.
print(filename,'\t',word_list)
    


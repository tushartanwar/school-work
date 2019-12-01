#!/usr/bin/python3
# Hadoop Streaming : Count of non-english words
# Reducer_filterWrds.py
# Author : Tushar Tanwar

import sys
import ast

prev_file = None
prev_word_list = []

# Looping over the mapper output.
for line in sys.stdin:
    # Stripping the extra spaces from the line.
    line = line.strip()
    # Splitting the mapper output using tab.
    curr_file, curr_word_list = line.split('\t',1)
    # Converting the mapper output string to list.
    curr_word_list = ast.literal_eval(curr_word_list.strip())
    # Logic to aggregate the non english words of the same file.
    if prev_file == curr_file:
        prev_word_list.extend(curr_word_list)
    else:
        if prev_file:
            out_dict = {}
            for word in prev_word_list:
                if word in out_dict:
                    out_dict[word] += 1
                else:
                    out_dict[word] = 1
            # Reducer output will be file name and the dictionary containing non-english words with counts
            print(prev_file,'\t',out_dict)
        prev_file = curr_file
        prev_word_list = curr_word_list
if prev_file == curr_file:
        out_dict = {}
        for word in prev_word_list:
            if word in out_dict:
                out_dict[word] += 1
            else:
                out_dict[word] = 1
        print(prev_file,'\t',out_dict)
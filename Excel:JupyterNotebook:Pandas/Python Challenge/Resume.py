#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 22:53:05 2019

@author: Manny
"""

# -*- coding: UTF-8 -*-
"""Resume Analysis Module."""
​
import os
import string
import pandas as pd
import numpy as np
​
# Counter is used later in the program
from collections import Counter
​
# Paths
resume_path = os.path.join(".", "Resources", 'resume.md')
​
# Skills to match
REQUIRED_SKILLS = {"excel", "python", "mysql", "statistics"}
DESIRED_SKILLS = {"r", "git", "html", "css", "leaflet"}
​
# function to load a file
def load_file(resume_path):
    """Helper function to read a file and return the data."""
    with open(resume_path, "r") as resume_file_handler:
        return resume_file_handler.read().lower().split()
​
# Grab the text for a Resume
word_list = load_file(resume_path)
​
# Create a set of unique words from the resume
resume = set()
​
# Remove trailing punctuation from words
for token in word_list:
    resume.add(token.split(',')[0].split('.')[0])
​
# Remove Punctuation that were read as whole words
punctuation = set(string.punctuation)
resume = resume - punctuation
print(resume)
​
# Calculate the Required Skills Match using Set Intersection
print("REQUIRED SKILLS")
print("=============")
print(resume & REQUIRED_SKILLS)
​
​
# Calculate the Desired Skills Match using Set Intersection
print("DESIRED SKILLS")
print("=============")
print(resume & DESIRED_SKILLS)
​
# Resume Word Count
# ==========================
# Initialize a dictionary with default values equal to zero
word_count = {}.fromkeys(word_list, 0)
​
# Loop through the word list and count each word.
for word in word_list:
    word_count[word] += 1
print(word_count)
​
# Using collections.Counter
word_counter = Counter(word_list)
print(word_counter)
​
# Comparing both word count solutions
print(word_count == word_counter)
​
# Top 10 Words
print("Top 10 Words")
print("=============")
​
# Don't worry about the underscore in front of _word_count
# It is just convention for internal use only
# More info here: https://dbader.org/blog/meaning-of-underscores-in-python
​
# Clean Punctuation
_word_count=[]
​
_word_count = {key.rstrip(string.punctuation): item for key, item in word_count.items()}   
    
# Clean Stop Words
df = pd.DataFrame(list(_word_count.items()), columns=['word', 'count'])
​
stop_words = ["i","me","my","myself","we","our","ours","ourselves","you","your","yours","yourself","yourselves","he","him","his","himself","she","her","hers","herself","it","its","itself","they","them","their","theirs","themselves","what","which","who","whom","this","that","these","those","am","is","are","was","were","be","been","being","have","has","had","having","do","does","did","doing","a","an","the","and","but","if","or","because","as","until","while","of","at","by","for","with","about","against","between","into","through","during","before","after","above","below","to","from","up","down","in","out","on","off","over","under","again","further","then","once","here","there","when","where","why","how","all","any","both","each","few","more","most","other","some","such","no","nor","not","only","own","same","so","than","too","very","s","t","can","will","just","don","should","now"]
​
_word_count = {key:item for key,item in _word_count.items() if key not in stop_words}
​
blank = ['']
​
_word_count = {key:item for key,item in _word_count.items() if key not in blank}
​
# Sort words by count and print the top 10
​
for key, value in sorted(_word_count.items()):
    print(key, value)
​
sorted_words = []
k = Counter(_word_count) 
  
# Finding 10 highest values 
print(k.most_common(10))
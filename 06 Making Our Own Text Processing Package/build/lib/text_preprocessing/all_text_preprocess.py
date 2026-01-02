# All text preprocess code is here
import os
import json
import re

import spacy
import unicodedata
from bs4 import BeautifulSoup
from textblob import TextBlob
from spacy.lang.en.stop_words import STOP_WORDS as sw

fpath = os.path.join(os.path.dirname(__file__), 'data/contractions.json')
contractions = json.load(open(fpath))

def word_count(x):
        return len(x.split())

def char_count(x):
        pattern = r'\s'
        return len(re.sub(pattern, '', x))

def avg_word_len(x):
        return char_count(x)/word_count(x)

def stop_words_count(x):
        temp = len([word for word in x.lower().split() if word in sw])
        return temp

def hashtags_count(x):
        return len(re.findall(r'#\w+', x))

def mentions_count(x):
        return len(re.findall(r'@\w+', x))

def numerics_count(x):
        return len(re.findall(r'\b\d+\b', x))

def upper_case_count(x):
        return len([word for word in x.split() if word.isupper()])
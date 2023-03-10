
import re
import unicodedata
import pandas as pd
import nltk
import prepare

import matplotlib.pyplot as plt
import seaborn as sns
 
 
 
 
def basic_clean(string):
    string = string.lower()
    string = unicodedata.normalize('NFKD', 
                          string).encode('ascii', 'ignore').decode('utf-8')
    string = re.sub(r'[^a-z0-9\s]', '', string)
    
    return string


def tokenizer(string):
    tokenize = nltk.tokenize.ToktokTokenizer()
    string = tokenize.tokenize(string)
    return string


def stem(string):
    ps = nltk.porter.PorterStemmer()
    string = [ps.stem(word) for word in string]
    return string


def lemmatizer(string):
    wnl = nltk.stem.WordNetLemmatizer()
    lems = [wnl.lemmatize(word) for word in string]
    return lems


    
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 20:43:29 2016

@author: Gopala Krishna
"""

#Importing Necessary Libraries

import string
import pandas as pd

#Function that cleans the given text
def preprocessing(text):
  exclude = set(string.punctuation)
  text = ''.join(ch for ch in text if ch not in exclude)
  text = text.replace("\n","")
  return text

#Function that creates bi-grams out of the given sentence
def bigrams(text):
    bigrams_list = zip(text.split(" ")[:-1], text.split(" ")[1:])
    return bigrams_list

#This function calculates the frequencies of the bi-grams that are appearing in the given sentence
def collocations_ranking(bigrams_list,word):
    df = pd.DataFrame(bigrams_list,columns=["first","second"])
    counts = pd.DataFrame(df.groupby(["first","second"]).size())
    counts = counts.reset_index()
    counts.columns = ["first","second","counts"]
    sorted_dataframe = counts.sort("counts",ascending=False)
    final = sorted_dataframe[sorted_dataframe["first"] == word].head(3)
    print final

#This is the main function that accepts the word and prints the top 3 collocation words for the given input word
def collocations(word):
    text = '''My name is gopal. His name is John. I like my name very much.'''
    text = preprocessing(text)
    bigrams_list = bigrams(text)
    collocations_ranking(bigrams_list,word)

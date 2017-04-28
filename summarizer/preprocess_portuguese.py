# coding=utf-8
from __future__ import print_function
from __future__ import unicode_literals
import collections
# import copy
import io
import nltk
import re
from sumy._compat import to_unicode
from sumy.nlp.stemmers import Stemmer

def stem(word, LANGUAGE = "portuguese"):
    stemmer = Stemmer(LANGUAGE)
    return stemmer(to_unicode(word).lower())
# from nltk.tokenize import sent_tokenize

# nltk.download('punkt')
stopwords = set()
sentences = []
sentences_processing = []
sentence_dictionary = collections.defaultdict(dict)
# sentence_dictionary1 = collections.defaultdict(dict)
stemWords = {}



def tokenize(filename):
    '''
    Tokenizes the sentences and words
    :param filename: path of the file containing the text to be summarized
    '''
    global sentences, sentences_processing, sentence_dictionary

    with io.open(filename, "r", encoding="utf-8") as inputFile:
        for line in inputFile:
            sentences.append(line)
            sentences_processing.append(line.lower().strip())
        inputFile.close()
    counter = 0
    stemmer = nltk.SnowballStemmer('portuguese')
    for sentence in sentences_processing:
        # print ("sent: "+sentence)
        # sentence = sentence[:-1]
        sentence = re.sub(',|\.|-|\(|\)', ' ', sentence)
        tokens = sentence.split()
        actualTokens = removeStopWords(tokens)
        stemmedTokens = [stem(word) for word in actualTokens]
        # stemmedTokens1 = [stem(word) for word in actualTokens]
        sentence_dictionary[counter] = stemmedTokens
        # sentence_dictionary1[counter] = stemmedTokens1
        counter += 1


def readStopWords():
    '''
    Reads the stopwords from the file
    '''
    with io.open("portuguese_stopwords.txt", encoding='utf-8') as textFile:
        for line in textFile:
            words = line.lower().strip()
            stopwords.add(words)
        textFile.close()


def removeStopWords(wordlist):
    '''
    Removes the stopwords from the sentences
    :param wordlist: list of stopwords
    '''
    newlist = []
    for word in wordlist:
        if word not in stopwords:
            newlist.append(word)
    return newlist



#
# def stemmerPortugese(words):
#     return


def cleanText(filename):
    '''
        Tokenize, Remove stopwords and reduce the words to their stem
    :param filename: path of file to be preprocessed
    '''
    global sentence_dictionary, sentences
    readStopWords()
    tokenize(filename)
    size = 0
    for i in range(0, len(sentence_dictionary)):
        size += len(sentence_dictionary[i])
    sentence_dictionary = {key: value for key, value in sentence_dictionary.items() if len(value)>0}
    # for i in sorted(sentence_dictionary.keys()):
        # print (sentence_dictionary[i])
        # print (sentence_dictionary1[i])
    # print (sentences)
    # print (size)
    return sentence_dictionary, sentences, size


cleanText("/home/akshay/TextSummarizer/Portuguese/documents/20100108_Record_423946.sents")
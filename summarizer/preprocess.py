# coding=utf-8
from __future__ import print_function
from __future__ import print_function
from __future__ import print_function
from __future__ import unicode_literals
import io, nltk, numpy, copy, collections, re, sys
from nltk.tokenize import sent_tokenize

# import sumy
# from sumy.summarizers.lsa import LsaSummarizer as summarizer
nltk.download('punkt')
stopwords = set()
sentences = []
sentences_processing = []
sentence_dictionary = collections.defaultdict(dict)


def tokenize(filename):
    global sentences, sentences_processing, sentence_dictionary
    with io.open(filename, "r", encoding="utf-8") as inputFile:
        data = inputFile.read()
        # sentences = data.strip().split(".")
        inputFile.close()
    # for sentence in sentences:
    #     print sentence
    # # print data
    sentences = sent_tokenize(data)
    sentences_processing = copy.deepcopy(sentences)
    # print("using nltk")
    counter = 0
    for sentence in sentences_processing:
        # print(sentence)
        sentence = sentence[:-1]
        # sentence = re.sub("\d+", "", sentence)
        sentence = re.sub(',|\.|-|\(|\)', ' ', sentence)
        # sentence = re.sub(r'[^\w\s]', ' ', sentence)
        tokens = sentence.strip().split()
        actualTokens = removeStopWords(tokens)
        stemmedTokens = stemmer_mar(actualTokens)
        sentence_dictionary[counter] = stemmedTokens
        counter += 1


def readStopWords():
    with io.open("stopwords.txt", encoding='utf-8') as textFile:
        for line in textFile:
            words = line.lower().strip()
            stopwords.add(words)
        textFile.close()


def removeStopWords(wordlist):
    newlist = []
    for word in wordlist:
        if word not in stopwords:
            newlist.append(word)
    return newlist


def remove_case(word):
    word_length = len(word) - 1
    if word_length > 5:
        suffix = "शया"
        if word.endswith(suffix):
            return word[:-len(suffix)]

    if word_length > 4:
        suffix = "शे"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "शी"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "चा"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "ची"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "चे"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "हून"
        if word.endswith(suffix):
            return word[:-len(suffix)]

    if word_length > 3:
        suffix = "नो"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "तो"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "ने"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "नी"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "ही"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "ते"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "या"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "ला"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "ना"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "ऊण"
        if word.endswith(suffix):
            return word[:-len(suffix)]

    if word_length > 2:
        suffix = " े"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = " ी"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "स"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "ल"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = " ा"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "त"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "म"
        if word.endswith(suffix):
            return word[:-len(suffix)]
    return word


def remove_No_Gender(word):
    word_length = len(word) - 1
    if word_length > 5:
        suffix = " ुरडा"
        if word.endswith(suffix):
            return word[:-len(suffix)]

    if word_length > 4:
        suffix = "ढा"
        if word.endswith(suffix):
            return word[:-len(suffix)]

    if word_length > 3:
        suffix = "रु"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "डे"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "ती"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = " ान"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = " ीण"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "डा"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "डी"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "गा"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "ला"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "ळा"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "या"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "वा"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "ये"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "वे"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "ती"
        if word.endswith(suffix):
            return word[:-len(suffix)]

    if word_length > 2:
        suffix = "अ"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = " े"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "ि "
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = " ु"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = " ौ"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = " ै"
        if word.endswith(suffix):
            return word[:-len(suffix)]

        suffix = " ा"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = " ी"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = " ू"
        if word.endswith(suffix):
            return word[:-len(suffix)]
        suffix = "त"
        if word.endswith(suffix):
            return word[:-len(suffix)]
    return word


def stemmer_mar(words):
    return [remove_No_Gender(remove_case(word)) for word in words]

def cleanText(filename = "input.txt"):
    global sentence_dictionary
    readStopWords()
    tokenize(filename)
    # print("after removing stopwords")
    size = 0
    for i in range(0, len(sentence_dictionary)):
        # print(" ".join(sentence_dictionary[i]))
        size += len(sentence_dictionary[i])
    # print (size)
    return sentence_dictionary, size

cleanText()
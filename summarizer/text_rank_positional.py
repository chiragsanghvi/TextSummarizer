# coding=utf-8
from __future__ import print_function
import collections
import os

import io
import networkx as nx
import math
import operator

import sys

from preprocess import cleanText


def generatepositionaldistribution():
    global nodeHash, sentenceDictionary, sentences, size
    positional_dictionary = collections.defaultdict(dict)
    count = 0
    for i in sentenceDictionary.keys():
        # print(len(sentenceDictionary))
        for j in range(0,len(sentenceDictionary[i])):
            count += 1
            position = float(count)/(float(size) + 1.0)
            positional_dictionary[i][j] = 1.0/(math.pi*math.sqrt(position*(1-position)))
            word = sentenceDictionary[i][j]
            if word in nodeHash:
                if nodeHash[word] < positional_dictionary[i][j]:
                    nodeHash[word] = positional_dictionary[i][j]
            else:
                nodeHash[word] = positional_dictionary[i][j]
    # print(positional_dictionary)
    # for key in nodeHash:
        # print(key + ": " + str(nodeHash[key]))



def textrank():
    global sentenceDictionary, nodeHash, textRank
    graph = nx.Graph()
    graph.add_nodes_from(nodeHash.keys())
    for i in sentenceDictionary.keys():
        for j in range(0, len(sentenceDictionary[i])):
            current_word = sentenceDictionary[i][j]
            next_words = sentenceDictionary[i][j+1:j+window]
            for word in next_words:
                graph.add_edge(current_word,word,weight=(nodeHash[current_word]+nodeHash[word])/2)
    textRank = nx.pagerank(graph,weight='weight')
    keyphrases = sorted(textRank, key=textRank.get,reverse=True)[:n]
    # print("keyphrases")
    # for i in range(len(keyphrases)):
    #     print(keyphrases[i])
    return keyphrases


def summarize(keyphrases, numberofSentences):
    global textRank, sentenceDictionary, sentences
    sentenceScore = {}
    for i in sentenceDictionary.keys():
        position = float(i+1) / (float(len(sentences)) + 1.0)
        # if position == 1.0:
        #     position = 0.99
        positionalFeatureWeight = 1.0 / (math.pi * math.sqrt(position * (1.0 - position)))
        sumKeyPhrases = 0.0
        for keyphrase in keyphrases:
            # if i in sentenceDictionary.keys():
                if keyphrase in sentenceDictionary[i]:
                    sumKeyPhrases += textRank[keyphrase]
        sentenceScore[i] = sumKeyPhrases * positionalFeatureWeight
    sortedSentenceScores = sorted(sentenceScore.items(), key=operator.itemgetter(1),reverse=True)[:numberofSentences]
    sortedSentenceScores = sorted(sortedSentenceScores,key=operator.itemgetter(0),reverse=False)
    # print("Summary: ")
    summary = []
    with io.open("../Marathi/summaries/"+(sys.argv[1]).split('/')[-1]+"_summary_positional","w",encoding='utf-8') as outFile:
        for i in range(0, len(sortedSentenceScores)):
        # try:
            outFile.write(sentences[sortedSentenceScores[i][0]] + "\n")
            # print(sentences[sortedSentenceScores[i][0]])
        # summary.append(sentences[sortedSentenceScores[i][0]])
        # except:
        # return summary
        # return summary


        # for i in range(0, len(sentenceDictionary)):
        #     for j in range(0, len(sentenceDictionary[i])):



window = 10
numberofSentences = 6
# sentenceDictionary, sentences, size = cleanText()
nodeHash = {}
textRank = {}
sentenceDictionary = collections.defaultdict(dict)


if len(sys.argv) > 1:
    # print("file")
    if len(sys.argv) > 3:
        # print("positional")
        sentenceDictionary, sentences, size = cleanText(sys.argv[1])
        # print(len(sentenceDictionary))
        # for i in sentenceDictionary.keys():
            # print(" ".join(sentenceDictionary[i]))
        window = int(sys.argv[3])
        numberofSentences = int(sys.argv[2])
        n = int(math.ceil(min(0.1 * size, 7 * math.log(size))))
        generatepositionaldistribution()
        keyphrases = textrank()
        summarize(keyphrases, numberofSentences)
    else:
        print("not enough parameters")
# else:
#     print("recursive")
#     docsFolder = "/home/akshay/PycharmProjects/Marathi/documents/"
#     for root, dirs, files in os.walk(docsFolder):
#         for filename in files:
#             if filename.endswith(".txt"):
#                 print(filename)
#                 sentenceDictionary = collections.defaultdict(dict)
#                 sentences = []
#                 sentenceDictionary, sentences, size = cleanText(docsFolder+filename)
#                 # print(len(sentenceDictionary))
#                 for i in sentenceDictionary.keys():
#                     print(" ".join(sentenceDictionary[i]))
#                 window = 10
#                 n = int(math.ceil(min(0.1 * size, 7 * math.log(size))))
#                 numberofSentences = 5
#                 generatepositionaldistribution()
#                 keyphrases = textrank()
#                 summarize(keyphrases, numberofSentences)
#










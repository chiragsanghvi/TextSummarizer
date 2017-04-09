# coding=utf-8
from __future__ import print_function
import collections
import networkx as nx
import math
import operator

from preprocess import cleanText

sentenceDictionary, sentences, size = cleanText("input.txt")
window = 2
numberofSentences = 4
n = int(math.ceil(min(0.1*size,7*math.log(size))))
nodeHash = {}
textRank = {}


def generatepositionaldistribution():
    global nodeHash, sentenceDictionary, sentences, size
    positional_dictionary = collections.defaultdict(dict)
    count = 0
    for i in range(0, len(sentenceDictionary)):
        for j in range(0, len(sentenceDictionary[i])):
            count += 1
            position = float(count)/(float(size) + 1.0)
            positional_dictionary[i][j] = 1.0/(math.pi*math.sqrt(position*(1-position)))
            word = sentenceDictionary[i][j]
            if word in nodeHash:
                if nodeHash[word] < positional_dictionary[i][j]:
                    nodeHash[word] = positional_dictionary[i][j]
            else:
                nodeHash[word] = positional_dictionary[i][j]
    print(positional_dictionary)
    for key in nodeHash:
        print(key + ": " + str(nodeHash[key]))


def textrank():
    global sentenceDictionary, nodeHash, textRank
    graph = nx.Graph()
    graph.add_nodes_from(nodeHash.keys())
    for i in range(0,len(sentenceDictionary)):
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
    for i in range(0,len(sentences)):
        position = float(i+1) / (float(len(sentences)) + 1.0)
        positionalFeatureWeight = 1.0 / (math.pi * math.sqrt(position * (1 - position)))
        sumKeyPhrases = 0.0
        for keyphrase in keyphrases:
            if keyphrase in sentenceDictionary[i]:
                sumKeyPhrases += textRank[keyphrase]
        sentenceScore[i] = sumKeyPhrases * positionalFeatureWeight
    sortedSentenceScores = sorted(sentenceScore.items(), key=operator.itemgetter(1),reverse=True)[:numberofSentences]
    sortedSentenceScores = sorted(sortedSentenceScores,key=operator.itemgetter(0),reverse=False)
    print("Summary: ")
    summary = []
    for i in range(0, len(sortedSentenceScores)):
        # try:
        print(sentences[sortedSentenceScores[i][0]])
            # summary.append(sentences[sortedSentenceScores[i][0]])
        # except:
            # return summary
    # return summary

generatepositionaldistribution()
keyphrases = textrank()
summarize(keyphrases, numberofSentences)
# for i in range(0, len(sentenceDictionary)):
#     for j in range(0, len(sentenceDictionary[i])):




import os, collections, math
from collections import defaultdict

docsFolder = "../Marathi/documents/"

for root, dirs, files in os.walk(docsFolder):
    for filename in files:
        print(filename)
        os.system("python text_rank_positional.py " + (docsFolder + filename) + " 5 2")
        print("Positional Done")
        os.system("python text_rank_similarity.py " + (docsFolder + filename))
        print("Similarity Done")


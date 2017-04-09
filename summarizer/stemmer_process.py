import io
import json
from collections import defaultdict

stemwords = defaultdict(dict)

def readStemWords():
    global stemwords

    with io.open("word_list_marathi.txt", encoding='utf-8') as textFile:
        index = 0
        for line in textFile:
            line = line.strip()
            if len(line) > 0:
                index += 1
                wordEndIndex = line.find(">")
                word = line[2:wordEndIndex]



                line = line[wordEndIndex + 1:]
                baseEndIndex = line.find("]")
                base = line[1:baseEndIndex].strip()
                line = line[baseEndIndex + 1:]
                stem = None

                # If there is a stem word for the same
                if len(base) >= 0:
                    stemEndIndex = base.find('-')
                    if stemEndIndex > 0:
                        stem = base[:stemEndIndex]

                line = line[line.find("{") + 1: line.find("}")].strip()
                related = list()

                if len(line) > 0:
                    split = line.split(",")
                    for s in split:
                        related.append(s[:s.find("|")])

                if stem == None and len(related) > 0:
                    stem = related[0]

                if stem != None:
                    stemwords[word] = defaultdict(dict)
                    stemwords[word]["stem"] = stem
                    stemwords[word]["related"] = related


    print(json.dumps(stemwords, sort_keys=True, indent=4))

    with io.open("process_word_list_marathi.txt", "w", encoding="utf-8") as modelFile:
        modelFile.write(json.dumps(unicode(repr(stemwords), 'unicode-escape'), ensure_ascii=False, sort_keys=True, indent=4))

readStemWords()

# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

import os
import sys

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.sum_basic import SumBasicSummarizer
from sumy.summarizers.luhn import LuhnSummarizer
# from sumy.summarizers.edmundson import EdmundsonSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words


LANGUAGE = "portuguese"
SENTENCES_COUNT = 2

if not 1 <= len(sys.argv) <= 3:
    print("You should provide no parameter, 1 or 2 parameters")
    print("Usage: python summarizer.py [optional: file] [optional: algorithm]")
    exit(1)


files_to_summarize = []
# if no algorithm is specified, apply all algorithms
summarizing_algorithms = [LsaSummarizer, TextRankSummarizer, LexRankSummarizer, SumBasicSummarizer, LuhnSummarizer]

if len(sys.argv) == 1:
    for data_folder in ["PT2010-2011", "PT2012-2013"]:
        docs_folder = os.path.join("PriberamCompressiveSummarizationCorpus", data_folder, "docs")

        for root, dirs, files in os.walk(docs_folder):
            for filename in files:
                if filename.endswith(".sents"):
                    file_path = os.path.join(root, filename)
                    files_to_summarize.append(file_path)

else:
    files_to_summarize.append(sys.argv[1])
    if len(sys.argv) == 3:
        chosen_method = sys.argv[2].lower()
        if chosen_method == "lsa": summarizer = LsaSummarizer
        elif chosen_method == "textrank": summarizer = TextRankSummarizer
        elif chosen_method == "lexrank": summarizer = LexRankSummarizer
        elif chosen_method == "sumbasic": summarizer = SumBasicSummarizer
        elif chosen_method == "luhn": summarizer = LuhnSummarizer
        else:
            print("Algorithm should be one of: LexRank, LSA, Luhn, SumBasic, TextRank")
            exit(1)
        # apply user-specified algorithm only
        summarizing_algorithms = []
        summarizing_algorithms.append(summarizer)


files_summarized_count = 0
# for urls
# url = "http://www.zsstritezuct.estranky.cz/clanky/predmety/cteni/jak-naucit-dite-spravne-cist.html"
# parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
# or for plain text files
for file_to_summarize in files_to_summarize:
    filename = file_to_summarize.rsplit('/', 1)[-1]

    # File Analysis - summarization
    parser = PlaintextParser.from_file(file_to_summarize, Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)

    for summarizer in summarizing_algorithms:
        # print(summarizer.__name__, file=f_out)
        method_name = summarizer.__name__
        summarizer = summarizer(stemmer)
        summarizer.stop_words = get_stop_words(LANGUAGE)

        for sentence in summarizer(parser.document, SENTENCES_COUNT):
            summary_destination_folder = os.path.join("generated_summaries", filename + "_" + method_name)
            # print(sentence)
            with open(summary_destination_folder, "w") as f_sum:
                print(sentence, file=f_sum)
        # print(file=f_out)
    # print("------------------------------------------------------------------------------", file=f_out)
    files_summarized_count += 1

print("Total Files summarized: ", files_summarized_count)


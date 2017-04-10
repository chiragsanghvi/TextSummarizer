# AUTOMATED TEXT SUMMARIZATION IN MARATHI AND PORTUGUESE

```

       Akshay Joshi	       Chirag Sanghvi	      Hirak Hemant Modi	           Pablo Garay
      akshayaj@usc.edu         cksanghv@usc.edu        hirakhem@usc.edu    	 garayfer@usc.edu
 ```
# Introduction
With the explosion of information, it is crucial to obtain the most useful information available from many sources. Text summarization seeks to find a reduced description of a document which is useful to satisfy the user’s information needs. Applications of text summarization encompass automatic generation of headlines for news and articles; creation of a meaningful subject line for emails; creating outlines for documents or abstracts for articles. Very little research and work has been done in text summarization for the Indian language Marathi (an Under-Resourced language). Most of the work done focusses on keyword extraction, but doesn’t manage to maintain the sanity of the sentences.
# Method

## Materials
We did not find any suitable corpus in Marathi language so we plan on collecting the articles to be summarized from various Marathi newspaper web sites.
Data used for the processing on the corpus include The EMILLE (Enabling Minority Language Engineering) which includes monolingual, parallel and annotated corpora for Asian Languages including Marathi. Also, the POS tagged word list from the Center for Indian Language resources of IIT Bombay.
In order to evaluate using the methods specified below, a human-made summary is needed. An approach to collect this information collect is using volunteers. Another source is to use the abstracts of articles or the lead of news articles as summaries of the documents.

## Procedure
We propose starting with extractive text summarization algorithms as a base to our work.  In order to accomplish this, we plan on using existing algorithms such as TextRank [4] for keyword extraction, as well as LexRank. Then, we plan to include abstractive text summarization features.
For example, to implement text summarization for the Marathi Language, we will follow three main steps [1]:
* **Preprocessing**: Involves processing the raw text corpus by following processes such as tokenization and stopword removal, while maintaining the sentence structure (the result of this step is a collection of sentences).
* **Stemming and/or lemmatization**: involves reducing the form of a word to its stem/lemma. To accomplish, language-specific knowledge is required. For this we use a rule based Marathi Stemmer.
* **Sentence ranking**: After the document’s text has been processed to a collection of sentences in a normal form (in other words, we have a normalized version of the sentences), the words and sentences are ranked based on selected features (for example, thematic term and position). 

In future feature extraction process, the features like SOV (Subject Object Verb - Experimental) verification, sentence positional value (POS tagging), TF-ISF (Term Frequency/ Inverse Sentence Frequency)  are going to be  used to make the summary more relevant and precise. 

## Evaluation Plan
Qualitatively, the objective is to find a summary grammatically and semantically correct, that is relevant, and that the user can approve (as opposed to disapprove) and/or give a score which constitutes an accepted summary (as opposed to a rejected summary proposal).
Quantitatively, the most common way to evaluate the informativeness of automatic text summaries is to compare them with human-made model summaries. These summaries will be compared with the output of our program using the ROUGE [3] metric. It considers the result of automatic text summarization and human-made summarization and computes the n-gram co-occurrence between them.

## Tools
NLTK, Basic Marathi Rule based stemmer, ROUGE [3]

# References

[1] Virat V. Giri, Dr.M.M. Math & Dr.U.P. Kulkarni, “A Survey of Automatic Text Summarization System for Different Regional Language in India”, In Bonfring International Journal of Software Engineering and Soft Computing, Vol. 6, Special Issue, October 2016 

[2]. Hovy, E., & Lin, C. Y. (1998, October). Automated text summarization and the SUMMARIST system. In Proceedings of a workshop on held at Baltimore, Maryland: October 13-15, 1998 (pp. 197-214). Association for Computational Linguistics.

[3] Lin, C. Y. (2004, July). Rouge: A package for automatic evaluation of summaries. In Text summarization branches out: Proceedings of the ACL-04 workshop (Vol. 8).

[4] Mihalcea, R., & Tarau, P. (2004, July). TextRank: Bringing order into texts. Association for Computational Linguistics.



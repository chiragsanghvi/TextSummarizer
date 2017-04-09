PRIBERAM COMPRESSIVE SUMMARIZATION CORPUS, v1.0
28 March 2014

1) General Information

This corpus contains 801 documents split into 80 topics, each of which has 10 documents (one has 11). The documents are news stories from major Portuguese newspapers, radio and TV stations. Each topic also has two human generated summaries up to 100 words. The human summaries are compressive: the annotators performed only sentence and word deletion operations.

If you use this corpus in your research, please cite the following paper:

"Priberam Compressive Summarization Corpus: A New Multi-Document Summarization Corpus for European Portuguese"
Miguel B. Almeida, Mariana S. C. Almeida, André F. T. Martins, Helena Figueira, Pedro Mendes, Cláudia Pinto
Proceedings of the Language Resources and Evaluation Conference (LREC) 2014, Reykjavik, Iceland

2) File Structure

In the main folder you will find this README alongside two folders:
- PT2010-2011, containing topics 41-80, related to events in the years 2010 and 2011 (topic 58, inside this folder, has 11 documents)
- PT2012-2013, containing topics 01-40, related to events in the years 2012 and 2013

Inside each of those folders you will find two subfolders. One of these subfolders is named "docs", and contains 40 subfolders (one for each topic). Each of those subfolders has a name between "01" and "80", which is the topic number. Within each of those subfolders you'll find 10 files with names such as "20110724_CM_387174", where:
-- 20110724 is the date in YYYYMMDD format
-- CM is the news source (please see the paper for details)
-- 387174 is a document ID
You will also find 10 corresponding files with the same name and the suffix ".sents". These are files with one sentence per line.

The other subfolder is named "summaries" and contains files with names of the format "NN.X", where NN is the topic ID (from 01 to 80) and X is the annotator ID.

3) License

Priberam Compressive Summarization Corpus (c) by Priberam Informática, S.A.

Priberam Compressive Summarization Corpus is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.

You should have received a copy of the license along with this work. If not, see <http://creativecommons.org/licenses/by-nc-sa/4.0/>. 

4) Acknowledgements

Priberam would like to thank Cofina, Controlinveste, and RTP for their collaboration in providing the news articles which were processed in the elaboration of the corpus. This work was partially supported by the EU/FEDER programme, QREN/POR Lisboa (Portugal), under the Discooperio project (contract 2011/18501), and by FCT grant PTDC/EEI-SII/2312/2012.

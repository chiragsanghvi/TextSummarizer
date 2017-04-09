# Creates directory structure with two folders: one for documents, another for summaries.
# For each document, checks if there exists a summary for it.
# If there exists a summary for the document,
# put document in the docs folder and its corresponding summary in the summaries folder
import os
from shutil import copyfile
from collections import Counter


def counterSubset(list1, list2):
    """ Check if all elements in list1 exist in list2 (in the same or more amount) """
    c1, c2 = Counter(list1), Counter(list2)
    for k, n in c1.items():
        if n > c2[k]:
            return False
    return True

def createDirectoryIfNotExists(path):
    """ Creates directory path specified if it doesn't already exist """
    if not os.path.exists(path):
        os.makedirs(path)

main_folder = "PreprocessedSummarizationCorpus"
docs_folder = "docs"
summaries_folder = "summaries"

for path in [main_folder,
             os.path.join(main_folder, "PT2010-2011"),
             os.path.join(main_folder, "PT2012-2013"),
             os.path.join(main_folder, "PT2010-2011", docs_folder),
             os.path.join(main_folder, "PT2010-2011", summaries_folder),
             os.path.join(main_folder, "PT2012-2013", docs_folder),
             os.path.join(main_folder, "PT2012-2013", summaries_folder)
             ]:
    createDirectoryIfNotExists(path)


for data_folder in ["PT2010-2011", "PT2012-2013"]:
# for data_folder in ["PT2010-2011"]:
    path_to_folder = os.path.join("PriberamCompressiveSummarizationCorpus", data_folder)
    path_to_summary_folder = os.path.join(path_to_folder, summaries_folder)

    for summary_filename in os.listdir(path_to_summary_folder):
        path_to_summary_file = os.path.join(path_to_summary_folder, summary_filename)
        (doc, annotator_id) = summary_filename.split(".")
        # print doc, annotator_id

        # Get lines of summary file
        sum_split_lines = []
        sum_original_lines = []
        with open(path_to_summary_file, "rb") as f_sum:
            # lines = f_sum.readlines()
            for line in f_sum:
                line = line.strip()
                # print line
                if line: #check if line not empty
                    sum_original_lines.append(line)
                    sum_split_lines.append(line.split())
        # print sum_lines

        # Analyze document - check if there is a summary for it in summary file
        path_to_doc_folder = os.path.join(path_to_folder, docs_folder, doc)

        for file in os.listdir(path_to_doc_folder):
            if file.endswith(".sents"): # use only files that end with .sents - the rest of files are duplications of these
                path_to_doc_file = os.path.join(path_to_doc_folder, file)

                with open(path_to_doc_file, "rb") as f_doc:
                    doc_text = f_doc.read().split()

                    for index_line in range(len(sum_split_lines)):
                        if counterSubset(sum_split_lines[index_line], doc_text) == True:
                            # print path_to_summary_file, path_to_doc_file
                            # print sum_original_lines[index_line]

                            new_path_to_doc_folder = os.path.join(main_folder, data_folder, docs_folder, doc)
                            new_path_to_summary_folder = os.path.join(main_folder, data_folder, summaries_folder, doc)

                            createDirectoryIfNotExists(new_path_to_doc_folder)
                            createDirectoryIfNotExists(new_path_to_summary_folder)

                            new_path_to_doc_file = os.path.join(new_path_to_doc_folder, file)
                            new_path_to_summary_file = os.path.join(new_path_to_summary_folder, file + "." + annotator_id)

                            # if there exists a summary for this doc, include doc in the folder of docs with summary
                            if not os.path.isfile(new_path_to_doc_file):
                                copyfile(path_to_doc_file, new_path_to_doc_file)

                            # save summary of doc to folder with summaries
                            with open(new_path_to_summary_file, "a+") as f_doc_sum: #need to append as there are docs with two sentences of summary
                                f_doc_sum.write(sum_original_lines[index_line])

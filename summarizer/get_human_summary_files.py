import os
from shutil import copyfile

human_summaries_folder = "human_summaries"

# create folder if not exists
if not os.path.exists(human_summaries_folder):
    os.makedirs(human_summaries_folder)

# count = 0
for data_folder in ["PT2010-2011", "PT2012-2013"]:
    docs_folder = os.path.join("PreprocessedSummarizationCorpus", data_folder, "summaries")

    for root, dirs, files in os.walk(docs_folder):
        for filename in files:
            new_filename = filename[:-2] + "_Human" #remove annotator part and add proper termination
            # count += 1
            file_src_path = os.path.join(root, filename)
            file_dest_path = os.path.join(human_summaries_folder, new_filename)
            # print file_src_path, file_dest_path
            copyfile(file_src_path, file_dest_path)
# print "Num of files", count
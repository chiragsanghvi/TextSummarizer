import os

# LANGUAGE = "Marathi"

def compute_bigrams(text):
    bigrams = [b for l in text for b in zip(l.split(" ")[:-1], l.split(" ")[1:])]
    return bigrams

def compute_bigram_from_file(file_path):
    with open(file_path, "rb") as f:
        text = f.read()
        return compute_bigrams([text])

for language in ["Portuguese", "Marathi"]:
    print language.upper()
    print "------------"

    if language == "Portuguese":
        human_summaries_folder = os.path.join("human_summaries")
        system_summaries_folder = os.path.join("generated_summaries")
        summarizer_types = ["LexRankSummarizer", "LsaSummarizer", "LuhnSummarizer", "SumBasicSummarizer", "TextRankSummarizer"]

    elif language == "Marathi":
        human_summaries_folder = os.path.join("..", "Marathi", "summaries")
        system_summaries_folder = os.path.join("..", "Marathi", "summaries")
        summarizer_types = ["TextRankPositionalSummarizer", "TextRankSimilaritySummarizer"]

    for type_summarizer in summarizer_types:
        avg_rouge_2_score = 0.0
        total_files = 0

        for file_reference in os.listdir(human_summaries_folder):
            reference_summary_file_path = os.path.join(human_summaries_folder, file_reference)
            reference_summary_bigrams = compute_bigram_from_file(reference_summary_file_path)
            # print reference_summary_bigrams

            file_candidate = file_reference.replace("Human", type_summarizer)
            candidate_summary_file_path = os.path.join(system_summaries_folder, file_candidate)
            candidate_summary_bigrams = compute_bigram_from_file(candidate_summary_file_path)

            num_cooccurrences = 0
            for elem in candidate_summary_bigrams:
                if elem in reference_summary_bigrams:
                    num_cooccurrences += 1
            # print candidate_summary_bigrams
            # print reference_summary_bigrams

            # print num_cooccurrences
            # print len(reference_summary_bigrams)

            rouge_2_score = float(num_cooccurrences) / float(len(reference_summary_bigrams))
            # print rouge_2_score

            avg_rouge_2_score += rouge_2_score
            total_files += 1

        avg_rouge_2_score = avg_rouge_2_score / float(total_files)

        print "Method: %s" %type_summarizer
        print "Average ROUGE-2 score", avg_rouge_2_score
        print



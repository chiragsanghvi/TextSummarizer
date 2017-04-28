import os
from pyrouge import Rouge155

r = Rouge155()
path = os.path.join("..", 'Marathi', 'summaries')
# r.model_dir = os.path.join("..", 'Marathi', 'summaries')
# r.system_filename_pattern = 'doc(\d+)_TextRankPositionalSummarizer'
# r.model_filename_pattern = 'doc(\d+)_Human'
# r.system_dir = os.path.join("..", 'Marathi', 'summaries')
# r.model_dir = os.path.join("..", 'Marathi', 'summaries')
# r.system_filename_pattern = 'doc(\d+)_TextRankSimilaritySummarizer'
# r.model_filename_pattern = 'doc(\d+)_Human'
# r.system_dir = 'system_summaries'
# r.model_dir = 'model_summaries'
# r.system_filename_pattern = '(\d+).txt'
# r.model_filename_pattern = '(\d+).txt'

r.system_dir = os.path.join('generated_summaries')
r.model_dir = os.path.join('human_summaries')
method = "TextRankSummarizer"
r.system_filename_pattern = '(\s+)_' + method
r.model_filename_pattern = '(\s+)_Baseline'


output = r.convert_and_evaluate()
# with open("evaluation_results/rouge.txt", "w") as f_eval:
#     f_eval.write(output)
output_dict = r.output_to_dict(output)
print "Rouge-2 F-Score:", output_dict['rouge_2_f_score']

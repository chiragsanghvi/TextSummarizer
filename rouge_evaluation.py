from pyrouge import Rouge155

r = Rouge155()
r.system_dir = 'system_summaries'
r.model_dir = 'model_summaries'
r.system_filename_pattern = '(\d+).txt'
r.model_filename_pattern = '(\d+).txt'

output = r.convert_and_evaluate()
with open("evaluation_results/rouge.txt", "w") as f_eval:
    f_eval.write(output)
output_dict = r.output_to_dict(output)
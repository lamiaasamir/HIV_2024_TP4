from poly_llm.to_test.closest_integer import closest_integer
from poly_llm.common.abstract_executor import AbstractExecutor
from poly_llm.common.prompt_generator import PromptGenerator
from poly_llm.generators.llm_test_generator import LLMTestGenerator
from transformers import AutoTokenizer, T5ForConditionalGeneration
import json
import torch
import importlib
import os

def remove_last_line(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Remove the last line
    lines = lines[:-1]

    with open(filename, 'w') as file:
        file.writelines(lines)



executor = AbstractExecutor(closest_integer)
prompt_generator = PromptGenerator(closest_integer)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model_name = "Salesforce/codet5-large-ntp-py"
tokenizer = AutoTokenizer.from_pretrained(model_name) #tokenizer#AutoTokenizer.from_pretrained("codellama/CodeLlama-7b-Python-hf")#
model = T5ForConditionalGeneration.from_pretrained(model_name).to(device)

llm_generator = LLMTestGenerator(model, tokenizer, closest_integer)
prompt = prompt_generator.generate_prompt()

print(f"THE PROMPT {prompt}")
test, test_name = llm_generator.create_test_function(prompt)


# Writing the Prompt to py file

filename = "test_generated.py"
llm_generator.write_test_to_file(test, filename=filename)

# # As a percaution because sometimes the last line is incomplete
# remove_last_line(filename)

# Milestone to make sure the generated tests are correct
input("Make sure generated tests are correct")

module_name = filename.split(".")[0]
function_name = test_name

# Dynamically import the module
module = importlib.import_module(module_name)
function = getattr(module, function_name)

executor2 = AbstractExecutor(function)

coverage_data = executor2._execute_input(closest_integer)
print(coverage_data)
line_coverage_percentage = (coverage_data['coverage']['covered_lines'] / coverage_data['coverage']['num_statements']) * 100
branch_coverage_percentage = (coverage_data['coverage']['covered_branches'] / coverage_data['coverage']['num_branches']) * 100

if coverage_data['coverage']:
    line_coverage_percentage = (coverage_data['coverage']['covered_lines'] / coverage_data['coverage']['num_statements']) * 100
    branch_coverage_percentage = (coverage_data['coverage']['covered_branches'] / coverage_data['coverage']['num_branches']) * 100
    print(f"For the PUT closest_integer zero shots:\n Line coverage percentage is {round(line_coverage_percentage,4)}%, Branch coverage percentage is {round(branch_coverage_percentage,4)}%")
else:
    print("LLM generated an incorrect test case, please edit the generated tests or rerun")



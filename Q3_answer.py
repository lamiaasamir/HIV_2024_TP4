from transformers import AutoTokenizer, T5ForConditionalGeneration
from poly_llm.common.abstract_executor import AbstractExecutor
from poly_llm.common.prompt_generator import PromptGenerator
from poly_llm.generators.llm_test_generator import LLMTestGenerator
from coverage import Coverage
import importlib.util
import os
import torch
import re

# Functions to test
from poly_llm.to_test.closest_integer import closest_integer
from poly_llm.to_test.file_name_check import file_name_check
from poly_llm.to_test.find_closest_elements import find_closest_elements
from poly_llm.to_test.numerical_letter_grade import numerical_letter_grade
from poly_llm.to_test.separate_paren_groups import separate_paren_groups

# Assuming these are the functions to be tested
functions_to_test = [closest_integer, file_name_check, find_closest_elements, numerical_letter_grade, separate_paren_groups]

functions_to_test_and_paths = [
    (closest_integer, "poly_llm/to_test/closest_integer.py"),
    (file_name_check, "poly_llm/to_test/file_name_check.py"),
    (find_closest_elements, "poly_llm/to_test/find_closest_elements.py"),
    (numerical_letter_grade, "poly_llm/to_test/numerical_letter_grade.py"),
    (separate_paren_groups, "poly_llm/to_test/separate_paren_groups.py"),
]


file_paths = {
    "closest_integer.py": "poly_llm/to_test/closest_integer.py",
    "file_name_check.py": "poly_llm/to_test/file_name_check.py",
    "find_closest_elements.py": "poly_llm/to_test/find_closest_elements.py",
    "numerical_letter_grade.py": "poly_llm/to_test/numerical_letter_grade.py",
    "separate_paren_groups.py": "poly_llm/to_test/separate_paren_groups.py",
}

model_name = "Salesforce/codet5p-770m-py"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

for func,func_path in functions_to_test_and_paths:
    # Instantiate the prompt generator and executor
    prompt_generator = PromptGenerator(func)
    executor = AbstractExecutor(func)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    llm_generator = LLMTestGenerator(model, tokenizer, func)
    
    file_contents = {}
    file_name=func.__name__+".py"

    with open(func_path, 'r') as file:
        file_contents[file_name] = file.read()   
    # print(file_name, "\n", file_contents)
    content=file_contents[file_name]

    extracted_asserts = {}

    # Extract all lines containing 'assert'
    # print("content\n",content)
    asserts = re.findall(r"assert .+", content)
    extracted_asserts[file_name] = '\n'.join(asserts)

    fewshot_examples=[extracted_asserts[file_name]]

    # print("fewshot_examples\n",fewshot_examples)

    # Generate the prompt and the test
    prompt = prompt_generator.generate_prompt(fewshot_examples)
    print(f"THE PROMPT {prompt}")
    test_code, test_name = llm_generator.create_test_function(prompt)

    # Save the generated test to a file
    filename = f"test_fewshots_newModel_{func.__name__}.py"
    llm_generator.write_test_to_file(test_code, filename=filename)
    input("Make sure generated tests are correct")

    # Setup coverage measurement
    # cov = Coverage(source=[os.path.dirname(func_path)])
    # cov.start()
    
    module_name = filename.split(".")[0]
    function_name = test_name
    module = importlib.import_module(module_name)
    test_func = getattr(module, function_name)
  
    executor2 = AbstractExecutor(test_func)
    coverage_data = executor2._execute_input(func)
    print(coverage_data)

    if coverage_data['coverage']:
        covered_lines = coverage_data['coverage']['covered_lines']
        num_statements = coverage_data['coverage']['num_statements']
        # missing_lines = coverage_data['coverage']['missing_lines']
        excluded_lines = coverage_data['coverage']['excluded_lines']

        # Adjusting total executable lines by subtracting excluded lines
        total_executable_lines = num_statements - excluded_lines

        # Calculating adjusted line coverage percentage
        line_coverage_percentage = (covered_lines / total_executable_lines) * 100

        total_branches = coverage_data['coverage']['num_branches'] 
        total_covered_branches=coverage_data['coverage']['covered_branches'] + 0.5 * coverage_data['coverage']['num_partial_branches']
        branch_coverage_percentage = (total_covered_branches / total_branches) * 100

        print(f"For the PUT {str(func.__name__)} few shots with a new model: \n  Line coverage percentage is {round(line_coverage_percentage,4)}%, Branch coverage percentage is {round(branch_coverage_percentage,4)}%")
    else:
        print("LLM generated an incorrect test case, please edit the generated tests or rerun")



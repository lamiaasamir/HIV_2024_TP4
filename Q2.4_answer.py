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

few_shot_examples = {
    "closest_integer.py": [
        ["assert closest_integer(\"10\") == 10\n"],
        ["assert closest_integer(\"14.5\") == 15\n"],
        ["assert closest_integer(\"10\") == 10\n", "assert closest_integer(\"14.5\") == 15\n"],
    ],
    "file_name_check.py": [
        ["assert file_name_check(\"example.txt\") == 'Yes'\n"],
        ["assert file_name_check(\"1example.dll\") == 'No'\n", "assert file_name_check('.txt') == 'No'\n"],
        ["assert file_name_check(\"example.txt\") == 'Yes'\n", "assert file_name_check('.txt') == 'No'\n"],
    ],
    "find_closest_elements.py": [
        ["assert find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) == (3.9, 4.0)\n"],
        ["assert find_closest_elements([1.0, 2.0, 5.9, 4.0, 5.0]) == (5.0, 5.9)\n"],
        ["assert find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) == (3.9, 4.0)\n", "assert find_closest_elements([1.0, 2.0, 5.9, 4.0, 5.0]) == (5.0, 5.9)\n"],
    ],
    "numerical_letter_grade.py": [
        ["assert numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'B', 'C-', 'C', 'A-']\n"],
        ["assert numerical_letter_grade([1.2]) == ['D+']\n"],
        ["assert numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'B', 'C-', 'C', 'A-']\n", "assert numerical_letter_grade([1.2]) == ['D+']\n"],
    ],
    "separate_paren_groups.py": [
        ["assert separate_paren_groups('(()()) ((())) () ((())()())') == ['(()())', '((()))', '()', '((())()())']\n"],
        ["assert separate_paren_groups('() (()) ((())) (((())))') == ['()', '(())', '((()))', '(((())))']\n"],
        ["assert separate_paren_groups('(()()) ((())) () ((())()())') == ['(()())', '((()))', '()', '((())()())']\n", "assert separate_paren_groups('() (()) ((())) (((())))') == ['()', '(())', '((()))', '(((())))']\n"],
    ],
}

# Assuming these are the functions to be tested
functions_to_test = [closest_integer, file_name_check, find_closest_elements, numerical_letter_grade, separate_paren_groups]

functions_to_test_and_paths = [
    (closest_integer, "poly_llm/to_test/closest_integer.py"),
    (file_name_check, "poly_llm/to_test/file_name_check.py"),
    (find_closest_elements, "poly_llm/to_test/find_closest_elements.py"),
    (numerical_letter_grade, "poly_llm/to_test/numerical_letter_grade.py"),
    (separate_paren_groups, "poly_llm/to_test/separate_paren_groups.py"),
]


# file_paths = {
#     "closest_integer.py": "poly_llm/to_test/closest_integer.py",
#     "file_name_check.py": "poly_llm/to_test/file_name_check.py",
#     "find_closest_elements.py": "poly_llm/to_test/find_closest_elements.py",
#     "numerical_letter_grade.py": "poly_llm/to_test/numerical_letter_grade.py",
#     "separate_paren_groups.py": "poly_llm/to_test/separate_paren_groups.py",
# }



model_name = "Salesforce/codet5-large-ntp-py"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name).to(torch.device("cuda" if torch.cuda.is_available() else "cpu"))

for func, func_path in functions_to_test_and_paths:
    prompt_generator = PromptGenerator(func)
    executor = AbstractExecutor(func)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    llm_generator = LLMTestGenerator(model, tokenizer, func)
    
    file_name = func.__name__ + ".py"
    few_shot_prompts = few_shot_examples.get(file_name, [])
    i=0
    for few_shot_prompt in few_shot_prompts:
        # Generate the prompt with few-shot example
        prompt = prompt_generator.generate_prompt([few_shot_prompt])
        examples_length=len(few_shot_prompt)
        print(f"THE PROMPT for fewshot technique of examples length = {examples_length} {prompt}")
        test_code, test_name = llm_generator.create_test_function(prompt)

        # Save the generated test to a file
        filename = f"test_different_fewshots{i}_length{examples_length}_{func.__name__}.py"
        i+=1
        with open(filename, 'w') as f:
            f.write(test_code)
        print(f"Generated test saved as {filename}")
        input("Review the generated test file. Press Enter to continue...")
        
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

            print(f"For the PUT {str(func.__name__)} different few shots with examples length = {examples_length}:\n  Line coverage percentage is {round(line_coverage_percentage,4)}%, Branch coverage percentage is {round(branch_coverage_percentage,4)}%")
        else:
            print("LLM generated an incorrect test case, please edit the generated tests or rerun")

        # # Cleanup
        # os.remove(filename)


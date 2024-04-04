from poly_llm.common.abstract_executor import AbstractExecutor
from poly_llm.common.prompt_generator import PromptGenerator
from poly_llm.generators.llm_test_generator import LLMTestGenerator
from transformers import AutoTokenizer, T5ForConditionalGeneration
import torch
import os
import importlib.util
from coverage import Coverage
import json
# Initialize the LLM (example with CodeT5)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model_name = "Salesforce/codet5-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name).to(device)

# Functions under test
from poly_llm.to_test import closest_integer, file_name_check, find_closest_elements, numerical_letter_grade, separate_paren_groups
functions = [closest_integer, file_name_check, find_closest_elements, numerical_letter_grade, separate_paren_groups]



# Initialize the LLM (example with CodeT5)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model_name = "Salesforce/codet5-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name).to(device)

# Functions under test
from poly_llm.to_test import closest_integer, file_name_check, find_closest_elements, numerical_letter_grade, separate_paren_groups
functions = [closest_integer, file_name_check, find_closest_elements, numerical_letter_grade, separate_paren_groups]
def measure_initial_coverage(function):
    executor = AbstractExecutor(function)
    return executor._execute_input()
def generate_tests_and_measure_coverage(function, test_type="zero_shot", few_shot_examples=None):
    prompt_generator = PromptGenerator(function)
    if test_type == "few_shot" and few_shot_examples:
        prompt = prompt_generator.generate_prompt(few_shot_examples)
    else:
        prompt = prompt_generator.generate_prompt()
    
    llm_generator = LLMTestGenerator(model, tokenizer, function)
    test_code = llm_generator.generate_assertions(prompt)
    
    # Write the test code to a temporary Python file
    temp_test_file = f"temp_test_{function.__name__}.py"
    with open(temp_test_file, "w") as file:
        file.write(test_code)
    
    # Dynamically execute the test file and measure coverage
    coverage_result = dynamic_test_execution_and_coverage(temp_test_file)
    
    # Cleanup
    os.remove(temp_test_file)
    
    return coverage_result

def dynamic_test_execution_and_coverage(test_file_path):
    # Create a coverage object and start coverage measurement
    cov = Coverage()
    cov.start()
    
    # Dynamically execute the test file
    spec = importlib.util.spec_from_file_location("module.name", test_file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    # Stop coverage measurement and save the report
    cov.stop()
    cov.save()
    report = {}
    cov.report(file=open('coverage_report.txt', 'w'), show_missing=True)  # Example to generate a text report
    with open('coverage.json', 'r') as f:
        report = json.load(f)
    
    return report["totals"]
def extract_few_shot_examples(function):
    # Implement logic based on provided steps or use existing test functions
    return ["Example assertion 1", "Example assertion 2"]  # Example return value
# Measure initial coverage for all functions
initial_coverages = {func.__name__: measure_initial_coverage(func) for func in functions}

# Generate tests and measure coverage using zero-shot
zero_shot_coverages = {func.__name__: generate_tests_and_measure_coverage(func, "zero_shot") for func in functions}

# Extract few-shot examples, generate tests, and measure coverage using few-shot
few_shot_examples = {func.__name__: extract_few_shot_examples(func) for func in functions}
few_shot_coverages = {func.__name__: generate_tests_and_measure_coverage(func, "few_shot", few_shot_examples[func.__name__]) for func in functions}

# Compare and report the coverage results
print("Initial Coverages:", initial_coverages)
print("Zero-shot Coverages:", zero_shot_coverages)
print("Few-shot Coverages:", few_shot_coverages)

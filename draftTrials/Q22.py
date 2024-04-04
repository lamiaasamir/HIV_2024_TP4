from poly_llm.common.abstract_executor import AbstractExecutor
from poly_llm.common.prompt_generator import PromptGenerator
from poly_llm.generators.llm_test_generator import LLMTestGenerator
from transformers import AutoTokenizer, T5ForConditionalGeneration
import torch
import importlib.util
import os
from coverage import Coverage
import re
import inspect

# Functions to test
from poly_llm.to_test.closest_integer import closest_integer
from poly_llm.to_test.file_name_check import file_name_check
from poly_llm.to_test.find_closest_elements import find_closest_elements
from poly_llm.to_test.numerical_letter_grade import numerical_letter_grade
from poly_llm.to_test.separate_paren_groups import separate_paren_groups

# Test functions
from poly_llm.to_test.closest_integer import test_closest_integer
from poly_llm.to_test.file_name_check import test_file_name_check
from poly_llm.to_test.find_closest_elements import test_find_closest_elements
from poly_llm.to_test.numerical_letter_grade import test_numerical_letter_grade
from poly_llm.to_test.separate_paren_groups import test_separate_paren_groups


def extract_test_assertions(function):
    """
    Extracts test assertions from a given function's file.
    """
    # Get the source file of the function
    src_file = inspect.getsourcefile(function)
    
    test_assertions = []
    with open(src_file, "r") as file:
        content = file.read()
        
        # Regex to find the test function for the specific PUT
        pattern = rf"def test_{function.__name__}\(\):.*?# pragma: no cover"
        matches = re.findall(pattern, content, re.DOTALL)
        
        if matches:
            # Extract assertions from the first match
            assertions = re.findall(r"(assert .+)", matches[0])
            test_assertions.extend(assertions)
            
    return "\n".join(test_assertions)

# Initialize the model and tokenizer
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model_name = "Salesforce/codet5-large-ntp-py"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name).to(device)

# Define the Python file to write tests to
filename = "test_generated.py"

function_testFunction_dict={
    closest_integer: test_closest_integer,
    file_name_check: test_file_name_check,
    find_closest_elements: test_find_closest_elements,
    numerical_letter_grade: test_numerical_letter_grade,
    separate_paren_groups: test_separate_paren_groups
    }


def measure_initial_coverage(function, test_function):
    # Initialize coverage measurement
    cov = Coverage(branch=True)
    cov.start()
    
    # Execute the test function directly
    test_function()
    
    cov.stop()  # Stop coverage measurement
    cov.save()
    data = cov.get_data()
    
    return data
def generate_and_execute_tests(function, few_shot_examples=None):
    prompt_generator = PromptGenerator(function)
    prompt = prompt_generator.generate_prompt(few_shot_examples=few_shot_examples)
    llm_generator = LLMTestGenerator(model, tokenizer, function)
    test_code, test_name = llm_generator.create_test_function(prompt)
    
    # Write test code to a Python file
    llm_generator.write_test_to_file(test_code, filename=filename)
    
    # Dynamically execute the test file and measure coverage
    return dynamic_test_execution_and_coverage(filename)

def dynamic_test_execution_and_coverage(test_file_path):
    spec = importlib.util.spec_from_file_location("generated_tests", test_file_path)
    module = importlib.util.module_from_spec(spec)
    cov = Coverage(branch=True)
    cov.start()
    spec.loader.exec_module(module)  # Execute the loaded module, which contains the test
    cov.stop()
    cov.save()
    cov.html_report(directory='coverage_reports')  # Save the report to a directory

# Prepare for dynamic test execution and coverage measurement
few_shot_examples = {func.__name__: extract_test_assertions(func) for func in function_testFunction_dict.keys()}

print(few_shot_examples)
few_shot_examples = {
    'closest_integer': ['''assert closest_integer("10") == 10\n
    assert closest_integer("14.5") == 15\n''']
    }

# Measure initial coverage, generate tests, and measure coverage again
initial_coverages = {}
zero_shot_coverages = {}
few_shot_coverages = {}
for func, test_func in function_testFunction_dict.items():
    # Measure initial coverage (considering any pre-existing tests if applicable)
    initial_coverages[func.__name__] = measure_initial_coverage(func, test_func)

    # Generate and execute tests using zero-shot and few-shot techniques
    zero_shot_coverages[func.__name__] = generate_and_execute_tests(func)
    few_shot_coverages[func.__name__] = generate_and_execute_tests(func, few_shot_examples=[few_shot_examples[func.__name__]])

# Compare coverages and print results
print("Initial Coverages:", initial_coverages)
print("Zero-shot Coverages:", zero_shot_coverages)
print("Few-shot Coverages:", few_shot_coverages)

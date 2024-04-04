from poly_llm.common.abstract_executor import AbstractExecutor
from poly_llm.common.prompt_generator import PromptGenerator
from poly_llm.generators.llm_test_generator import LLMTestGenerator
from transformers import AutoTokenizer, T5ForConditionalGeneration
import json
import torch
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

#model intialization
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model_name = "Salesforce/codet5-large-ntp-py"
tokenizer = AutoTokenizer.from_pretrained(model_name) #tokenizer#AutoTokenizer.from_pretrained("codellama/CodeLlama-7b-Python-hf")#
model = T5ForConditionalGeneration.from_pretrained(model_name).to(device)


# Python file to write tests to
filename = "test_generated.py"

functions = [closest_integer, file_name_check, find_closest_elements, numerical_letter_grade, separate_paren_groups]
test_functions =[test_closest_integer, test_file_name_check, test_find_closest_elements, test_numerical_letter_grade, test_separate_paren_groups]

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

def measure_initial_coverage(function):
    executor = AbstractExecutor(function)
    return executor._execute_input() #return coverage data

def generate_and_execute_tests(function, few_shot_examples=None):
    prompt_generator = PromptGenerator(function)
    prompt = prompt_generator.generate_prompt(few_shot_examples=few_shot_examples)
    llm_generator = LLMTestGenerator(model, tokenizer, function)
    test, test_name = llm_generator.create_test_function(prompt)
    llm_generator.write_test_to_file(test,filename=filename)
    
    # Re-measure coverage after generating new tests
    executor = AbstractExecutor(function)
    return executor._execute_input() 

# Step 1: Measure initial coverage
initial_coverages = {func.__name__: measure_initial_coverage(func) for func in test_functions}

# Step 2: Generate and execute tests using zero-shot technique
zero_shot_coverages = {func.__name__: generate_and_execute_tests(func) for func in functions}

# Step 3: Generate and execute tests using few-shot technique
# Generate the few_shot_examples dictionary
few_shot_examples = {func.__name__: [extract_test_assertions(func)] for func in functions}

few_shot_examples = {
    'closest_integer': ['''assert closest_integer("10") == 10\n
    assert closest_integer("14.5") == 15\n''']
    }

few_shot_coverages = {func.__name__: generate_and_execute_tests(func, few_shot_examples.get(func.__name__)) for func in functions}

# Step 4: Compare coverages and print results
print("Initial Coverages:", json.dumps(initial_coverages, indent=2))
print("Zero-shot Coverages:", json.dumps(zero_shot_coverages, indent=2))
print("Few-shot Coverages:", json.dumps(few_shot_coverages, indent=2))

# Further analysis and comparison of coverages would follow here






from transformers import AutoTokenizer, T5ForConditionalGeneration
from poly_llm.common.abstract_executor import AbstractExecutor
from poly_llm.common.prompt_generator import PromptGenerator
from poly_llm.generators.llm_test_generator import LLMTestGenerator
from coverage import Coverage
import importlib.util
import os
import torch

# Functions to test
from poly_llm.to_test.closest_integer import closest_integer
from poly_llm.to_test.file_name_check import file_name_check
from poly_llm.to_test.find_closest_elements import find_closest_elements
from poly_llm.to_test.numerical_letter_grade import numerical_letter_grade
from poly_llm.to_test.separate_paren_groups import separate_paren_groups

functions_to_test_and_paths = [
    (closest_integer, "poly_llm/to_test/closest_integer.py"),
    (file_name_check, "poly_llm/to_test/file_name_check.py"),
    (find_closest_elements, "poly_llm/to_test/find_closest_elements.py"),
    (numerical_letter_grade, "poly_llm/to_test/numerical_letter_grade.py"),
    (separate_paren_groups, "poly_llm/to_test/separate_paren_groups.py"),
]

model_name = "Salesforce/codet5-large-ntp-py"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)
model.to(torch.device("cuda" if torch.cuda.is_available() else "cpu"))

for func, func_path in functions_to_test_and_paths:
    prompt_generator = PromptGenerator(func)
    llm_generator = LLMTestGenerator(model, tokenizer, func)

    # Generate the prompt and the test
    prompt = prompt_generator.generate_prompt()
    test_code, test_name = llm_generator.create_test_function(prompt)

    # Save the generated test to a file
    filename = f"test_{func.__name__}.py"
    with open(filename, 'w') as f:
        f.write(test_code)
    print(f"Generated test saved as {filename}")
    input("Review the generated test. Press Enter to continue...")

    # Setup coverage measurement specifically for the PUT file
    cov = Coverage(source=[func_path])
    
    # Dynamically load the generated test module and execute the test function
    spec = importlib.util.spec_from_file_location("test_module", filename)
    test_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(test_module)
    test_func = getattr(test_module, test_name)

    # Execute the test function
    try:
        test_func()
    except Exception as e:
        print(f"An error occurred while executing {test_name}: {e}")


    print(f"\nCoverage report for {func.__name__}:")
    cov.report()

    # Optionally, generate an HTML report for detailed analysis
    cov.html_report(directory=f"coverage_reports/{func.__name__}")

    # Clean up
    # os.remove(filename)


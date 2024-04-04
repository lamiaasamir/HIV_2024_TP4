from poly_llm.to_test.find_closest_elements import find_closest_elements
from poly_llm.common.abstract_executor import AbstractExecutor
from poly_llm.common.prompt_generator import PromptGenerator
from poly_llm.generators.llm_test_generator import LLMTestGenerator
from transformers import AutoTokenizer, T5ForConditionalGeneration
import torch
import importlib
import os
from coverage import Coverage

# Initialize your model and tokenizer here (assuming they're already defined)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model_name = "Salesforce/codet5-large-ntp-py"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name).to(device)

# Define the path to the function under test (PUT)
put_path = 'poly_llm/to_test/find_closest_elements.py'

# Initialize the classes for generating tests
executor = AbstractExecutor(find_closest_elements)
prompt_generator = PromptGenerator(find_closest_elements)
llm_generator = LLMTestGenerator(model, tokenizer, find_closest_elements)

# Generate a prompt and the test code using LLM
prompt = prompt_generator.generate_prompt()
test_code = llm_generator.generate_assertions(prompt)

# Define where to write the generated test
filename = "test_generated.py"

# Write the test code to a file
with open(filename, "w") as file:
    file.write(test_code)

# Dynamically import and execute the generated test, measuring coverage
def execute_test_and_measure_coverage():
    # Specify the modules or files to include in the coverage analysis
    cov = Coverage(branch=True, include=[put_path])
    cov.start()

    # Dynamically import the module containing the generated test
    module_name = os.path.splitext(filename)[0]
    spec = importlib.util.spec_from_file_location(module_name, filename)
    generated_test_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(generated_test_module)

    cov.stop()  # Stop coverage measurement

    # Save the coverage report to a file and display the report
    cov.save()
    print("Coverage Report:")
    cov.report()

execute_test_and_measure_coverage()

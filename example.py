
from poly_llm.to_test.file_name_check import file_name_check
from poly_llm.common.abstract_executor import AbstractExecutor
from poly_llm.common.prompt_generator import PromptGenerator
from poly_llm.generators.llm_test_generator import LLMTestGenerator
from transformers import AutoTokenizer, T5ForConditionalGeneration
import json
from coverage import Coverage
import importlib
if __name__ == '__main__':
    # Create an instance of the AbstractExecutor class
    #executor = AbstractExecutor(parse_nested_parens)
    executor = AbstractExecutor(file_name_check)
    prompt_generator = PromptGenerator(file_name_check)
    
    model_name = "Salesforce/codet5-large-ntp-py"
    tokenizer = AutoTokenizer.from_pretrained(model_name) #tokenizer#AutoTokenizer.from_pretrained("codellama/CodeLlama-7b-Python-hf")#
    model = T5ForConditionalGeneration.from_pretrained(model_name) 

    llm_generator = LLMTestGenerator(model, tokenizer, file_name_check)
    prompt = prompt_generator.generate_prompt()

    '''few_shot_examples=[def test_file_name_check(): \n 
    assert file_name_check("example.txt") == 'Yes'  \n
    assert file_name_check("1example.dll") == 'No' \n]'''

    print(prompt)
    test, test_name = llm_generator.create_test_function(prompt)
    print(test)
    filename = "test_generated.py"

    llm_generator.write_test_to_file(test, filename=filename)

    module_name = filename.split(".")[0]
    function_name = test_name

    # Dynamically import the module
    module = importlib.import_module(module_name)
    function = getattr(module, function_name)

    executor2 = AbstractExecutor(function)

    coverage_date = executor2._execute_input(file_name_check)
    print(coverage_date)

    '''

    inputs = [
        "example.txt",
        "1example.dll",
        's1sdf3.asd',
        'K.dll',
        'MY16FILE3.exe',
        'His12FILE94.exe',
        '_Y.txt',
        '?aREYA.exe',
        '/this_is_valid.dll',
        'this_is_valid.wow',
    ]

    # Execute the inputs and print the results
    for input in inputs:
        #exceptions, execution_time, coverage = executor._execute_input(input)
        coverage_date = executor._execute_input(input)
        print(coverage_date)
    '''
 


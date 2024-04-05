from poly_llm.to_test.file_name_check import test_file_name_check
from poly_llm.to_test.closest_integer import test_closest_integer
from poly_llm.to_test.find_closest_elements import test_find_closest_elements
from poly_llm.to_test.numerical_letter_grade import test_numerical_letter_grade
from poly_llm.to_test.separate_paren_groups import test_separate_paren_groups

from poly_llm.common.abstract_executor import AbstractExecutor
from poly_llm.common.prompt_generator import PromptGenerator
from poly_llm.generators.llm_test_generator import LLMTestGenerator
from transformers import AutoTokenizer, T5ForConditionalGeneration
import json
import torch
import importlib

executor = AbstractExecutor(test_closest_integer)
coverage_data = executor._execute_input()
# print(coverage_data)

line_coverage_percentage = (coverage_data['coverage']['covered_lines'] / coverage_data['coverage']['num_statements']) * 100
branch_coverage_percentage = (coverage_data['coverage']['covered_branches'] / coverage_data['coverage']['num_branches']) * 100

print(f"For the PUT closest_integer:\n Line coverage percentage is {round(line_coverage_percentage,4)}%, Branch coverage percentage is {round(branch_coverage_percentage,4)}%")

executor = AbstractExecutor(test_file_name_check)
coverage_data = executor._execute_input()
# print(coverage_data)
line_coverage_percentage = coverage_data['coverage']['percent_covered']
        
#calculating branch coverage
total_branches = coverage_data['coverage']['num_branches'] 
total_covered_branches=coverage_data['coverage']['covered_branches'] + 0.5 * coverage_data['coverage']['num_partial_branches']
branch_coverage_percentage = (total_covered_branches / total_branches) * 100

print(f"For the PUT file_name_check:\n Line coverage percentage is {round(line_coverage_percentage,4)}%, Branch coverage percentage is {round(branch_coverage_percentage,4)}%")



executor = AbstractExecutor(test_find_closest_elements)
coverage_data = executor._execute_input()
# print(coverage_data)

line_coverage_percentage = coverage_data['coverage']['percent_covered']
        
#calculating branch coverage
total_branches = coverage_data['coverage']['num_branches'] 
total_covered_branches=coverage_data['coverage']['covered_branches'] + 0.5 * coverage_data['coverage']['num_partial_branches']
branch_coverage_percentage = (total_covered_branches / total_branches) * 100
 
print(f"For the PUT find_closest_elements:\n Line coverage percentage is {round(line_coverage_percentage,4)}%, Branch coverage percentage is {round(branch_coverage_percentage,4)}%")


executor = AbstractExecutor(test_numerical_letter_grade)
coverage_data = executor._execute_input()
# print(coverage_data)

line_coverage_percentage = coverage_data['coverage']['percent_covered']
        
#calculating branch coverage
total_branches = coverage_data['coverage']['num_branches'] 
total_covered_branches=coverage_data['coverage']['covered_branches'] + 0.5 * coverage_data['coverage']['num_partial_branches']
branch_coverage_percentage = (total_covered_branches / total_branches) * 100

print(f"For the PUT numerical_letter_grade:\n Line coverage percentage is {round(line_coverage_percentage,4)}%, Branch coverage percentage is {round(branch_coverage_percentage,4)}%")


executor = AbstractExecutor(test_separate_paren_groups)
coverage_data = executor._execute_input()
# print(coverage_data)

line_coverage_percentage = coverage_data['coverage']['percent_covered']
        
#calculating branch coverage
total_branches = coverage_data['coverage']['num_branches'] 
total_covered_branches=coverage_data['coverage']['covered_branches'] + 0.5 * coverage_data['coverage']['num_partial_branches']
branch_coverage_percentage = (total_covered_branches / total_branches) * 100

print(f"For the PUT separate_paren_groups:\n Line coverage percentage is {round(line_coverage_percentage,4)}%, Branch coverage percentage is {round(branch_coverage_percentage,4)}%")




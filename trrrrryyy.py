import re
file_paths = {
    "closest_integer.py": "poly_llm/to_test/closest_integer.py",
    "file_name_check.py": "poly_llm/to_test/file_name_check.py",
    "find_closest_elements.py": "poly_llm/to_test/find_closest_elements.py",
    "numerical_letter_grade.py": "poly_llm/to_test/numerical_letter_grade.py",
    "separate_paren_groups.py": "poly_llm/to_test/separate_paren_groups.py",
}
file_contents = {}

for file_name, path in file_paths.items():
    with open(path, 'r') as file:
        file_contents[file_name] = file.read()   
    # print(file_name, "\n", file_contents)

extracted_asserts = {}

for file_name, content in file_contents.items():
    # Extract all lines containing 'assert'
    asserts = re.findall(r"assert .+", content)
    extracted_asserts[file_name] = '\n'.join(asserts)

for x in extracted_asserts.keys():
    print(x,"\n",extracted_asserts[x])
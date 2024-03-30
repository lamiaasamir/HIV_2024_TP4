def test_file_name_check(file_name_check):
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("1example.dll") == 'No'
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("1example.dll") == 'No'
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("1example.dll") == 'No'
def test_file_name_check(file_name_check):
    assert file_name_check('test.txt') == 'Yes'
    assert file_name_check('test.exe') == 'Yes'
    assert file_name_check('test.dll') == 'Yes'
    assert file_name_check('test.txt.exe') == 'Yes'
    assert file_name_check('test.txt.dll') == 'Yes'
    assert file_name_check('test.exe.dll') == 'Yes'
    assert file_name_check('test.exe.txt') == 'Yes'
    assert file_name_check('test.exe.txt.exe') == 'Yes'
    assert file_name_check('test.exe.txt.dll') == 'Yes'
    assert file_name_check('test.exe.txt.exe.dll') == 'Yes'
    assert file_name_check('test.exe.txt.exe.txt.exe.dll') == 'Yes'
def test_file_name_check(file_name_check):
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("1example.dll") == 'No'
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("1example.dll") == 'No'
    assert file_name_check("example.txt") == 'Yes'
def test_file_name_check(file_name_check):
    assert file_name_check('test.txt') == 'Yes'
    assert file_name_check('test.exe') == 'Yes'
    assert file_name_check('test.dll') == 'Yes'
    assert file_name_check('test.txt.exe') == 'Yes'
    assert file_name_check('test.txt.dll') == 'Yes'
    assert file_name_check('test.exe.dll') == 'Yes'
    assert file_name_check('test.exe.txt') == 'Yes'
    assert file_name_check('test.exe.txt.exe') == 'Yes'
    assert file_name_check('test.exe.txt.dll') == 'Yes'
    assert file_name_check('test.exe.txt.exe.dll') == 'Yes'
    assert file_name_check('test.exe.txt.exe.txt.exe.dll') == 'Yes'
def test_file_name_check(file_name_check):
    assert file_name_check('test.txt') == 'Yes'
    assert file_name_check('test.exe') == 'Yes'
    assert file_name_check('test.dll') == 'Yes'
    assert file_name_check('test.txt.exe') == 'Yes'
    assert file_name_check('test.txt.dll') == 'Yes'
    assert file_name_check('test.exe.dll') == 'Yes'
    assert file_name_check('test.exe.txt') == 'Yes'
    assert file_name_check('test.exe.txt.exe') == 'Yes'
    assert file_name_check('test.exe.txt.dll') == 'Yes'
    assert file_name_check('test.exe.txt.exe.dll') == 'Yes'
    assert file_name_check('test.exe.txt.exe.txt.exe.dll') == 'Yes'
def test_file_name_check(file_name_check):
    assert file_name_check('test.txt') == 'Yes'
    assert file_name_check('test.exe') == 'Yes'
    assert file_name_check('test.dll') == 'Yes'
    assert file_name_check('test.txt.exe') == 'Yes'
    assert file_name_check('test.txt.dll') == 'Yes'
    assert file_name_check('test.exe.dll') == 'Yes'
    assert file_name_check('test.exe.txt') == 'Yes'
    assert file_name_check('test.exe.txt.exe') == 'Yes'
    assert file_name_check('test.exe.txt.dll') == 'Yes'
    assert file_name_check('test.exe.txt.exe.dll') == 'Yes'
    assert file_name_check('test.exe.txt.exe.txt.exe.dll') == 'Yes'
def test_file_name_check(file_name_check):
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("1example.dll") == 'No'
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("1example.dll") == 'No'
    assert file_name_check("example.txt") == 'Yes'
def test_file_name_check(file_name_check):
    assert file_name_check('test.txt') == 'Yes'
    assert file_name_check('test.exe') == 'Yes'
    assert file_name_check('test.dll') == 'Yes'
    assert file_name_check('test.txt.exe') == 'Yes'
    assert file_name_check('test.txt.dll') == 'Yes'
    assert file_name_check('test.exe.dll') == 'Yes'
    assert file_name_check('test.exe.txt') == 'Yes'
    assert file_name_check('test.exe.txt.exe') == 'Yes'
    assert file_name_check('test.exe.txt.dll') == 'Yes'
    assert file_name_check('test.exe.txt.exe.dll') == 'Yes'
    assert file_name_check('test.exe.txt.exe.txt.exe.dll') == 'Yes'
def test_file_name_check(file_name_check):
    assert file_name_check('test.txt') == 'Yes'
    assert file_name_check('test.exe') == 'Yes'
    assert file_name_check('test.dll') == 'Yes'
    assert file_name_check('test.txt.exe') == 'Yes'
    assert file_name_check('test.txt.dll') == 'Yes'
    assert file_name_check('test.exe.dll') == 'Yes'
    assert file_name_check('test.exe.txt') == 'Yes'
    assert file_name_check('test.exe.txt.exe') == 'Yes'
    assert file_name_check('test.exe.txt.dll') == 'Yes'
    assert file_name_check('test.exe.txt.exe.dll') == 'Yes'
    assert file_name_check('test.exe.txt.exe.txt.exe.dll') == 'Yes'
def test_find_closest_elements(find_closest_elements):
    assert find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) == (3.9, 4.0)
    assert find_closest_elements([1.0, 2.0, 5.9, 4.0, 5.0]) == (5.0, 5.9)
    assert find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) == (3.9, 4.0)
    assert find_closest_elements([1.0, 2.0, 5.9, 4.0, 5.0]) == (5.0, 5.9)
    assert find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) == (3.9, 4.0)
def test_numerical_letter_grade(numerical_letter_grade):
    assert numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'B', 'C-', 'C', 'A-']
    assert numerical_letter_grade([1.2]) == ['D+']
    assert numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'B', 'C-', 'C', 'A-']
def test_closest_integer(closest_integer):
    assert closest_integer("10") == 10
    assert closest_integer("14.5") == 15
    assert closest_integer("10") == 10
    assert closest_integer("14.5") == 15
def test_closest_integer(closest_integer):
    assert closest_integer("10") == 10
    assert closest_integer("0.5") == 1
    assert closest_integer("-14.5") == -15
    assert closest_integer("-0.5") == -1
    assert closest_integer("14.5") == 15
    assert closest_integer("0") == 0
def test_closest_integer(closest_integer):
    assert closest_integer("10") == 10
    assert closest_integer("14.5") == 15
    assert closest_integer("0.5") == 1
    assert closest_integer("-14.5") == -15
    assert closest_integer("-0.5") == -1
def test_closest_integer(closest_integer):
    assert closest_integer("10") == 10
    assert closest_integer("14.5") == 15
    assert closest_integer("10") == 10
    assert closest_integer("14.5") == 15
def test_closest_integer(closest_integer):
    assert closest_integer("10") == 10
    assert closest_integer("14.5") == 15
    assert closest_integer("10") == 10
    assert closest_integer("14.5") == 15
def test_closest_integer(closest_integer):
    assert closest_integer("10") == 10
    assert closest_integer("14.5") == 15
    assert closest_integer("-14.5") == -15
    assert closest_integer("-0.5") == -1
def test_file_name_check(file_name_check):
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("1example.dll") == 'No'
    assert file_name_check('.txt') == 'No'
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("1example.dll") == 'No'
    assert file_name_check('.txt') == 'No'
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("1example.dll") == 'No'
    assert file_name_check('.txt') == 'No'
def test_file_name_check(file_name_check):
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("1example.dll") == 'No'
    assert file_name_check('.txt') == 'No'
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("1example.dll") == 'No'
    assert file_name_check('.txt') == 'No'
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("1example.dll") == 'No'
    assert file_name_check('.txt') == 'No'

 

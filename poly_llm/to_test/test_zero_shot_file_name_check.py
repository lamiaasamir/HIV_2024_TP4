import pytest
from file_name_check import file_name_check
# Assuming your code is in module named "mycode"
# Replace "<module>" with the actual name of your module

@pytest.mark.parametrize('filename,expected', [
    ('example.txt', 'Yes'),
    ('1example.dll', 'No'),
    ('hello.exe', 'Yes'),
    ('abcde.pdf', 'No'),
    ('123456789.doc', 'No'),
    ('123.txt', 'Yes'),
    ('exampl etxt', 'No'),
    ('example..txt', 'No'),
    ('example', 'No'),
    ('123.txt', 'Yes'),
    ('123.tXt', 'No'),
    ('123.TXT', 'No'),
    ('123.Exe', 'No'),
    ('123.EXE', 'No'),
])
def test_validity(filename, expected):
    assert file_name_check(filename) == expected
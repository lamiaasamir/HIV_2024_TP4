def test_file_name_check(file_name_check):
    assert file_name_check('example.exe.dll') == 'No'
    assert file_name_check('example.exe') == 'Yes'
    assert file_name_check('example.txt') == 'Yes'
    assert file_name_check('example.exe.dll') == 'No'


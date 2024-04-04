def test_file_name_check(file_name_check):
    assert file_name_check('test.txt') == 'Yes'
    assert file_name_check('test.exe') == 'Yes'
    assert file_name_check('test.txt.dll') == 'No'
    assert file_name_check('test.exe.dll') == 'No'


def test_file_name_check(file_name_check):
    assert file_name_check('test.txt') == 'Yes'
    assert file_name_check('test.exe') == 'Yes'
    assert file_name_check('test.txt.dll') == 'No'
    assert file_name_check('test.exe.dll') == 'No'
    assert file_name_check('test.dll') == 'Yes'
    assert file_name_check('test.txt.exe') == 'No'
    assert file_name_check('test.txt.dll') == 'No'
    assert file_name_check('test.exe.txt') == 'No'
    assert file_name_check('test.exe.txt.exe.txt.exe.dll') == 'No'
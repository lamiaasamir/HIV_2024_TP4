import unittest
from file_name_check import file_name_check
class FileNameCheckerTest(unittest.TestCase):
    """Tests for the `file_name_check` function."""
    def test_valid_names(self):
        """Test names that meet all requirements."""
        self.assertEqual(file_name_check('example.txt'), 'Yes')
        self.assertEqual(file_name_check('myFile.exe'), 'Yes')
        self.assertEqual(file_name_check('helloWorld.dll'), 'Yes')
    def test_invalid_characters(self):
        """Test invalid characters at the beginning of the filename."""
        self.assertEqual(file_name_check('#test.txt'), 'No')
        self.assertEqual(file_name_check('@image.jpg'), 'No')
        self.assertEqual(file_name_check('/home/user/.bashrc'), 'No')
    def test_no_extension(self):
        """Test filenames with missing extensions."""
        self.assertEqual(file_name_check('filename'), 'No')
        self.assertEqual(file_name_check('anotherFile.'), 'No')
    def test_multiple_extensions(self):
        """Test filenames with multiple dots."""
        self.assertEqual(file_name_check('document.doc.pdf'), 'No')
        self.assertEqual(file_name_check('archive..tar'), 'No')
    def test_wrong_order(self):
        """Test filenames where extension comes first."""
        self.assertEqual(file_name_check('.pngImage'), 'No')
        self.assertEqual(file_name_check('.mp3Song'), 'No')
    def test_too_many_digits(self):
        """Test filenames with too many consecutive digits."""
        self.assertEqual(file_name_check('file12345.zip'), 'No')
        self.assertEqual(file_name_check('pic09876.gif'), 'No')
    def test_empty_beginning(self):
        """Test filenames starting with an empty part."""
        self.assertEqual(file_name_check('.config'), 'No')
        self.assertEqual(file_name_check('.profile'), 'No')
    def test_missing_dot(self):
        """Test filenames with missing dots."""
        self.assertEqual(file_name_check('texttxt'), 'No')
        self.assertEqual(file_name_check('exedll'), 'No')

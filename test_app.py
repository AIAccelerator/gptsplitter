import unittest
import app
from unittest.mock import patch, MagicMock

class TestApp(unittest.TestCase):
    @patch('app.st')
    def test_pdf_upload(self, mock_st):
        mock_st.file_uploader.return_value = MagicMock(type='application/pdf')
        with open('example.pdf', 'rb') as f:
            mock_st.file_uploader.return_value.getvalue.return_value = f.read()
        app.main()
        # TODO: Add assertions based on the expected behavior of app.main()

    @patch('app.st')
    def test_doc_upload(self, mock_st):
        mock_st.file_uploader.return_value = MagicMock(type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        with open('example.docx', 'rb') as f:
            mock_st.file_uploader.return_value.getvalue.return_value = f.read()
        app.main()
        # TODO: Add assertions based on the expected behavior of app.main()

if __name__ == '__main__':
    unittest.main()

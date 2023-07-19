import unittest
from file_handler import PDFHandler, DocHandler

class TestFileHandler(unittest.TestCase):
    def test_pdf_handler(self):
        handler = PDFHandler()
        with open('example.pdf', 'rb') as file:
            content = handler.read(file)
        self.assertIsNotNone(content)
        # Add more assertions based on the expected content of example.pdf

    def test_doc_handler(self):
        handler = DocHandler()
        with open('example.docx', 'rb') as file:
            content = handler.read(file)
        self.assertIsNotNone(content)
        # Add more assertions based on the expected content of example.docx

if __name__ == '__main__':
    unittest.main()

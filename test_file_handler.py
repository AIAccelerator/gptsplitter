import unittest
from file_handler import PDFHandler, DocHandler

class TestFileHandler(unittest.TestCase):
    def test_pdf_handler(self):
        handler = PDFHandler()
        # TODO: Add tests for PDFHandler

    def test_doc_handler(self):
        handler = DocHandler()
        # TODO: Add tests for DocHandler

if __name__ == '__main__':
    unittest.main()

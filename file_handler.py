
import PyPDF2
import docx
import pandas as pd

class FileHandler:
    def read(self, file):
        raise NotImplementedError

class PDFHandler(FileHandler):
    def __init__(self):
        import PyPDF2

    def read(self, file):
        reader = PyPDF2.PdfReader(file)
        content = ""
        for page in range(len(reader.pages)):
            content += reader.pages[page].extract_text()
        return content

class DocHandler(FileHandler):
    def __init__(self):
        import docx

    def read(self, file):
        doc = docx.Document(file)
        content = "\n".join([paragraph.text for paragraph in doc.paragraphs])
        return content
class TextFileHandler:
    def read(self, file):
        return file.read()

class XlsHandler(FileHandler):
    def __init__(self):
        import pandas as pd

    def read(self, file):
        df = pd.read_excel(file)
        return df.to_string()
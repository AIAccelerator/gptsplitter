
import PyPDF2
import docx

class FileHandler:
    def read(self, file):
        raise NotImplementedError

class PDFHandler(FileHandler):
    def __init__(self):
        import PyPDF2

    def read(self, file):
        reader = PyPDF2.PdfFileReader(file)
        content = ""
        for page in range(reader.getNumPages()):
            content += reader.getPage(page).extractText()
        return content

class DocHandler(FileHandler):
    def __init__(self):
        import docx

    def read(self, file):
        doc = docx.Document(file)
        content = "\n".join([paragraph.text for paragraph in doc.paragraphs])
        return content
class FileHandler:
    def read(self, file):
        raise NotImplementedError

class PDFHandler(FileHandler):
    def __init__(self):
        import PyPDF2

    def read(self, file):
        reader = PyPDF2.PdfFileReader(file)
        content = ""
        for page in range(reader.getNumPages()):
            content += reader.getPage(page).extractText()
        return content

class DocHandler(FileHandler):
    def __init__(self):
        import docx

    def read(self, file):
        doc = docx.Document(file)
        content = "\n".join([paragraph.text for paragraph in doc.paragraphs])
        return content

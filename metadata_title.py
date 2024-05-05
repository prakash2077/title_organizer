from PyPDF2 import PdfReader


def read_title(path):
    reader = PdfReader(path)
    title = reader.metadata.title
    return title


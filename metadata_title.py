from PyPDF2 import PdfReader


# extract title from metadata
def read_title(path):
    reader = PdfReader(path)
    title = reader.metadata.title
    return title


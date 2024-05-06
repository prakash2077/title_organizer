import os
import metadata_title


def clean_title(name):
    if name:
        invalid_chars = list(r'\:*?"<>|/')
        for char in invalid_chars:
            if char in name:
                name = name.replace(char, ' ')
    return name


pdfs = os.listdir('PDFs')

for pdf in pdfs:
    title = metadata_title.read_title(f'PDFs/{pdf}')
    title = clean_title(title)
    print(title)
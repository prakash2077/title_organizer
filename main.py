# for files
import os
# extract metadata title
import metadata_title

# filter out invalid characters in the name
def clean_title(name):
    if name:
        invalid_chars = list(r'\:*?"<>|/')
        for char in invalid_chars:
            if char in name:
                name = name.replace(char, ' ')
    return name

# get all pdfs
pdfs = os.listdir('PDFs')

# print title for all pdfs
for pdf in pdfs:
    title = metadata_title.read_title(f'PDFs/{pdf}')
    title = clean_title(title)
    print(title)
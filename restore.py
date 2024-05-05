import os
import shutil

pdfs = os.listdir('Backup')
shutil.rmtree('PDFs')
os.mkdir('PDFs')
for pdf in pdfs:
    path = r'Backup/' + pdf
    shutil.copy(src=path, dst='PDFs')
import os
import shutil

# list pdfs from backup
pdfs = os.listdir('Backup')
# delete the directory PDFs
shutil.rmtree('PDFs')

os.mkdir('PDFs')

# restore files from backup folder
for pdf in pdfs:
    path = r'Backup/' + pdf
    shutil.copy(src=path, dst='PDFs')
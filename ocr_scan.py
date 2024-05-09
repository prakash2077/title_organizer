# Importing the os module to perform file operations
import os
# Importing the pytesseract module to extract text from images
import pytesseract as tess
# Importing the Image module from the PIL package to work with images
from PIL import Image
# Importing the convert_from_path function from the pdf2image module to convert PDF files to images
from pdf2image import convert_from_path


path = r'C:\Users\Prakash\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
#This function takes a PDF file name as input and returns the name of the text file that contains the extracted text.
def read_pdf(file_name):
    # Store all pages of one file here:
    pages = []

    try:
        # Convert the PDF file to a list of PIL images:
        images = convert_from_path(file_name, 500, poppler_path=r"C:\Users\Prakash\Downloads\Compressed\Release-24.02.0-0\poppler-24.02.0\Library\bin")

        # Extract text from each image:
        for i, image in enumerate(images):
          # Generating filename for each image
            filename = "page_" + str(i) + "_" + os.path.basename(file_name) + ".jpeg"
            image.save(filename, "JPEG")
          # Saving each image as JPEG
            tess.pytesseract.tesseract_cmd = path
            text = tess.image_to_string(Image.open(filename))  # Extracting text from each image using pytesseract
            pages.append(text)
          # Appending extracted text to pages list

    except Exception as e:
        print(str(e))

    # Write the extracted text to a file:
    # output_file_name = os.path.splitext(file_name)[0] + ".txt"  # Generating output file name
    # with open(output_file_name, "w") as f:
    #     f.write("\n".join(pages))
      # Writing extracted text to output file

    return pages

#print function returns the final converted text
# pdf_file = "Computer Science_removed.pdf"
pdf_file = "siva.pdf"
print(read_pdf(pdf_file))
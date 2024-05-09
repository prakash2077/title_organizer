from PyPDF2 import PdfReader

reader = PdfReader('PDFs/Computer Science.pdf')

page = reader.pages[0]

def visitor_body(text, cm, tm, fontDict, fontSize):
    y = tm[5]
    if y>50 and y<720:
        print(text)
        font_name = fontDict.get('/BaseFont')
        if font_name:
            font_name = font_name[1:]  # Remove the leading '/'
        else:
            font_name = "Unknown Font"
        print(font_name)
page.extract_text(visitor_text=visitor_body)

# print(text)
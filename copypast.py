import pytesseract
from PIL import Image

img = Image.open('снимок.png')
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


text = pytesseract.image_to_string(img, lang='rus')
print(text)
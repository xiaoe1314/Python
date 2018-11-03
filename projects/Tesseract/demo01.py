import pytesseract
from PIL import Image


pytesseract.pytesseract.tesseract_cmd = r"E:\Software\TesseractOCR\tesseract.exe"

image = Image.open('e.jpg')

text = pytesseract.image_to_string(image, lang='eng')

print(text)


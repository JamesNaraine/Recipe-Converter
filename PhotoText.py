from PIL import Image
import pytesseract 

# import tesseract 
pytesseract.pytesseract.tesseract_cmd = r'<"C:\Users\Lucas\Desktop\New Stuff\VS\Recipe-Converter\Tesseract-OCR\tesseract.exe">'
# pytesseract.pytesseract.tesseract_cmd = r'<C:\Users\Lucas\AppData\Local\Programs\Tesseract-OCR\tesseract.exe>'

# tessdata_dir_config = '--tessdata-dir "C:\Program Files\Tesseract-OCR\tessdata"'

image = Image.open(r"C:\Users\Lucas\Desktop\New Stuff\VS\Recipe-Converter\Images\20240409_122721.jpg")


text = pytesseract.image_to_string(image)
print(text)
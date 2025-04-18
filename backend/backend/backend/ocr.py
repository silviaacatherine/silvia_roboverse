import pytesseract
from PIL import Image
import io

def extract_text_from_image(file):
    img = Image.open(io.BytesIO(file.read()))
    text = pytesseract.image_to_string(img)
    return text.strip()

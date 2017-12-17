try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract
import numpy as np

class ImageToStringConverter():
    def __init__(self):
        pytesseract.pytesseract.tesseract_cmd = 'C:\\Tesseract-OCR\\tesseract.exe' #TODO create conf file or input parameter
        pass

    def convert_to_text(self, image):
        if type(image) is np.ndarray:
            image = Image.fromarray(image)
        return pytesseract.image_to_string(image)
import cv2
from image_to_string_converter import ImageToStringConverter
import string_to_google as g
from translator import GoogleTranslator
import re

cap = cv2.VideoCapture(0)

if (cap.isOpened() == False):
    print("Error opening video stream or file")

ret, frame = cap.read()

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('Frame', frame)
        # Press Q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    else:
        break

converter = ImageToStringConverter()
menustring = (converter.convert_to_text(frame))
print (menustring)

lines = menustring.split('\n')
for line in lines:

    translator= GoogleTranslator()
    line = re.sub(r'[^A-Za-z0-9]+', ' ', line)
    translated_text= translator.translate(line)

    print(translated_text)

    g.search_google_image(translated_text + ' food')



cap.release()
cv2.destroyAllWindows()
import cv2
from image_to_string_converter import ImageToStringConverter
import string_to_google as g
import translated_menu_builder as menu_buil
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

print ("String from image: {}".format(menustring))

lines = menustring.split('\n')

line_to_image = []

for line in lines:
    translator= GoogleTranslator()
    line = re.sub(r'[^A-Za-z0-9]+', ' ', line)
    translated_text= translator.translate(line)

    print(translated_text)

    if (len(translated_text.strip()) > 0):
        image_path = g.search_google_image(translated_text + ' food')
        line_to_image.append([image_path, translated_text])

if len(line_to_image) > 0:
    new_menu = menu_buil.build_translated_menu(line_to_image)
else:
    print ("No text found!")

cap.release()
cv2.destroyAllWindows()
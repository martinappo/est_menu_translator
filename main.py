import cv2
from image_to_string_converter import ImageToStringConverter

cap = cv2.VideoCapture(1)

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
print converter.convert_to_text(frame)

cap.release()
cv2.destroyAllWindows()
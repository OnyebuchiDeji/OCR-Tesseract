import pytesseract
import PIL.Image
import cv2

"""
    PSM 11 is best for non-uniformly structured text on images.
    Likewise for 12.

    PSM 6 is best for uniformly-structured text
    Because of this, the below config worked well with the uniformly structured `text_image.png`
"""

myconfig = r"--psm 6 --oem 3"

text = pytesseract.image_to_string(PIL.Image.open("./res/text_image.png"), config=myconfig)

with open("app_1-text_image_png.txt", "w") as wfs:
    wfs.write(text)

print(text)
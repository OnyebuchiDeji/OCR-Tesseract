"""
    Demonstrating drawing boxes around whole words instead of just the characters only

    Throughout the demonstration, none of the page segmentation modes worked on `text_image_2_1.jpg` (or `text_image_2.jpeg`)
    
    Also, oem 2 does not work. Neither did it work for NeuralNine during his demonstration.
"""


import pytesseract
from pytesseract import Output
import cv2

myconfig = r"--psm 6 --oem 2"


# img = cv2.imread("./res/text_image.png")
# img = cv2.imread("./res/letter-to-santa-claus.png")
# img = cv2.imread("./res/text_image_1.png")
# img = cv2.imread("./res/text_image_4.jpg")
img = cv2.imread("./res/text_image_2_1.jpg")

height, width, _ = img.shape
"""
    image_to_data is used
"""
data = pytesseract.image_to_data(img, config=myconfig, output_type=Output.DICT)

# print("Data Only:\n", data, "\n")
# print("Keys:\n", data.keys(), "\n")
#   prints all the detected text
# print("Data Text:\n", data['text'], "\n")

amount_of_boxes = len(data['text'])

for i in range(amount_of_boxes):
    """
        by increasing the confidence, it makes detection stricter ensuring only actual words are discovered
        From observation, the confidence checks if the word detexted is an actual word. A confidence above 80 removes
        words detected that are either incomplete or poorly interpreted or that it thinks are not actual words.

        For example, Logo brand names are not actual dictionary words. A high threshold may remove such words.

        But for certain more complicated images, like `text_image_1.png`, having a low confidence works better.
    """
    if float(data['conf'][i]) > 80:
        (x, y, width, height) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
        #   draw a rect around the text
        img = cv2.rectangle(img, (x, y), (x + width, y + height), (0, 255, 0), 2)
        #   Add recognized text
        img = cv2.putText(img, data['text'][i], (x, y + height + 20),
                          cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2, cv2.LINE_AA)



cv2.imshow("img", img)
cv2.waitKey(0)


"""
    Demonstrates drawing rectangles around detected text

    Observations:
    
    1.  For the `text_image.png`, because its text is uniform, psm 6 works better as it detects all characters
        compared to psm 11.
    2.  The first demonstration draws rectangles around each text detected.
    3.  psm 6 also works well for `handwritten3.jpg` and `handwritten4.jpg`
    4.  Neither work well for `handwritten6.jpg` because of the cursive writing style.
    5.  psm 6 and 11 work very well for `letter-to-santa-claus.png`
"""

import pytesseract
import cv2

myconfig = r"--psm 6 --oem 3"

# img = cv2.imread("./res/text_image.png")
# img = cv2.imread("./res/handwritten3.jpg")
# img = cv2.imread("./res/handwritten4.jpg")
img = cv2.imread("./res/letter-to-santa-claus.png")
height, width, _ = img.shape
"""
    Output is several lines like these:
        character <upper_left_corner_coord> <lower_left_corner_coord> <unknown_last_datum>
"""
boxes = pytesseract.image_to_boxes(img, config=myconfig)

print(boxes)

for box in boxes.splitlines():
    box = box.split(" ")
    #   color is bgr
    img = cv2.rectangle(img, (int(box[1]), height - int(box[2])), (int(box[3]), height - int(box[4])), (0, 255, 0), 2)

cv2.imshow("img", img)
cv2.waitKey(0)
####    Date: Sunday 14th September, 2025


####    Demonstrating the use of Tesseract with the Comand Line and Listing other Useful Information

1.  Extract text and output to command line:

    `tesseract text_image_1.png stdout`

2.  Using Page Segmentation Modes:
    `tesseract text_image_3.png stdout --psm 11`

3.  Using OCR Engine Modes:
    `tesseract text_image_3.png stdout --psm 11 --ocr 2`

4.  Specifying language:
    E.g. To find German words:
    `tesseract text_image_3.png stdout -l deu`

####    Page Segmentation Modes:

0.  Orientation and Script Detction (OSD) only.
1.  Automatic Page Segmentation with OSD
2.  Automatic Page Segmentation, but no OSD or OCR
3.  Fully Automatic Page Segmentation, but no OSD. (Default)
4.  Assume a single column of text of variable size.
5.  Assume a single uniform block of vertically aligned text
6.  Assume a single uniform block of text
7.  Treat the image as a single text line,
8.  Treat the image as a single word
9.  Treat the image as a single word in a circle
10. Treat the image as a single character
11. Sparse text. Find as much text as possible in no particular order.
12. Sparse text with OSD.
13. Raw Line. Treat the image as a single text line, bypassing hacks that are Tesseract-specific,


####    OCR Engine Modes:
0.  Legact Engine only
1.  Neural nets LSTM (Long-Short-Term Memory) only
2.  Legacy + LSTM engines
3.  Default, based on what is available.
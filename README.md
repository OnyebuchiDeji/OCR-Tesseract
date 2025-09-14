### Date: Sunday 14th September, 2025


#   Extract Text From Images in Python (OCR) using Tesseract

### Reference
**Extract Text From Images in Python (OCR), 2022, NeuralNine [Youtube]**


### Install Tesseract for Windows:
1.  Go to GitHub: https://github.com/tesseract-ocr/tesseract?tab=readme-ov-file
2.  In the README:
    +   Scroll to Installing Tesseract
    +   Click You can either [Install Tesseract via pre-built binary package](https://tesseract-ocr.github.io/tessdoc/Installation.html)
    +   Scroll down to Windows section and click on link *Installer for Windows for Tesseract 3.05, Tesseract 4 and Tesseract 5 are available from Tesseract at 
        [UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki), Or choose any version you want.
    +   Click the download link for the Tesseract installer:
        ```The latest installers can be downloaded here:
                [tesseract-ocr-w64-setup-5.5.0.20241111.exe (64 bit)](https://github.com/tesseract-ocr/tesseract/releases/download/5.5.0/tesseract-ocr-w64-setup-5.5.0.20241111.exe)
        ``` 
3.  Once installed, go to the install location and add that location path to the PAth environment variable
    +   In additon, in the Tesseract-OCR folder, there is the `tessdata` folder; create a completely new environment variable
        and name it `TESSDATA_PREFIX` and link it to that `tessdata`

4.  Now, in your project directory or computer's global environment, install `Pytesseract` using `pip install pytesseract`


### Date Finished: Sunday 14th September, 2025
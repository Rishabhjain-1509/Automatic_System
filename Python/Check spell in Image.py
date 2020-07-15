# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 14:44:34 2020

@author: Rishabh Jain
"""


# Import modules
from PIL import Image
import pytesseract


# Include tesseract executable in your path
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Rishabh Jain\AppData\Local\Tesseract-OCR\tesseract.exe"

# Create an image object of PIL library
image = Image.open('image.png')

# pass image into pytesseract module
# pytesseract is trained in many languages
image_to_text = pytesseract.image_to_string(image, lang='eng')

# Print the text
print(image_to_text)

data = image_to_text.split()

print(data)



from spellchecker import SpellChecker
 
spell = SpellChecker()
 
# find those words that may be misspelled
misspelled = spell.unknown(data)
 
for word in misspelled:
    # Get the one `most likely` answer
    print(spell.correction(word))
 
    # Get a list of `likely` options
    print(spell.candidates(word))   

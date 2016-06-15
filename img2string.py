try:
    import Image
except ImportError:
    from PIL import Image

import pytesseract

text = pytesseract.image_to_string(Image.open('test.jpg'))

# print text.strip()

data = text.split(" ")
print data

# for i in range(0, 160):
#     print text[i]
# print i


# print(pytesseract.image_to_string(Image.open('test-european.jpg'), lang='fra'))

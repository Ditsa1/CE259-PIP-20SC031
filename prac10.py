# 20CS031 - DITSA MANDANI
# Repo. Link - https://github.com/Ditsa1/CE259-PIP-20SC031

import img2pdf
from PIL import Image

# importing the image file
imp_path = "C:/Users/Ditsa/Desktop/sem3result.png"

# creating a pdf file
pdf_path = "C:/Users/Ditsa/Desktop/sem3result.pdf"

image = Image.open(imp_path)

# creating a pdf from the image
pdf_bytes = img2pdf.convert(image.filename)

# opening file
file = open(pdf_path, "wb")

# writing file
file.write(pdf_bytes)

# closing the image
image.close()

# closing the file
file.close()

print("Success - PDF created.")

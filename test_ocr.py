# import pytesseract
# from PIL import Image
# import cv2

# # Configuración de Tesseract OCR
# pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'  # Ajusta la ruta si es necesario

# # Cargar y preprocesar la imagen
# def preprocess_image(image_path):
#     img = cv2.imread(image_path, cv2.IMREAD_COLOR)
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convertir a escala de grises
#     img = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]  # Binarización
#     return img

# # Ruta de la imagen
# image_path = 'datasets/datosv2.jpeg'
# img = preprocess_image(image_path)

# # Extraer el texto
# texto = pytesseract.image_to_string(img, lang='spa')

# # Mostrar el texto
# print("Texto extraído:")
# print(texto)


import easyocr
import pandas as pd

# Cargar el modelo de EasyOCR
reader = easyocr.Reader(['es'])  # Modelo para español

# Ruta de la imagen
image_path = 'datasets/datosv2.jpeg'

# Leer texto de la imagen
results = reader.readtext(image_path)

# Mostrar los resultados
data = []
for result in results:
    print(f"Texto detectado: {result[1]}")
    data.append(result[1])

# Guardar los resultados como texto plano
with open('datasets/texto_extraido.txt', 'w') as f:
    f.write('\n'.join(data))

print("Texto extraído guardado en 'texto_extraido.txt'")

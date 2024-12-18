from PIL import Image
import pytesseract
import pandas as pd
import numpy as np

# Configuración de Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'  # Ajusta la ruta si es necesario

# Función para extraer texto y coordenadas normalizadas
def get_text_and_coordinates(image_path):
    image = Image.open(image_path)
    width, height = image.size  # Dimensiones de la imagen

    # Extraer datos OCR con coordenadas
    ocr_data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT, lang="spa")

    # Lista para almacenar las palabras y sus coordenadas normalizadas
    words_data = []

    for i in range(len(ocr_data['text'])):
        word = ocr_data['text'][i].strip()
        if word:
            x = (ocr_data['left'][i] / width) * 1000  # Normalizar x
            y = (ocr_data['top'][i] / height) * 1000  # Normalizar y
            w = (ocr_data['width'][i] / width) * 1000
            h = (ocr_data['height'][i] / height) * 1000

            words_data.append({"word": word, "x": x, "y": y, "w": w, "h": h})

    return words_data

# Función para ordenar las palabras y reconstruir líneas
def ordenar_y_reconstruir_tabla(words_data, tolerance=10):
    # Ordenar palabras por posición vertical (y), luego horizontal (x)
    words_data = sorted(words_data, key=lambda k: (k['y'], k['x']))

    # Agrupar palabras que están en la misma línea (basado en la proximidad de 'y')
    lines = []
    current_line = []
    prev_y = -1

    for word in words_data:
        if abs(word['y'] - prev_y) > tolerance and current_line:
            lines.append(current_line)
            current_line = []
        current_line.append(word)
        prev_y = word['y']
    if current_line:
        lines.append(current_line)

    # Reconstruir las líneas como texto completo
    reconstructed_lines = [" ".join([word['word'] for word in line]) for line in lines]
    return reconstructed_lines

# Extraer palabras y coordenadas
image_path = 'datasets/datosv2.jpeg'
words_data = get_text_and_coordinates(image_path)

# Reconstruir la tabla ordenada
reconstructed_lines = ordenar_y_reconstruir_tabla(words_data)

# Crear un DataFrame para la tabla ordenada
df = pd.DataFrame({"Línea": reconstructed_lines})

# Guardar en Excel
output_file = 'datasets/tabla_reconstruida.xlsx'
df.to_excel(output_file, index=False)

print(f"Tabla reconstruida guardada en {output_file}.")

from PIL import Image
import pytesseract
from transformers import LayoutLMv3Processor, LayoutLMv3ForTokenClassification
import torch
import pandas as pd

# Configuración de Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'  # Ajusta la ruta si es necesario

# Cargar LayoutLM modelo preentrenado
processor = LayoutLMv3Processor.from_pretrained("microsoft/layoutlmv3-base", apply_ocr=False)
model = LayoutLMv3ForTokenClassification.from_pretrained("microsoft/layoutlmv3-base")

# Preprocesar la imagen con Tesseract para obtener texto y coordenadas
def get_normalized_boxes(image_path):
    image = Image.open(image_path)
    width, height = image.size  # Obtener dimensiones de la imagen

    # Extraer datos OCR
    ocr_data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT, lang="spa")

    words = []
    boxes = []

    for i in range(len(ocr_data['text'])):
        word = ocr_data['text'][i].strip()
        if word:  # Filtrar palabras vacías
            x, y, w, h = ocr_data['left'][i], ocr_data['top'][i], ocr_data['width'][i], ocr_data['height'][i]
            # Normalizar coordenadas
            x_norm = int((x / width) * 1000)
            y_norm = int((y / height) * 1000)
            w_norm = int(((x + w) / width) * 1000)
            h_norm = int(((y + h) / height) * 1000)

            words.append(word)
            boxes.append([x_norm, y_norm, w_norm, h_norm])

    return words, boxes, image

# Procesar la imagen
image_path = 'datasets/datosv2.jpeg'
words, boxes, image = get_normalized_boxes(image_path)

# Convertir los datos al formato de LayoutLM
encoding = processor(image, words, boxes=boxes, return_tensors="pt", truncation=True, padding="max_length", max_length=512)

# Realizar la predicción
with torch.no_grad():
    outputs = model(**encoding)

# Obtener predicciones
predictions = torch.argmax(outputs.logits, dim=-1)[0].tolist()
labels = [model.config.id2label[pred] for pred in predictions]

# Organizar los resultados en una lista de diccionarios
data = []
for word, label in zip(words, labels):
    data.append({"Palabra": word, "Etiqueta": label})

# Crear un DataFrame
df = pd.DataFrame(data)

# Guardar en Excel
output_file = 'datasets/resultados_layoutlm.xlsx'
df.to_excel(output_file, index=False)

print(f"Resultados guardados en {output_file}.")

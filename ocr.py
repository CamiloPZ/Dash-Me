import pytesseract
from PIL import Image
import pandas as pd
import re
import cv2

# Configura pytesseract (ajusta la ruta si es necesario)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Ruta predeterminada en Windows
pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'


# Cargar y preprocesar la imagen
def preprocess_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convertir a escala de grises
    img = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]  # Binarización
    img = cv2.medianBlur(img, 3)  # Reducir ruido
    return img

# Extraer texto de la imagen
def extract_text_from_image(image_path):
    img = preprocess_image(image_path)
    return pytesseract.image_to_string(img, lang='spa')

# Procesamiento de texto con regex
def procesar_texto(texto):
    produccion, mano_obra, equipos, paralizaciones = [], [], [], []

    # Extraer Avances de Producción
    avances_produccion = re.findall(r'(\d{2})\s+([^\n]+)\s+([A-Z]{1,2})\s+(\d+)\s+([A-Z]\d+)\s+(\d+)\s+(\d+)', texto)
    for item in avances_produccion:
        produccion.append({"Item": item[0], "Actividad": item[1].strip(), "UND": item[2],
                           "CANT": item[3], "AREA": item[4], "FASE": item[5], "HORAS": item[6]})
    
    # Extraer Mano de Obra
    mano_obra_data = re.findall(r'(\d{2})\s+([^\n]+)\s+(\d+)\s+(\d+)', texto)
    for item in mano_obra_data:
        mano_obra.append({"Item": item[0], "Rol": item[1].strip(), "CANT": item[2], "HORAS": item[3]})

    # Extraer Equipos
    equipos_data = re.findall(r'(\d{2})\s+([^\n]+)\s+([A-Z]{2})\s+(\d+)', texto)
    for item in equipos_data:
        equipos.append({"Item": item[0], "Descripción": item[1].strip(), "UND": item[2], "HORAS": item[3]})

    # Extraer Paralizaciones
    paralizaciones_data = re.findall(r'(\d{2})\s+([^\n]+)\s+(\d{1,2}:\d{2})\s+(\d{1,2}:\d{2})', texto)
    for item in paralizaciones_data:
        paralizaciones.append({"Item": item[0], "Evento": item[1].strip(), "Inicio": item[2], "Fin": item[3]})
    
    return produccion, mano_obra, equipos, paralizaciones

# Ruta de la imagen
image_path = 'datasets/datosv2.jpeg'

# Extraer y procesar texto
texto = extract_text_from_image(image_path)
produccion, mano_obra, equipos, paralizaciones = procesar_texto(texto)

# Crear DataFrames
df_produccion = pd.DataFrame(produccion)
df_mano_obra = pd.DataFrame(mano_obra)
df_equipos = pd.DataFrame(equipos)
df_paralizaciones = pd.DataFrame(paralizaciones)

print(df_produccion)
print(df_mano_obra)
print(df_equipos)
print(df_paralizaciones)

# Guardar en Excel
output_file = 'datasets/reporte_actividad_procesado.xlsx'
with pd.ExcelWriter(output_file) as writer:
    if not df_produccion.empty:
        df_produccion.to_excel(writer, sheet_name='Avances_Produccion', index=False)
    if not df_mano_obra.empty:
        df_mano_obra.to_excel(writer, sheet_name='Mano_Obra', index=False)
    if not df_equipos.empty:
        df_equipos.to_excel(writer, sheet_name='Equipos', index=False)
    if not df_paralizaciones.empty:
        df_paralizaciones.to_excel(writer, sheet_name='Paralizaciones', index=False)

print(f"Datos extraídos y guardados en {output_file}.")
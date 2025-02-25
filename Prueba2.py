import pytesseract
from pdf2image import convert_from_path
import cv2
import numpy as np
import pandas as pd

ruta_pdf = r"C:\Users\USUARIO\Desktop\pdf to excel\Novedades Punteo Inserciones.pdf"
ruta_excel = r"C:\Users\USUARIO\Desktop\pdf to excel\salida.xlsx"

# Convertir PDF a imágenes
imagenes = convert_from_path(ruta_pdf)

# Configurar Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

data = []

for imagen in imagenes:
    img_cv = np.array(imagen)
    img_gray = cv2.cvtColor(img_cv, cv2.COLOR_RGB2GRAY)
    _, img_thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    texto_extraido = pytesseract.image_to_string(img_thresh, lang="spa")

    # Separar en filas
    filas = texto_extraido.split("\n")
    for fila in filas:
        columnas = fila.split()  # Ajusta el separador según el formato
        data.append(columnas)

# Crear DataFrame y guardar en Excel
if data:
    df = pd.DataFrame(data)
    df.to_excel(ruta_excel, index=False, engine='openpyxl')
    print(f"✅ Archivo Excel generado exitosamente: {ruta_excel}")
else:
    print("⚠ No se pudo extraer la tabla correctamente.")

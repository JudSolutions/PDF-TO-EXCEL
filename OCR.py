import os
from pdf2image import convert_from_path
import tabula
import pytesseract
import pandas as pd

# Ruta al ejecutable de Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Ruta al archivo PDF
ruta_pdf = r"C:\Users\USUARIO\Desktop\pdf to excel\Libro1.pdf"

# Extraer todas las tablas del PDF
tablas = tabula.read_pdf(ruta_pdf, pages='all', multiple_tables=True, lattice=True)

# Verificar si se encontraron tablas
if not tablas:
    print("No se encontraron tablas en el PDF.")
else:
    # Crear un objeto ExcelWriter para guardar múltiples DataFrames en un solo archivo de Excel
    with pd.ExcelWriter(r"C:\Users\USUARIO\Desktop\pdf to excel\salida.xlsx", engine='openpyxl') as writer:
        for i, tabla in enumerate(tablas):
            # Guardar cada tabla en una hoja diferente
            tabla.to_excel(writer, sheet_name=f'Tabla_{i+1}', index=False)
            print("Archivo Excel generado exitosamente.")

# Convertir el PDF a imágenes
paginas = convert_from_path(ruta_pdf, poppler_path=r'C:\Users\USUARIO\Downloads\Release-24.07.0-0\poppler-24.07.0\Library\bin')

# Lista para almacenar el texto extraído de cada página
texto_paginas = []

# Extraer texto de cada página
for pagina in paginas:
    texto = pytesseract.image_to_string(pagina, lang='spa')  # 'spa' para español
    texto_paginas.append(texto)

# Crear un DataFrame a partir del texto extraído
df = pd.DataFrame({'Contenido': texto_paginas})

# Ruta para guardar el archivo Excel
ruta_excel = r"C:\Users\USUARIO\Desktop\pdf to excel\salida.xlsx"

# Guardar el DataFrame en un archivo Excel
df.to_excel(ruta_excel, index=False)

print(f"Archivo Excel generado: {ruta_excel}")



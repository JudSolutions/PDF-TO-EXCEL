import pdfplumber
import pandas as pd

# Ruta del archivo PDF
ruta_pdf = r"C:\Users\USUARIO\Desktop\pdf to excel\Novedad punteo 10022025.pdf"

# Lista para almacenar las tablas extraídas
data = []

# Abrir el PDF y extraer tablas
with pdfplumber.open(ruta_pdf) as pdf:
    for page in pdf.pages:
        tables = page.extract_table({"snap_tolerance": 3})
        if tables:
            for row in tables:
                data.append(row)

# Verificar si se extrajo información
if data:
    # Definir nombres de columnas según la imagen proporcionada
    columnas = ["ITEM / ID", "CÓDIGO", "APELLIDOS Y NOMBRES", "CÉDULA", "Pag.", "Doc.",
                "SOPORTE DE ENTREGA", "ANEXOS", "FOLIOS", "OBSERVACIONES"]

    # Crear DataFrame
    df = pd.DataFrame(data, columns=columnas)

    # Ruta para guardar el archivo Excel
    ruta_excel = r"C:\Users\USUARIO\Desktop\pdf to excel\salida.xlsx"

    # Guardar en Excel
    df.to_excel(ruta_excel, index=False, engine='openpyxl')

    print(f"✅ Archivo Excel generado exitosamente: {ruta_excel}")
else:
    print("⚠ No se pudo extraer la tabla. Intenta mejorar la calidad del PDF.")


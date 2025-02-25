import pandas as pd
import tabula

def pdf_para_dataframe (ruta_del_pdf):
    # Extraer tablas del archivo PDF
    tablas = tabula.read_pdf(ruta_del_pdf, pages='all', multiple_tables=True)

    # Inicializa un DataFrame vacío para almacenar las tablas combinadas
    dataframe_combinado = pd.DataFrame()

    # Combinar todas las tablas en un solo DataFrame
    for tabla in tablas:
        df = tabla.copy()
        dataframe_combinado = pd.concat([dataframe_combinado, df], ignore_index=True)

    return dataframe_combinado

# Ruta del archivo PDF en tu computadora (asegúrate de que sea correcta)
ruta_del_pdf = r"C:\Users\USUARIO\Desktop\pdf to excel\Novedad punteo 10022025.pdf"

# Llamar a la función para convertir el PDF en un único DataFrame
dataframe_combinado2 = pdf_para_dataframe(ruta_del_pdf)

# Mostrar el DataFrame resultante
print(dataframe_combinado2)
# Guardar a Excel
ruta_excel = "c:/Users/USUARIO/Desktop/pdf to excel/salida.xlsx"
dataframe_combinado2.to_excel(ruta_excel, index=False)

print(f"✅ Archivo Excel generado correctamente en: {ruta_excel}")

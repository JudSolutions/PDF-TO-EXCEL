import pytesseract
from pdf2image import convert_from_path
import cv2
import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox

# Configurar Tesseract (ajusta la ruta según tu instalación)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def convertir_pdf():
    """Selecciona un PDF y lo convierte a Excel."""
    archivo_pdf = filedialog.askopenfilename(filetypes=[("Archivos PDF", "*.pdf")])
    
    if not archivo_pdf:
        messagebox.showwarning("Advertencia", "No seleccionaste ningún archivo.")
        return

    ruta_excel = archivo_pdf.replace(".pdf", ".xlsx")

    try:
        imagenes = convert_from_path(archivo_pdf)
        data = []

        for imagen in imagenes:
            img_cv = np.array(imagen)
            img_gray = cv2.cvtColor(img_cv, cv2.COLOR_RGB2GRAY)
            _, img_thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

            texto_extraido = pytesseract.image_to_string(img_thresh, lang="spa")
            filas = texto_extraido.split("\n")
            for fila in filas:
                columnas = fila.split()  # Ajusta si es necesario
                data.append(columnas)

        if data:
            df = pd.DataFrame(data)
            df.to_excel(ruta_excel, index=False, engine='openpyxl')
            messagebox.showinfo("Éxito", f"Archivo Excel guardado en:\n{ruta_excel}")
        else:
            messagebox.showwarning("Error", "No se pudo extraer la tabla correctamente.")

    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un problema:\n{str(e)}")

# Crear ventana con Tkinter
root = tk.Tk()
root.title("PDF a Excel")
root.geometry("400x300")
root.resizable(False, False)

# Botón para seleccionar PDF
btn_convertir = tk.Button(root, text="Seleccionar PDF y Convertir", command=convertir_pdf, font=("Arial", 12), bg="#4CAF50", fg="white", padx=10, pady=5)
btn_convertir.pack(pady=50)

# Ejecutar la interfaz gráfica
root.mainloop()


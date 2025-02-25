import pytesseract

# Configurar la ruta de Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Verificar si Tesseract está configurado correctamente
print(pytesseract.get_tesseract_version())  # Debería imprimir la versión de Tesseract

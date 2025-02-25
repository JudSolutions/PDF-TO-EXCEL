from pdf2image import convert_from_path

poppler_path = r"C:\Program Files (x86)\poppler-24.07.0\Library\bin"  # Ajusta según la ubicación de tu instalación
images = convert_from_path(r"C:\Users\USUARIO\Desktop\pdf to excel\Novedad punteo 10022025.pdf", poppler_path=poppler_path)

# Guarda la primera página como imagen
images[0].save("output.png", "PNG")
print("Conversión exitosa")


# Ahora intenta cargarla con OpenCV
import cv2
img = cv2.imread("output.png")

if img is None:
    print("Error: No se pudo cargar la imagen.")
else:
    print("Imagen cargada correctamente.")

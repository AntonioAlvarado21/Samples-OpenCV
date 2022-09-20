# Reconomiento de patrones
import cv2 as cv
import numpy as np

# Cargamos las imagenes
placas = cv.imread('Photos/placas.jpg')
placa = cv.imread('Photos/placa.png')
cv.imshow('Placa a buscar', placa)

# Convertimos a escala de grises
placas_gray = cv.cvtColor(placas, cv.COLOR_BGR2GRAY)
placa_gray = cv.cvtColor(placa, cv.COLOR_BGR2GRAY)

# Obtenemos las dimensiones de las placa
alt, anch = placas_gray.shape[:2]
print("PLACAS:\nAltura: " + str(alt), "Ancho: " + str(anch))

alto, ancho = placa_gray.shape[:2]
print("PLACA:\nAltura: " + str(alto), "Ancho: " + str(ancho))

# Buscamos la placa en las placas
resultado = cv.matchTemplate(placas_gray, placa_gray, cv.TM_CCOEFF_NORMED)
min, max, pos_min, pos_max = cv.minMaxLoc(resultado)

# Dibujamos un rectangulo en la placa
pixel_superior_izquierdo = pos_max
pixel_inferior_derecho = (pos_max[0] + ancho, pos_max[1]+alto)

cv.rectangle(placas, pixel_superior_izquierdo, pixel_inferior_derecho, (255, 0, 0), 4)
#cv.rectangle(placas, pos_max, (pos_max[0] + ancho, pos_max[1] + alto), (0, 0, 255), 2)

cv.imshow('Resultado de coincidencias', placas)

# Esperamos a que se presione una tecla
cv.waitKey(0)
cv.destroyAllWindows()
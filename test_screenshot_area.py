import cv2
import numpy as np
import pyautogui

captura_mostrada = False

while True:
    # Tomar la captura de pantalla
    screenshot = pyautogui.screenshot(region=(0, 0, 1920, 1080))
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

    # Mostrar la captura de pantalla si aún no ha sido mostrada
    if not captura_mostrada:
        cv2.imshow('screenshot', screenshot)
        captura_mostrada = True

    # Esperar a que se presione la tecla 'Esc' para salir del bucle
    if cv2.waitKey(1) == 27:
        break

# Cerrar la ventana y liberar los recursos
cv2.destroyAllWindows()

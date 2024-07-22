# Controlador de Ratón con Gestos de Mano

Este programa permite controlar el ratón de tu computadora utilizando gestos de mano capturados a través de la cámara web. Utiliza OpenCV y MediaPipe para la detección de manos y PyAutoGUI para mover el puntero del ratón y realizar clics.

## Descripción

El programa captura video desde la cámara web y utiliza MediaPipe para detectar las posiciones de los dedos de la mano. Si se detecta que el dedo índice está hacia abajo, el programa mueve el puntero del ratón a la posición correspondiente en la pantalla y realiza un clic.

## Cómo Funciona

1. **Captura de Video**: Se captura el video en tiempo real desde la cámara web utilizando OpenCV.
2. **Detección de Manos**: MediaPipe Hands se utiliza para detectar la mano en el cuadro de video y extraer las coordenadas de los puntos clave de la mano.
3. **Cálculo de Posición**: Se calculan las posiciones (x, y) del punto base (muñeca) y el punto índice (punta del dedo) de la mano.
4. **Movimiento del Ratón**: Las coordenadas se escalan a la resolución de la pantalla y se utiliza PyAutoGUI para mover el puntero del ratón a la posición correspondiente.
5. **Detección de Gesto de Clic**: Se calcula la distancia entre el punto base y el punto índice. Si la distancia es menor que la distancia entre el punto base y un punto de referencia (el medio de la mano), se detecta que el dedo índice está hacia abajo y se realiza un clic con el ratón utilizando PyAutoGUI.

## Requisitos

- Python 3.x
- OpenCV
- MediaPipe
- NumPy
- PyAutoGUI

## Instalación

1. Clona este repositorio:
    ```bash
    git clone https://github.com/JosueReyes13/Mouse
    cd Mouse
    ```

2. Instala las dependencias necesarias:
    ```bash
    pip install opencv-python mediapipe numpy pyautogui
    ```

## Uso

Ejecuta el script `controlador_raton.py`:
```bash
python controlador_raton.py

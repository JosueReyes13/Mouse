import cv2
import mediapipe as mp
import numpy as np
import pyautogui

# Obtener la resolución de la pantalla
screen_width, screen_height = pyautogui.size()

# Establecer los puntos iniciales y finales del área de la pantalla
SCREEN_GAME_X_INI = 0
SCREEN_GAME_Y_INI = 0
SCREEN_GAME_X_FIN = screen_width
SCREEN_GAME_Y_FIN = screen_height

# Calcular la relación de aspecto de la pantalla
aspect_ratio_screen = (SCREEN_GAME_X_FIN - SCREEN_GAME_X_INI) / (SCREEN_GAME_Y_FIN - SCREEN_GAME_Y_INI)
print("aspect_ratio_screen:", aspect_ratio_screen)

# Coordenada inicial
X_Y_INI = 0

# Función para calcular la distancia
def calculate_distance(x1, y1, x2, y2):
    p1 = np.array([x1, y1])
    p2 = np.array([x2, y2])
    return np.linalg.norm(p1 - p2)

# Función para detectar si el dedo está hacia abajo
def detect_finger_down(hand_landmarks):
    finger_down = False
    color_base = (255, 0, 112)
    color_index = (255, 198, 82)
    x_base1 = int(hand_landmarks.landmark[0].x * width)
    y_base1 = int(hand_landmarks.landmark[0].y * height)
    x_base2 = int(hand_landmarks.landmark[9].x * width)
    y_base2 = int(hand_landmarks.landmark[9].y * height)
    x_index = int(hand_landmarks.landmark[8].x * width)
    y_index = int(hand_landmarks.landmark[8].y * height)
    d_base = calculate_distance(x_base1, y_base1, x_base2, y_base2)
    d_base_index = calculate_distance(x_base1, y_base1, x_index, y_index)
    if d_base_index < d_base:
        finger_down = True
        color_base = (255, 0, 255)
        color_index = (255, 0, 255)
    cv2.circle(frame, (x_base1, y_base1), 5, color_base, 2)
    cv2.circle(frame, (x_index, y_index), 5, color_index, 2)
    cv2.line(frame, (x_base1, y_base1), (x_base2, y_base2), color_base, 3)
    cv2.line(frame, (x_base1, y_base1), (x_index, y_index), color_index, 3)
    return finger_down

# Inicializar MediaPipe Hands
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Capturar video desde la cámara
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Color para el puntero del ratón
color_mouse_pointer = (255, 0, 255)

# Configurar MediaPipe Hands
with mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.5) as hands:
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        height, width, _ = frame.shape
        frame = cv2.flip(frame, 1)
        
        # Convertir el frame a RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Procesar la imagen con MediaPipe Hands
        results = hands.process(frame_rgb)
        
        if results.multi_hand_landmarks is not None:
            for hand_landmarks in results.multi_hand_landmarks:
                x = int(hand_landmarks.landmark[9].x * width)
                y = int(hand_landmarks.landmark[9].y * height)
                xm = np.interp(x, (X_Y_INI, width), (SCREEN_GAME_X_INI, SCREEN_GAME_X_FIN))
                ym = np.interp(y, (X_Y_INI, height), (SCREEN_GAME_Y_INI, SCREEN_GAME_Y_FIN))
                pyautogui.moveTo(int(xm), int(ym))
                if detect_finger_down(hand_landmarks):
                    pyautogui.click()
                cv2.circle(frame, (x, y), 10, color_mouse_pointer, 3)
                cv2.circle(frame, (x, y), 5, color_mouse_pointer, -1)
        
        # Mostrar el resultado
        cv2.imshow('output', frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

# Liberar la captura de video y cerrar ventanas
cap.release()
cv2.destroyAllWindows()

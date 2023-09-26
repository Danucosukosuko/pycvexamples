import cv2
import numpy as np

def move_and_modify_strips(input_video_path, output_video_path):
    cap = cv2.VideoCapture(input_video_path)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    
    # Obtenemos el ancho y alto del video original
    width = int(cap.get(3))
    height = int(cap.get(4))
    
    out = cv2.VideoWriter(output_video_path, fourcc, 30, (width, height), isColor=True)
    
    strip_height = 50  # Altura de las franjas que se moverán
    strip_speed = 5    # Velocidad de desplazamiento de las franjas
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Crea una copia del frame
        frame_copy = frame.copy()
        
        # Genera una franja de colores aleatorios
        if np.random.randint(0, 2) == 0:
            color_strip = np.random.randint(50, 101)  # Valor RGB entre 50 y 100
            strip = np.full((strip_height, width, 3), color_strip, dtype=np.uint8)
        else:
            strip = np.zeros((strip_height, width, 3), dtype=np.uint8)
        
        # Calcula la posición de la franja en el frame
        y_position = np.random.randint(0, height - strip_height)
        
        # Desplaza la franja horizontalmente
        for x_offset in range(0, width, strip_speed):
            x_end = x_offset + strip_speed
            if x_end > width:
                x_end = width
            
            frame_copy[y_position:y_position + strip_height, x_offset:x_end] = strip[:, :x_end - x_offset, :]
        
        out.write(frame_copy)
    
    cap.release()
    out.release()

if __name__ == "__main__":
    input_video_path = "NOMBREDELVIDEO.MP4"  # Nombre del video de entrada
    output_video_path = "NOMBREDELVIDEO_con_franjas.mp4"  # Nombre del video de salida
    
    move_and_modify_strips(input_video_path, output_video_path)

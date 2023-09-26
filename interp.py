import cv2

def apply_interpolation_effect(input_video_path, output_video_path, scale_factor=2):
    cap = cv2.VideoCapture(input_video_path)
    
    # Verifica si el video se abrió correctamente
    if not cap.isOpened():
        print("Error al abrir el archivo de video.")
        return

    # Obtiene las propiedades del video original
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    fps = int(cap.get(5))
    fourcc = int(cap.get(6))

    # Define el nuevo tamaño del video
    new_width = frame_width * scale_factor
    new_height = frame_height * scale_factor

    # Define el objeto VideoWriter para el video de salida
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (new_width, new_height))

    while True:
        ret, frame = cap.read()
        
        if not ret:
            break

        # Aplica la interpolación para cambiar el tamaño del frame
        frame = cv2.resize(frame, (new_width, new_height), interpolation=cv2.INTER_LINEAR)

        # Escribe el frame en el nuevo video
        out.write(frame)

    # Libera los recursos
    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    input_video_path = "NOMBREDELVIDEO_con_franjas.MP4"  # Ruta del video de entrada
    output_video_path = "NOMBREDELVIDEO_interpolacion.mp4"  # Ruta del video de salida

    apply_interpolation_effect(input_video_path, output_video_path, scale_factor=2)

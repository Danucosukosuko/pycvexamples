import cv2
import os

def extract_frames(video_path, output_folder):
    # Verifica si la carpeta de salida existe, si no, créala
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Abre el archivo de vídeo
    cap = cv2.VideoCapture(video_path)

    # Verifica si el archivo de vídeo se abrió correctamente
    if not cap.isOpened():
        print("Error al abrir el archivo de vídeo.")
        return

    frame_count = 0

    while True:
        # Lee un frame del vídeo
        ret, frame = cap.read()

        # Si no hay más frames, sal del bucle
        if not ret:
            break

        # Formatea el nombre del archivo de salida
        frame_filename = f"{os.path.splitext(os.path.basename(video_path))[0]}_{frame_count:04d}.png"

        # Guarda el frame como imagen en la carpeta de salida
        frame_path = os.path.join(output_folder, frame_filename)
        cv2.imwrite(frame_path, frame)

        frame_count += 1

    # Cierra el archivo de vídeo
    cap.release()

    print(f"Se extrajeron {frame_count} frames en '{output_folder}'.")

if __name__ == "__main__":
    video_path = "NOMBREDELVIDEO.MP4"  # Reemplaza con la ruta de tu vídeo
    output_folder = "frames"  # Nombre de la carpeta de salida

    extract_frames(video_path, output_folder)

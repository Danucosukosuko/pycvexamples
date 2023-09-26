import cv2
import os
import random

def create_video_from_frames(frames_folder, output_video_path, frames_per_chunk=3):
    # Obtener la lista de nombres de archivos de los frames
    frame_files = sorted([f for f in os.listdir(frames_folder) if f.endswith(".png")])

    # Verificar si hay suficientes frames para crear el nuevo video
    if len(frame_files) < frames_per_chunk:
        print("No hay suficientes frames para crear el video.")
        return

    # Abre el primer frame para obtener sus dimensiones
    first_frame = cv2.imread(os.path.join(frames_folder, frame_files[0]))
    frame_height, frame_width, _ = first_frame.shape

    # Configurar el codec y el objeto VideoWriter
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video_path, fourcc, 30, (frame_width, frame_height))

    frame_count = 0

    while frame_count < len(frame_files):
        # Seleciona aleatoriamente 3 frames para eliminar
        frames_to_delete = random.sample(range(frame_count, min(frame_count + frames_per_chunk, len(frame_files))), frames_per_chunk)

        for i in range(len(frame_files)):
            if i not in frames_to_delete:
                # Lee el frame y escribe en el nuevo video
                frame = cv2.imread(os.path.join(frames_folder, frame_files[i]))
                out.write(frame)

        frame_count += frames_per_chunk

    # Cierra el objeto VideoWriter
    out.release()

    print(f"Nuevo video creado en '{output_video_path}'.")

if __name__ == "__main__":
    frames_folder = "frames"  # Carpeta que contiene los frames
    output_video_path = "nuevo_video.mp4"  # Nombre del nuevo video

    create_video_from_frames(frames_folder, output_video_path)

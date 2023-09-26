import cv2
import numpy as np

def apply_vintage_effects(input_video_path, output_video_path):
    cap = cv2.VideoCapture(input_video_path)

    if not cap.isOpened():
        print("Error al abrir el archivo de video.")
        return

    # Cambiar la resolución a 144p (256x144 píxeles) y formato 4:3
    frame_width, frame_height = 256, 144
    aspect_ratio = 4/3
    fps = int(cap.get(5))
    fourcc = int(cap.get(6))

    out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, int(frame_width / aspect_ratio)))

    stripe_height = frame_height // 2  # Altura de las rayas (mitad de la altura del video)
    displacement_range = np.arange(2, 6)  # Rango de desplazamiento entre 2px y 5px

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Cambiar el tamaño del frame a 144p y formato 4:3
        frame = cv2.resize(frame, (frame_width, int(frame_width / aspect_ratio)))

        # Aplicar efectos vintage con dos rayas de desplazamiento desde la izquierda
        rows, cols, _ = frame.shape
        frame_distorted = np.copy(frame)

        # Posición inicial de la primera raya (altura aleatoria)
        y1 = np.random.randint(0, rows - stripe_height)
        y2 = y1 + stripe_height  # Posición de la segunda raya

        displacement1 = np.random.choice(displacement_range)  # Desplazamiento aleatorio para la primera raya
        displacement2 = np.random.choice(displacement_range)  # Desplazamiento aleatorio para la segunda raya

        frame_distorted[y1:y1+stripe_height, displacement1:] = frame[y1:y1+stripe_height, :-displacement1]
        frame_distorted[y2:y2+stripe_height, displacement2:] = frame[y2:y2+stripe_height, :-displacement2]

        out.write(frame_distorted)

    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    input_video_path = "video3.mp4"  # Ruta del video original
    output_video_path = "video_vintage_144p_4_3_small_stripes.mp4"  # Ruta del video con efectos vintage, calidad 144p, formato 4:3 y dos rayas en movimiento desde la izquierda con desplazamiento de 2 a 5px

    apply_vintage_effects(input_video_path, output_video_path)

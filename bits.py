import cv2

def reduce_bitrate(input_video_path, output_video_path, quality=1):
    cap = cv2.VideoCapture(input_video_path)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    
    # Obtenemos el ancho y alto del video original
    width = int(cap.get(3))
    height = int(cap.get(4))
    
    out = cv2.VideoWriter(output_video_path, fourcc, 30, (width, height), isColor=True)
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Reduce la calidad del frame (aumenta el valor de calidad para una mayor compresión)
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), quality]
        _, encimg = cv2.imencode('.jpg', frame, encode_param)
        frame = cv2.imdecode(encimg, 1)
        
        out.write(frame)
    
    cap.release()
    out.release()

if __name__ == "__main__":
    input_video_path = "NOMBREDELVIDEO.MP4"  # Nombre del video de entrada
    output_video_path = "NOMBREDELVIDEO_16Mbps.mp4"  # Nombre del video de salida
    
    reduce_bitrate(input_video_path, output_video_path, quality=10)

import cv2

def denoise_image(image_path):
    # Đọc ảnh từ đường dẫn
    image = cv2.imread(image_path)
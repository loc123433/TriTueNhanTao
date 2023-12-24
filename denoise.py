import cv2

def denoise_image(image_path):
    # Đọc ảnh từ đường dẫn
    image = cv2.imread(image_path)

    # Áp dụng Median filtering để làm giảm nhiễu
    denoised_image = cv2.medianBlur(image, 5)  # Kích thước kernel = 5

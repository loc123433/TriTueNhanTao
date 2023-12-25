import cv2 
#themcode
def denoise_image(image_path):
    # Đọc ảnh từ đường dẫn
    image = cv2.imread(image_path)

    # Áp dụng Median filtering để làm giảm nhiễu
    denoised_image = cv2.medianBlur(image, 5)  # Kích thước kernel = 5
    #deniused_image
    # Hiển thị ảnh gốc và ảnh đã được làm giảm nhiễu
    cv2.imshow("Original Image", image)
    cv2.imshow("Denoised Image", denoised_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
 
    # Đường dẫn đến ảnh
image_path = "NoiseKT(2).jpg"

# Gọi hàm denoise_image với đường dẫn ảnh
denoise_image(image_path)
#them ham chuc
#them chuc nang
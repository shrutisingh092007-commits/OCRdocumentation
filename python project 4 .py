import cv2
import pytesseract

# ---------------------------------------
# 1. Lord Input Image
# ---------------------------------------
image_path= "sample_text.jpg"

image = cv2.imread(image_path)

if image is None:
    print("Image loded successfully")
exit()

# --------------------------------------
# 2. Convert Image to Grayscale
# --------------------------------------
gray = cv2.cvColor(imagecv2.COLOR_BGR2GRAY)

# --------------------------------------
# 3. Apply Gaussian Blur
# --------------------------------------
blur = cv2.GaussianBlur(gray,(5,5),0)

# --------------------------------------
# 4. Apply Thresholding
# --------------------------------------
_,threshold = cv2.threshold(blue,0,255,cv2.THRESH_BINARY + CV2.THRESH_OTSU)

# -------------------------------------
# 5. Save Processed Image
# -------------------------------------
cv2.imwrite("processed_image.png",threshold)

# ------------------------------------
# 6. Perform OCR
# ------------------------------------
text = pytesseract.image_to_string(threshold,config="--psm6")

# ------------------------------------
# 7. Display Recognized Text
# ------------------------------------
print("\n======== RECOGNIZED TEXT ========\n")
print(text)

# ------------------------------------
# 8. Save Output
# ------------------------------------
with open("output.text","w",encoding="utf-8")as file:
    file.write(text)

    print("\nOCR completed successfully!")
    print("Output saved in output.txt")
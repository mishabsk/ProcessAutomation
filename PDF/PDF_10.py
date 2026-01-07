from PIL import Image
import pytesseract

# Correct path to tesseract.exe on your computer
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\gfg0753\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

# Path to the image
image_path = r"d.jpg"

# Open the image and convert it to grayscale
img = Image.open(image_path).convert("L")

# Extract text from the image
text = pytesseract.image_to_string(img)

# Clean up unwanted characters and print result
print(text.replace("\x0c", "").strip())

from PIL import Image
import pytesseract

# Path to tesseract.exe (update if different on your computer)
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\gfg0753\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

# Open the image
img = Image.open("sample_text.png")

# Convert to grayscale (makes it easier for OCR)
img = img.convert("L")

# Extract text from the image
text = pytesseract.image_to_string(img)

# Remove extra characters and print the text
print(text.replace("\x0c", "").strip())

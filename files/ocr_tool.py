"""
Section 10: Image Text Extractor (OCR)
Covers: Optical Character Recognition, Handle Error and Exceptions
"""

import re


def extract_text_from_image(image_path):
    """
    Extracts text from an image using pytesseract, if available.
    Handles missing library / missing tesseract binary / bad file path gracefully.
    """
    try:
        import pytesseract
        from PIL import Image
    except ImportError:
        print("OCR libraries not installed. Run: pip install pytesseract pillow "
              "(and install the tesseract-ocr binary) to enable this feature.")
        return None

    try:
        image = Image.open(image_path)
    except FileNotFoundError:
        print(f"Image not found at: {image_path}")
        return None
    except Exception as e:
        print(f"Could not open image: {e}")
        return None

    try:
        text = pytesseract.image_to_string(image)
    except Exception as e:
        print(f"OCR engine failed (is tesseract-ocr installed on this system?): {e}")
        return None

    return text


def clean_extracted_text(text):
    """Basic cleanup: collapse whitespace, strip stray symbols."""
    if not text:
        return ""
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^\w\s.,:@/-]", "", text)
    return text.strip()


def run_ocr_menu():
    print("\n--- Image Text Extractor (OCR) ---")
    path = input("Path to image file (e.g. a scanned note or receipt): ").strip()
    raw_text = extract_text_from_image(path)
    if raw_text is None:
        return
    cleaned = clean_extracted_text(raw_text)
    print("\nRaw extracted text:")
    print(raw_text)
    print("\nCleaned text:")
    print(cleaned)

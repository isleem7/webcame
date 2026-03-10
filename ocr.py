import easyocr
import cv2
import re

# Initialisation EasyOCR
reader = easyocr.Reader(['ar', 'en'], gpu=False)

def extraire_matricule(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print(f"❌ Image non trouvée : {image_path}")
        return None

    img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    resultats = reader.readtext(gray, detail=0)

    print("🧾 OCR brut EasyOCR :")
    print(resultats)

    texte = " ".join(resultats)

    chiffres = re.findall(r"\d+", texte)
    chiffres = " ".join(chiffres)

    arabe = ""
    if "تونس" in texte:
        arabe = "تونس"
    elif "نت" in texte:
        arabe = "نت"

    if chiffres:
        return f"{chiffres} {arabe}".strip()

    return None

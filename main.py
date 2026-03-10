from capture_webcam import capture_webcam
from ocr import traiter_image
from database import enregistrer_acces
from datetime import datetime

def main():

    print("🚦 Lancement de la capture de la webcam")

    image = capture_webcam()

    if image is None:
        print("❌ Aucune image capturée")
        return

    print("🔍 Extraction de la matricule...")

    matricule = traiter_image(image)

    if not matricule:
        print("❌ Aucune matricule détectée")
        return

    print("🚗 Matricule détectée :", matricule)

    maintenant = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    statut = "AUTORISÉ"

    enregistrer_acces(matricule, maintenant, statut)

    print("💾 Enregistré dans la base de données")


if __name__ == "__main__":
    main()
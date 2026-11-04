
import os
from ultralytics import YOLO

def train_banana_model():
    # Définition des chemins et paramètres d'entraînement
    dataset_path = '/content/drive/MyDrive/fieldscan/data/bananalsd_dataset_split'
    model_pretrained = 'yolov8n-cls.pt'
    
    print(" Initialisation du modèle YOLOv8 classification...")
    
    # 1. Charger le modèle pré-entraîné (Nano)
    model = YOLO(model_pretrained)

    # 2. Lancer l'entraînement sur le dataset préparé
    print(_get_training_message(dataset_path))
    
    results = model.train(
        data=dataset_path, 
        epochs=25,          # Nombre d'époques d'apprentissage
        imgsz=224,          # Taille des images normalisée
        batch=16,           # Taille des lots (batch size)
        device=0,           # Utilisation du GPU (si disponible)
        name='banana_lsd_run'
    )

    print("\n Entraînement terminé avec succès !")
    print(" Les poids du modèle et les résultats sont sauvegardés dans le dossier 'runs/classify/'")
    
    return results

def _get_training_message(path):
    return f" Démarrage de l'entraînement à partir du dataset : {path}"

if __name__ == '__main__':
    train_banana_model()

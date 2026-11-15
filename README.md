# Field Scan : Suivi Agricole Automatisé (Sentinel-2 & Vision par Ordinateur)

## Présentation du Projet
**Field Scan** est un pipeline automatisé de suivi de la santé des cultures appliqué à **62 parcelles agricoles** (`G0_0` à `G7_7`) situées en Équateur. Le projet combine l'analyse macroscopique par imagerie satellite Sentinel-2 (saisons humide et sèche) et la vision par ordinateur haute précision par drone (modèles YOLOv8-cls / MobileNetV3) pour détecter précocement le stress végétatif et les maladies foliaires.

---

## Contexte Agronomique : Le Bananier
La culture du bananier impose des contraintes techniques spécifiques qui guident l'architecture du pipeline :

- **Structure végétale :** Le bananier est une grande herbe dotée d'un faux-tronc (bases de feuilles enroulées) issu d'un bulbe souterrain. Chaque pied mère produit un seul régime avant d'être coupé, relayé par ses rejets successifs, ce qui densifie progressivement la plantation.
- **Maladies principales :**
  - *La cercosporiose noire (Black Sigatoka) :* Champignon foliaire débutant par de petites stries brunes qui évoluent en taches noires cernées de jaune, entraînant le dessèchement des feuilles et une chute de rendement.
  - *La fusariose (Fusarium wilt) :* Champignon du sol attaquant les vaisseaux de la plante (jaunissement des vieilles feuilles puis flétrissement), difficilement détectable depuis l'espace à ses débuts et sans traitement curatif.
- **Besoin en eau :** Avec des racines peu profondes et une forte consommation hydrique, le bananier est très sensible aux variations d'irrigation entre la saison humide et la saison sèche.
- **Impacts sur le traitement d'images :**
  - Le comptage individuel des pieds est complexe en raison d'une canopée dense où les rejets sont masqués par le pied mère.
  - Les premiers symptômes de maladie mesurent quelques millimètres, bien en deçà de la résolution spatiale de Sentinel-2 (10 mètres), d'où la nécessité de coupler la télédétection satellite avec des prises de vues rapprochées (drones / feuilles au sol).

---

## Architecture Technique et Pipeline Réalisé

### 1. Alignement Spatial et Données
- **Zone d'étude :** Équateur (Longitude : `-79.860°` à `-79.788°` Ouest, Latitude : `-3.312°` à `-3.240°` Sud).
- **Reprojection métrique :** Les contours vectoriels des 62 parcelles (`EPSG:4326`) sont reprojetés en **WGS 84 / UTM zone 17S (`EPSG:32717`)** afin de garantir une superposition au pixel près avec les rasters Sentinel-2 à 10 mètres.
- **Cloisonnement saisonnier :** Traitement séparé des acquisitions de la saison humide (`humide/`) et de la saison sèche (`seche/`).

### 2. Prétraitement Radiométrique et Calcul du NDVI
- **Normalisation :** Conversion des bandes brutes Sentinel-2 (`uint16`, valeurs jusqu'à `17 279`) en réflectance de surface physique par division par `10 000`.
- **Formule NDVI validée :** Exploitation des bandes `B04` (Rouge, 10 m) et `B08` (Proche Infrarouge, 10 m) :
  `NDVI = (B08 - B04) / (B08 + B04)`
- **Gestion des résolutions :** La bande `B11` (SWIR à 20 m, dimensions `5490 x 5490`) est écartée du calcul matriciel direct avec les bandes à 10 m (`10980 x 10980`) en attendant un rééchantillonnage dédié pour le NDMI.

### 3. Extraction Zonale et Seuils d'Alerte
- **Masquage parcellaire :** Extraction statistique pixel par pixel à l'intérieur de chaque polygone (`rasterio.mask`) avec filtrage des valeurs nulles.
- **Seuil critique de vigueur :** Fixé à **`NDVI = 0.35`**. Toute parcelle passant sous ce seuil déclenche une alerte prioritaire pour orienter les inspections de terrain ou les vols de drones.
- **Livrables générés :** Export automatique des indicateurs parcellaires dans `bulletin_parcelle.csv` (saison humide) et `bulletin_parcelle_seche.csv` (saison sèche), complétés par des expériences tabulaires sur le *California Dataset*.

---

## Structure du Dépôt

```text
field-scan/
│
├── src/
│   ├── train_yolo.py              # Entraînement du modèle de classification YOLOv8-cls
│   └── fusion_sig.py              # Traitement Sentinel-2, reprojection EPSG:32717 et calcul NDVI
│
├── resultats_complets/
│   ├── bulletin_parcelle.csv      # Indicateurs NDVI par parcelle (Saison Humide)
│   ├── bulletin_parcelle_seche.csv # Indicateurs NDVI par parcelle (Saison Sèche)
│   └── parcelles_analysees.geojson # Contours vectoriels des 62 parcelles
│
├── data_card.md                   # Fiche technique des jeux de données (Sentinel-2, BananaLSD, California)
├── requirements.txt               # Dépendances Python (GeoPandas, Rasterio, NumPy, Pandas, Ultralytics)
└── README.md                      # Documentation complète du projet

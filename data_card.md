# Data Card — Projet Field Scan (Suivi Agricole & Données Complémentaires)

## 1. Résumé du Jeu de Données
Ce dépôt intègre des données multispectrales Sentinel-2 pour le suivi agronomique de 62 parcelles agricoles (G0_0 à G7_7) en Équateur, ainsi qu'un jeu de données tabulaire complémentaire (California Dataset) utilisé pour les phases d'expérimentation, d'analyse statistique ou de modélisation prédictive du projet.

---

## 2. Zone d'Étude et Caractéristiques Spatiales (Pipeline Principal)
- Localisation principale : Zone agricole en Équateur.
- Emprise géographique (WGS 84 / EPSG:4326) :
  - Longitude : -79.860° à -79.788° Ouest
  - Latitude : -3.312° à -3.240° Sud
- Système de coordonnées de référence (SCR) de traitement : EPSG:32717 (WGS 84 / UTM zone 17S) pour l'alignement métrique des rasters.

---

## 3. Structure et Composition des Données

### A. Données Vectorielles (Contours des parcelles)
- Fichier : parcelles_analysees.geojson
- Format : GeoJSON (polygones).
- Contenu : 62 entités représentant les limites exactes de chaque parcelle cultivée (G0_0 à G7_7).

### B. Imagerie Satellitaire Sentinel-2 (Télédétection)
- Source : Capteur MSI (MultiSpectral Instrument) de la mission Copernicus Sentinel-2 (ESA).
- Organisation temporelle : Réparties en deux sous-répertoires (humide/ et seche/).
- Bandes spectrales exploitées :
  - B04.tif (Rouge — 665 nm) : Résolution de 10 mètres (10980 x 10980 pixels). Absorption chlorophyllienne.
  - B08.tif (Proche Infrarouge / PIR — 842 nm) : Résolution de 10 mètres (10980 x 10980 pixels). Structure cellulaire de la biomasse.
  - B11.tif (SWIR — 1610 nm) : Résolution de 20 mètres (non utilisée pour l'instant dans le calcul direct du NDVI).
- Encodage : Entiers non signés 16 bits (uint16), normalisés par division par 10 000 pour obtenir la réflectance de surface.

### C. Données Tabulaires Complémentaires (California Dataset)
- Source : Jeu de données de référence de type California (utilisé pour les tests de modélisation, de régression ou d'analyse exploratoire de données tabulaires).
- Rôle dans le projet : Support d'entraînement ou de validation croisée pour les algorithmes de traitement de données tabulaires associés aux métriques du pipeline.

### D. Sorties du Pipeline
- Fichiers générés : bulletin_parcelle.csv (saison humide) et bulletin_parcelle_seche.csv (saison sèche).
- Schéma : id (int), nom (string), ndvi_moyen / ndvi_moyen_seche (float).

---

## 4. Prétraitements et Métriques Dérivées
- Calcul du NDVI : NDVI = (B08 - B04) / (B08 + B04)
- Seuil agronomique : Seuil critique fixé à NDVI = 0.35 pour l'identification des parcelles en stress végétatif nécessitant une inspection par drone (YOLOv8n / MobileNetV3).

---

## 5. Limites et Biais Connus
- Couverture nuageuse : Impact potentiel sur les acquisitions optiques Sentinel-2 en saison humide.
- Effets de bordure : Pixels mixtes possibles sur les parcelles de très petite surface (résolution de 10 m).

---

## 6. Licence et Attribution
- Imagerie Sentinel-2 : Données ouvertes du programme Copernicus (ESA / Commission Européenne).
- Données vectorielles et résultats : Propriété du projet Field Scan.

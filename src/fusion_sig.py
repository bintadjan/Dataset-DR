
import os
import geopandas as gpd
import pandas as pd

def generate_field_bulletin():
    # Définition des chemins d'accès (ajustés pour Google Drive / Colab)
    parcels_path = '/content/drive/MyDrive/fieldscan/outputs/parcelles_grille.geojson'
    bulletin_path = '/content/drive/MyDrive/fieldscan/outputs/bulletin_grille.csv'
    output_geojson = '/content/drive/MyDrive/fieldscan/outputs/bulletin_sante_complet.geojson'

    print(" Initialisation du traitement SIG...")

    # 1. Chargement des polygones des parcelles
    if not os.path.exists(parcels_path):
        raise FileNotFoundError(f"Fichier de parcelles introuvable : {parcels_path}")
    parcels_gdf = gpd.read_file(parcels_path)
    print(f" Parcelles chargées : {len(parcels_gdf)} zones identifiées.")

    # 2. Chargement des métriques et indices (NDVI, NDMI, alertes)
    if not os.path.exists(bulletin_path):
        raise FileNotFoundError(f"Fichier de bulletin CSV introuvable : {bulletin_path}")
    df_metrics = pd.read_csv(bulletin_path)
    print(f" Métriques chargées : {len(df_metrics)} lignes de données.")

    # 3. Fusion des données spatiales et tabulaires sur la clé commune 'nom'
    merged_gdf = parcels_gdf.merge(df_metrics, on='nom', how='left')

    # 4. Sauvegarde du fichier final au format GeoJSON
    os.makedirs(os.path.dirname(output_geojson), exist_ok=True)
    merged_gdf.to_file(output_geojson, driver='GeoJSON')
    
    print(f"\n Bulletin consolidé avec succès !")
    print(f" Fichier spatial prêt pour QGIS : {output_geojson}")
    
    return merged_gdf

if __name__ == '__main__':
    generate_field_bulletin()

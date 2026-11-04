## Contexte : le bananier

**Une plante, pas un arbre.** Le bananier est une très grande herbe. Son « tronc »
est un faux-tronc formé de bases de feuilles enroulées, qui part d'une tige
souterraine (le bulbe).

**Pied mère et rejets.** Chaque pied mère produit un seul régime, puis il est coupé.
À sa base poussent des rejets (nouvelles pousses). L'agriculteur en garde un
qui remplace le pied mère : ce sont les « générations » successives. Avec le temps,
la plantation devient plus dense, et les rejets se mélangent au pied mère.

**Maladies principales.**
- *La cercosporiose noire (Black Sigatoka)* : un champignon des feuilles. Elle débute
  par de petites stries brunes, puis des taches noires cernées de jaune, et la feuille
  finit par sécher. La plante produit moins, et les traitements sont fréquents et coûteux.
- *La fusariose (Fusarium wilt)* : un champignon du sol qui attaque les vaisseaux de la
  plante. Les vieilles feuilles jaunissent, puis la plante se flétrit. Elle est difficile
  à repérer du ciel au début, et il n'existe pas de traitement.

**Besoin en eau.** Le bananier consomme beaucoup d'eau et ses racines sont peu profondes :
il souffre vite d'un manque d'irrigation.

**Ce que ça change pour le projet.**
- Compter les pieds est difficile : la canopée est dense et les rejets sont cachés
  par le pied mère.
- Les premiers symptômes de maladie mesurent quelques millimètres, bien en dessous de la
  résolution d'un satellite (10 m pour Sentinel-2).
- Les photos de feuilles prises au sol ne ressemblent pas aux images prises du ciel :
  cet écart est à documenter.


## 🗂️ Structure du Dépôt

```text
field-scan/
│
├── src/
│   ├── train_yolo.py     # Entraînement du modèle de classification YOLOv8-cls
│   └── fusion_sig.py     # Fusion des données géospatiales et métriques (NDVI, NDMI)
│
├── data_card.md          # Description détaillée du dataset (BananaLSD & Sentinel-2)
├── requirements.txt      # Dépendances du projet (Geopandas, Ultralytics, Pandas...)
└── README.md             # Documentation du projet

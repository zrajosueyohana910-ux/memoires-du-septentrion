# Guide technique — MémoireS du Septentrion

*ZRA Josue Yohana et Bambe Kennedy · IBAI, Université de Garoua · UE « Hypermédia et Web Sémantique », Master 1 Arts et Humanités · Octobre 2026*

**Version 2.1** — 17 octobre 2026

Ce guide s'adresse à un développeur ou à un relecteur technique. Il décrit l'architecture, l'installation, la chaîne de production et le déploiement du projet.

---

## 1. Présentation du projet

**MémoireS du Septentrion** est une archive hypermédia sémantique du patrimoine culturel du Septentrion camerounais (Adamaoua, Nord, Extrême-Nord). Elle relie dans un graphe RDF des peuples, des langues, des sites, des contes, des rituels, des fêtes et des instruments, puis les présente dans un prototype de 17 pages HTML.

**Livrables** :
- archive.ttl : ontologie RDF (223 triplets, 23 entités, 10 alignements Wikidata)
- 5 requêtes SPARQL (requetes.sparql)
- 17 pages HTML (n01 à n16 + 404)
- annotations.jsonld (Web Annotation Data Model)
- Charte graphique « Forêt & Mémoire » (tokens.css)
- Site déployé sur Vercel

---

## 2. Architecture générale

COUCHE 5 — PRÉSENTATION : HTML/CSS · Charte « Forêt & Mémoire »
COUCHE 4 — LOGIQUE : Navigation hiérarchique · Liens contextuels
COUCHE 3 — ACCÈS : Fuseki local · Wikidata (SERVICE)
COUCHE 2 — CONVERSION : csv_vers_turtle.py · ttl_vers_json.py
COUCHE 1 — DONNÉES : archive.ttl · 3 CSV · annotations.jsonld

---

## 3. Prérequis

- Python 3.12+ avec rdflib
- Apache Jena Fuseki (pour les requêtes SPARQL)
- Navigateur moderne (Firefox, Chrome, Safari, Edge)
- Git (pour le versionnement)

---

## 4. Installation locale

```bash
# 1. Cloner le dépôt
git clone https://github.com/zrajosueyohana910-ux/memoires-du-septentrion.git
cd memoires-du-septentrion

# 2. Créer un environnement virtuel
python3 -m venv venv
source venv/bin/activate

# 3. Installer les dépendances
pip install rdflib

# 4. Régénérer l'ontologie
python csv_vers_turtle.py donnees

# 5. Régénérer les 17 pages HTML
python generer_noeuds.py

# 6. Ouvrir le prototype
xdg-open noeuds/n01.html
```

---

## 5. Chaîne de production

```
3 CSV sources (entites, relations, alignements)
    ↓ csv_vers_turtle.py (RDFLib)
archive.ttl (223 triplets, 23 entités, 10 alignements)
    ↓ ttl_vers_json.py
patrimoine.json (11 fiches exportables)
    ↓ generer_noeuds.py
17 pages HTML (n01 à n16 + 404)
    ↓ git push
Déploiement Vercel
```

---

## 6. Structure du dépôt

```
memoires-du-septentrion/
├── 00_rendu/                    Dossier de rendu structuré
│   ├── 01_documents/            Note de cadrage, dossier de conception
│   ├── 02_ontologie/            archive.ttl
│   ├── 03_requetes/             requetes.sparql
│   ├── 04_prototype/            n01 à n16 + 404
│   ├── 05_annotations/          annotations.jsonld
│   ├── 06_sources/              CSV sources
│   └── 07_scripts/              Scripts Python
├── noeuds/                      17 pages HTML
├── donnees/                     3 CSV sources
├── archive.ttl                  Ontologie RDF
├── requetes.sparql              5 requêtes SPARQL
├── annotations.jsonld           Web Annotation
├── csv_vers_turtle.py           Génération archive.ttl
├── generer_noeuds.py            Génération des 17 pages
├── ttl_vers_json.py             Conversion JSON
├── noeud-template.html          Template des pages
├── corps_noeuds.py              Contenus des 16 nœuds
├── tokens.css                   Charte « Forêt & Mémoire »
├── guide-technique.md           Ce guide
└── guide-utilisation.md         Guide utilisateur
```

---

## 7. Déploiement

### 7.1 GitHub

```bash
git init
git add .
git commit -m "init: MémoireS du Septentrion"
git remote add origin https://github.com/VOTRE-USER/memoires-du-septentrion.git
git push -u origin main
```

### 7.2 Vercel

1. Connecter le dépôt GitHub à Vercel
2. Root Directory : public
3. Framework Preset : Other
4. Deploy

**URL** : https://memoires-du-septentrion.vercel.app

---

## 8. Problèmes connus

| Problème | Cause | Solution |
|---|---|---|
| QC2 vide | Aucune source ne relie instruments, rituels, peuples | Assumé, propriétés prêtes |
| Médias absents | Droits à clarifier (INALCO/CNRS) | Autorisations à obtenir |
| Domaine fictif | memoria-nord.cm n'existe pas | Mini-serveur 303 à simuler |
| CORS Fuseki | Blocage navigateur → Fuseki | Proxy local ou requêtes depuis Fuseki |
| WGS84 non relevées | Coordonnées à saisir pour la carte | Relever sur OpenStreetMap |

---

## 9. Perspectives techniques

- Valider l'ontologie dans Protégé (HermiT)
- Visualiser avec WebVOWL
- Brancher les nœuds sur Fuseki en live
- Intégrer les médias (audio, vidéo, images)
- Relever les coordonnées WGS84 pour la carte
- Étendre le corpus aux autres peuples du Septentrion

---

*Version 2.1 · 17 octobre 2026 · ZRA Josue Yohana et Bambe Kennedy*

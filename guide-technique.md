# Guide technique : MémoireS du Nord

*ZRA et Bambe Kennedy · IBAI, Université de Garoua · UE « Hypermédia et Web Sémantique », Master 1 Arts et Humanités · Octobre 2026*

Ce guide s'adresse à un relecteur technique ou à un développeur qui veut comprendre et reproduire le projet. Pour la navigation dans l'archive, voir `guide-utilisation.md`.

## 1. Présentation du projet

MémoireS du Nord est une archive hypermédia sémantique du patrimoine culturel du Nord-Cameroun. Elle relie dans un graphe RDF des peuples, des langues, des sites, des contes, des rituels, des fêtes et des instruments, puis les présente dans un prototype de 9 pages HTML.

Livrables : un graphe `archive.ttl` (133 triplets, 23 entités dont la fiche du jeu de données, 10 alignements Wikidata vérifiés), 5 requêtes SPARQL, 9 pages hypermédias, un exemple d'annotations (Web Annotation et Media Fragments), une ontologie et un script de génération.

## 2. Architecture générale

```
COUCHE 4  PRÉSENTATION   HTML/CSS · Leaflet · YASGUI · JSON-LD
              ↕
COUCHE 3  LOGIQUE        liens contextuels · fiches par SPARQL
              ↕
COUCHE 2  ACCÈS          Fuseki local · mini-serveur 303 · Wikidata (SERVICE)
              ↕
COUCHE 1  DONNÉES        archive.ttl · alignements · annotations
```

Les requêtes descendent de la présentation vers les données, les résultats remontent. Seul Wikidata est un service extérieur au projet.

## 3. Prérequis techniques

- Python 3.12 ou plus, avec la bibliothèque `rdflib`.
- Apache Jena Fuseki, qui exige un environnement Java (version indiquée par la documentation de votre version de Fuseki).
- Un navigateur moderne.
- Une connexion Internet pour Leaflet, les tuiles de la carte et la requête fédérée QC4 (Wikidata).

## 4. Installation pas à pas

1. Récupérer le dossier du projet et s'y placer.
2. Créer un environnement virtuel :
   ```bash
   python -m venv .venv
   source .venv/bin/activate        # Windows : .venv\Scripts\activate
   ```
3. Installer la dépendance : `pip install rdflib`
4. Vérifier que les fichiers de la section 6 sont présents, en particulier le dossier `donnees/`.

## 5. Chaîne de production des données

1. **Sources** : trois CSV dans `donnees/` : `entites.csv` (entités et classes), `relations.csv` (triplets), `alignements.csv` (liens vers Wikidata, avec la colonne `verifie`).
2. **Contrôle** : `python csv_vers_turtle.py donnees --verifier` refuse les références orphelines et signale les alignements non vérifiés.
3. **Génération** : `python csv_vers_turtle.py donnees` écrit `archive.ttl`. Seuls les alignements marqués vérifiés y entrent ; les autres vont dans `alignements_a_verifier.ttl`.
4. **Chargement dans Fuseki** : soit via l'interface (`http://localhost:3030`, nouveau jeu de données puis import de `archive.ttl`), soit en ligne de commande :
   ```bash
   fuseki-server --file=archive.ttl /memoires
   ```
5. **Interrogation** : ouvrir YASGUI, pointer vers l'endpoint (`http://localhost:3030/memoires/sparql`, ou `/query` selon la version) et exécuter une requête de `requetes.sparql`, une à la fois.

## 6. Structure des fichiers

```
memoires-du-nord/
├── donnees/
│   ├── entites.csv              entités et classes
│   ├── relations.csv            triplets
│   └── alignements.csv          alignements externes
├── csv_vers_turtle.py           contrôle + génération Turtle
├── archive.ttl                  graphe généré
├── alignements_a_verifier.ttl   alignements en attente (généré)
├── ontologie-memoires-du-nord.ttl   classes et propriétés
├── requetes.sparql              QC1 à QC5
├── annotations.jsonld           exemple Web Annotation
├── noeud-template.html          gabarit des pages
├── generer_noeuds.py            génère n01 à n09
├── noeuds/                      n01.html … n09.html
└── media/                       à créer (non fourni, voir section 7)
```

## 7. Problèmes connus et solutions

- **QC2 renvoie 0 résultat.** Aucune source ne relie instruments, rituels et peuples ; nous n'avons rien inventé. Les propriétés `mv:jouePendant` et `mv:joueParPeuple` sont déclarées et la requête est prête : il suffit d'ajouter des lignes dans `relations.csv` quand la source existe.
- **CORS.** Un navigateur peut bloquer les appels d'une page vers l'endpoint Fuseki local. Solution : passer par un proxy local, ou interroger directement depuis l'interface de Fuseki. Les pages actuelles sont statiques et n'interrogent pas Fuseki.
- **Médias non intégrés.** Les pages référencent `media/…` (photos, vidéos, audio, sous-titres WebVTT) qui n'existent pas encore : les droits sont à clarifier, en particulier pour les contes issus d'un fonds de recherche.
- **Redirection 303.** Le domaine `memoria-nord.cm` est fictif : un mini-serveur local doit simuler la redirection `/id/` vers `/page/` ou `/data/`, car Fuseki ne la fait pas.
- **QC4 dépend d'Internet** : sans accès à Wikidata, la requête fédérée échoue ou revient vide.

## 8. Perspectives techniques

- Valider l'ontologie dans Protégé (raisonneur HermiT) et la visualiser avec OntoGraf ou WebVOWL.
- Brancher les pages sur Fuseki (fiches par SPARQL, annotations sur les images) avec `textContent` pour éviter l'injection.
- Intégrer les médias une fois les droits établis, avec leurs annotations.
- Déployer en ligne avec une vraie résolution `/id/`, `/page/`, `/data/`.

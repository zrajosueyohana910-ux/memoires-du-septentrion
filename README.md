cd ~/Téléchargements/hypermedia_web_semantique
source venv/bin/activate

python3 << 'PYEOF'
from pathlib import Path

contenu = """# MémoireS du Septentrion

**Archive hypermédia sémantique du patrimoine culturel du Septentrion camerounais**
(Adamaoua · Nord · Extrême-Nord)

---

## À propos du projet

Ce projet explore le patrimoine culturel du Septentrion camerounais à travers une **archive hypermédia sémantique**. Il comporte plusieurs dimensions :

- **Modélisation sémantique** : une ontologie RDF (`archive.ttl`) avec 223 triplets, 23 entités et 10 alignements Wikidata vérifiés.
- **Interrogation** : 5 requêtes SPARQL (dont 1 fédérée vers Wikidata et 1 agrégat).
- **Prototype hypermédia** : 16 nœuds HTML navigables + 1 page 404, avec annotations Web Annotation Data Model.
- **Charte graphique** : « Forêt & Mémoire » (vert forêt, or safran, crème).

---

## Stack technique

- **Ontologie** : RDF, Turtle, DCTerms, FOAF, SKOS, schema.org, PROV-O, Europeana Data Model
- **Requêtes** : SPARQL (Apache Jena Fuseki, YASGUI)
- **Prototype** : HTML/CSS statique, JSON-LD, Web Annotation
- **Scripts** : Python 3.12 + RDFLib
- **Charte** : CSS avec variables (tokens)

---

## Structure du dépôt
memoires-du-septentrion/
├── 00_rendu/ Dossier de rendu structuré
│ ├── 01_documents/ Note de cadrage, dossier de conception, guides
│ ├── 02_ontologie/ archive.ttl
│ ├── 03_requetes/ requetes.sparql
│ ├── 04_prototype/ n01 à n16 + 404
│ ├── 05_annotations/ annotations.jsonld
│ ├── 06_sources/ CSV sources
│ └── 07_scripts/ Scripts Python
├── noeuds/ 16 nœuds HTML + 404
├── donnees/ 3 CSV sources
├── archive.ttl Ontologie RDF (223 triplets)
├── requetes.sparql 5 requêtes SPARQL
├── annotations.jsonld Web Annotation Data Model
├── csv_vers_turtle.py Génération de archive.ttl
├── generer_noeuds.py Génération des 16 nœuds
├── ttl_vers_json.py Conversion vers JSON
├── noeud-template.html Template des nœuds
├── corps_noeuds.py Contenus des 16 nœuds
├── tokens.css Charte graphique « Forêt & Mémoire »
├── guide-technique.md
└── guide-utilisation.md

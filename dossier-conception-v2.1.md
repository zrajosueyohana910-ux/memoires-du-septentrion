# Dossier de conception — MémoireS du Septentrion

*ZRA Josue Yohana et Bambe Kennedy · IBAI, Université de Garoua · UE « Hypermédia et Web Sémantique », Master 1 Arts et Humanités · Octobre 2026*

**Version 2.1** — remplace la version 2.0 (17 octobre 2026)

---

## 1. Objet du document

Ce dossier de conception décrit les choix techniques et méthodologiques du projet **MémoireS du Septentrion**, une archive hypermédia sémantique du patrimoine culturel du Septentrion camerounais (Adamaoua, Nord, Extrême-Nord). Il remplace la version 2.0 et intègre les enrichissements récents : extension du périmètre aux 3 régions, refonte de la navigation (4 liens + 5 catégories), charte graphique « Forêt & Mémoire », déploiement sur Vercel.

Il prolonge la note de cadrage et précède les guides technique et d'utilisation.

---

## 2. Modèle de données

### 2.1 Entités et classes locales

Le corpus compte **23 entités**, réparties dans huit classes locales (préfixe `mv:`) rattachées à des classes standard :

| Classe locale | Classe parente | Entités |
|---|---|---|
| `mv:Peuple` | `foaf:Group` | Kapsiki, Mafa, Fulbe |
| `mv:Langue` | `dct:LinguisticSystem` | Psikyɛ, Fulfulde |
| `mv:Site` | `schema:Place` | Diy-Gid-Biy, Rhumsiki, Lamidat de Garoua |
| `mv:Lieu` | `schema:Place` | Monts Mandara, Garoua, Bibemi, Cameroun |
| `mv:RecueilDeContes` | `edm:ProvidedCHO` | Contes de Goggo Addi |
| `mv:Rituel` | `schema:Event` | Rituels mafa |
| `mv:Fete` | `schema:Event` | Msla, Goalala, Maray |
| `mv:Instrument` | *(aucune)* | Balafon, Tambour d'eau, Corne-flûte |

**Personnes** (`foaf:Person`) : Goggo Addi, Ursula Baumgardt.
**Métadonnées du jeu de données** (`dcat:Dataset`) : `dataset:archive`.

### 2.2 Décisions de modélisation

- **Goggo Addi est modélisée comme une personne**. Le recueil de contes est une entité distincte, reliée par `dct:creator` (Goggo Addi) et `dct:contributor` / `prov:wasAttributedTo` (Ursula Baumgardt). Cette séparation permet à QC1 de répondre précisément à « collectés par qui ? ».
- **Goge et Garaya sont retirés** : la source consultée ne les rattache pas au Septentrion.
- **Les périodes des sites** sont notées par deux entiers (`mv:siecleDebut`, `mv:siecleFin`). Seul Diy-Gid-Biy en porte une (XIIe-XVIIe siècle).
- **Le nombre de locuteurs** est rattaché à la langue Psikyɛ.

### 2.3 Propriétés

**Propriétés réutilisées** : `dct:language`, `dct:spatial`, `dct:relation`, `dct:creator`, `dct:contributor`, `dct:temporal`, `schema:containedInPlace`, `schema:birthPlace`, `schema:deathPlace`, `prov:wasAttributedTo`, `skos:prefLabel`, `skos:altLabel`, `skos:scopeNote`.

**Propriétés locales** : `mv:associeAuPeuple`, `mv:pratiquePar`, `mv:siecleDebut`, `mv:siecleFin`, `mv:inscritUnesco`, `mv:critereUnesco`, `mv:region`, `mv:categorie`, `mv:niveau`, `mv:miseEnAvant`.

**Prévues mais non peuplées** : `mv:jouePendant` et `mv:joueParPeuple` (QC2).

### 2.4 Vocabulaires

DCTerms, FOAF, SKOS, schema.org, PROV-O, Europeana Data Model, Web Annotation, Media Fragments.

---

## 3. URI et Linked Data

- **Schéma** : `/id/{type}/{slug}` (chose), `/page/` (HTML), `/data/` (RDF).
- **Redirection 303** : `/id/` → `/page/` ou `/data/` selon le client.
- **Domaine fictif** : `memoria-nord.cm` (à simuler localement).

---

## 4. Architecture en 5 couches

COUCHE 5 — PRÉSENTATION
HTML/CSS (17 nœuds) · Charte « Forêt & Mémoire »
↕
COUCHE 4 — LOGIQUE
Navigation hiérarchique (4 liens + 5 catégories) · Liens contextuels
↕
COUCHE 3 — ACCÈS
Fuseki local · Wikidata (SERVICE)
↕
COUCHE 2 — CONVERSION
csv_vers_turtle.py · ttl_vers_json.py
↕
COUCHE 1 — DONNÉES
archive.ttl (223 triplets) · 3 CSV · annotations.jsonld
text


---

## 5. Alignements Wikidata

**Règle** :
- `owl:sameAs` : individus (lieux, sites, personnes)
- `skos:exactMatch` : concepts exacts (langues, peuples, instruments)
- `skos:closeMatch` : correspondances approximatives

**Les 10 alignements vérifiés** (contrôlés manuellement le 13/10/2026) :

| # | Entité locale | Q-id | Relation |
|---|---|---|---|
| 1 | `langue:psikye` | Q56304 | `skos:exactMatch` |
| 2 | `langue:fulfulde` | Q33454 | `skos:exactMatch` |
| 3 | `peuple:fulbe` | Q202575 | `skos:exactMatch` |
| 4 | `instrument:balafon` | Q789141 | `skos:exactMatch` |
| 5 | `lieu:cameroun` | Q1009 | `owl:sameAs` |
| 6 | `lieu:garoua` | Q157915 | `owl:sameAs` |
| 7 | `peuple:kapsiki` | Q2437423 | `skos:closeMatch` |
| 8 | `peuple:mafa` | Q3276439 | `skos:closeMatch` |
| 9 | `lieu:monts-mandara` | Q1888885 | `owl:sameAs` |
| 10 | `site:diy-gid-biy` | Q5285004 | `owl:sameAs` |

**Corrections documentées** :
- Q1000 (Gabon) → Q1009 (Cameroun)
- Q312582 (incorrect) → Q157915 (Garoua)

---

## 6. Questions de compétence et requêtes SPARQL

| QC | Question | Type | État |
|---|---|---|---|
| **QC1** | Contes par peuple, langue, collectrice | Sélection | ✅ |
| **QC2** | Instruments / rituels / peuples | Sélection | ⚠️ Vide |
| **QC3** | Sites des Monts Mandara et période | Sélection | ✅ |
| **QC4** | Libellé et description Wikidata | Fédérée | ✅ |
| **QC5** | Comptage par catégorie | Agrégat | ✅ |

**Résultats** : QC1 (1 ligne), QC3 (2 sites), QC4 (10 lignes), QC5 (23 entités).

---

## 7. Prototype hypermédia (17 pages)

| Fichier | Titre | Catégorie |
|---|---|---|
| n01 | Accueil | — |
| n02 | Explorer | Index |
| n03 | Peuples | Liste |
| n04 | Langues | Liste |
| n05 | Sites patrimoniaux | Liste |
| n06 | Rituels et fêtes | Liste |
| n07 | Instruments | Liste |
| n08 | Contribuer | — |
| n09 | À propos | — |
| n10 | Diy-Gid-Biy | Fiche |
| n11 | Kapsiki | Fiche |
| n12 | Mafa | Fiche |
| n13 | Fulbe | Fiche |
| n14 | Contes de Goggo Addi | Fiche |
| n15 | Rituels mafa | Fiche |
| n16 | Balafon | Fiche |
| 404 | Page introuvable | — |

**Navigation** :

Accueil → Explorer → 5 catégories → fiches détaillées
text


**Lois UX respectées** :
- **Hick** : 4 choix principaux
- **Fitts** : zones tactiles ≥ 44px
- **Nielsen** : cohérence, reconnaissance, page 404

---

## 8. Charte graphique « Forêt & Mémoire »

| Rôle | Couleur | Code |
|---|---|---|
| Primaire | Vert forêt | `#1B4332` |
| Secondaire | Or safran | `#D4A017` |
| Accent | Rouge terre | `#A63A2A` |
| Fond | Crème | `#FAF6EE` |
| Texte | Encre verte | `#1A2E22` |

**Typographies** : Cormorant Garamond (titres) + Inter (texte).

**Mode sombre** : automatique via `prefers-color-scheme`.

---

## 9. Annotation multimédia

Modèle **Web Annotation Data Model** avec Media Fragments :
- `xywh=pixel:x,y,l,h` pour les zones d'image
- `t=debut,fin` pour les extraits audio/vidéo
- Motivations : `identifying` (relier à une entité) et `describing` (description)

---

## 10. Licences, droits et provenance

- **Métadonnées** : CC BY 4.0
- **Contes de Goggo Addi** : droits INALCO/CNRS à préciser
- **Provenance** : `dct:source` + `prov:wasAttributedTo` par entité
- **Illustrations IA** : mention explicites dans les crédits

---

## 11. Déploiement

- **Dépôt GitHub** : `github.com/zrajosueyohana910-ux/memoires-du-septentrion`
- **Site Vercel** : `memoires-du-septentrion.vercel.app`
- **Dossier de rendu** : `00_rendu/` (7 sections structurées)

---

## 12. Perspectives techniques

- Valider l'ontologie dans Protégé
- Brancher les nœuds HTML sur Fuseki
- Intégrer les médias (après clarification des droits)
- Relever les coordonnées WGS84 pour la carte
- Étendre le corpus à d'autres peuples du Septentrion

---

*Version 2.1 · 17 octobre 2026 · ZRA Josue Yohana et Bambe Kennedy*

# Note de cadrage — MémoireS du Septentrion

*ZRA Josue Yohana et Bambe Kennedy · IBAI, Université de Garoua · UE « Hypermédia et Web Sémantique », Master 1 Arts et Humanités · Octobre 2026*

**Version 2.1** — remplace la version 2.0 (17 octobre 2026)

---

## 1. Sujet

**MémoireS du Septentrion** est une archive hypermédia sémantique du patrimoine culturel du Septentrion camerounais (Adamaoua, Nord, Extrême-Nord). Elle relie, dans un graphe de données RDF, des peuples, des langues, des sites, des contes, des rituels, des fêtes et des instruments de musique, puis les présente dans un prototype hypermédia de 17 pages HTML.

Le projet comporte plusieurs dimensions :

- **Modélisation sémantique** : ontologie RDF (`archive.ttl`) avec 223 triplets, 23 entités et 10 alignements Wikidata vérifiés.
- **Interrogation** : 5 requêtes SPARQL (dont 1 fédérée vers Wikidata et 1 agrégat).
- **Prototype hypermédia** : 16 nœuds HTML + 1 page 404, avec annotations Web Annotation Data Model.
- **Charte graphique** : « Forêt & Mémoire » (vert forêt, or safran, crème).
- **Navigation** : 4 liens principaux + 5 sous-catégories (loi de Hick respectée).
- **Déploiement** : site en ligne sur Vercel.

---

## 2. Contexte et justification

Le patrimoine du Septentrion camerounais est riche mais dispersé et peu structuré en données ouvertes. L'inscription récente du paysage culturel de Diy-Gid-Biy au patrimoine mondial de l'UNESCO (juillet 2025) renforce l'intérêt de documenter la région.

Un graphe lié à Wikidata et interrogeable en SPARQL rend ces connaissances **réutilisables**, **vérifiables** et **traçables**, avec leur provenance. C'est une démarche typique des humanités numériques.

---

## 3. Objectifs

### 3.1 Objectif général

Concevoir et publier une archive hypermédia sémantique du patrimoine culturel du Septentrion camerounais, en associant modélisation RDF, requêtes SPARQL, prototype HTML accessible et charte graphique cohérente.

### 3.2 Objectifs spécifiques

| N° | Objectif | Indicateur |
|---|---|---|
| O1 | **Modéliser** un graphe RDF cohérent | ≥ 50 triplets, ≥ 15 entités |
| O2 | **Interroger** le graphe en SPARQL | 5 requêtes (dont 1 fédérée, 1 agrégat) |
| O3 | **Aligner** les entités sur des bases externes | ≥ 10 alignements vérifiés |
| O4 | **Publier** un prototype hypermédia accessible | ≥ 8 nœuds, ≥ 3 types de médias |
| O5 | **Structurer** la navigation selon les lois UX | 4 liens + 5 catégories |
| O6 | **Déployer** le prototype en ligne | Site Vercel accessible |

### 3.3 État d'avancement (17 octobre 2026)

| Exigence | Seuil | État |
|---|---|---|
| Triplets RDF | ≥ 50 | **223** ✅ |
| Entités | ≥ 15 | **23** ✅ |
| Requêtes SPARQL | 5 (dont 1 fédérée, 1 agrégat) | **5 écrites** (QC2 vide assumée) ⚠️ |
| Alignements externes | ≥ 10 | **10 vérifiés** ✅ |
| Nœuds hypermédias | ≥ 8 | **17** (16 nœuds + 404) ✅ |
| Accessibilité | WCAG AA | ✅ |
| Charte graphique | — | **« Forêt & Mémoire »** ✅ |
| Navigation UX | Hick, Fitts, Nielsen | ✅ |
| Déploiement | — | **Vercel** ✅ |

---

## 4. Public visé

| Public | Besoin | Apport du projet |
|---|---|---|
| **Étudiants et jeunes chercheurs** | Ressources fiables, méthodes | Fiches structurées, requêtes SPARQL |
| **Chercheurs** | Sources vérifiables, données ouvertes | Ontologie RDF, alignements Wikidata |
| **Acteurs culturels locaux** | Visibilité du patrimoine | Documentation structurée |
| **Grand public et diaspora** | Découverte accessible | Site en ligne, navigation simple |

---

## 5. Corpus

Le corpus compte **23 entités** organisées en 10 catégories :

| Catégorie | Entités | Nombre |
|---|---|---|
| Peuples | Kapsiki, Mafa, Fulbe | 3 |
| Langues | Psikyɛ, Fulfulde | 2 |
| Sites | Diy-Gid-Biy, Rhumsiki, Lamidat de Garoua | 3 |
| Lieux | Monts Mandara, Garoua, Bibemi, Cameroun | 4 |
| Recueil de contes | Contes de Goggo Addi | 1 |
| Rituels | Rituels mafa | 1 |
| Fêtes | Msla, Goalala, Maray | 3 |
| Instruments | Balafon, Tambour d'eau, Corne-flûte | 3 |
| Personnes | Goggo Addi, Ursula Baumgardt | 2 |
| Métadonnées | dataset:archive | 1 |

**Tous les identifiants Wikidata ont été vérifiés manuellement** le 13 octobre 2026. Deux corrections ont été nécessaires :
- Cameroun : Q1009 (et non Q1000, qui est le Gabon)
- Garoua : Q157915 (et non Q312582)

---

## 6. Questions de compétence

| QC | Question | Type | État |
|---|---|---|---|
| **QC1** | Quels contes sont associés à quel peuple, dans quelle langue et collectés par qui ? | Sélection | ✅ |
| **QC2** | Quels instruments sont joués lors de quels rituels ou fêtes, et par quels peuples ? | Sélection | ⚠️ Vide |
| **QC3** | Quels sites patrimoniaux sont situés dans les Monts Mandara, et à quelle période remontent-ils ? | Sélection | ✅ |
| **QC4** | Pour chaque entité alignée, quels sont le libellé et la description correspondants sur Wikidata ? | Fédérée | ✅ |
| **QC5** | Combien d'entités par catégorie compte le graphe ? | Agrégat | ✅ |

**QC2 est une limite assumée** : aucune source ne relie instruments, rituels et peuples.

---

## 7. Architecture et outils

### 7.1 Architecture en 5 couches

| Couche | Composants | État |
|---|---|---|
| **5. Présentation** | HTML/CSS (17 nœuds), charte « Forêt & Mémoire » | ✅ |
| **4. Logique** | Navigation hiérarchique, liens contextuels | ✅ |
| **3. Accès** | Fuseki local, Wikidata (SERVICE) | ⏳ À charger |
| **2. Conversion** | csv_vers_turtle.py, ttl_vers_json.py | ✅ |
| **1. Données** | archive.ttl, 3 CSV, annotations.jsonld | ✅ |

### 7.2 Outils

- **RDFLib** (Python) : manipulation du graphe
- **Apache Jena Fuseki** : serveur SPARQL local
- **YASGUI** : interface de requêtes SPARQL
- **Leaflet** : carte interactive
- **Git/GitHub** : versionnement
- **Vercel** : déploiement

### 7.3 Vocabulaires

DCTerms, FOAF, SKOS, schema.org, PROV-O, Europeana Data Model, Web Annotation, Media Fragments.

---

## 8. Rôles

| Membre | Responsabilités |
|---|---|
| **ZRA Josue Yohana** (CM-UGa-23IBAI0093) | Conception, ontologie, UI/UX, documentation |
| **Bambe Kennedy** (CM-UGa-23IBAI0096) | Données RDF, requêtes SPARQL, démonstration technique |

---

## 9. Risques et points de vigilance

| Risque | Impact | Parade |
|---|---|---|
| **QC2 vide** | Moyen | Assumé, propriétés prêtes à être peuplées |
| **Droits des contes** | Élevé | Déclaration `dct:rights` en cours (INALCO/CNRS) |
| **Médias absents** | Moyen | Autorisations à obtenir ; placeholder explicite |
| **Domaine fictif** | Faible | Mini-serveur 303 à simuler |
| **CORS Fuseki/navigateur** | Moyen | Proxy local ou requêtes depuis Fuseki |
| **Charge horaire** | Élevé | Priorisation sur les livrables obligatoires |

---

## 10. Étapes

| Étape | État |
|---|---|
| 1. Cadrage | ✅ Fait (v2.1) |
| 2. Conception | ✅ Dossier de conception v2.1 |
| 3. Réalisation | ✅ Archive RDF, 5 requêtes, 17 nœuds HTML |
| 4. Tests | ⏳ À faire (requêtes, utilisateurs) |
| 5. Documentation | ✅ Guide technique, guide d'utilisation |
| 6. Déploiement | ✅ Vercel |
| 7. Soutenance | ⏳ À préparer |

---

## 11. Charte graphique et navigation

### 11.1 Charte « Forêt & Mémoire »

| Rôle | Couleur | Code |
|---|---|---|
| Primaire | Vert forêt | `#1B4332` |
| Secondaire | Or safran | `#D4A017` |
| Accent | Rouge terre | `#A63A2A` |
| Fond | Crème | `#FAF6EE` |
| Texte | Encre verte | `#1A2E22` |

**Typographies** : Cormorant Garamond (titres) + Inter (texte).

### 11.2 Navigation et lois UX

MémoireS du Septentrion
├── Accueil (n01)
├── Explorer (n02)
│ ├── Peuples (n03)
│ ├── Langues (n04)
│ ├── Sites patrimoniaux (n05)
│ ├── Rituels et fêtes (n06)
│ └── Instruments (n07)
├── Contribuer (n08)
└── À propos (n09)
text


**Lois UX respectées** :
- **Hick** : 4 choix principaux (au lieu de 9)
- **Fitts** : zones tactiles ≥ 44px
- **Nielsen** : cohérence, reconnaissance, page 404

---

## 12. Liens

- **Dépôt GitHub** : `github.com/zrajosueyohana910-ux/memoires-du-septentrion`
- **Site Vercel** : `memoires-du-septentrion.vercel.app`
- **Ontologie** : `archive.ttl` (223 triplets)

---

*Version 2.1 · 17 octobre 2026 · ZRA Josue Yohana et Bambe Kennedy*

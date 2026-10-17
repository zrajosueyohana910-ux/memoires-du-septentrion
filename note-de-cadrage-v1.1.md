# Note de cadrage : MémoireS du Nord

**Version 1.1 · 13 octobre 2026** (remplace la version 1.0)

ZRA et Bambe Kennedy · Institut des Beaux-Arts et de l'Innovation (IBAI), Université de Garoua · UE « Hypermédia et Web Sémantique », Master 1 Arts et Humanités

## 1. Sujet

« MémoireS du Nord » est une archive hypermédia sémantique du patrimoine culturel du Nord-Cameroun. Elle relie, dans un graphe RDF, des peuples, des langues, des sites, des contes, des rituels, des fêtes et des instruments de musique, puis les présente sous forme de pages hypermédias navigables et annotées. Le projet relève de l'option « archive hypermédia annotée / édition numérique sémantique ». Il sera présenté en séance 12 (soutenance orale de 10 minutes et démonstration).

## 2. Contexte et justification

Le patrimoine du Nord-Cameroun est riche mais dispersé et peu structuré en données ouvertes. L'inscription du paysage culturel de Diy-Gid-Biy à l'UNESCO (juillet 2025, source à citer) renforce l'intérêt de le documenter. Un graphe lié à Wikidata rend ces connaissances interrogeables, réutilisables et vérifiables, avec leur provenance.

## 3. Objectifs et état d'avancement

- Modéliser et publier un graphe RDF cohérent sur au moins 15 entités.
- Interroger ce graphe par 5 requêtes SPARQL, dont une d'agrégat et une fédérée vers Wikidata.
- Aligner au moins 10 entités sur des bases externes.
- Réaliser un prototype hypermédia d'au moins 8 nœuds, avec au moins 3 types de médias, des annotations (Web Annotation, Media Fragments) et une accessibilité soignée.

| Exigence | Seuil | État au 13 octobre 2026 |
|---|---|---|
| Triplets RDF | ≥ 50 (visé : 80 à 120) | **133** : seuil et cible dépassés ✅ |
| Entités | ≥ 15 | **23** (22 entités du corpus et la fiche de métadonnées du jeu de données) ✅ |
| Requêtes SPARQL | 5, dont 1 agrégat et 1 fédérée | 5 écrites ; QC1, QC3, QC4 et QC5 fonctionnelles, **QC2 vide** faute de source ⚠️ |
| Alignements externes | ≥ 10 | **10 vérifiés** sur Wikidata ✅ |
| Nœuds hypermédias | ≥ 8, avec ≥ 3 types de médias | **9 nœuds générés** ; fichiers médias **non intégrés** (droits à clarifier) ⚠️ |
| Accessibilité | alt, WebVTT, contrastes, clavier | structure en place (mode sombre automatique, navigation au clavier, lien d'évitement) ; textes alternatifs et sous-titres **à rédiger** ⚠️ |
| Annotation multimédia | Web Annotation, Media Fragments | fichier d'exemple réalisé ✅ |
| Licence et provenance | CC BY 4.0 ou ODbL, `dct:source`, `prov:` | licence déclarée sur les métadonnées ✅ ; `dct:source` par entité **à renseigner** ⏳ |

Sur les 133 triplets, environ 95 décrivent le corpus ; les autres déclarent le vocabulaire local (une vingtaine), la fiche du jeu de données et les 10 alignements.

## 4. Public visé (à valider avec l'enseignant)

Étudiants et chercheurs en humanités numériques, acteurs culturels locaux, grand public intéressé par le patrimoine du Nord.

## 5. Corpus

Le corpus compte 23 entités :

| Catégorie | Entités | Nombre |
|---|---|---|
| Peuples | Kapsiki, Mafa, Fulbe | 3 |
| Langues | Psikyɛ, Fulfulde | 2 |
| Sites | Diy-Gid-Biy, Rhumsiki, Lamidat de Garoua | 3 |
| Lieux | Monts Mandara, Garoua, Bibemi, Cameroun | 4 |
| Recueil de contes | Contes de Goggo Addi | 1 |
| Rituels | Rituels mafa | 1 |
| Fêtes | Msla, Goalala, Maray | 3 |
| Instruments | Balafon, tambour d'eau, corne-flûte | 3 |
| Personnes | Goggo Addi (conteuse peule), Ursula Baumgardt (collectrice, INALCO et CNRS) | 2 |
| Métadonnées | Fiche du jeu de données (`dataset:archive` : licence, créateurs, date) | 1 |

La fiche du jeu de données n'est pas une entité patrimoniale : elle porte les métadonnées du graphe. Goggo Addi est modélisée comme une personne, et son recueil comme une entité distincte.

Tous les identifiants Wikidata ont été vérifiés manuellement sur wikidata.org le 13 octobre 2026. Deux corrections ont été nécessaires : le Cameroun est Q1009 (et non Q1000, qui correspond au Gabon) et Garoua est Q157915 (et non Q312582). Les alignements non vérifiés sont automatiquement séparés par le script dans `alignements_a_verifier.ttl`, aujourd'hui vide.

## 6. Questions de compétence

| QC | Question | Type | État |
|---|---|---|---|
| QC1 | Quels contes sont associés à quel peuple, dans quelle langue et collectés par qui ? | sélection | fonctionnelle |
| QC2 | Quels instruments sont joués lors de quels rituels ou fêtes, et par quels peuples ? | sélection | **vide** : aucune source ne relie instruments, rituels et peuples |
| QC3 | Quels sites patrimoniaux sont situés dans les Monts Mandara, et à quelle période remontent-ils ? | sélection | fonctionnelle |
| QC4 | Pour chaque entité alignée, quels sont le libellé et la description correspondants sur Wikidata ? | **fédérée** | fonctionnelle (accès Internet requis) |
| QC5 | Combien d'entités par catégorie compte le graphe ? | **agrégat** | fonctionnelle |

QC2 est une limite assumée : nous n'avons pas inventé de liens. Les propriétés nécessaires sont déjà déclarées dans l'ontologie.

## 7. Architecture et outils

| Couche | Composants | État |
|---|---|---|
| 4. Présentation | HTML/CSS, Leaflet, YASGUI, JSON-LD | 9 pages statiques générées ✅ |
| 3. Logique | liens contextuels, fiches par SPARQL | liens contextuels faits ; fiches par SPARQL **à faire** |
| 2. Accès | Fuseki local, mini-serveur 303, Wikidata (`SERVICE`) | Fuseki **à charger pour la démo** ; 303 à simuler ⏳ |
| 1. Données | `archive.ttl`, alignements, annotations | générés ✅ |

Les URI suivent le schéma `/id/`, `/page/`, `/data/` (10 types de ressources). Deux scripts Python produisent les livrables : `csv_vers_turtle.py` (trois CSV vers `archive.ttl`, avec refus des références orphelines) et `generer_noeuds.py` (9 pages HTML à partir d'un gabarit). Autres outils : RDFLib, Protégé, WebVOWL, VS Code. Vocabulaires : DCTerms, FOAF, SKOS, schema.org, PROV-O, Europeana Data Model.

## 8. Rôles

| Membre | Responsabilités |
|---|---|
| ZRA | conception, ontologie, soutenance orale |
| Bambe Kennedy | données RDF, requêtes SPARQL, démonstration technique |

## 9. Risques et points de vigilance

- **QC2 vide** : source manquante, limite assumée et présentée comme telle.
- **Droits** : les contes de Goggo Addi proviennent d'une collecte de recherche. Leur régime de droits sera établi et déclaré avec `dct:rights`, la licence CC BY 4.0 ne couvrant que les métadonnées produites par le binôme.
- **Médias absents** : sans photos, vidéo et audio réels, le critère des trois types de médias n'est pas démontré tant que les droits ne sont pas clarifiés.
- **Technique** : accès Internet nécessaire à QC4 et aux cartes, restrictions CORS entre navigateur et Fuseki, redirection 303 à simuler (domaine fictif), insertion de contenu sécurisée en JavaScript (`textContent`).
- **Données à compléter** : coordonnées géographiques des lieux pour la carte, peuple associé à chaque fête.
- **Charge horaire** : le cours signale 54 h de travail pour 45 h officielles ; l'effort se concentre sur les livrables.

## 10. Étapes

| Étape | État |
|---|---|
| 1. Cadrage | fait (version 1.1) |
| 2. Conception | dossier de conception rédigé ; ontologie écrite, à valider sous Protégé |
| 3. Réalisation | environ 80 % : `archive.ttl` généré, 5 requêtes écrites, 9 nœuds générés ; Fuseki à charger pour la démo |
| 4. Tests | à faire : vérification des requêtes, essai auprès de 2 à 3 utilisateurs |
| 5. Documentation | guide technique rédigé, guide d'utilisation à venir, licences et sources à compléter |
| 6. Soutenance | à préparer : 10 minutes, du contexte aux limites, avec démonstration en direct |

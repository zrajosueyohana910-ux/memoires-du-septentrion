# Dossier de conception : MémoireS du Nord

**Version 1.1 · 13 octobre 2026** (remplace la version 1.0)

ZRA et Bambe Kennedy · Institut des Beaux-Arts et de l'Innovation (IBAI), Université de Garoua · UE « Hypermédia et Web Sémantique », Master 1 Arts et Humanités

## Modifications depuis la version 1.0

- Les 10 alignements Wikidata sont vérifiés (section 5), avec deux corrections d'identifiants.
- Le graphe compte 133 triplets et 23 entités, avec l'ajout de la fiche du jeu de données (sections 2 et 3).
- QC4 est fonctionnelle ; QC2 reste vide faute de source (section 6). La requête QC5 a été révisée pour compter aussi la fiche du jeu de données.
- La chaîne de production est automatisée par deux scripts Python (section 11).
- La section 10 distingue désormais ce qui est fait, ce qui reste à faire et les limites assumées.

## 1. Objet

Ce dossier décrit les choix de conception du projet : modèle de données, URI, architecture, alignements, requêtes, prototype hypermédia, annotations et droits. Il prolonge la note de cadrage (version 1.1) et correspond à l'étape 2 du plan, avec un recoupement sur l'étape 3 pour les éléments déjà réalisés. Les guides technique et d'utilisation détaillent l'installation et la navigation.

## 2. Modèle de données

### 2.1 Entités et classes

Le graphe décrit 23 entités, rangées dans des classes locales (préfixe `mv:`) rattachées à des classes standard :

| Classe | Rattachée à | Entités | Nombre |
|---|---|---|---|
| `mv:Peuple` | `foaf:Group` | Kapsiki, Mafa, Fulbe | 3 |
| `mv:Langue` | `dct:LinguisticSystem` | Psikyɛ, Fulfulde | 2 |
| `mv:Site` | `schema:Place` | Diy-Gid-Biy, Rhumsiki, Lamidat de Garoua | 3 |
| `mv:Lieu` | `schema:Place` | Monts Mandara, Garoua, Bibemi, Cameroun | 4 |
| `mv:RecueilDeContes` | `edm:ProvidedCHO` | Contes de Goggo Addi | 1 |
| `mv:Rituel` | `schema:Event` | Rituels mafa | 1 |
| `mv:Fete` | `schema:Event` | Msla, Goalala, Maray | 3 |
| `mv:Instrument` | (aucune) | balafon, tambour d'eau, corne-flûte | 3 |
| `foaf:Person` | (classe standard) | Goggo Addi, Ursula Baumgardt | 2 |
| `dcat:Dataset` | (classe standard) | fiche du jeu de données (`dataset:archive`) | 1 |

Ces classes servent la question QC5 (comptage par catégorie).

### 2.2 Décisions de modélisation

- **Goggo Addi est une personne** (conteuse peule, née en 1911 à Bibemi, morte en novembre 1999 à Garoua). Le recueil est une entité distincte, reliée par `dct:creator` (Goggo Addi) et par `dct:contributor` et `prov:wasAttributedTo` (Ursula Baumgardt, qui a enregistré et fait transcrire les contes entre 1985 et 1989).
- **Les métadonnées du jeu de données sont séparées des entités du corpus.** `dataset:archive` porte la licence, les créateurs et la date, mais ce n'est pas une entité patrimoniale ; elle est comptée dans les 23 entités pour la transparence du comptage.
- **Les alignements non vérifiés sont isolés** : le script les écrit dans `alignements_a_verifier.ttl` et non dans `archive.ttl`. Ce fichier est aujourd'hui vide.
- **Goge et Garaya sont retirés** : la source consultée ne les rattache pas au Nord-Cameroun.
- **Aucun conte d'un autre peuple n'est ajouté** faute de source fiable.
- **Les périodes des sites** sont notées par deux entiers (`mv:siecleDebut`, `mv:siecleFin`) pour pouvoir les comparer en SPARQL (QC3). Seul Diy-Gid-Biy en porte une (XIIe au XVIIe siècle, à sourcer).
- **Le nombre de locuteurs** est rattaché à la langue Psikyɛ et non au peuple kapsiki.

### 2.3 Propriétés

- **Réutilisées** : `dct:language`, `dct:spatial`, `dct:relation`, `dct:creator`, `dct:contributor`, `dct:temporal`, `schema:containedInPlace`, `schema:birthPlace`, `schema:deathPlace`, `schema:knowsLanguage`, `prov:wasAttributedTo`, `skos:prefLabel`, `skos:altLabel`, `skos:scopeNote`.
- **Locales** : `mv:associeAuPeuple`, `mv:pratiquePar`, `mv:siecleDebut`, `mv:siecleFin`, `mv:inscritUnesco`, `mv:critereUnesco`.
- **Déclarées mais non peuplées** : `mv:jouePendant` et `mv:joueParPeuple` (QC2), en attente d'une source.
- **Point faible assumé** : `dct:relation` est très générique. Elle sera remplacée par des relations plus précises si les sources le permettent.

L'ontologie complète (classes, propriétés d'objet et de données, domaines et portées, disjonction des catégories) est écrite dans `ontologie-memoires-du-nord.ttl`. Elle reste à valider sous Protégé avec le raisonneur HermiT.

### 2.4 Vocabulaires

Le noyau retenu est DCTerms, FOAF, SKOS, schema.org, PROV-O, Europeana Data Model (pour le recueil) et DCAT (pour la fiche du jeu de données). CIDOC-CRM reste une option pour les objets patrimoniaux mais n'est pas utilisé. Dix vocabulaires pour une centaine de triplets surchargeraient le modèle. Web Annotation et Media Fragments couvrent les médias.

## 3. URI et Linked Data

- **Schéma** : `http://memoria-nord.cm/id/{type}/{slug}` pour la chose, `/page/` pour la page HTML, `/data/` pour les données RDF. Il couvre les 23 entités, réparties en 10 types : peuple, langue, site, lieu, personne, collection, rituel, fete, instrument, dataset.
- **Redirection 303** : une URI `/id/` identifie une chose du monde réel et ne renvoie pas directement la page, mais une redirection 303 vers `/page/` (client HTML) ou `/data/` (client RDF).
- **Simulation locale** : le domaine est fictif et Fuseki ne gère pas le 303. Un mini-serveur local (Flask ou `.htaccess`) simulera la redirection ; cette partie n'est pas encore réalisée.
- **Vocabulaire local** : `http://memoria-nord.cm/vocab#` n'est pas encore déréférençable.

## 4. Architecture en quatre couches

| Couche | Composants | État |
|---|---|---|
| 4. Présentation | HTML/CSS, Leaflet, YASGUI, JSON-LD | 9 pages statiques générées |
| 3. Logique | liens contextuels, parcours adaptatif, fiches par SPARQL | liens contextuels faits ; fiches par SPARQL à faire |
| 2. Accès | Fuseki local, mini-serveur 303, cache JSON (facultatif), Wikidata en `SERVICE` | Fuseki à charger pour la démo ; 303 à simuler |
| 1. Données | `archive.ttl`, alignements, annotations | générés |

Les requêtes descendent de la présentation vers les données, et les résultats remontent. Wikidata est le seul service extérieur au projet. Figure 1 : schéma des quatre couches (à insérer).

## 5. Alignements

Règle appliquée : `owl:sameAs` pour les individus (lieux, sites, personnes), `skos:exactMatch` pour les concepts (langues, peuples, instruments), `skos:closeMatch` pour une correspondance approximative.

Les 10 alignements ci-dessous ont été vérifiés manuellement sur wikidata.org le 13 octobre 2026 :

| # | Entité | Identifiant | Description Wikidata | Relation |
|---|---|---|---|---|
| 1 | `langue:psikye` | Q56304 | langue parlée au Cameroun et au Nigeria | `skos:exactMatch` |
| 2 | `langue:fulfulde` | Q33454 | langue africaine (peul) | `skos:exactMatch` |
| 3 | `peuple:fulbe` | Q202575 | Peuls (ethnie) | `skos:exactMatch` |
| 4 | `instrument:balafon` | Q789141 | instrument de percussion idiophone | `skos:exactMatch` |
| 5 | `lieu:cameroun` | Q1009 | pays d'Afrique centrale, indépendant depuis 1960 | `owl:sameAs` |
| 6 | `lieu:garoua` | Q157915 | ville du Cameroun (Nord) | `owl:sameAs` |
| 7 | `peuple:kapsiki` | Q2437423 | groupe ethnique (Kapsiki) | `skos:closeMatch` |
| 8 | `peuple:mafa` | Q3276439 | groupe ethnique africain | `skos:closeMatch` |
| 9 | `lieu:monts-mandara` | Q1888885 | massif montagneux entre le Cameroun et le Nigeria | `owl:sameAs` |
| 10 | `site:diy-gid-biy` | Q5285004 | monument du Cameroun (Diy-Gid-Biy des monts Mandara) | `owl:sameAs` |

**Deux corrections ont été nécessaires** par rapport aux identifiants du briefing initial : le Cameroun est Q1009 (et non Q1000, qui correspond au Gabon), et Garoua est Q157915 (et non Q312582).

Le seuil de 10 alignements est atteint exactement, sans marge de sécurité : si un seul alignement se révélait erroné, le seuil ne serait plus atteint. À ce stade, il n'y a aucun alignement GeoNames ni DBpedia ; ils restent une piste pour des lieux comme Garoua et les Monts Mandara. Rhumsiki, Bibemi et Goggo Addi ne sont pas encore alignés.

## 6. Questions de compétence et requêtes

| QC | Question | Type | État | Résultat attendu |
|---|---|---|---|---|
| QC1 | Quels contes sont associés à quel peuple, dans quelle langue et collectés par qui ? | sélection | fonctionnelle | 1 ligne : Contes de Goggo Addi, Fulbe, Fulfulde, Goggo Addi, Ursula Baumgardt |
| QC2 | Quels instruments sont joués lors de quels rituels ou fêtes, et par quels peuples ? | sélection | **vide** | 0 ligne : aucune source ne relie instruments, rituels et peuples |
| QC3 | Quels sites patrimoniaux sont situés dans les Monts Mandara, et à quelle période remontent-ils ? | sélection | fonctionnelle | 2 lignes : Diy-Gid-Biy (XIIe-XVIIe) et Rhumsiki (période vide) |
| QC4 | Pour chaque entité alignée, quels sont le libellé et la description correspondants sur Wikidata ? | **fédérée** (`SERVICE`) | fonctionnelle | 10 lignes ; un libellé ou une description absents en français restent vides |
| QC5 | Combien d'entités par catégorie compte le graphe ? | **agrégat** (`COUNT`, `GROUP BY`) | fonctionnelle | 23 entités : Lieu 4, Peuple 3, Site 3, Fête 3, Instrument 3, Langue 2, Personne 2, Recueil 1, Rituel 1, Jeu de données 1 |

QC4 est pleinement exploitable depuis la vérification des 10 alignements, sous réserve d'un accès Internet depuis Fuseki. QC2 reste une limite assumée : nous n'avons pas inventé de liens, et le jour où une source existe, une ligne dans `relations.csv` suffit à la remplir. QC5 a été révisée dans cette version pour associer chaque classe à son libellé et compter la fiche du jeu de données.

## 7. Prototype hypermédia

Neuf nœuds sont générés par `generer_noeuds.py` à partir de `noeud-template.html`. Chaque page est une `WebPage` en JSON-LD dont la propriété `about` pointe vers les URI `/id/` du graphe.

| Nœud | Contenu | Liens sortants | Médias prévus |
|---|---|---|---|
| n01 | Accueil | n02 à n09 | 1 image, 1 audio |
| n02 | Diy-Gid-Biy | n01, n04, n07, n08 | 5 images, 1 vidéo |
| n03 | Kapsiki | n01, n05, n08 | 2 images, 1 audio |
| n04 | Mafa | n01, n02, n07 | 2 images |
| n05 | Instruments | n01, n03, n07, n08 | 1 audio, 1 vidéo |
| n06 | Contes de Goggo Addi | n01, n07, n09 | 1 audio, transcription |
| n07 | Rituels et fêtes | n01, n02, n05, n06 | 2 images, 1 vidéo |
| n08 | Carte interactive (Leaflet) | n01 à n07, n09 | carte |
| n09 | Fulbe et Lamidat de Garoua | n01, n06, n08 | 2 images |

**Accessibilité** : langue déclarée, lien d'évitement, repères de navigation, ordre de titres cohérent, focus visible, contrastes en clair et en sombre (mode sombre automatique), navigation au clavier. Les textes alternatifs, légendes, sous-titres WebVTT et transcriptions sont des emplacements à rédiger.

**Limite actuelle** : les fichiers médias (photos, vidéos, audio) ne sont pas intégrés, en attendant la clarification des droits. Les pages sont statiques et n'interrogent pas encore Fuseki. La carte s'affiche sans marqueurs tant que les coordonnées géographiques ne sont pas relevées.

**Sécurité et réseau** : tout contenu inséré en JavaScript utilisera `textContent`, jamais `innerHTML`. Les appels du navigateur vers Fuseki poseront un problème de CORS, à traiter par un proxy local.

## 8. Annotation multimédia

Les annotations suivent le Web Annotation Data Model, regroupées dans une `AnnotationPage`. Un fichier d'exemple, `annotations.jsonld`, contient 4 annotations : deux sur une zone d'image, une sur un extrait vidéo, une sur un extrait audio de conte.

Les cibles utilisent des Media Fragments : `xywh=pixel:x,y,l,h` pour une zone d'image, `t=début,fin` pour un extrait audio ou vidéo. Deux motivations sont employées : `identifying` (relier une zone à une entité du graphe) et `describing` (texte alternatif). Les URL des médias, les coordonnées des zones et les textes de description sont des valeurs d'exemple. Les annotations seront chargées dans un graphe nommé séparé afin de ne pas fausser le comptage de QC5.

## 9. Licences, droits et provenance

- Les métadonnées produites par le binôme sont sous licence CC BY 4.0, déclarée sur la fiche du jeu de données. Cette licence ne couvre pas les contes ni les médias.
- Les contes de Goggo Addi relèvent d'un fonds de recherche (INALCO et CNRS) : leur régime de droits sera établi puis déclaré avec `dct:rights`.
- Chaque entité recevra un `dct:source` (colonne prévue dans `entites.csv`, aujourd'hui à renseigner). La provenance de la collecte est portée par `prov:wasAttributedTo`.
- Toute photo, vidéo ou extrait audio publié exige une autorisation vérifiée.

## 10. Points ouverts et limites assumées

**Fait**
- Graphe `archive.ttl` généré par script (133 triplets, 23 entités), alignements vérifiés (10 sur 10).
- Cinq requêtes écrites ; QC1, QC3, QC4 et QC5 fonctionnelles.
- Neuf nœuds générés, exemple d'annotations, ontologie écrite.

**Reste à faire**
- Charger le graphe dans Fuseki pour la démonstration et simuler la redirection 303.
- Valider l'ontologie sous Protégé (raisonneur HermiT) et la visualiser avec OntoGraf ou WebVOWL.
- Relever les coordonnées géographiques (WGS84) pour la carte.
- Renseigner `dct:source` pour chaque entité.
- Établir le peuple associé à chaque fête.
- Brancher les pages sur Fuseki (fiches par SPARQL, annotations sur les images).

**Limites assumées**
- **QC2 est vide** : aucune source ne relie instruments, rituels et peuples.
- **Les médias ne sont pas intégrés** : le critère des trois types de médias n'est donc pas démontré avec des fichiers réels, tant que les droits ne sont pas clarifiés.
- **`dct:relation` est trop générique** et CIDOC-CRM n'est pas utilisé.
- **Faits à confirmer dans les sources** : nombre de vestiges et critère UNESCO de Diy-Gid-Biy, nombre de contes, classification et nombre de locuteurs du psikyɛ, présence des Mafa depuis le XVe siècle, localisation de Diy-Gid-Biy et de Rhumsiki dans les Monts Mandara.

## 11. Chaîne de production

1. **Saisie** : trois fichiers CSV dans `donnees/` : `entites.csv`, `relations.csv`, `alignements.csv`.
2. **Contrôle** : `python csv_vers_turtle.py donnees --verifier` refuse les références orphelines et signale les alignements non vérifiés. Résultat : 23 entités, 40 relations, 10 alignements (10 vérifiés).
3. **Génération** : `python csv_vers_turtle.py donnees` écrit `archive.ttl` (133 triplets, 23 entités, 10 alignements vérifiés) et `alignements_a_verifier.ttl` (vide).
4. **Chargement** dans Fuseki, puis **interrogation** depuis YASGUI : étape à finaliser pour la démonstration.
5. **Pages** : `python generer_noeuds.py` produit les 9 nœuds HTML.

Deux scripts Python (`csv_vers_turtle.py` et `generer_noeuds.py`) assurent donc la reproductibilité du graphe et du prototype. Le script de génération sépare automatiquement les alignements non vérifiés dans un fichier distinct : c'est la garantie qu'aucun identifiant non contrôlé n'entre dans le graphe publié. Outils : Protégé, RDFLib, Fuseki, WebVOWL, Leaflet, VS Code.

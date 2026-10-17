# Guide d'utilisation : MémoireS du Nord

*ZRA Josué Yohana et Bambe Kennedy · IBAI, Université de Garoua · UE « Hypermédia et Web Sémantique », Master 1 Arts et Humanités · Octobre 2026*

## 1. À qui s'adresse ce guide

Ce guide s'adresse aux étudiants, chercheurs, curieux et membres de la diaspora qui souhaitent parcourir une archive du patrimoine culturel du Nord-Cameroun : peuples, langues, sites, contes, rituels, fêtes et instruments. Aucune connaissance technique n'est nécessaire, sauf pour la section 7. L'installation et la reproduction du projet sont décrites dans `guide-technique.md`.

## 2. Accès au prototype

Le prototype est composé de 9 pages HTML situées dans le dossier `noeuds/`. Aucun serveur n'est nécessaire :

1. Ouvrez le dossier du projet, puis le dossier `noeuds/`.
2. Double-cliquez sur `n01.html` : la page s'ouvre dans votre navigateur (Firefox, Chrome, Edge ou Safari récents).
3. Naviguez avec les liens affichés en haut de chaque page.

Une connexion Internet est utile pour la carte (page n08), qui charge Leaflet et le fond de carte en ligne. Les autres pages fonctionnent hors connexion, mais sans leurs médias (voir section 8).

## 3. Parcours recommandé

Commencez par l'accueil (n01), puis choisissez l'un des deux parcours :

- **Sites et rituels** : n01 → n02 (Diy-Gid-Biy) → n04 (Mafa) → n07 (rituels et fêtes) → n05 (instruments) → n03 (Kapsiki) → n08 (carte).
- **Mémoire orale** : n01 → n06 (contes de Goggo Addi) → n09 (Fulbe et Lamidat de Garoua) → n08 (carte).

Chaque page propose en haut des liens contextuels vers les pages voisines, ce qui permet d'improviser son propre chemin.

## 4. Les 9 nœuds

- **n01, Accueil** : présente l'archive et donne accès aux huit autres pages.
- **n02, Diy-Gid-Biy** : ensemble de vestiges en pierre sèche, inscrit à l'UNESCO en juillet 2025.
- **n03, Kapsiki** : peuple des Monts Mandara, de langue psikyɛ.
- **n04, Mafa** : peuple présent depuis le XVe siècle et lié au site de Diy-Gid-Biy.
- **n05, Instruments** : le balafon (xylophone à calebasses), le tambour d'eau (percussion rituelle) et la corne-flûte (instrument à vent rituel).
- **n06, Contes de Goggo Addi** : contes de la conteuse peule Goggo Addi (1911-1999), enregistrés et transcrits par Ursula Baumgardt entre 1985 et 1989.
- **n07, Rituels et fêtes** : rituels mafa et fêtes agricoles et pastorales Msla, Goalala et Maray.
- **n08, Carte interactive** : carte des sites et lieux du corpus, avec une liste de liens équivalente.
- **n09, Fulbe et Lamidat de Garoua** : l'élite islamisée du Nord et la chefferie traditionnelle peule du Lamidat.

## 5. Fonctionnalités

| Fonctionnalité | État |
|---|---|
| Navigation contextuelle entre les 9 pages | disponible |
| Mode sombre automatique, selon le réglage de votre appareil | disponible |
| Métadonnées structurées (JSON-LD) dans chaque page, visibles dans le code source | disponible |
| Carte interactive (Leaflet) | disponible, **sans marqueurs** pour l'instant |
| Lecteur audio pour les contes | prévu dans les pages, **activé quand les fichiers audio seront fournis** |
| Sous-titres WebVTT pour les vidéos | piste prévue, **fichiers à produire** |
| Transcription des contes (n06) | emplacement prévu, **texte à rédiger** |

## 6. Accessibilité

- **Clavier** : la touche `Tab` passe d'un lien à l'autre, `Entrée` l'active, et le lien ou bouton sélectionné est entouré d'un contour visible. Les lecteurs audio et vidéo se commandent aussi au clavier.
- **Lien d'évitement** : au premier appui sur `Tab`, « Aller au contenu » apparaît et permet de sauter la navigation.
- **Repères de navigation** : chaque page distingue en-tête, navigation, contenu principal et pied de page, ce qui aide les lecteurs d'écran.
- **Mode sombre** : il suit automatiquement le réglage de votre système (`prefers-color-scheme`).
- **Textes alternatifs** : chaque image dispose d'un emplacement prévu pour sa description. Le texte définitif est **encore à rédiger** et s'affichera quand les images seront intégrées.

## 7. Interroger les données (utilisateur avancé)

Le graphe `archive.ttl` peut être interrogé en SPARQL :

1. Démarrez Apache Jena Fuseki (nécessite Java) et chargez `archive.ttl` dans un jeu de données, par l'interface `http://localhost:3030` ou en ligne de commande (voir le guide technique).
2. Ouvrez YASGUI et indiquez l'adresse du jeu de données, par exemple `http://localhost:3030/memoires/sparql` (ou `/query`, selon la version). Si le navigateur bloque la connexion (restriction CORS), utilisez la page de requête intégrée à l'interface de Fuseki.
3. Ouvrez `requetes.sparql`, copiez le bloc `PREFIX` en tête de fichier et **une seule** requête, puis cliquez sur le bouton d'exécution.

Deux exemples : **QC1** (contes par peuple) renvoie une ligne, les Contes de Goggo Addi avec le peuple fulbe, la langue fulfulde et la collectrice Ursula Baumgardt. **QC5** (comptage par catégorie) renvoie 23 entités au total, réparties en dix catégories. La requête **QC4** interroge aussi Wikidata et nécessite donc Internet.

## 8. Limites connues

- **QC2 est vide** : aucune source ne relie les instruments, les rituels et les peuples. Nous n'avons rien inventé.
- **Les médias ne sont pas intégrés** : photos, vidéos et audio sont absents, car les droits sont à clarifier, en particulier pour les contes issus du fonds de recherche INALCO et CNRS. Les pages affichent donc des emplacements vides ou des images manquantes.
- **Le domaine `memoria-nord.cm` est fictif** : la redirection 303 entre les identifiants et les pages est à simuler localement.
- **La carte n'a pas de marqueurs** : les coordonnées géographiques (WGS84) sont à relever.
- **Les pages sont statiques** : elles n'interrogent pas encore Fuseki.

## 9. Contact et ressources

- **Binôme** : ZRA Josué Yohana et Bambe Kennedy, IBAI, Université de Garoua. Contact : zrajosueyohana910@gmail.com.
- **Références** : UNESCO (inscription de Diy-Gid-Biy, à citer précisément), Wikidata (10 identifiants vérifiés le 13 octobre 2026), INALCO et CNRS (fonds des contes de Goggo Addi). GeoNames reste une piste d'alignement : aucun identifiant n'est utilisé pour l'instant.
- **Licence** : les métadonnées produites par le binôme sont sous licence CC BY 4.0. Cette licence ne couvre ni les contes ni les médias, dont les droits restent à établir.
- **À citer** : pour toute réutilisation, mentionnez le projet « MémoireS du Nord », ses auteurs et, pour les contes, les sources de collecte.

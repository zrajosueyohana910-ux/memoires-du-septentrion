## 11. Maquette et conception UX/UI

> **À insérer dans le CDC après la section 10** (ou avant les annexes). Les passages entre crochets [ ] sont à compléter ou à vérifier dans le fichier Figma avant de générer le PDF.


### 11.1 Identité du portail

Le portail porte le nom de marque **Mémoires du Cameroun** (logo « MC », cercle doré). Son titre complet, *Portail de ressources sur la culture et les humanités numériques au Cameroun*, reste le sous-titre officiel du projet, et le fil conducteur *« Le Cameroun, mémoire et innovation à l'ère numérique »* sert d'accroche en page d'accueil. Le nom court est mémorisable ; le sous-titre garantit la conformité au thème imposé.


### 11.2 Démarche UX suivie

| Étape | Action | Résultat |
|---|---|---|
| 1 | Partir du CDC | Personas (§3.2), objectifs O1 à O5 (§2.2), arborescence (§5.1) et MoSCoW (§5.2) comme cahier de conception |
| 2 | Définir la charte | Piste « Terre & Or » : palette, typographies, ton visuel adaptés au patrimoine et à l'archive |
| 3 | Maquette haute fidélité (Figma) | Écrans de la page d'accueil en desktop (1440 px), puis wireframes des pages clés et écran mobile |
| 4 | Revue critique maquette / CDC | Contrôle de cohérence (périmètre, vocabulaire, chiffres) et de l'accessibilité (contrastes WCAG AA calculés) |
| 5 | Corrections | Écarts critiques corrigés avant le développement ; écarts mineurs documentés (§11.8) |

**Limite assumée.** Aucun test utilisateur n'a été mené sur la maquette à ce stade ; la validation d'usage est prévue lors de la recette (§10.2) sur mobile réel et au clavier.


### 11.3 Charte graphique (« Terre & Or »)


### 11.3.1 Palette

|   | Rôle | Code | Usage et contraste mesuré |
|---|---|---|---|
|  | Bleu nuit (fond du hero, du pied de page) | #2E4053 | Texte crème : 9,9:1 ; texte blanc : 10,6:1 |
|  | Crème (fonds des sections claires) | #FDF6E3 | Texte noir : 17,5:1 ; texte bleu nuit : 9,9:1 |
|  | Ocre / terre cuite (bandeau de contribution) | #8B4513 | Texte blanc : 7,1:1 ; texte crème : 6,6:1 |
|  | Or vif (boutons, cercles, décor) | #D4A017 | Texte noir ou bleu nuit dessus : 8,0:1. Texte blanc dessus à proscrire (2,4:1) |
|  | Or foncé (numéros 01 à 03, icônes, liens sur fond crème) | #8A6400 | Sur crème : 5,0:1 (conforme AA, texte normal) |
|  | Noir profond (texte principal) | #111111 [à confirmer] | Sur crème : 17,5:1 |

> **Règle d'usage de l'or.** L'or vif (#D4A017) donne 2,2:1 sur crème : il n'est donc jamais utilisé pour du texte ou des icônes porteuses de sens sur fond clair. Il sert de fond de bouton (avec texte sombre) ou d'élément décoratif. Sur bleu nuit, il atteint 4,5:1 : il est réservé aux grands titres et éléments graphiques ; le petit texte (moins de 24 px) y est en crème.

*Contrastes calculés selon la formule WCAG 2.x à partir des codes couleur de la maquette ; à vérifier une dernière fois sur les valeurs exactes de Figma.*


### 11.3.2 Typographie

| Usage | Police | Justification |
|---|---|---|
| Titres | Playfair Display (serif éditorial) | Registre patrimonial et éditorial ; donne une identité reconnaissable au portail |
| Texte courant, menus, boutons | Inter (sans-serif) | Lisibilité à l'écran, y compris sur petits écrans ; très bonne couverture des caractères français |

**Contraintes de performance.** Deux familles seulement, et un nombre limité de graisses, afin de réduire le poids des polices (connectivité variable, §3.3). Polices à servir en local (fichiers dans le projet) ou avec `font-display: swap`. Corps de texte : 16 px minimum ; titres en `rem`.


### 11.3.3 Mise en page et composants

- Grille sur 12 colonnes en desktop (1440 px), 1 colonne en mobile.
- Sections alternant bleu nuit, crème et ocre pour rythmer la page et séparer les trois temps : *découvrir*, *explorer*, *contribuer*.
- Composants réutilisables : bouton principal (or, texte sombre), bouton secondaire (contour), carte de ressource, bloc « chemin », pied de page.
- Visuels : photographies libres de droits (Unsplash ou Wikimedia Commons) **avec crédit visible** ; images optimisées (§6).


### 11.4 Navigation

Menu principal : **Patrimoine · Ressources & Méthodes · Acteurs & projets · À propos · [Contribuer]**, avec une icône de recherche (F12). *Contribuer* est présenté en bouton doré pour en faire un appel à l'action permanent (objectif O5). Le logo ramène à l'accueil. Sur mobile, le menu devient un menu burger. Le pied de page reprend les liens secondaires (Explorer, Le projet) et les mentions légales.

**Justification.** Six rubriques du CDC (§5.1) pour cinq entrées visibles en texte plus un bouton : la navigation reste lisible, la rubrique la plus engageante (Contribuer) est la plus visible, et la structure du site correspond exactement à l'arborescence du CDC.


### 11.5 Description écran par écran et lien avec les fonctionnalités

> Insérer ici les captures de la maquette Figma (une par écran) avec la légende « Figure n : titre de l'écran ».

| N° | Écran | Contenu et rôle | Fonctionnalités et objectifs |
|---|---|---|---|
| 1 | En-tête / navigation | Logo « MC — Mémoires du Cameroun », menu principal, bouton Contribuer, icône de recherche. Barre fixe, lisible sur tous les écrans | F01 ; F12 (icône ; inactive si la recherche n'est pas livrée) ; F11 |
| 2 | Hero (accueil) | Sur-titre « Culture · Recherche · Transmission », fil conducteur en grand titre, image circulaire avec badge « Patrimoine vivant », compteur « 6 régions à explorer », deux CTA (« Explorer le patrimoine », « Découvrir les méthodes »), crédit photo | F02 ; F09 ; F11 ; accès à F03 et F05 ; O1, O2 |
| 3 | Trois chemins d'exploration | Trois colonnes numérotées 01 à 03 : Patrimoines vivants, Méthodes numériques, Communauté de recherche. Chacune mène à la rubrique correspondante, et reprend les trois axes du CDC (§1.4) | F02 ; F03 ; F04 ; F06 ; O1, O3, O4 |
| 4 | Ressources récentes | Trois cartes avec image, numéro et catégorie, et un lien « Voir toutes les ressources ». Alimentées par les fichiers JSON | F02 ; F04 ; F05 ; F10 ; O2, O3 |
| 5 | Une mémoire collective (bandeau ocre) | Invitation à contribuer (« Vous détenez une histoire, une archive ou une ressource ? ») et CTA « Proposer une contribution » vers la page Contribuer | F07 ; O5 |
| 6 | Pied de page (bleu nuit) | Logo et description, colonnes Explorer et Le projet, mention « Contenus sous licence CC BY-SA 4.0 », copyright « © 2026 Mémoires du Cameroun » | F01 ; F08 ; contraintes éditoriales (§6) |
| 7 | Liste Patrimoine (wireframe) | Titre, filtres par région et par type, grille de fiches. Structure réutilisée pour les listes Outils/ressources et Acteurs et projets | F03 ; F05 ; F06 ; F09 ; O2, O3 |
| 8 | Fiche détail (wireframe) | Titre, image avec crédit et licence, métadonnées (région, catégorie), description, sources, liens associés. Structure réutilisée pour les fiches méthodes et projets | F04 ; F10 ; F11 ; O1, O2, O4 |
| 9 | Contribuer (wireframe) | Texte d'invitation, formulaire (nom, courriel, type de proposition, message), message de confirmation, encart pédagogique sur le branchement en production, lien mailto | F07 ; O5 |
| 10 | Accueil mobile et menu burger | Version 1 colonne du hero et menu burger ouvert, zones tactiles d'au moins 44 px | F01 ; F09 ; F11 |

**Fonctionnalités non représentées dans la maquette** : F08 (page À propos : mise en page standard avec le même gabarit que la fiche détail), F13 (glossaire), F14 (carte interactive), F15 (FR/EN) et F16 (mode sombre). F13 est une priorité *Should*, les trois autres sont des *Could* : elles seront maquettées si le temps le permet.


### 11.6 Accessibilité et responsive

| Axe | Choix |
|---|---|
| Contrastes | Conformes WCAG AA après correction (§11.3.1). Tout texte de moins de 24 px respecte 4,5:1 |
| Structure | HTML sémantique (`header`, `nav`, `main`, `section`, `footer`), un seul `h1` par page, hiérarchie des titres respectée |
| Clavier et focus | Tous les éléments interactifs atteignables au clavier ; focus visible défini en CSS avec `:focus-visible` (anneau or foncé ou blanc selon le fond) [état de focus à ajouter dans Figma] |
| Images | Texte alternatif sur chaque image porteuse de sens ; image décorative avec `alt` vide ; crédit visible |
| Texte sur image | Voile sombre ou aplat sous le texte pour garantir le contraste |
| Formulaire | Libellés associés aux champs, messages d'erreur textuels (pas seulement la couleur) |
| Responsive | Approche mobile-first, points de rupture indicatifs : 640 px (tablette), 1024 px (desktop). Colonnes empilées en mobile, menu burger |


### 11.7 Cohérence avec le CDC

La maquette respecte les 6 rubriques du CDC (§5.1), les trois axes éditoriaux (§1.4), les objectifs O1 à O5 (§2.2) et le périmètre : le portail référence et oriente, il n'héberge pas d'archives. Pour cette raison, le badge du hero indique « Patrimoine vivant » et non « Archives vivantes ».


### 11.8 Écarts identifiés lors de la revue de maquette

Les écarts identifiés lors de la revue de maquette ont été traités ou documentés. Les écarts critiques (sémantique du badge, compteur de régions, contrastes) ont été corrigés avant la phase de développement.

| N° | Écart constaté | Correction ou traitement | Gravité | Statut |
|---|---|---|---|---|
| 1 | Page Contribuer absente du menu principal | Bouton « Contribuer » ajouté au menu | Haute | **Corrigé** |
| 2 | « Ressources » et « Méthodes » séparés, contre une rubrique unique au CDC | Fusion en « Ressources & Méthodes » | Moyenne | **Corrigé** |
| 3 | Compteur « 10 régions » non soutenu par le contenu | Remplacé par « 6 régions à explorer ». Valeur à aligner sur le nombre de régions effectivement couvertes par les fiches publiées | Haute | **Corrigé** [vérifier à l'intégration des fiches] |
| 4 | Badge « Archives vivantes » en contradiction avec §1.3 (pas d'hébergement d'archives) | Remplacé par « Patrimoine vivant » | Haute | **Corrigé** |
| 5 | Numéros et icônes dorés sur crème (2,2:1) | Or foncé #8A6400 (5,0:1) | Haute | **Corrigé** |
| 6 | Petits textes en or sur bleu nuit (4,5:1, limite) | Texte inférieur à 24 px passé en crème #FDF6E3 (9,9:1) | Moyenne | **Corrigé** |
| 7 | Pas d'écran de liste, de fiche ni de Contribuer | Trois wireframes ajoutés (écrans 7, 8, 9) | Haute | **Corrigé** |
| 8 | Maquette desktop seule, alors que le CDC annonce mobile-first | Écran mobile ajouté (accueil + menu burger, écran 10) | Moyenne | **Corrigé** |
| 9 | Libellés « Dossier thématique » et « Guide pratique » hors des 4 types de fiches du modèle de données (§5.3) | À aligner dans le code sur les types : Fiche patrimoine, Fiche méthode, Outil, Acteur/projet | Moyenne | **Documenté** |
| 10 | Liens « Crédits » et « Communauté de recherche » sans page dédiée | Redirigés vers la page À propos | Faible | **Documenté** |
| 11 | Icône de recherche (F12, *Should*) | Fonctionnelle si F12 est livrée, sinon masquée | Faible | **Documenté** |
| 12 | État de focus clavier non représenté | Défini en CSS (`:focus-visible`) ; maquetté si le temps le permet | Moyenne | **Documenté** |


### 11.9 Évolutions possibles

- Maquettes du glossaire (F13), de la carte interactive (F14), du sélecteur FR/EN (F15) et du mode sombre (F16, avec une palette sombre dont les contrastes sont à recalculer).
- Test d'usage auprès de quelques étudiants (mobile, connexion lente) et ajustement de la maquette.
- Composant de recherche avec suggestions (F12).

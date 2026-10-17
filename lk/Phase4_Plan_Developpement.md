# Phase 4 : plan de développement React — Mémoires du Cameroun

Préparation du développement : composants issus de la maquette, arborescence, routes, ordre de travail par priorité, points d'attention. Stack : Vite + React + React Router, données en JSON local, déploiement Vercel.

## 1. Principes d'architecture (et pourquoi)

| Choix | Justification |
|---|---|
| **Données en import statique** (`import data from "../data/patrimoine.json"`) | Pas de `fetch`, donc pas de `useEffect`, pas de chargement ni d'erreur réseau à gérer : le point faible actuel (useEffect en apprentissage) est évité, et le site marche hors connexion une fois chargé |
| **`useState` + `useMemo`, pas de Context** | Les seuls états sont : filtres, menu burger, formulaire. Context n'apporte rien ici (risque R2). Il ne se justifierait que pour F15 (langue) ou F16 (thème), qui sont des *Could* |
| **Composants `ui/` réutilisables** (Button, Badge, Card, SectionTitle) | Cohérence visuelle avec Figma, moins de code, critère « composants réutilisables » du CDC §10.1 |
| **Variables CSS (tokens)** dans un seul fichier | La charte (couleurs corrigées, polices) vit à un seul endroit ; Zra peut la livrer à Kennedy sans toucher aux composants |
| **Une page = un fichier dans `pages/`, une section = un composant dans `components/`** | Lisibilité du dépôt pour le jury et pour la reprise par un seul membre (R11) |

## 2. Arborescence proposée

```
memoires-du-cameroun/
├─ public/
│  ├─ images/                 # images optimisées (WebP), nommées en minuscules
│  └─ favicon.svg
├─ src/
│  ├─ main.jsx                # point d'entrée, BrowserRouter
│  ├─ App.jsx                 # définition des routes
│  ├─ data/
│  │  ├─ patrimoine.json
│  │  ├─ methodes.json
│  │  ├─ ressources.json      # outils / ressources
│  │  └─ acteurs.json
│  ├─ components/
│  │  ├─ layout/              # Layout, Header, MobileMenu, Footer, SkipLink, ScrollToTop
│  │  ├─ ui/                  # Button, Badge, Card, SectionTitle, Tag
│  │  ├─ home/                # Hero, PathsSection, PathCard, RecentResources, ContributeBanner
│  │  ├─ resources/           # ResourceCard, FilterBar, ResourceList
│  │  └─ contribute/          # ContributeForm, ProductionNote
│  ├─ pages/                  # Home, Patrimoine, PatrimoineDetail, RessourcesMethodes,
│  │                          # MethodeDetail, ActeursProjets, ProjetDetail, Contribuer,
│  │                          # APropos, NotFound
│  ├─ hooks/                  # useFilters.js, usePageTitle.js
│  ├─ utils/                  # data.js (getById, valeursUniques)
│  └─ styles/                 # tokens.css, global.css (+ un .css par composant)
├─ vercel.json
├─ index.html
└─ README.md
```

## 3. Découpage en composants, écran par écran

| Écran Figma | Composants | Props / données principales | F |
|---|---|---|---|
| 1. En-tête | `Header` (Logo, `NavLink`s, bouton Contribuer, icône recherche, `BurgerButton`), `MobileMenu` | `menuOuvert` (useState) | F01, F12 |
| 2. Hero | `Hero` (Eyebrow, titre, `Button` ×2, image ronde, `Badge` « Patrimoine vivant », compteur, crédit photo) | Compteur **calculé** : `new Set(patrimoine.map(f => f.region)).size` | F02 |
| 3. Trois chemins | `PathsSection` + `PathCard` ×3 | `numero`, `icone`, `titre`, `texte`, `lien` (tableau constant) | F02 |
| 4. Ressources récentes | `RecentResources` + `ResourceCard` ×3 | 3 fiches sélectionnées par un champ `mise_en_avant` (voir §6) | F02, F04, F10 |
| 5. Bandeau ocre | `ContributeBanner` | Lien vers `/contribuer` | F07 |
| 6. Pied de page | `Footer` | Liens, licence CC BY-SA 4.0 | F01, F08 |
| 7. Liste Patrimoine | `FilterBar` + `ResourceList` + `ResourceCard` | `useFilters(donnees)` renvoie `filtres`, `setFiltre`, `resultats` | F03, F05, F06 |
| 8. Fiche détail | `PatrimoineDetail` (titre, image + crédit, métadonnées, description, sources) | `useParams()` → `getById` ; id inconnu → `NotFound` | F04 |
| 9. Contribuer | `ContributeForm`, `ProductionNote` | États : `valeurs`, `erreurs`, `envoye` | F07 |
| 10. Mobile | Mêmes composants, CSS responsive | Points de rupture 640 / 1024 px | F09 |

> Les pages Ressources & Méthodes et Acteurs & projets **réutilisent** `FilterBar`, `ResourceList` et `ResourceCard` : c'est l'argument de réutilisabilité à donner en soutenance.

## 4. Routes (React Router)

| Chemin | Page | F |
|---|---|---|
| `/` | `Home` | F02 |
| `/patrimoine` | `Patrimoine` | F03 |
| `/patrimoine/:id` | `PatrimoineDetail` | F04 |
| `/ressources-methodes` | `RessourcesMethodes` (méthodes + outils, filtre par type) | F05 |
| `/methodes/:id` | `MethodeDetail` | F04 |
| `/acteurs-projets` | `ActeursProjets` | F06 |
| `/projets/:id` | `ProjetDetail` | F04, F06 |
| `/contribuer` | `Contribuer` | F07 |
| `/a-propos` | `APropos` | F08 |
| `*` | `NotFound` | — |

`vercel.json` (obligatoire pour que le rechargement d'une route fonctionne) :

```json
{ "rewrites": [{ "source": "/(.*)", "destination": "/index.html" }] }
```

## 5. Ordre de développement (par priorité Must)

Chaque bloc se termine par un commit, un déploiement Vercel et une vérification mobile. Ne pas passer au suivant tant que le critère n'est pas rempli.

| Bloc | Contenu | F | Qui | Critère de fin |
|---|---|---|---|---|
| **A. Fondations** | `tokens.css` (palette corrigée, polices), `global.css`, `Layout`, `Header`, `Footer`, routes avec pages vides, `vercel.json` | F01, F09, F11 (base) | Kennedy (code), Zra (tokens, specs) | Toutes les routes s'ouvrent et se **rechargent** sur Vercel |
| **B. Données** | 4 fichiers JSON avec 2 ou 3 fiches de test chacun, `utils/data.js`, `ResourceCard` | F10 | Binôme | Une carte s'affiche depuis le JSON |
| **C. Accueil** | `Hero`, `PathsSection`, `RecentResources`, `ContributeBanner` | F02 | Kennedy, Zra (intégration visuelle) | Page conforme à la maquette, contrastes corrigés |
| **D. Patrimoine** | Liste, `FilterBar`, `useFilters`, fiche détail | F03, F04 | Kennedy | Filtres région + type fonctionnels ; id inconnu → page 404 |
| **E. Ressources et méthodes** | Liste outils/méthodes, filtre par type, `MethodeDetail` | F05, F04 | Kennedy | Mêmes composants que D, réutilisés |
| **F. Acteurs et projets** | Liste et `ProjetDetail` | F06 | Kennedy | Idem E |
| **G. Contribuer** | `ContributeForm` (validation, confirmation), `ProductionNote`, lien `mailto:` | F07 | Kennedy (code), Zra (textes) | Erreurs affichées en texte, message de confirmation annoncé |
| **H. À propos** | Projet, équipe, méthodologie, sources, licences | F08 | Zra | Texte relu, crédits et licences exacts |
| **I. Passe qualité** | Accessibilité (voir §6), responsive, Lighthouse, liens | F09, F11 | Binôme | Lighthouse accessibilité ≥ 90 ; parcours complet au clavier |
| **J. Should** (si le temps le permet) | F12 recherche globale, F13 glossaire | F12, F13 | Kennedy, Zra | Aucun *Must* dégradé |

Les contenus (fiches) progressent **en parallèle** : Zra remplace les fiches de test par les vraies fiches au fil des blocs D, E, F.

## 6. Points d'attention

### Accessibilité (F11)
- **Lien d'évitement** (« Aller au contenu ») en premier élément du `Layout`, visible au focus.
- **Menu burger** : `<button aria-expanded aria-controls>`, fermeture à la touche Échap, focus rendu au bouton.
- **`NavLink`** pose automatiquement `aria-current="page"` sur la page active : s'en servir pour le style de l'entrée active.
- **Changement de page** : `ScrollToTop` + titre de page à jour (`usePageTitle` avec `useEffect`) ; exercice utile et simple pour apprendre `useEffect`.
- **Formulaire** : `<label htmlFor>`, erreurs en texte reliées au champ (`aria-describedby`), message de confirmation dans une zone `aria-live="polite"`.
- **Focus visible** défini dans `global.css` :

```css
:root {
  --bleu-nuit: #2E4053; --creme: #FDF6E3; --ocre: #8B4513;
  --or: #D4A017; --or-fonce: #8A6400; --noir: #111111;
  --font-titre: "Playfair Display Variable", Georgia, serif;
  --font-texte: "Inter Variable", system-ui, sans-serif;
}
:focus-visible { outline: 3px solid var(--or-fonce); outline-offset: 3px; }
.sur-fonce :focus-visible { outline-color: var(--creme); } /* hero, footer, bandeau ocre */
```

- **Images** : `alt` utile, ou `alt=""` si décorative ; crédit visible ; texte sur image avec voile sombre.
- **Mouvement** : respecter `@media (prefers-reduced-motion: reduce)`.

### Responsive (F09)
- Mobile-first : le CSS de base cible le mobile, `@media (min-width: 640px)` et `(min-width: 1024px)` ajoutent les colonnes.
- Grilles avec `repeat(auto-fit, minmax(16rem, 1fr))` pour les cartes.
- Hero : image ronde et compteur repositionnés sous le texte en mobile.
- Zones tactiles ≥ 44 px ; aucun défilement horizontal.

### Routing (F04)
- `BrowserRouter` dans `main.jsx` ; `Routes` et `Route` dans `App.jsx`.
- Dans les pages de détail : `useParams()`, recherche de la fiche par `id`, redirection vers `NotFound` si absente.
- Les `id` des JSON sont stables (slug ou nombre) : ne jamais les renuméroter après publication.

### Polices et performance
- Polices servies en local avec Fontsource (`npm install @fontsource-variable/inter @fontsource-variable/playfair-display`, noms de paquets à vérifier sur npm) : pas d'appel à Google Fonts, donc plus rapide et sobre en données.
- Images en WebP, dimensionnées, `loading="lazy"` sauf l'image du hero.
- Aucune bibliothèque d'icônes lourde : icônes SVG en ligne ou fichiers SVG.

### Données
- Modèle de données du CDC §5.3 respecté. **Ajout mineur proposé** : un champ booléen `mise_en_avant` pour choisir les 3 cartes de l'accueil. À consigner dans le README et à ajouter au CDC §5.3.
- Le compteur de régions du hero est **calculé** depuis `patrimoine.json` : le chiffre affiché ne peut jamais dépasser le contenu réel. Si le résultat n'est pas 6, adapter le texte plutôt que les données.

### Git (critère §10.1)
- Une branche par bloc (`feat/accueil`, `feat/patrimoine`…), fusion dans `main` après vérification du déploiement.
- Messages de commit courts et explicites : `feat: carte de ressource`, `fix: contraste des numéros`, `docs: README`.
- Tag `v1.0` sur le dépôt livré.

## 7. Questions à trancher avant d'écrire le code

1. **Écrire les composants clés en code commenté ?** Je propose ensuite le code commenté de : `App.jsx` (routes), `Layout` + `Header` (burger accessible), `useFilters` + `FilterBar`, `ResourceCard`, `ContributeForm` (validation et confirmation).
2. **Compteur du hero** : validez-vous le calcul automatique depuis le JSON (recommandé) ?
3. **Champ `mise_en_avant`** : validez-vous cet ajout au modèle de données ?

# Phase 4 : plan de développement React — Mémoires du Cameroun

Document de travail pour le binôme (développement : Kennedy ; contenu et relecture : Zra). Il part des 10 écrans de la maquette (CDC §11.5) et des fonctionnalités F01 à F16 (CDC §5.2).

---

## 1. Choix techniques et justification

| Sujet | Choix | Pourquoi |
|---|---|---|
| Outil de build | Vite + React | Validé en phase 2 (Create React App n'est plus maintenu) |
| Routage | `react-router-dom` (`BrowserRouter`, `Routes`, `Route`, `useParams`, `NavLink`) | Routes dynamiques pour les fiches détail (F04) |
| Données | **Fichiers JSON importés directement** (`import data from "../data/patrimoine.json"`) | Pas de `fetch`, donc pas de `useEffect` ni d'état de chargement : adapté au niveau actuel, fonctionne hors connexion, simple à tester (F10) |
| État | `useState` + props. **Pas de Context** | Le seul état partagé est local (filtres, menu, formulaire). Context n'apporte rien ici (risque R2) |
| Style | CSS classique : un `tokens.css` (variables) + un fichier CSS par composant | Pas de dépendance supplémentaire (sobriété), palette centralisée |
| Bibliothèques UI | Aucune | Poids, maîtrise, et le design est déjà défini dans Figma |

---

## 2. Arborescence des dossiers

```
mémoires-du-cameroun/
├── public/
│   ├── images/               # images optimisées (WebP), nommées en minuscules
│   └── fonts/                # Playfair Display, Inter (si hébergées en local)
├── src/
│   ├── main.jsx              # point d'entrée, BrowserRouter
│   ├── App.jsx               # table des routes
│   ├── styles/
│   │   ├── tokens.css        # couleurs, polices, espacements (variables)
│   │   └── global.css        # reset, typographie, focus, utilitaires
│   ├── data/
│   │   ├── patrimoine.json
│   │   ├── methodes.json
│   │   ├── outils.json
│   │   └── projets.json
│   ├── components/
│   │   ├── layout/           # Layout, Header, Footer, SkipLink
│   │   ├── ui/               # Button, Badge, Card, FilterBar, CreditImage, SectionTitle
│   │   ├── home/             # Hero, ThreePaths, RecentResources, ContributeBanner
│   │   └── forms/            # ContributeForm
│   ├── pages/                # Home, Patrimoine, PatrimoineDetail, Ressources,
│   │                         # MethodeDetail, Acteurs, ProjetDetail, Contribuer,
│   │                         # APropos, NotFound
│   └── utils/
│       └── filters.js        # fonctions de filtrage et de comptage (pures)
├── vercel.json               # réécriture des routes (obligatoire sur Vercel)
├── index.html
├── package.json
└── README.md
```

**Routes**

| Chemin | Page | Fonctionnalité |
|---|---|---|
| `/` | Home | F02 |
| `/patrimoine` | Liste + filtres | F03 |
| `/patrimoine/:id` | Fiche détail | F04 |
| `/ressources` | Méthodes et outils (deux onglets ou deux sections) | F05 |
| `/methodes/:id` | Fiche méthode | F04 |
| `/acteurs` | Liste des acteurs et projets | F06 |
| `/projets/:id` | Fiche projet | F04, F06 |
| `/contribuer` | Formulaire simulé | F07 |
| `/a-propos` | Projet, équipe, sources, licences | F08 |
| `*` | NotFound | — |

---

## 3. Découpage en composants à partir des écrans

| Écran de la maquette | Composants | Props principales | F |
|---|---|---|---|
| 1. En-tête | `Header` (logo, `NavLink`, bouton burger, bouton Contribuer, icône de recherche) | aucune (état `open` interne) | F01, F12 |
| 2. Hero | `Hero`, `CreditImage`, `Button` | `regionsCount` (calculé depuis les données) | F02 |
| 3. Trois chemins | `ThreePaths` avec 3 `PathCard` | tableau `paths` défini dans le composant | F02 |
| 4. Ressources récentes | `RecentResources` + `Card` + `Badge` | `items` (3 premiers éléments des JSON) | F02, F04, F10 |
| 5. Bandeau ocre | `ContributeBanner` + `Button` (lien vers `/contribuer`) | aucune | F07 |
| 6. Pied de page | `Footer` | aucune | F01, F08 |
| 7. Liste Patrimoine | `FilterBar` + grille de `Card` | `items`, `filters`, `onChange` | F03 |
| 8. Fiche détail | `DetailLayout` (titre, `CreditImage`, métadonnées, sources) | `item` | F04 |
| 9. Contribuer | `ContributeForm` + encart pédagogique | état interne (`values`, `errors`, `sent`) | F07 |
| 10. Mobile | Même composants ; CSS responsive et menu burger | — | F01, F09 |

**Principe de réutilisation.** `Card`, `FilterBar` et `DetailLayout` servent aux quatre types de fiches. On évite quatre listes et quatre détails séparés : c'est le gain de temps principal.

---

## 4. Ordre de développement (par priorité Must)

| Étape | Contenu | Fonctionnalités | Critère de fin |
|---|---|---|---|
| 0 | Vite + Router + `vercel.json` + premier déploiement + test d'une route au rechargement | — | Une URL `/test` s'ouvre au rechargement sur Vercel |
| 1 | `tokens.css`, polices, `Layout`, `Header`, `Footer`, `SkipLink` | F01, F11 | Navigation entre pages vides, menu burger mobile |
| 2 | Données de test (3 entrées par fichier JSON, marquées TEST) | F10 | Les 4 JSON se chargent sans erreur |
| 3 | `Card`, `Badge`, page Patrimoine avec filtres région et type | F03 | Filtrer met à jour la liste, message « aucun résultat » |
| 4 | Page détail (`useParams`) et gestion de l'id inconnu | F04 | Chaque carte ouvre sa fiche ; id inconnu → NotFound |
| 5 | Page d'accueil (Hero, trois chemins, ressources récentes, bandeau) | F02 | Accueil conforme à la maquette |
| 6 | Ressources & Méthodes, Acteurs & Projets (réutilisent Card, FilterBar, détail) | F05, F06 | Listes et détails fonctionnels |
| 7 | Contribuer : formulaire simulé | F07 | Validation, confirmation, encart, lien `mailto:` |
| 8 | À propos, NotFound | F08 | Page À propos complète |
| 9 | Passe responsive et accessibilité | F09, F11 | Lighthouse accessibilité ≥ 90, parcours clavier complet |
| 10 | Intégration des vraies fiches (en continu dès que le contenu arrive) | F10 | Plancher de 14 fiches |
| 11 | Should : glossaire, puis recherche globale | F13, F12 | Si le temps le permet |

Ordre de sacrifice en cas de retard (CDC §8.3) : F16, F15, F14, F13, F12. Les étapes 0 à 9 correspondent au Must et ne sont pas sacrifiées.

---

## 5. Exemples de code commentés

### 5.1 `src/styles/tokens.css` : palette et contrastes (CDC §11.3.1)

```css
:root {
  /* Couleurs (contrastes mesurés, voir CDC §11.3.1) */
  --bleu-nuit: #2e4053;   /* fond hero/footer ; texte crème 9,9:1 */
  --creme:     #fdf6e3;   /* fond sections claires */
  --ocre:      #8b4513;   /* bandeau contribution ; texte blanc 7,1:1 */
  --or:        #d4a017;   /* FONDS et décor uniquement ; texte sombre dessus */
  --or-fonce:  #8a6400;   /* numéros, icônes, liens sur crème (5,0:1) */
  --noir:      #111111;

  /* Typographie */
  --font-titre: "Playfair Display", Georgia, serif;
  --font-texte: "Inter", system-ui, sans-serif;

  /* Espacements et rayons */
  --espace: 1rem;
  --rayon: 0.5rem;
}

/* Focus visible pour la navigation clavier (F11) */
:focus-visible {
  outline: 3px solid var(--or-fonce);
  outline-offset: 2px;
}
/* Sur fond sombre, l'anneau est blanc */
.fond-sombre :focus-visible { outline-color: #fff; }
```

### 5.2 `vercel.json` : routes qui survivent au rechargement (risque R3)

```json
{
  "rewrites": [{ "source": "/(.*)", "destination": "/index.html" }]
}
```

### 5.3 `src/App.jsx` : table des routes

```jsx
import { Routes, Route } from "react-router-dom";
import Layout from "./components/layout/Layout";
import Home from "./pages/Home";
import Patrimoine from "./pages/Patrimoine";
import PatrimoineDetail from "./pages/PatrimoineDetail";
import NotFound from "./pages/NotFound";
// ... autres pages

export default function App() {
  return (
    <Routes>
      {/* Layout contient Header + <Outlet /> + Footer */}
      <Route element={<Layout />}>
        <Route path="/" element={<Home />} />
        <Route path="/patrimoine" element={<Patrimoine />} />
        <Route path="/patrimoine/:id" element={<PatrimoineDetail />} />
        {/* /ressources, /methodes/:id, /acteurs, /projets/:id, /contribuer, /a-propos */}
        <Route path="*" element={<NotFound />} />
      </Route>
    </Routes>
  );
}
```

### 5.4 `Layout.jsx` : titre de page et retour en haut à chaque navigation

```jsx
import { Outlet, useLocation } from "react-router-dom";
import { useEffect } from "react";
import Header from "./Header";
import Footer from "./Footer";
import SkipLink from "./SkipLink";

export default function Layout() {
  const { pathname } = useLocation();

  // Remonte en haut de page à chaque changement de route
  useEffect(() => { window.scrollTo(0, 0); }, [pathname]);

  return (
    <>
      <SkipLink />  {/* lien « Aller au contenu » visible au focus (F11) */}
      <Header />
      <main id="contenu" tabIndex={-1}>
        <Outlet />
      </main>
      <Footer />
    </>
  );
}
```

### 5.5 `pages/Patrimoine.jsx` : filtres avec `useState`

```jsx
import { useState } from "react";
import patrimoine from "../data/patrimoine.json";
import Card from "../components/ui/Card";
import FilterBar from "../components/ui/FilterBar";
import { filterItems } from "../utils/filters";

const REGIONS = ["Adamaoua", "Centre", "Est", "Extrême-Nord", "Littoral",
                 "Nord", "Nord-Ouest", "Ouest", "Sud", "Sud-Ouest"];
const CATEGORIES = ["matériel", "immatériel", "linguistique"];

export default function Patrimoine() {
  // Un seul objet d'état pour les deux filtres ("" = tous)
  const [filters, setFilters] = useState({ region: "", categorie: "" });

  const items = filterItems(patrimoine, filters);

  return (
    <section aria-labelledby="titre-patrimoine">
      <h1 id="titre-patrimoine">Patrimoine</h1>

      <FilterBar
        filters={filters}
        onChange={setFilters}
        regions={REGIONS}
        categories={CATEGORIES}
      />

      {/* Annonce le nombre de résultats aux lecteurs d'écran */}
      <p aria-live="polite">{items.length} fiche(s)</p>

      {items.length === 0 ? (
        <p>Aucune fiche ne correspond à ces filtres.</p>
      ) : (
        <ul className="grille">
          {items.map((f) => (
            <li key={f.id}>
              <Card
                to={`/patrimoine/${f.id}`}
                titre={f.titre}
                badge={f.categorie}
                image={f.image}
                alt={f.alt}
              />
            </li>
          ))}
        </ul>
      )}
    </section>
  );
}
```

```js
// src/utils/filters.js : fonction pure, facile à tester
export function filterItems(items, { region, categorie }) {
  return items.filter(
    (f) => (!region || f.region === region) && (!categorie || f.categorie === categorie)
  );
}

// Compteur du hero : calculé depuis les données, donc toujours vrai
export function countRegions(items) {
  return new Set(items.map((f) => f.region)).size;
}
```

### 5.6 `pages/PatrimoineDetail.jsx` : route dynamique

```jsx
import { useParams, Link } from "react-router-dom";
import patrimoine from "../data/patrimoine.json";
import NotFound from "./NotFound";

export default function PatrimoineDetail() {
  const { id } = useParams();                       // :id de l'URL
  const fiche = patrimoine.find((f) => f.id === id);

  if (!fiche) return <NotFound />;                  // id inconnu → 404

  return (
    <article>
      <Link to="/patrimoine">← Retour au patrimoine</Link>
      <h1>{fiche.titre}</h1>
      <p>{fiche.region} · {fiche.categorie}</p>

      <figure>
        <img src={fiche.image} alt={fiche.alt} loading="lazy" />
        <figcaption>{fiche.credit} — {fiche.licence}</figcaption>
      </figure>

      <p>{fiche.description}</p>

      <h2>Sources</h2>
      <ul>
        {fiche.sources.map((s) => (
          <li key={s.url}><a href={s.url}>{s.titre}</a> (consulté le {s.consulte})</li>
        ))}
      </ul>
    </article>
  );
}
```

### 5.7 `forms/ContributeForm.jsx` : formulaire simulé (F07)

```jsx
import { useState } from "react";

const VIDE = { nom: "", email: "", type: "", message: "" };

function valider(v) {
  const e = {};
  if (!v.nom.trim()) e.nom = "Indiquez votre nom.";
  if (!/^\S+@\S+\.\S+$/.test(v.email)) e.email = "Adresse e-mail invalide.";
  if (!v.type) e.type = "Choisissez un type de proposition.";
  if (v.message.trim().length < 20) e.message = "Message trop court (20 caractères minimum).";
  return e;
}

export default function ContributeForm() {
  const [values, setValues] = useState(VIDE);
  const [errors, setErrors] = useState({});
  const [sent, setSent] = useState(false);

  const handleChange = (e) =>
    setValues({ ...values, [e.target.name]: e.target.value });

  const handleSubmit = (e) => {
    e.preventDefault();
    const err = valider(values);
    setErrors(err);
    if (Object.keys(err).length === 0) {
      // SIMULATION : aucun envoi réel. En production : Formspree ou EmailJS.
      setSent(true);
      setValues(VIDE);
    }
  };

  if (sent) {
    return <p role="status">Merci ! Votre proposition a bien été prise en compte (démonstration).</p>;
  }

  return (
    <form onSubmit={handleSubmit} noValidate>
      <label htmlFor="nom">Nom</label>
      <input id="nom" name="nom" value={values.nom} onChange={handleChange}
             aria-invalid={!!errors.nom} aria-describedby={errors.nom ? "err-nom" : undefined} />
      {errors.nom && <p id="err-nom" className="erreur">{errors.nom}</p>}

      {/* Même schéma pour email, type (select) et message (textarea) */}

      <button type="submit">Envoyer</button>
      <p>Ou écrivez-nous directement : <a href="mailto:ADRESSE@A-COMPLETER">ADRESSE@A-COMPLETER</a></p>
    </form>
  );
}
```

### 5.8 Menu burger accessible (extrait de `Header.jsx`)

```jsx
const [open, setOpen] = useState(false);

<button
  aria-expanded={open}          // état annoncé aux lecteurs d'écran
  aria-controls="menu-principal"
  aria-label="Menu"
  onClick={() => setOpen(!open)}
>
  ☰
</button>
<nav id="menu-principal" aria-label="Navigation principale" className={open ? "ouvert" : ""}>
  {/* NavLink ajoute la classe "active" ; ajouter aria-current est automatique */}
</nav>
```

---

## 6. Format des données (modèle du CDC §5.3)

Les noms de champs sont sans accent pour le code. **Aucun contenu n'est inventé ici** : remplacez les valeurs `[…]` par vos fiches sourcées et supprimez les entrées « TEST » avant la livraison.

```json
[
  {
    "id": "test-1",
    "titre": "[TEST — à remplacer par le titre réel]",
    "region": "Nord",
    "categorie": "immatériel",
    "niveau": "débutant",
    "description": "[À rédiger]",
    "image": "/images/[fichier].webp",
    "alt": "[Description de l'image]",
    "credit": "[Auteur, source]",
    "licence": "[ex. CC BY-SA 4.0 — à vérifier fichier par fichier]",
    "sources": [
      { "titre": "[Titre de la source]", "url": "[https://…]", "consulte": "[AAAA-MM-JJ]" }
    ]
  }
]
```

Règles : `id` unique, en minuscules, sans espace (il sert dans l'URL) ; deux sources minimum par fiche ; `credit` et `licence` obligatoires pour toute image.

---

## 7. Points d'attention

**Accessibilité (F11)**
- Lien d'évitement « Aller au contenu » en premier élément focalisable.
- Un seul `h1` par page ; `header`, `nav`, `main`, `footer` présents.
- Boutons et liens atteignables au clavier ; focus visible (`:focus-visible`).
- Images : `alt` renseigné, `alt=""` pour le décor ; texte sur image avec voile sombre.
- Formulaire : `label` lié à chaque champ, erreurs en texte et `aria-invalid`.
- Menu burger : `aria-expanded` et `aria-controls`.
- Titre de page (`document.title`) mis à jour par page, avec un `useEffect` simple dans chaque page.

**Responsive (F09)**
- Écrire d'abord le CSS mobile, puis `@media (min-width: 640px)` et `@media (min-width: 1024px)`.
- Grille de cartes : 1 colonne en mobile, 2 en tablette, 3 en desktop.
- Zones tactiles d'au moins 44 px ; corps de texte à 16 px minimum.

**Routage**
- `vercel.json` présent **avant** le premier déploiement.
- Utiliser `Link` et `NavLink`, jamais `<a href>` pour les liens internes (sinon rechargement complet).
- Page `NotFound` pour toute route ou tout `id` inconnu.

**Performance et connectivité**
- Images en WebP, redimensionnées à leur taille d'affichage ; `loading="lazy"` sous la ligne de flottaison.
- Polices : deux familles, graisses limitées ; `font-display: swap`.
- Aucune dépendance inutile ; vérifier le poids avec `npm run build`.

**Qualité et Git**
- Une branche par fonctionnalité, commits courts et lisibles (« Ajoute le filtre région sur Patrimoine »).
- Déployer à chaque étape terminée, pas seulement à la fin (risque R7).
- `.gitignore` : `node_modules`, `dist`.

**Cohérence avec le CDC et la maquette**
- Le compteur du hero se calcule avec `countRegions(patrimoine)` : il reste vrai quand les fiches changent. S'il affiche un autre chiffre que « 6 », mettez la maquette à jour.
- Libellés des cartes alignés sur les types du modèle de données : Fiche patrimoine, Fiche méthode, Outil, Acteur/projet (écart n° 9 du CDC).
- Les liens « Crédits » et « Communauté de recherche » pointent vers `/a-propos` (écart n° 10).
- Icône de recherche : à masquer tant que F12 n'est pas livrée.

---

## 8. Checklist de fin de phase

- [ ] Dépôt GitHub avec historique propre
- [ ] Site déployé sur Vercel, routes OK au rechargement
- [ ] F01 à F11 livrées (voir recette CDC §10.2)
- [ ] Au moins 14 fiches intégrées, chacune avec 2 sources et un crédit d'image
- [ ] Lighthouse accessibilité ≥ 90 ; navigation au clavier complète
- [ ] Test sur un téléphone réel
- [ ] README rédigé (installation, scripts, structure, rôles)

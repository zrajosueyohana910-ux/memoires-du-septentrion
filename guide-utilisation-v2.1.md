# Guide d'utilisation — MémoireS du Septentrion

*ZRA Josue Yohana et Bambe Kennedy · IBAI, Université de Garoua · UE « Hypermédia et Web Sémantique », Master 1 Arts et Humanités · Octobre 2026*

**Version 2.1** — 17 octobre 2026

Ce guide s'adresse aux utilisateurs finaux (étudiants, chercheurs, curieux, diaspora) qui souhaitent parcourir l'archive.

---

## 1. À qui s'adresse ce guide

Aux personnes qui veulent découvrir le patrimoine culturel du Septentrion camerounais (Adamaoua, Nord, Extrême-Nord) sans connaissance technique préalable.

---

## 2. Accès au prototype

### Option A — En ligne (recommandé)

**URL** : https://memoires-du-septentrion.vercel.app

Aucune installation nécessaire.

### Option B — En local

1. Ouvrez le dossier `noeuds/`
2. Double-cliquez sur `n01.html`
3. Naviguez avec les liens

---

## 3. Parcours recommandé

```
Accueil (n01)
    ↓
Explorer (n02)
    ↓
┌──────────────┬──────────────┬──────────────┬──────────────┬──────────────┐
│   Peuples    │   Langues    │    Sites     │  Rituels et  │  Instruments │
│     (n03)    │     (n04)    │    (n05)     │  fêtes (n06) │     (n07)    │
└──────┬───────┴──────────────┴──────┬───────┴──────────────┴──────────────┘
       │                              │
       ↓                              ↓
┌──────────────┐              ┌──────────────┐
│  Fiches      │              │  Fiche       │
│  détaillées  │              │  détaillée   │
│ (n10 à n13)  │              │  (n10, n15)  │
└──────────────┘              └──────────────┘
```

---

## 4. Les 17 pages du prototype

| Page | Titre | Description |
|---|---|---|
| n01 | Accueil | Présentation générale |
| n02 | Explorer | Index des 5 catégories |
| n03 | Peuples | Liste des peuples |
| n04 | Langues | Liste des langues |
| n05 | Sites patrimoniaux | Liste des sites |
| n06 | Rituels et fêtes | Liste des rituels et fêtes |
| n07 | Instruments | Liste des instruments |
| n08 | Contribuer | Comment contribuer |
| n09 | À propos | Présentation du projet |
| n10 | Diy-Gid-Biy | Fiche détaillée |
| n11 | Kapsiki | Fiche détaillée |
| n12 | Mafa | Fiche détaillée |
| n13 | Fulbe | Fiche détaillée |
| n14 | Contes de Goggo Addi | Fiche détaillée |
| n15 | Rituels mafa | Fiche détaillée |
| n16 | Balafon | Fiche détaillée |
| 404 | Page introuvable | En cas d'URL incorrecte |

---

## 5. Fonctionnalités

| Fonctionnalité | État |
|---|---|
| Navigation hiérarchique (4 liens + 5 catégories) | OUI |
| Fiches détaillées | OUI |
| Mode sombre automatique | OUI |
| Accessibilité clavier | OUI |
| Structure HTML sémantique | OUI |
| JSON-LD intégré | OUI |
| Page 404 personnalisée | OUI |
| Carte interactive (n08) | SANS MARQUEURS |
| Lecteur audio (contes) | MÉDIAS À INTÉGRER |
| Sous-titres WebVTT | FICHIERS À PRODUIRE |

---

## 6. Accessibilité

- **Navigation clavier** : Tab, Entrée, focus visible (or safran)
- **Mode sombre** : automatique via prefers-color-scheme
- **Structure sémantique** : header, nav, main, article, footer
- **Contrastes** : WCAG AA
- **Texte alternatif** : sur chaque image

---

## 7. Interroger les données (utilisateur avancé)

### 7.1 Lancer Fuseki

```bash
fuseki-server --file=archive.ttl /memoires
```

### 7.2 Ouvrir YASGUI

Aller sur http://localhost:3030, pointer vers l'endpoint /memoires/sparql.

### 7.3 Exécuter une requête

Copier une requête de requetes.sparql (QC1, QC3, QC4, QC5) dans YASGUI.

**Exemples** :
- QC1 (contes par peuple) → 1 ligne
- QC5 (comptage par catégorie) → 23 entités

---

## 8. Limites connues

- **QC2 vide** : aucune source ne relie instruments, rituels, peuples
- **Médias non intégrés** : photos, vidéos, audio absents
- **Carte sans marqueurs** : coordonnées WGS84 à relever
- **Domaine fictif** : memoria-nord.cm (redirection 303 à simuler)
- **Corpus limité** : 23 entités (extension progressive)

---

## 9. Contact

Email : zrajosueyohana910@gmail.com

**Dépôt** : github.com/zrajosueyohana910-ux/memoires-du-septentrion

---

*Version 2.1 · 17 octobre 2026 · ZRA Josue Yohana et Bambe Kennedy*

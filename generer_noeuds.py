#!/usr/bin/env python3
"""Génère les 9 nœuds hypermédias de MémoireS du Nord à partir de noeud-template.html.
Usage : python generer_noeuds.py [dossier_de_sortie]   (défaut : ./noeuds)
Bibliothèque standard uniquement."""
import html
import json
import sys
from pathlib import Path
from string import Template
from corps_noeuds import CORPS, SURTITRES

ID = "http://memoria-nord.cm/id/"
PAGE = "http://memoria-nord.cm/page/noeud/"

# slug, titre, résumé, entités décrites (uri, nom), liens sortants, médias
NOEUDS = {
    "n01": ("Accueil",
            "Archive hypermédia sémantique du patrimoine culturel du Septentrion camerounais.",
            [("dataset/archive", "MémoireS du Septentrion")],
            ["n02", "n09"],
            {"images": 1}),
    "n02": ("Explorer",
            "Choisissez une catégorie pour explorer le patrimoine du Septentrion.",
            [],
            ["n03", "n04", "n05", "n06", "n07"],
            {}),
    "n03": ("Peuples",
            "Découvrez les peuples du Septentrion camerounais.",
            [("peuple/kapsiki", "Kapsiki"), ("peuple/mafa", "Mafa"), ("peuple/fulbe", "Fulbe")],
            ["n01", "n02", "n11", "n12", "n13"],
            {"images": 1}),
    "n04": ("Langues",
            "Les langues parlées dans le Septentrion.",
            [("langue/psikye", "Psikyɛ"), ("langue/fulfulde", "Fulfulde")],
            ["n01", "n02"],
            {}),
    "n05": ("Sites patrimoniaux",
            "Lieux et monuments remarquables du Septentrion.",
            [("site/diy-gid-biy", "Diy-Gid-Biy"), ("site/rhumsiki", "Rhumsiki"), ("site/lamidat-de-garoua", "Lamidat de Garoua")],
            ["n01", "n02", "n10"],
            {"images": 1}),
    "n06": ("Rituels et fêtes",
            "Célébrations et traditions du Septentrion.",
            [("rituel/rituels-mafa", "Rituels mafa"), ("fete/msla", "Msla"), ("fete/goalala", "Goalala"), ("fete/maray", "Maray")],
            ["n01", "n02", "n15"],
            {"images": 1}),
    "n07": ("Instruments",
            "Instruments de musique traditionnels du Septentrion.",
            [("instrument/balafon", "Balafon"), ("instrument/tambour-d-eau", "Tambour d'eau"), ("instrument/corne-flute", "Corne-flûte")],
            ["n01", "n02", "n16"],
            {}),
    "n08": ("Contribuer",
            "Participez à l'enrichissement de l'archive.",
            [],
            ["n01", "n09"],
            {}),
    "n09": ("À propos",
            "Présentation du projet et de l'équipe.",
            [("dataset/archive", "MémoireS du Septentrion")],
            ["n01", "n02", "n08"],
            {}),
    "n10": ("Diy-Gid-Biy",
            "Ensemble de vestiges en pierre sèche, inscrit à l'UNESCO en juillet 2025.",
            [("site/diy-gid-biy", "Diy-Gid-Biy")],
            ["n01", "n02", "n05", "n12", "n15"],
            {"images": 3}),
    "n11": ("Kapsiki",
            "Peuple des Monts Mandara, de langue psikyɛ.",
            [("peuple/kapsiki", "Kapsiki")],
            ["n01", "n02", "n03", "n05"],
            {"images": 2}),
    "n12": ("Mafa",
            "Peuple présent depuis le XVe siècle, lié au site Diy-Gid-Biy.",
            [("peuple/mafa", "Mafa")],
            ["n01", "n02", "n03", "n10", "n15"],
            {"images": 2}),
    "n13": ("Fulbe",
            "Élite islamisée, classe dirigeante du Septentrion.",
            [("peuple/fulbe", "Fulbe")],
            ["n01", "n02", "n03", "n05"],
            {"images": 2}),
    "n14": ("Contes de Goggo Addi",
            "Recueil des contes de la conteuse peule Goggo Addi.",
            [("collection/contes-goggo-addi", "Contes de Goggo Addi"), ("personne/goggo-addi", "Goggo Addi")],
            ["n01", "n02", "n06"],
            {"audio": 1}),
    "n15": ("Rituels mafa",
            "Sacrifices et cérémonies pratiqués sur les sites sacrés.",
            [("rituel/rituels-mafa", "Rituels mafa")],
            ["n01", "n02", "n06", "n10", "n12"],
            {"images": 2}),
    "n16": ("Balafon",
            "Xylophone à calebasses, instrument de percussion idiophone mélodique.",
            [("instrument/balafon", "Balafon")],
            ["n01", "n02", "n07"],
            {}),
}

LEAFLET_HEAD = (
    '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.css">\n'
    '<script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.js"></script>'
)
LEAFLET_BODY = """<div id="carte" role="region" aria-label="Carte interactive des sites du corpus" style="height:24rem"></div>
<h2>Sites du corpus (alternative textuelle)</h2>
<ul>
<li><a href="n02.html">Diy-Gid-Biy</a></li>
<li><a href="n09.html">Lamidat de Garoua</a></li>
</ul>
<script>
/* Vue par défaut, à remplacer par les marqueurs issus d'une requête SPARQL (coordonnées à relever). */
var carte = L.map("carte").setView([9.0, 13.5], 7);
L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {attribution: "© OpenStreetMap"}).addTo(carte);
</script>"""


def medias(slug, spec):
    blocs = []
    for i in range(1, spec.get("images", 0) + 1):
        blocs.append(
            f'<figure><img src="../media/{slug}-{i}.jpg" alt="[À rédiger : description de la photo {i}]">'
            f"<figcaption>[Légende et crédit à rédiger]</figcaption></figure>")
    if spec.get("video"):
        blocs.append(
            f'<figure><video controls preload="metadata"><source src="../media/{slug}.mp4" type="video/mp4">'
            f'<track kind="subtitles" srclang="fr" label="Français" src="../media/{slug}.vtt" default>'
            f"Votre navigateur ne sait pas lire cette vidéo.</video>"
            f"<figcaption>[Légende et crédit à rédiger]</figcaption></figure>")
    if spec.get("audio"):
        blocs.append(
            f'<figure><audio controls src="../media/{slug}.mp3"></audio>'
            f"<figcaption>[Légende et crédit à rédiger]</figcaption></figure>")
    if spec.get("transcription"):
        blocs.append("<details><summary>Transcription</summary><p>[Transcription à rédiger]</p></details>")
    return "\n".join(blocs)


def jsonld(slug, titre, about):
    doc = {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "@id": PAGE + slug,
        "name": titre,
        "inLanguage": "fr",
        "isPartOf": {"@type": "WebSite", "name": "MémoireS du Nord", "url": "http://memoria-nord.cm/"},
    }
    if about:
        doc["about"] = [{"@id": ID + uri, "name": nom} for uri, nom in about]
    # "</" échappé pour qu'aucune donnée ne puisse fermer la balise <script>
    return json.dumps(doc, ensure_ascii=False, indent=2).replace("</", "<\\/")


def main():
    base = Path(__file__).parent
    sortie = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("noeuds")
    sortie.mkdir(parents=True, exist_ok=True)
    gabarit = Template((base / "noeud-template.html").read_text(encoding="utf-8"))
    for slug, (titre, resume, about, liens, spec) in NOEUDS.items():
        items = "\n".join(
            f'<li><a href="{cible}.html">{html.escape(NOEUDS[cible][0])}</a></li>' for cible in liens)
        page = gabarit.substitute(
            titre=html.escape(titre), resume=html.escape(resume), liens=items,
            medias=medias(slug, spec), jsonld=jsonld(slug, titre, about),
            extra_head=LEAFLET_HEAD if slug == "n08" else "",
            extra_body=LEAFLET_BODY if slug == "n08" else "",
            corps=CORPS.get(slug, "<p>Contenu à rédiger.</p>"),
            surtitre=SURTITRES.get(slug, slug.upper()))
        (sortie / f"{slug}.html").write_text(page, encoding="utf-8")
    print(f"{len(NOEUDS)} pages écrites dans {sortie}")


if __name__ == "__main__":
    main()

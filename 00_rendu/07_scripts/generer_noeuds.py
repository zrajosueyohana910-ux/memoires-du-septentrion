#!/usr/bin/env python3
"""Génère les 9 nœuds hypermédias de MémoireS du Nord à partir de noeud-template.html.
Usage : python generer_noeuds.py [dossier_de_sortie]   (défaut : ./noeuds)
Bibliothèque standard uniquement."""
import html
import json
import sys
from pathlib import Path
from string import Template

ID = "http://memoria-nord.cm/id/"
PAGE = "http://memoria-nord.cm/page/noeud/"

# slug, titre, résumé, entités décrites (uri, nom), liens sortants, médias
NOEUDS = {
    "n01": ("Accueil",
            "Archive hypermédia sémantique du patrimoine culturel du Nord-Cameroun.",
            [("dataset/archive", "MémoireS du Nord")],
            ["n02", "n03", "n04", "n05", "n06", "n07", "n08", "n09"],
            {"images": 1, "audio": 1}),
    "n02": ("Diy-Gid-Biy",
            "Ensemble de vestiges en pierre sèche, inscrit à l'UNESCO en juillet 2025.",
            [("site/diy-gid-biy", "Diy-Gid-Biy")],
            ["n01", "n04", "n07", "n08"],
            {"images": 5, "video": 1}),
    "n03": ("Kapsiki",
            "Peuple des Monts Mandara, de langue psikyɛ.",
            [("peuple/kapsiki", "Kapsiki")],
            ["n01", "n05", "n08"],
            {"images": 2, "audio": 1}),
    "n04": ("Mafa",
            "Peuple présent depuis le XVe siècle, lié au site Diy-Gid-Biy.",
            [("peuple/mafa", "Mafa")],
            ["n01", "n02", "n07"],
            {"images": 2}),
    "n05": ("Instruments",
            "Balafon, tambour d'eau et corne-flûte.",
            [("instrument/balafon", "Balafon"),
             ("instrument/tambour-d-eau", "Tambour d'eau"),
             ("instrument/corne-flute", "Corne-flûte")],
            ["n01", "n03", "n07", "n08"],
            {"audio": 1, "video": 1}),
    "n06": ("Contes de Goggo Addi",
            "Recueil des contes de la conteuse peule Goggo Addi, enregistrés et transcrits "
            "par Ursula Baumgardt entre 1985 et 1989.",
            [("collection/contes-goggo-addi", "Contes de Goggo Addi"),
             ("personne/goggo-addi", "Goggo Addi")],
            ["n01", "n07", "n09"],
            {"audio": 1, "transcription": 1}),
    "n07": ("Rituels et fêtes",
            "Rituels mafa et fêtes Msla, Goalala et Maray.",
            [("rituel/rituels-mafa", "Rituels mafa"), ("fete/msla", "Msla"),
             ("fete/goalala", "Goalala"), ("fete/maray", "Maray")],
            ["n01", "n02", "n05", "n06"],
            {"images": 2, "video": 1}),
    "n08": ("Carte interactive",
            "Carte des sites et lieux du corpus.",
            [],
            ["n01", "n02", "n03", "n04", "n05", "n06", "n07", "n09"],
            {}),
    "n09": ("Fulbe et Lamidat de Garoua",
            "Les Fulbe, élite islamisée du Nord, et la chefferie traditionnelle du Lamidat de Garoua.",
            [("peuple/fulbe", "Fulbe"), ("site/lamidat-de-garoua", "Lamidat de Garoua")],
            ["n01", "n06", "n08"],
            {"images": 2}),
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
            extra_body=LEAFLET_BODY if slug == "n08" else "")
        (sortie / f"{slug}.html").write_text(page, encoding="utf-8")
    print(f"{len(NOEUDS)} pages écrites dans {sortie}")


if __name__ == "__main__":
    main()

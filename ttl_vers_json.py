#!/usr/bin/env python3
"""Convertit archive.ttl (MémoireS du Nord) en JSON pour le site React."""
import argparse
import json
from pathlib import Path
from rdflib import Graph, Namespace
from rdflib.namespace import RDF, SKOS, DCTERMS

MV = Namespace("http://memoria-nord.cm/vocab#")
SCHEMA = Namespace("https://schema.org/")

CLASSES_AFFICHABLES = {
    MV.Site: "matériel",
    MV.Rituel: "immatériel",
    MV.Fete: "immatériel",
    MV.RecueilDeContes: "immatériel",
    MV.Instrument: "immatériel",
}


def extraire_label(g, sujet, langue="fr"):
    for label in g.objects(sujet, SKOS.prefLabel):
        if hasattr(label, "language") and label.language == langue:
            return str(label)
    for label in g.objects(sujet, SKOS.prefLabel):
        return str(label)
    return None


def extraire_description(g, sujet):
    descriptions = [str(d) for d in g.objects(sujet, DCTERMS.description)]
    if not descriptions:
        return "[Description à compléter.]"
    return max(descriptions, key=len)


def extraire_litteral(g, sujet, predicat, defaut=None):
    for valeur in g.objects(sujet, predicat):
        s = str(valeur)
        if s.lower() in ("true", "1"):
            return True
        if s.lower() in ("false", "0"):
            return False
        return s
    return defaut


def extraire_uri(g, sujet, predicat, defaut=None):
    for valeur in g.objects(sujet, predicat):
        uri = str(valeur)
        if "memoria-nord.cm/media/" in uri:
            slug = uri.split("/")[-1].replace(".jpg", ".svg").replace(".png", ".svg")
            return "/images/" + slug
        return uri
    return defaut


def extraire_sources(g, sujet):
    sources = []
    for source in g.objects(sujet, DCTERMS.source):
        uri = str(source)
        titre = uri.split("/")[-1]
        if not titre:
            try:
                titre = uri.split("//")[1].split("/")[0]
            except IndexError:
                titre = uri
        titre = titre.replace("_", " ").replace("-", " ").strip()
        if not titre:
            titre = "Source externe"
        sources.append({"titre": titre, "url": uri, "consulte": "2026-10-14"})
    if not sources:
        sources.append({
            "titre": "Wikidata",
            "url": "https://www.wikidata.org/",
            "consulte": "2026-10-14"
        })
    return sources


def convertir(chemin_ttl="archive.ttl"):
    g = Graph()
    g.parse(chemin_ttl, format="turtle")
    fiches = []
    sujets_traites = set()

    for sujet in g.subjects(RDF.type, None):
        if sujet in sujets_traites:
            continue
        for type_sujet in g.objects(sujet, RDF.type):
            if type_sujet in CLASSES_AFFICHABLES:
                label = extraire_label(g, sujet)
                if not label:
                    continue
                slug = str(sujet).split("/")[-1]
                categorie_defaut = CLASSES_AFFICHABLES[type_sujet]
                fiche = {
                    "id": slug,
                    "titre": label,
                    "region": extraire_litteral(g, sujet, MV.region, "Nord"),
                    "categorie": extraire_litteral(g, sujet, MV.categorie, categorie_defaut),
                    "niveau": extraire_litteral(g, sujet, MV.niveau, "débutant"),
                    "description": extraire_description(g, sujet),
                    "image": extraire_uri(g, sujet, SCHEMA.image, "/images/placeholder.svg"),
                    "alt": "Représentation de " + label,
                    "credit": "Wikimedia Commons",
                    "licence": extraire_litteral(g, sujet, DCTERMS.rights, "CC BY-SA 4.0"),
                    "mise_en_avant": extraire_litteral(g, sujet, MV.miseEnAvant, False),
                    "sources": extraire_sources(g, sujet)
                }
                fiches.append(fiche)
                sujets_traites.add(sujet)
                break

    fiches.sort(key=lambda f: (not f["mise_en_avant"], f["titre"]))
    return fiches


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--entree", default="archive.ttl")
    parser.add_argument("--sortie", default="patrimoine.json")
    args = parser.parse_args()

    fiches = convertir(args.entree)
    with open(args.sortie, "w", encoding="utf-8") as f:
        json.dump(fiches, f, ensure_ascii=False, indent=2)

    print("OK " + str(len(fiches)) + " fiches exportees vers " + args.sortie)
    for f in fiches:
        marqueur = "[*]" if f["mise_en_avant"] else "[ ]"
        print("   " + marqueur + " " + f["titre"] + " (" + f["categorie"] + ", " + f["region"] + ")")


if __name__ == "__main__":
    main()

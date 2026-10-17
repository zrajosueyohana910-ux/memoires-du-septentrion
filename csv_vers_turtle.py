#!/usr/bin/env python3
"""MémoireS du Nord : génère archive.ttl à partir de trois fichiers CSV.

  entites.csv      id, classes, label_fr, description_fr, source
  relations.csv    sujet, predicat, objet, type   (sujet vide = même sujet que la ligne précédente)
  alignements.csv  entite, relation, cible, verifie, note

Seuls les alignements marqués verifie=oui entrent dans archive.ttl.
Les autres vont dans alignements_a_verifier.ttl.

Usage :
  python csv_vers_turtle.py donnees --verifier      (contrôle des CSV, sans rdflib)
  python csv_vers_turtle.py donnees                 (génère les fichiers, nécessite rdflib)
Installation : pip install rdflib
"""
import argparse
import csv
import re
import sys
from pathlib import Path

BASE = "http://memoria-nord.cm/"
TYPES = ["peuple", "langue", "site", "lieu", "personne", "collection",
         "rituel", "fete", "instrument", "dataset"]
STD = {
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "owl": "http://www.w3.org/2002/07/owl#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "dct": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "foaf": "http://xmlns.com/foaf/0.1/",
    "schema": "https://schema.org/",
    "edm": "http://www.europeana.eu/schemas/edm/",
    "prov": "http://www.w3.org/ns/prov#",
    "wd": "http://www.wikidata.org/entity/",
    "mv": BASE + "vocab#",
}
# classes locales : (classe parente, étiquette)
CLASSES_MV = {
    "Peuple": ("foaf:Group", "Peuple"),
    "Langue": ("dct:LinguisticSystem", "Langue"),
    "Site": ("schema:Place", "Site patrimonial"),
    "Lieu": ("schema:Place", "Lieu"),
    "RecueilDeContes": ("edm:ProvidedCHO", "Recueil de contes"),
    "Rituel": ("schema:Event", "Rituel"),
    "Fete": ("schema:Event", "Fête"),
    "Instrument": (None, "Instrument de musique"),
}
TYPES_OBJET = {"uri", "fr", "string", "integer", "gYear", "gYearMonth", "date"}
OUI = {"oui", "o", "yes", "y", "1", "true"}


def expand(curie):
    if curie.startswith(("http://", "https://")):
        return curie
    pref, sep, local = curie.partition(":")
    if not sep:
        raise ValueError(f"CURIE invalide : {curie!r}")
    if pref in STD:
        return STD[pref] + local
    if pref in TYPES:
        return f"{BASE}id/{pref}/{local}"
    raise ValueError(f"Préfixe inconnu : {pref!r} dans {curie!r}")


def cible_uri(cible):
    if re.fullmatch(r"Q\d+", cible):
        return STD["wd"] + cible
    m = re.fullmatch(r"geonames:(\d+)", cible)
    if m:
        return f"https://sws.geonames.org/{m.group(1)}/"
    if cible.startswith(("http://", "https://")):
        return cible
    raise ValueError(f"Cible d'alignement non reconnue : {cible!r} (attendu : Q123, geonames:123 ou URL)")


def lire(chemin):
    with open(chemin, newline="", encoding="utf-8-sig") as f:
        return [{k: (v or "").strip() for k, v in ligne.items()} for ligne in csv.DictReader(f)]


def charger(dossier):
    entites = lire(dossier / "entites.csv")
    relations = lire(dossier / "relations.csv")
    alignements = lire(dossier / "alignements.csv")
    precedent = ""
    for r in relations:  # remplissage du sujet vide avec le sujet précédent
        if r["sujet"]:
            precedent = r["sujet"]
        else:
            r["sujet"] = precedent
    return entites, relations, alignements


def verifier(entites, relations, alignements):
    erreurs, avertissements = [], []
    ids = {e["id"] for e in entites}
    for e in entites:
        try:
            [expand(c.strip()) for c in e["classes"].split("|")]
            expand(e["id"])
        except ValueError as ex:
            erreurs.append(f"entites.csv : {ex}")
        if not e["label_fr"]:
            erreurs.append(f"entites.csv : {e['id']} n'a pas de label_fr")
    for i, r in enumerate(relations, start=2):
        ou = f"relations.csv ligne {i}"
        if r["sujet"] not in ids:
            erreurs.append(f"{ou} : sujet inconnu {r['sujet']!r}")
        if r["type"] not in TYPES_OBJET:
            erreurs.append(f"{ou} : type {r['type']!r} inconnu")
        try:
            expand(r["predicat"])
            if r["type"] == "uri":
                expand(r["objet"])
                if r["objet"].partition(":")[0] in TYPES and r["objet"] not in ids:
                    erreurs.append(f"{ou} : référence orpheline {r['objet']!r}")
        except ValueError as ex:
            erreurs.append(f"{ou} : {ex}")
    n_verifies = 0
    for i, a in enumerate(alignements, start=2):
        ou = f"alignements.csv ligne {i}"
        if a["entite"] not in ids:
            erreurs.append(f"{ou} : entité inconnue {a['entite']!r}")
        try:
            expand(a["relation"])
            cible_uri(a["cible"])
        except ValueError as ex:
            erreurs.append(f"{ou} : {ex}")
        if a["cible"] == "Q1000":
            avertissements.append(f"{ou} : Q1000 est probablement le Gabon, pas le Cameroun (à vérifier)")
        if a["verifie"].lower() in OUI:
            n_verifies += 1
    if len(entites) < 15:
        avertissements.append(f"{len(entites)} entités (< 15 requis)")
    if n_verifies < 10:
        avertissements.append(f"{n_verifies} alignement(s) vérifié(s) sur 10 requis")
    return erreurs, avertissements, n_verifies


def construire(entites, relations, alignements, sortie, sortie_verif):
    try:
        from rdflib import Graph, Literal, URIRef, RDF, RDFS
        from rdflib.namespace import XSD
    except ImportError:
        sys.exit("rdflib est absent : pip install rdflib")

    def nouveau_graphe():
        g = Graph()
        for pref, uri in STD.items():
            g.bind(pref, uri)
        for t in TYPES:
            g.bind(t, f"{BASE}id/{t}/")
        return g

    def U(curie):
        return URIRef(expand(curie))

    g = nouveau_graphe()
    for nom, (parent, etiquette) in CLASSES_MV.items():
        c = U("mv:" + nom)
        g.add((c, RDF.type, RDFS.Class))
        if parent:
            g.add((c, RDFS.subClassOf, U(parent)))
        g.add((c, RDFS.label, Literal(etiquette, lang="fr")))

    for e in entites:
        s = U(e["id"])
        classes = [c.strip() for c in e["classes"].split("|")]
        for c in classes:
            g.add((s, RDF.type, U(c)))
        g.add((s, U("skos:prefLabel"), Literal(e["label_fr"], lang="fr")))
        if "foaf:Person" in classes:
            g.add((s, U("foaf:name"), Literal(e["label_fr"])))
        if e["description_fr"]:
            g.add((s, U("dct:description"), Literal(e["description_fr"], lang="fr")))
        if e["source"]:
            src = e["source"]
            g.add((s, U("dct:source"), URIRef(src) if src.startswith("http") else Literal(src)))

    for r in relations:
        t, v = r["type"], r["objet"]
        if t == "uri":
            o = U(v)
        elif t == "fr":
            o = Literal(v, lang="fr")
        elif t == "integer":
            o = Literal(int(v))
        elif t == "string":
            o = Literal(v)
        else:  # gYear, gYearMonth, date
            o = Literal(v, datatype=getattr(XSD, t))
        g.add((U(r["sujet"]), U(r["predicat"]), o))

    g_verif = nouveau_graphe()
    n_ok = 0
    for a in alignements:
        triplet = (U(a["entite"]), U(a["relation"]), URIRef(cible_uri(a["cible"])))
        if a["verifie"].lower() in OUI:
            g.add(triplet)
            n_ok += 1
        else:
            g_verif.add(triplet)

    g.serialize(destination=str(sortie), format="turtle")
    g_verif.serialize(destination=str(sortie_verif), format="turtle")
    print(f"{sortie} : {len(g)} triplets, {len(entites)} entités, {n_ok} alignement(s) vérifié(s)")
    print(f"{sortie_verif} : {len(g_verif)} alignement(s) en attente de vérification")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("dossier", nargs="?", default=".", help="dossier contenant les trois CSV")
    p.add_argument("--sortie", default="archive.ttl")
    p.add_argument("--sortie-verif", default="alignements_a_verifier.ttl")
    p.add_argument("--verifier", action="store_true", help="contrôler les CSV sans générer de Turtle")
    args = p.parse_args()

    entites, relations, alignements = charger(Path(args.dossier))
    erreurs, avertissements, n_verifies = verifier(entites, relations, alignements)
    for a in avertissements:
        print("AVERTISSEMENT :", a)
    for e in erreurs:
        print("ERREUR :", e)
    print(f"{len(entites)} entités, {len(relations)} relations, "
          f"{len(alignements)} alignements ({n_verifies} vérifiés)")
    if erreurs:
        sys.exit(1)
    if not args.verifier:
        construire(entites, relations, alignements, Path(args.sortie), Path(args.sortie_verif))


if __name__ == "__main__":
    main()

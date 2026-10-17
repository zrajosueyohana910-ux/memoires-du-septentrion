"""Contenus spécifiques des nœuds MémoireS du Septentrion (approche A — hiérarchique)."""

CORPS = {
    # ============ n01 — Accueil ============
    "n01": """<p class="noeud__texte">
<strong>MémoireS du Septentrion</strong> est une archive hypermédia sémantique consacrée
au patrimoine culturel du Septentrion camerounais (Adamaoua, Nord, Extrême-Nord).
Elle relie, dans un graphe de données RDF, des peuples, des langues, des sites,
des contes, des rituels, des fêtes et des instruments de musique.
</p>
<p class="noeud__texte">
Cette archive est le résultat d'une démarche en humanités numériques : chaque
entité est modélisée selon des vocabulaires standards (DCTerms, FOAF, SKOS,
schema.org) et alignée sur Wikidata.
</p>
<p class="noeud__texte">
Pour explorer cette archive, consultez la page <a href="n02.html">Explorer</a>.
</p>""",

    # ============ n02 — Explorer (INDEX) ============
    "n02": """<p class="noeud__texte">
Choisissez une catégorie pour explorer le patrimoine du Septentrion :
</p>
<ul class="noeud__liste">
<li><a href="n03.html">Peuples</a> — Découvrez les peuples du Septentrion</li>
<li><a href="n04.html">Langues</a> — Les langues parlées dans la région</li>
<li><a href="n05.html">Sites patrimoniaux</a> — Lieux et monuments remarquables</li>
<li><a href="n06.html">Rituels et fêtes</a> — Célébrations et traditions</li>
<li><a href="n07.html">Instruments</a> — Instruments de musique traditionnels</li>
</ul>""",

    # ============ n03 — Peuples ============
    "n03": """<p class="noeud__texte">
Les peuples du Septentrion camerounais sont documentés dans notre ontologie :
</p>
<ul class="noeud__liste">
<li><a href="n11.html">Kapsiki</a> — Peuple des Monts Mandara, de langue psikyɛ</li>
<li><a href="n12.html">Mafa</a> — Peuple présent depuis le XV<sup>e</sup> siècle</li>
<li><a href="n13.html">Fulbe</a> — Élite islamisée, classe dirigeante du Nord</li>
</ul>""",

    # ============ n04 — Langues ============
    "n04": """<p class="noeud__texte">
Les langues documentées dans notre archive :
</p>
<ul class="noeud__liste">
<li><strong>Psikyɛ</strong> — Langue tchadique (branche Biu-Mandara), environ 40 500 locuteurs en 1982. Parlée par les Kapsiki.</li>
<li><strong>Fulfulde</strong> — Langue véhiculaire du Nord-Cameroun, parlée par les Fulbe et les communautés peules.</li>
</ul>""",

    # ============ n05 — Sites patrimoniaux ============
    "n05": """<p class="noeud__texte">
Les sites patrimoniaux du Septentrion :
</p>
<ul class="noeud__liste">
<li><a href="n10.html">Diy-Gid-Biy</a> — Vestiges en pierre sèche, inscrits à l'UNESCO en 2025</li>
<li><strong>Rhumsiki</strong> — Village kapsiki emblématique des Monts Mandara</li>
<li><strong>Lamidat de Garoua</strong> — Chefferie traditionnelle peule</li>
</ul>""",

    # ============ n06 — Rituels et fêtes ============
    "n06": """<p class="noeud__texte">
Le patrimoine immatériel du Septentrion comprend des rituels et des fêtes :
</p>
<ul class="noeud__liste">
<li><a href="n15.html">Rituels mafa</a> — Sacrifices et cérémonies sur les sites sacrés</li>
<li><strong>Msla</strong> — Fête agricole et pastorale marquant la fin des récoltes</li>
<li><strong>Goalala</strong> — Célébration rythmée par des danses et des joutes</li>
<li><strong>Maray</strong> — Fête communautaire qui rassemble éleveurs et agriculteurs</li>
</ul>""",

    # ============ n07 — Instruments ============
    "n07": """<p class="noeud__texte">
Les instruments de musique traditionnels du Septentrion :
</p>
<ul class="noeud__liste">
<li><a href="n16.html">Balafon</a> — Xylophone à calebasses, instrument de percussion idiophone mélodique</li>
<li><strong>Tambour d'eau</strong> — Percussion rituelle composée d'une calebasse remplie d'eau</li>
<li><strong>Corne-flûte</strong> — Instrument à vent rituel fabriqué à partir d'une corne d'animal</li>
</ul>""",

    # ============ n08 — Contribuer ============
    "n08": """<p class="noeud__texte">
Ce portail est un projet collaboratif. Vous pouvez contribuer de plusieurs façons :
</p>
<ul class="noeud__liste">
<li>Proposer une nouvelle fiche (peuple, site, rituel, instrument…)</li>
<li>Signaler une erreur ou une correction</li>
<li>Partager une source ou une référence</li>
<li>Proposer une image libre de droits</li>
</ul>
<p class="noeud__texte">
Pour toute contribution, contactez-nous à l'adresse indiquée dans la page
<a href="n09.html">À propos</a>.
</p>""",

    # ============ n09 — À propos ============
    "n09": """<p class="noeud__texte">
<strong>MémoireS du Septentrion</strong> est une archive hypermédia sémantique du
patrimoine culturel du Septentrion camerounais (Adamaoua, Nord, Extrême-Nord).
</p>
<p class="noeud__texte">
Le projet a été réalisé par ZRA Josue Yohana et Bambe Kennedy, étudiants en
Master 1 Arts et Humanités à l'Institut des Beaux-Arts et de l'Innovation (IBAI),
Université de Garoua.
</p>
<p class="noeud__texte">
<strong>Licence :</strong> métadonnées sous CC BY 4.0. Médias et contes : droits à préciser.
</p>""",

    # ============ n10 — Diy-Gid-Biy (fiche) ============
    "n10": """<p class="noeud__texte">
<strong>Diy-Gid-Biy</strong> est un ensemble de vestiges en pierre sèche situés
dans les Monts Mandara, dans l'Extrême-Nord du Cameroun. Ces constructions,
bâties entre le XII<sup>e</sup> et le XVII<sup>e</sup> siècle, témoignent d'une
organisation sociale complexe.
</p>
<p class="noeud__texte">
Le site a été inscrit au <strong>patrimoine mondial de l'UNESCO</strong> en
juillet 2025, sous le critère (iii).
</p>
<p class="noeud__texte">
Ce site est associé au peuple <a href="n12.html">Mafa</a>, qui pratique encore
aujourd'hui des <a href="n15.html">rituels</a> sur les lieux sacrés.
</p>""",

    # ============ n11 — Kapsiki (fiche) ============
    "n11": """<p class="noeud__texte">
Les <strong>Kapsiki</strong> sont un peuple des Monts Mandara, à la frontière
entre le Cameroun et le Nigeria. Ils sont connus pour leur agriculture en
terrasses et leur architecture en pierre sèche.
</p>
<p class="noeud__texte">
Leur langue, le <strong>psikyɛ</strong>, appartient à la famille tchadique
(branche Biu-Mandara). On estime à environ 40 500 le nombre de locuteurs en 1982.
</p>""",

    # ============ n12 — Mafa (fiche) ============
    "n12": """<p class="noeud__texte">
Les <strong>Mafa</strong> sont un peuple du Septentrion, présent dans la région
des Monts Mandara depuis au moins le XV<sup>e</sup> siècle.
</p>
<p class="noeud__texte">
Ils sont historiquement liés au site de <a href="n10.html">Diy-Gid-Biy</a>, dont
ils seraient les bâtisseurs ou les héritiers. Les Mafa pratiquent encore
aujourd'hui des <a href="n15.html">rituels</a> sur les sites sacrés.
</p>""",

    # ============ n13 — Fulbe (fiche) ============
    "n13": """<p class="noeud__texte">
Les <strong>Fulbe</strong> (ou Peuls) constituent une élite islamisée du
Septentrion, historiquement classe dirigeante de la région. Leur langue est le
<strong>fulfulde</strong>, langue véhiculaire du Nord.
</p>
<p class="noeud__texte">
Ils sont associés au <strong>Lamidat de Garoua</strong>, chefferie
traditionnelle peule et institution centrale de la région.
</p>""",

    # ============ n14 — Contes de Goggo Addi (fiche) ============
    "n14": """<p class="noeud__texte">
<strong>Goggo Addi</strong> (1911-1999) était une conteuse peule née à Bibemi.
Ses contes, transmis oralement en langue <strong>fulfulde</strong>, ont été
enregistrés et transcrits par <strong>Ursula Baumgardt</strong>, chercheuse à
l'INALCO et au CNRS, entre 1985 et 1989.
</p>
<p class="noeud__texte">
Ce recueil est une archive sonore majeure pour la littérature orale fulfulde.
</p>""",

    # ============ n15 — Rituels mafa (fiche) ============
    "n15": """<p class="noeud__texte">
Les <strong>rituels mafa</strong> sont des sacrifices et cérémonies pratiqués
sur les sites de <a href="n10.html">Diy-Gid-Biy</a>, mêlant vénération des
ancêtres et protection des lieux sacrés.
</p>
<p class="noeud__texte">
Ces rituels sont associés au peuple <a href="n12.html">Mafa</a> et témoignent
de la continuité des pratiques culturelles dans les Monts Mandara.
</p>""",

    # ============ n16 — Balafon (fiche) ============
    "n16": """<p class="noeud__texte">
Le <strong>balafon</strong> est un xylophone à calebasses, instrument de
percussion idiophone mélodique utilisé lors des cérémonies et fêtes
traditionnelles d'Afrique de l'Ouest et centrale.
</p>
<p class="noeud__texte">
Il fait partie des instruments emblématiques du patrimoine musical du
Septentrion camerounais.
</p>""",
}

# Sur-titres spécifiques (non utilisés pour l'instant, mais prêts)
SURTITRES = {
    "n01": "Accueil",
    "n02": "Explorer",
    "n03": "Peuples",
    "n04": "Langues",
    "n05": "Sites patrimoniaux",
    "n06": "Rituels et fêtes",
    "n07": "Instruments",
    "n08": "Contribuer",
    "n09": "À propos",
    "n10": "Fiche Diy-Gid-Biy",
    "n11": "Fiche Kapsiki",
    "n12": "Fiche Mafa",
    "n13": "Fiche Fulbe",
    "n14": "Fiche Contes de Goggo Addi",
    "n15": "Fiche Rituels mafa",
    "n16": "Fiche Balafon",
}

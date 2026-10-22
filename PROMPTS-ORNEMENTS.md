# Prompts Gemini — motifs floraux

Faites toutes les images **dans une seule conversation**, pour garder le même style.
Enregistrez-les dans le dossier `ornements/` avec le nom indiqué, puis dites-le à Claude :
il retirera le fond blanc pour que les motifs se posent proprement sur le site.

## Message d'ouverture

```
Je crée des ornements pour un site de faire-part de mariage. Style commun à toutes les images :
illustration aquarelle et gouache raffinée, fleurs d'anémones et de pivoines rouge bordeaux et blanc ivoire,
cœurs dorés, feuillages vert sauge pâle, fines arabesques et filets dorés de style art nouveau,
traits précis et élégants, rendu haut de gamme comme un faire-part de luxe.
Fond blanc pur uni (#FFFFFF), sans ombre portée, sans texte, sans lettre, sans filigrane.
Confirme simplement, je t'envoie les demandes une par une.
```

## Les demandes

**`cadre.png`** — le cadre des prénoms
```
Image 1 : un cadre vertical en forme d'arche ornée, format 3:4. Bordure dorée et bordeaux avec un fleuron bordeaux
en haut au centre, de longues branches fleuries (fleurs bordeaux et ivoire, boutons, feuilles) qui montent
le long des côtés gauche et droit. L'intérieur du cadre est entièrement vide et blanc, très large, pour y écrire du texte.
```

**`coin.png`** — un coin, que le site retourne pour les quatre angles
```
Image 2 : un ornement d'angle placé uniquement dans le coin SUPÉRIEUR GAUCHE de l'image, format carré 1:1.
Petit triangle bordeaux à filet doré avec un croissant de lune doré, prolongé par des arabesques dorées
et deux petites fleurs ivoire qui suivent les bords haut et gauche. Le reste de l'image est blanc et vide.
```

**`separateur.png`** — le séparateur entre les sections
```
Image 3 : une frise horizontale fine et centrée, format 4:1. Au centre une grande fleur ivoire au cœur bordeaux,
de part et d'autre des petites fleurs bordeaux, des boutons et des feuilles, prolongés par des arabesques dorées
qui s'affinent vers les extrémités. Symétrique. Beaucoup de blanc au-dessus et en dessous.
```

**`bouquet.png`** — la branche qui déborde sur le bord des sections
```
Image 4 : une branche de fleurs qui entre dans l'image par le bord GAUCHE, format vertical 2:3.
Trois grandes anémones rouge bordeaux à cœur doré, quelques boutons, feuilles vert sauge à nervures dorées.
La tige est coupée net au bord gauche de l'image. Le reste de l'image est blanc.
```

**`fond.png`** — le motif de fond, très pâle
```
Image 5 : un motif de fond carré 1:1, raccordable en mosaïque, de grandes anémones et feuillages
dessinés en rose très pâle et beige, très peu contrastés, comme un papier peint délicat en filigrane.
```

## Si une image dérape

- Fond coloré : « Refais-la avec un fond blanc pur uni. »
- Texte apparu : « Supprime tout texte et toute lettre. »
- Cadre trop chargé à l'intérieur : « Laisse l'intérieur du cadre entièrement vide. »

## Version autonome en anglais (ChatGPT, Recraft, Ideogram, Firefly, Midjourney)

Chaque prompt se suffit à lui-même. Pour Midjourney, ajoutez le paramètre indiqué à la fin.

**cadre.png** (`--ar 3:4`)
```
Ornate arched wedding frame, vertical, luxury invitation style. Thin gold and deep burgundy double border shaped like a gothic arch, a small burgundy and gold floral crest at the top center. Watercolor and gouache flowers climbing up both sides: deep burgundy anemones and peonies with gold centers, ivory white blossoms, small buds, pale sage green leaves with gold veins, fine gold art nouveau filigree. The inside of the frame is completely empty plain white, large space for text. Symmetrical, elegant, highly detailed. Isolated on a pure white background, no text, no letters, no watermark, no shadow.
```

**coin.png** (`--ar 1:1`)
```
Decorative corner ornament placed only in the top-left corner of the image. A small deep burgundy triangle with a thin gold border and a tiny gold crescent moon and star, extended by gold art nouveau filigree scrolls and two small ivory white watercolor flowers with sage leaves running along the top and left edges. The rest of the image is empty pure white. Luxury wedding invitation style, fine details, no text, no watermark, no shadow.
```

**separateur.png** (`--ar 4:1`)
```
Thin horizontal floral divider for a wedding invitation, centered and symmetrical. In the middle one large ivory white flower with a deep burgundy center, flanked by small deep burgundy blossoms, buds and sage green leaves, extended on both sides by fine gold filigree scrolls that taper to thin points. Watercolor and gouache illustration, gold accents. Lots of empty white space above and below. Isolated on a pure white background, no text, no watermark, no shadow.
```

**bouquet.png** (`--ar 2:3`)
```
A branch of flowers entering the image from the left edge, the stem cut cleanly at the left border. Three large deep burgundy red anemones with gold centers, a few buds, sage green leaves with fine gold veins. Elegant watercolor and gouache botanical illustration, luxury wedding invitation style. The rest of the image is empty pure white. No text, no watermark, no shadow.
```

**fond.png** (`--ar 1:1 --tile`)
```
Seamless tileable wallpaper pattern of large anemone flowers and leaves, drawn in very pale blush pink and light beige line art with soft watercolor wash, very low contrast, delicate like a watermark on luxury paper. Cream background. No text, no watermark.
```

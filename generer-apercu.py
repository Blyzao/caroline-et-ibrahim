"""Génère img/apercu.jpg, l'image d'aperçu du lien (WhatsApp, Facebook) : 1200x630,
photo du couple à droite, prénoms et date sur fond crème à gauche.

Usage : python generer-apercu.py   (modifier les textes plus bas pour un autre mariage)
Les polices (Google Fonts, licence OFL) sont téléchargées dans polices/ au premier lancement.
"""
import os
import urllib.request

from PIL import Image, ImageDraw, ImageFont

SITE = os.path.dirname(os.path.abspath(__file__))
POLICES = os.path.join(SITE, "polices")
SOURCES = {
    "PinyonScript.ttf": "https://github.com/google/fonts/raw/main/ofl/pinyonscript/PinyonScript-Regular.ttf",
    "BodoniModa.ttf": "https://github.com/google/fonts/raw/main/ofl/bodonimoda/BodoniModa%5Bopsz,wght%5D.ttf",
    "Lora.ttf": "https://github.com/google/fonts/raw/main/ofl/lora/Lora%5Bwght%5D.ttf",
}
os.makedirs(POLICES, exist_ok=True)
for nom, url in SOURCES.items():
    if not os.path.exists(os.path.join(POLICES, nom)):
        urllib.request.urlretrieve(url, os.path.join(POLICES, nom))
L, H = 1200, 630
CREME, BORDEAUX, OR, TEXTE = (251, 246, 241), (138, 26, 43), (184, 146, 90), (69, 35, 43)


def police(nom, taille, graisse=None):
    f = ImageFont.truetype(os.path.join(POLICES, nom), taille)
    if graisse:
        try:
            f.set_variation_by_axes([graisse] if nom != "BodoniModa.ttf" else [11, graisse])
        except Exception:
            pass
    return f


# Photo recadrée au format 1,91:1, le couple à droite
photo = Image.open(os.path.join(SITE, "images", "principale-large.jpg")).convert("RGB")
echelle = H / photo.height
photo = photo.resize((round(photo.width * echelle), H), Image.LANCZOS)
fond = Image.new("RGB", (L, H), CREME)
fond.paste(photo, (L - photo.width, 0))

# Voile crème opaque à gauche, qui s'efface vers la photo
voile = Image.new("L", (L, H))
pv = voile.load()
for x in range(L):
    a = 255 if x < 470 else max(0, round(255 * (1 - (x - 470) / 260)))
    for y in range(H):
        pv[x, y] = a
fond.paste(Image.new("RGB", (L, H), CREME), (0, 0), voile)

d = ImageDraw.Draw(fond)
cx = 300  # centre de la colonne de texte


def centre(texte, f, y, couleur, espacement=0):
    if espacement:
        largeur = sum(d.textlength(c, font=f) for c in texte) + espacement * (len(texte) - 1)
        x = cx - largeur / 2
        for c in texte:
            d.text((x, y), c, font=f, fill=couleur)
            x += d.textlength(c, font=f) + espacement
    else:
        d.text((cx, y), texte, font=f, fill=couleur, anchor="ma")


centre("NOUS NOUS DISONS OUI", police("Lora.ttf", 22, 500), 112, TEXTE, espacement=5)
d.line([(cx - 60, 156), (cx + 60, 156)], fill=OR, width=2)
script = police("PinyonScript.ttf", 96)
centre("Caroline", script, 178, BORDEAUX)
centre("&", police("PinyonScript.ttf", 70), 288, BORDEAUX)
centre("Ibrahim", script, 350, BORDEAUX)
d.line([(cx - 60, 486), (cx + 60, 486)], fill=OR, width=2)
centre("01 · 01 · 2027", police("BodoniModa.ttf", 34, 500), 506, BORDEAUX, espacement=6)
centre("ABIDJAN", police("Lora.ttf", 20, 500), 560, TEXTE, espacement=6)

sortie = os.path.join(SITE, "img", "apercu.jpg")
fond.save(sortie, "JPEG", quality=84, optimize=True, progressive=True)
print(sortie, os.path.getsize(sortie) // 1024, "Ko")

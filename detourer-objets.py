"""Détoure un objet plein : seul le fond blanc relié au bord devient transparent.

Sert à la boîte cadeau et aux petits paquets : le blanc à l'intérieur de l'objet (roses ivoire) reste opaque,
contrairement à preparer-ornements.py qui rend transparent tout ce qui est clair.

Usage : python detourer-objets.py <source> <sortie> <taille_max> [seuil, 205 par défaut]
"""
import sys
from collections import deque

from PIL import Image, ImageFilter

src, sortie, taille = sys.argv[1], sys.argv[2], int(sys.argv[3])
# Pixels plus clairs que ce seuil et reliés au bord = fond ; 205 retire aussi l'ombre grise posée sous l'objet
SEUIL = int(sys.argv[4]) if len(sys.argv) > 4 else 205
im = Image.open(src).convert("RGB")
im.thumbnail((taille * 2, taille * 2))  # travail à 2x, réduit à la fin pour des bords lisses
w, h = im.size
px = im.load()

# Remplissage depuis les bords : un pixel est du fond s'il est très clair et touche le fond
fond = bytearray(w * h)
file = deque()
for x in range(w):
    file.append((x, 0)); file.append((x, h - 1))
for y in range(h):
    file.append((0, y)); file.append((w - 1, y))
while file:
    x, y = file.popleft()
    i = y * w + x
    if fond[i]:
        continue
    r, g, b = px[x, y]
    if min(r, g, b) < SEUIL:  # assez foncé : c'est l'objet
        continue
    fond[i] = 1
    if x > 0: file.append((x - 1, y))
    if x < w - 1: file.append((x + 1, y))
    if y > 0: file.append((x, y - 1))
    if y < h - 1: file.append((x, y + 1))

masque = Image.new("L", (w, h))
masque.putdata([0 if v else 255 for v in fond])
# Ombre douce et bord adouci : légère érosion puis flou pour éviter un liseré blanc
masque = masque.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1.2))

objet = im.convert("RGBA")
objet.putalpha(masque)
objet = objet.crop(objet.getbbox())
objet.thumbnail((taille, taille), Image.LANCZOS)
objet.save(sortie, optimize=True)
print(sortie, objet.size)

"""Retire le fond blanc des motifs de ornements/ (sauf fond.png) pour qu'ils se posent sur le site.

Usage : python preparer-ornements.py
Les originaux sont gardés dans ornements/originaux/.
"""
import shutil
from pathlib import Path

from PIL import Image

DOSSIER = Path(__file__).parent / "ornements"
ORIGINAUX = DOSSIER / "originaux"
LARGEUR_MAX = 1200


def blanc_vers_transparent(im: Image.Image) -> Image.Image:
    # « Couleur vers alpha » : le blanc devient transparent, les tons clairs semi-transparents,
    # sans halo blanc autour des fleurs.
    im = im.convert("RGBA")
    px = im.load()
    for y in range(im.height):
        for x in range(im.width):
            r, g, b, _ = px[x, y]
            a = max(255 - r, 255 - g, 255 - b)
            if a < 6:
                px[x, y] = (255, 255, 255, 0)
                continue
            f = 255 / a
            px[x, y] = tuple(max(0, min(255, round(255 - (255 - c) * f))) for c in (r, g, b)) + (a,)
    return im


def main() -> None:
    ORIGINAUX.mkdir(exist_ok=True)
    for chemin in sorted(DOSSIER.iterdir()):
        if chemin.suffix.lower() not in {".png", ".jpg", ".jpeg", ".webp"}:
            continue
        nom = chemin.stem
        original = ORIGINAUX / chemin.name
        if not original.exists():
            shutil.copy2(chemin, original)
        im = Image.open(original)
        im.thumbnail((LARGEUR_MAX, LARGEUR_MAX))
        if nom != "fond":
            im = blanc_vers_transparent(im)
            im = im.crop(im.getbbox() or (0, 0, im.width, im.height))
        sortie = DOSSIER / f"{nom}.png"
        im.save(sortie, optimize=True)
        if chemin != sortie:
            chemin.unlink()
        print(f"{sortie.name} : {im.size[0]}x{im.size[1]}")


if __name__ == "__main__":
    main()

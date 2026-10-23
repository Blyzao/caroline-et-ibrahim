# Caroline & Ibrahim — invitation de mariage

Site d'invitation au mariage de Caroline et Ibrahim, le **vendredi 1er janvier 2027** à Abidjan.

**En ligne : https://blyzao.github.io/caroline-et-ibrahim/**

Une seule page, sans framework ni étape de compilation : HTML, CSS et JavaScript.
Les confirmations de présence sont enregistrées dans une feuille Google Sheets
par un petit script Google Apps Script.

## Ce que voit l'invité

- **Ouverture** : un cadre fleuri en arche avec les prénoms, une explosion de confettis
  et la musique au premier clic.
- **Invitation personnalisée** : un lien `?invite=Famille-Kouassi` affiche « Cher·e Famille Kouassi »
  et préremplit son nom.
- **Le grand jour** : la date, un compte à rebours, un calendrier de janvier 2027
  et l'ajout à Google Agenda ou au calendrier du téléphone.
- **Programme** : une frise à icônes, avec un lien d'itinéraire pour chaque lieu.
- **Lieu de réception** : photo, adresse et carte.
- **Galerie** : un carrousel 3D circulaire, qui défile seul et s'agrandit au toucher.
- **Confirmation de présence** : nom, téléphone avec indicatif (Côte d'Ivoire par défaut),
  présence, lien avec les mariés et un mot facultatif.
- **Ambiance** : pétales qui tombent, apparitions au défilement, et défilement automatique
  qui s'arrête dès que l'invité touche l'écran puis reprend après 8 secondes d'inactivité.

Le site s'adapte aux téléphones jusqu'à 320 px de large et respecte le réglage
« réduire les animations » du système.

## Contenu du dépôt

| Chemin | Rôle |
| --- | --- |
| `index.html` | Le site entier : structure, styles et scripts |
| `img/` | Photos optimisées pour le web, et drapeaux du sélecteur d'indicatif (`img/drapeaux/`) |
| `ornements/` | Motifs floraux détourés : cadre, coin, séparateur, bouquet, fond |
| `musique/musique.mp3` | Musique lancée à l'ouverture |
| `script-google.gs` | Script Google Apps Script qui enregistre les réponses |
| `preparer-ornements.py` | Retire le fond blanc des motifs générés |
| `PROMPTS-ORNEMENTS.md` | Prompts pour générer les motifs floraux avec une IA |

Les photos et motifs originaux, non optimisés (`images/`, `ornements/originaux/`), restent en local
et ne sont pas versionnés.

## Personnaliser

Tout se règle en haut du script de `index.html`, dans l'objet `REGLAGES` :

| Réglage | Rôle |
| --- | --- |
| `dateMariage` | Date et heure de début, en UTC (Abidjan est à UTC+0) : sert au compte à rebours et au calendrier |
| `heureFixee` | `true` pour que l'ajout à l'agenda indique l'heure, `false` pour un événement sur la journée |
| `lieu` | Adresse utilisée pour l'ajout à l'agenda |
| `programme` | Les étapes de la journée : `heure`, `icone`, `titre`, et au choix `lieu`, `quartier`, `texte` |
| `urlScript` | Adresse du script Google qui enregistre les réponses |

Icônes disponibles pour le programme : `mairie`, `eglise`, `photo`, `reception`, `gateau`, `bal`.

Les prénoms, textes et photos se modifient directement dans le HTML.

## Relier le formulaire à Google Sheets

1. Créez une feuille Google Sheets vide (**sheets.new**).
2. Menu **Extensions → Apps Script**. Effacez le contenu, collez celui de `script-google.gs`, puis **enregistrez (Ctrl+S)**.
3. **Déployer → Nouveau déploiement** → type **Application Web** :
   - Exécuter en tant que : **Moi**
   - Qui a accès : **Tout le monde**
4. Autorisez l'accès. L'écran « Google n'a pas validé cette application » est normal pour un script personnel :
   **Paramètres avancés → Accéder à … (non sécurisé) → Autoriser**.
5. Copiez l'**URL de l'application Web**, qui finit par `/exec`, et collez-la dans `REGLAGES.urlScript`.

Les réponses arrivent dans l'onglet **Présences**, créé automatiquement : date, nom, téléphone avec indicatif,
présence, catégorie, message et lien d'invitation utilisé.
Pour compter par catégorie : **Insertion → Tableau croisé dynamique**, « Catégorie » en lignes.

**Mettre à jour le script sans changer d'adresse.** Après avoir collé le nouveau code et **enregistré** :
**Déployer → Gérer les déploiements → crayon (Modifier) → Version : « Nouvelle version » → Déployer**.
Sans « Nouvelle version », le déploiement reste sur l'ancien code.
Pour vérifier la version en ligne, ouvrez l'adresse du script suivie de `?reveil=1` : elle affiche la valeur
de la constante `VERSION` du script.

**Fiabilité.** Google endort le script quand personne ne l'utilise, et le réveiller peut prendre jusqu'à 30 secondes.
Le site le réveille dès que l'invité approche du formulaire. En cas de coupure réseau, il renvoie la réponse
une fois, et le script reconnaît l'identifiant de la réponse pour ne pas l'enregistrer en double.

Pour changer les catégories d'invités, modifiez la liste « Vous êtes » dans `index.html` **et** `CATEGORIES`
dans le script, avec les mêmes valeurs : le script refuse une catégorie qu'il ne connaît pas.

## Motifs floraux

Les motifs sont générés par IA avec les prompts de `PROMPTS-ORNEMENTS.md`, déposés dans `ornements/`
(`cadre.png`, `coin.png`, `separateur.png`, `bouquet.png`, `fond.png`), puis préparés avec :

    python preparer-ornements.py

Le script, qui demande la bibliothèque Pillow, retire le fond blanc et garde les originaux dans `ornements/originaux/`.
Tant qu'un motif manque, le site affiche un simple filet doré à sa place.

## Travailler en local

Le site doit être servi par un petit serveur, pour que le navigateur charge les images et la musique :

    python -m http.server 8765

puis ouvrez http://localhost:8765/.

## Mise en ligne

Le site est publié par **GitHub Pages** depuis la branche `main` : chaque `git push` le met à jour,
en une à quelques minutes. GitHub Pages garde la page en cache une dizaine de minutes : rechargez la page
si l'ancienne version s'affiche encore.

## Licence et crédits

Le **code** (`index.html`, `script-google.gs`, `preparer-ornements.py`) est publié sous **licence MIT** :
voir [LICENSE](LICENSE).

Ne sont **pas** couverts par cette licence :

- **Les photos** (`img/`, hors `img/drapeaux/`) et **les motifs floraux** (`ornements/`) : images créées
  pour ce mariage, tous droits réservés. Ne les réutilisez pas sans l'accord des mariés.
- **La musique** (`musique/musique.mp3`) : *A Thousand Years* de Christina Perri, œuvre protégée
  appartenant à ses ayants droit. Remplacez-la par une musique libre de droits si vous réutilisez ce site.
- **Les drapeaux** (`img/drapeaux/`) : fournis par [flagcdn.com](https://flagcdn.com), domaine public.
- **Les polices** Bodoni Moda, Cormorant Garamond, Pinyon Script et Jost : Google Fonts, sous licence SIL Open Font.

Site réalisé par [Blyzao](https://github.com/Blyzao).

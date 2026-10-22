# Invitation — Caroline & Ibrahim

Site d'une seule page : `index.html`. Les images web sont dans `img/` ; les originaux restent dans `images/`.

## 1. Relier la confirmation de présence (10 min, gratuit)

1. Créez une feuille Google Sheets vide, par exemple « Mariage C&I ».
2. Menu **Extensions → Apps Script**. Effacez le contenu, collez celui de `script-google.gs`, enregistrez.
3. **Déployer → Nouveau déploiement** → type **Application Web** :
   - Exécuter en tant que : **Moi**
   - Qui a accès : **Tout le monde**
4. Autorisez l'accès quand Google le demande, puis copiez l'**URL de l'application Web** (elle finit par `/exec`).
5. Dans `index.html`, collez-la dans `REGLAGES.urlScript`.

Les réponses arrivent dans l'onglet **Présences**, créé automatiquement : nom, oui ou non,
catégorie (famille, ami·e ou collègue de l'un ou l'autre), message et lien d'invitation.
Pour compter par catégorie : **Données → Tableau croisé dynamique**, lignes « Catégorie », valeurs « Présence ».

Pour changer les catégories, modifiez la liste « Vous êtes » dans `index.html` **et** `CATEGORIES`
dans le script, avec les mêmes valeurs : le script refuse une catégorie qu'il ne connaît pas.

Si vous modifiez le script plus tard : **Déployer → Gérer les déploiements → Modifier → Nouvelle version**, sinon l'ancienne version reste en ligne.

## 2. Motifs floraux

Générez-les avec les prompts de `PROMPTS-ORNEMENTS.md`, déposez-les dans `ornements/`
(`cadre.png`, `coin.png`, `separateur.png`, `bouquet.png`, `fond.png`), puis lancez :

    python preparer-ornements.py

Le script retire le fond blanc et garde les originaux dans `ornements/originaux/`.
Tant qu'un motif manque, le site affiche un simple filet doré à sa place.

## 3. Programme

Dans `index.html`, complétez `REGLAGES.programme` : une ligne par moment, par exemple
`{ heure: "15:00", titre: "Cérémonie religieuse", detail: "Chapelle du Sofitel" }`.

## 4. Musique

Le fichier `musique/musique.mp3` démarre quand l'invité clique sur « Ouvrir l'invitation » ; un bouton rond en bas à droite permet de le couper. Sans fichier, le bouton n'apparaît pas.

Gardez un fichier léger (moins de 5 Mo) : les invités l'ouvriront souvent en 4G.

## 5. Heure de la cérémonie

Le compte à rebours vise le 1er janvier 2027 à minuit. Quand l'heure est fixée, changez `REGLAGES.dateMariage` dans `index.html`, par exemple `"2027-01-01T15:00:00Z"` pour 15 h (Abidjan est à l'heure UTC), et passez `heureFixee` à `true` pour que l'ajout à l'agenda indique l'heure.

## 6. Liens personnalisés

Ajoutez `?invite=` suivi du nom à l'adresse du site :

    https://votre-site/?invite=Famille-Kouassi

L'écran d'ouverture affiche « Cher·e Famille Kouassi » et le nom est prérempli dans les formulaires. Le lien d'origine est noté dans l'onglet Présences.

## 7. Mettre en ligne gratuitement

**Netlify (le plus simple)** : allez sur app.netlify.com/drop et glissez le dossier entier (sans `images/`, inutile en ligne).

**GitHub Pages** : créez un dépôt public, envoyez-y le dossier, puis **Settings → Pages → Deploy from branch → main**.

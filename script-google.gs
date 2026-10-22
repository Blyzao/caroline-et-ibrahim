/** @OnlyCurrentDoc */
// L'annotation ci-dessus limite l'autorisation demandée par Google à cette seule feuille.

/**
 * Script Google Apps Script : reçoit les confirmations de présence et les range
 * dans la feuille Google Sheets à laquelle il est attaché.
 * Mise en place : voir LISEZ-MOI.md.
 */

const ONGLET_PRESENCES = "Présences";

// Lisible à l'adresse du script suivie de ?reveil=1 : permet de vérifier quelle version est déployée.
const VERSION = "3-anti-doublon";

// Mêmes valeurs que la liste « Vous êtes » du formulaire
const CATEGORIES = {
  "famille-caroline": "Famille de Caroline",
  "famille-ibrahim": "Famille d'Ibrahim",
  "ami-caroline": "Ami·e de Caroline",
  "ami-ibrahim": "Ami·e d'Ibrahim",
  "collegue": "Collègue",
  "autre": "Autre"
};

function doPost(e) {
  try {
    const d = JSON.parse(e.postData.contents);
    if (d.type !== "presence") return reponse({ ok: false, erreur: "type inconnu" });
    const nom = propre(d.nom, 80);
    const categorie = CATEGORIES[d.categorie];
    const telephone = numero(d.indicatif, d.telephone);
    if (!nom || !categorie || !telephone) return reponse({ ok: false, erreur: "champs manquants" });
    const presence = d.presence === "oui" ? "oui" : "non";

    // Le site renvoie la même réponse, avec le même identifiant, si le premier envoi n'a pas abouti
    // chez l'invité alors que Google l'avait peut-être déjà reçu : on ne l'enregistre qu'une fois.
    if (d.id) {
      const cache = CacheService.getScriptCache();
      const cle = "envoi-" + String(d.id).slice(0, 64);
      if (cache.get(cle)) return reponse({ ok: true });
      cache.put(cle, "1", 1800);
    }

    // Pas de verrou : appendRow ajoute la ligne d'un bloc, même si deux invités répondent en même temps.
    // L'ancien verrou faisait échouer un envoi quand le précédent était lent.
    onglet(ONGLET_PRESENCES, ["Date", "Nom", "Téléphone", "Présence", "Catégorie", "Message", "Lien d'invitation"])
      .appendRow([new Date(), nom, telephone, presence, categorie, propre(d.message, 500), propre(d.invite, 60)]);
    return reponse({ ok: true });
  } catch (err) {
    return reponse({ ok: false, erreur: "serveur" });
  }
}

// Appelé par le site quand l'invité approche du formulaire : réveille le script pour que l'envoi soit rapide.
function doGet() {
  return reponse({ ok: true, version: VERSION });
}

function onglet(nom, entetes) {
  const classeur = SpreadsheetApp.getActiveSpreadsheet();
  let f = classeur.getSheetByName(nom);
  if (!f) {
    f = classeur.insertSheet(nom);
    f.appendRow(entetes);
    f.setFrozenRows(1);
  }
  return f;
}

// « +225 0700000000 » : 10 chiffres pour la Côte d'Ivoire, de 6 à 14 ailleurs ; null si invalide.
// L'apostrophe initiale garde le numéro en texte dans la feuille (sinon le « + » lancerait une formule).
function numero(indicatif, tel) {
  const ind = String(indicatif || "");
  const chiffres = String(tel || "").replace(/\D/g, "");
  if (!/^\+\d{1,4}$/.test(ind)) return null;
  const valide = ind === "+225" ? chiffres.length === 10 : chiffres.length >= 6 && chiffres.length <= 14;
  return valide ? "'" + ind + " " + chiffres : null;
}

// Coupe à la bonne longueur et neutralise les formules (=, +, -, @) qu'un invité taperait
function propre(v, max) {
  const s = String(v || "").trim().slice(0, max);
  return /^[=+\-@]/.test(s) ? "'" + s : s;
}

function reponse(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj)).setMimeType(ContentService.MimeType.JSON);
}

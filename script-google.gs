/**
 * Script Google Apps Script : reçoit les confirmations de présence et les range
 * dans la feuille Google Sheets à laquelle il est attaché.
 * Mise en place : voir LISEZ-MOI.md.
 */

const ONGLET_PRESENCES = "Présences";

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
    if (!nom || !categorie) return reponse({ ok: false, erreur: "champs manquants" });
    const presence = d.presence === "oui" ? "oui" : "non";

    const verrou = LockService.getScriptLock();
    verrou.waitLock(10000);
    try {
      onglet(ONGLET_PRESENCES, ["Date", "Nom", "Présence", "Catégorie", "Message", "Lien d'invitation"])
        .appendRow([new Date(), nom, presence, categorie, propre(d.message, 500), propre(d.invite, 60)]);
    } finally {
      verrou.releaseLock();
    }
    return reponse({ ok: true });
  } catch (err) {
    return reponse({ ok: false, erreur: "requête invalide" });
  }
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

// Coupe à la bonne longueur et neutralise les formules (=, +, -, @) qu'un invité taperait
function propre(v, max) {
  const s = String(v || "").trim().slice(0, max);
  return /^[=+\-@]/.test(s) ? "'" + s : s;
}

function reponse(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj)).setMimeType(ContentService.MimeType.JSON);
}

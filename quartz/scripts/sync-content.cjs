const fs = require('fs');
const path = require('path');

const SOURCE = path.join(__dirname, '../../Pokemon PnP');
const TARGET = path.join(__dirname, '../content');

// Diese Ordner werden NICHT kopiert (nur für Spielleiter)
const EXCLUDE = [
  '07-Kampagne (Nur Spielleiter)',
  '08-Spielsitzungen (Nur Spielleiter)',
  '98-Templates',
  '99-Admin',
  '.obsidian'
];

function copyRecursive(src, dest) {
  const stats = fs.statSync(src);

  if (stats.isDirectory()) {
    const dirName = path.basename(src);
    if (EXCLUDE.includes(dirName)) {
      console.log(`⏭️  Überspringe: ${dirName}`);
      return;
    }

    if (!fs.existsSync(dest)) {
      fs.mkdirSync(dest, { recursive: true });
    }

    fs.readdirSync(src).forEach(child => {
      copyRecursive(path.join(src, child), path.join(dest, child));
    });
  } else {
    fs.copyFileSync(src, dest);
  }
}

// Content-Ordner leeren
if (fs.existsSync(TARGET)) {
  fs.rmSync(TARGET, { recursive: true });
}
fs.mkdirSync(TARGET, { recursive: true });

// Dateien kopieren
console.log('📁 Synchronisiere Spieler-Inhalte...');
copyRecursive(SOURCE, TARGET);
console.log('✅ Fertig!');

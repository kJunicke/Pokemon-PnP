# Wiki-Setup mit Quartz

Diese Anleitung beschreibt die Einrichtung eines Online-Wikis für Spieler mit Quartz + GitHub Pages.

**Ziel-URL:** `https://kjunicke.github.io/Pokemon-PnP`

**Rollback-Punkt:** Commit `21cd0e8` (vor Wiki-Setup)

---

## Übersicht

```
Pokemon/
├── quartz/                    # Quartz-Installation
│   ├── quartz.config.ts       # Hauptkonfiguration
│   ├── quartz.layout.ts       # Layout
│   ├── content/               # Öffentliche Dateien (wird beim Build gefüllt)
│   ├── scripts/
│   │   └── sync-content.cjs   # Kopiert Spieler-Inhalte (.cjs weil Quartz ES Modules nutzt)
│   └── package.json
├── Pokemon PnP/               # Obsidian-Vault (unverändert)
└── .github/
    └── workflows/
        └── deploy.yml         # Automatisches Deployment
```

---

## Schritt 1: Quartz klonen ✅

```bash
# Im Pokemon-Repo-Root
git clone https://github.com/jackyzha0/quartz.git quartz
cd quartz
rm -rf .git
npm install
```

**Was passiert:**
- Quartz wird als Unterordner geklont
- `.git` entfernt (kein Submodule, wird Teil unseres Repos)
- Dependencies installiert

---

## Schritt 2: sync-content.cjs erstellen ✅

**Datei:** `quartz/scripts/sync-content.cjs`

> **Wichtig:** Die Endung muss `.cjs` sein, da Quartz ES Modules verwendet und CommonJS-Syntax (`require`) sonst nicht funktioniert.

```javascript
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
```

**Was passiert:**
- Kopiert alle Dateien aus `Pokemon PnP/` nach `quartz/content/`
- Schließt SL-Ordner aus (07, 08, 98, 99, .obsidian)

---

## Schritt 3: quartz.config.ts anpassen ✅

**Datei:** `quartz/quartz.config.ts`

Folgende Werte ändern:

```typescript
const config: QuartzConfig = {
  configuration: {
    pageTitle: "Pokemon PnP",
    enableSPA: true,
    enablePopovers: true,
    analytics: null,
    locale: "de-DE",
    baseUrl: "kjunicke.github.io/Pokemon-PnP",
    ignorePatterns: ["private", "templates", ".obsidian"],
    defaultDateType: "modified",
    // ...
  },
  // ...
}
```

**Wichtige Einstellungen:**
- `pageTitle`: Titel der Website
- `locale`: Deutsches Datumsformat
- `baseUrl`: GitHub Pages URL (ohne https://)
- `ignorePatterns`: Zusätzliche Ausschlüsse

---

## Schritt 4: GitHub Actions Workflow erstellen ✅

**Datei:** `.github/workflows/deploy.yml`

```yaml
name: Deploy Quartz Wiki

on:
  push:
    branches:
      - master

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: 22

      - name: Install Dependencies
        run: |
          cd quartz
          npm ci

      - name: Sync Content
        run: node quartz/scripts/sync-content.cjs

      - name: Build Quartz
        run: |
          cd quartz
          npx quartz build

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: quartz/public

  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

**Was passiert:**
1. Code wird ausgecheckt
2. Node.js 22 wird installiert
3. npm-Dependencies werden installiert
4. `sync-content.js` kopiert Spieler-Inhalte
5. Quartz baut die Website
6. `public/` wird zu GitHub Pages deployt

---

## Schritt 5: .gitignore erweitern ✅

**Datei:** `.gitignore` (im Root)

Folgende Zeilen hinzufügen:

```
# Quartz
quartz/node_modules/
quartz/public/
quartz/.quartz-cache/
```

> **WICHTIG:** `quartz/content/` darf NICHT in der `.gitignore` stehen!
> Quartz nutzt git um Dateien zu finden - ignorierte Ordner werden beim Build nicht gefunden.

**Warum diese Einträge:**
- `node_modules/`: Dependencies (werden bei Build neu installiert)
- `public/`: Generierte Website (wird bei Build neu erstellt)
- `.quartz-cache/`: Build-Cache

---

## Schritt 6: GitHub Pages aktivieren ⏳

1. Gehe zu: https://github.com/kJunicke/Pokemon-PnP/settings/pages
2. Unter "Build and deployment":
   - Source: **GitHub Actions** auswählen
3. Speichern

---

## Schritt 7: Erster Deploy ✅

```bash
git add .
git commit -m "Add Quartz wiki setup"
git push
```

Nach 1-2 Minuten ist das Wiki live unter:
**https://kjunicke.github.io/Pokemon-PnP**

---

## Workflow danach

1. Bearbeite Inhalte in Obsidian wie gewohnt
2. `git add . && git commit -m "Update" && git push`
3. Wiki aktualisiert sich automatisch

---

## Troubleshooting

### Build schlägt fehl
- Prüfe GitHub Actions: https://github.com/kJunicke/Pokemon-PnP/actions
- Häufige Ursachen: Node-Version, fehlende Dateien

### Seite zeigt 404
- GitHub Pages Source muss auf "GitHub Actions" stehen
- Warte 1-2 Minuten nach dem Push

### Links funktionieren nicht
- Quartz nutzt `.html`-Endungen, keine Ordner
- Trailing Slashes vermeiden

### Lokales Testen
```bash
cd quartz
node scripts/sync-content.cjs
npx quartz build --serve
# Öffne http://localhost:8080
```

---

## Öffentliche Ordner

Diese Ordner sind für Spieler sichtbar:
- ✅ 01-Regeldex
- ✅ 02-Attackendex
- ✅ 03-Kommandodex
- ✅ 04-Talentdex
- ✅ 05-Pokémon
- ✅ 06-Welt
- ✅ 09-Spieler
- ✅ Spielerhandbuch.md
- ✅ Alle anderen .md Dateien im Root

Diese Ordner sind **privat** (nicht im Wiki):
- ❌ 07-Kampagne (Nur Spielleiter)
- ❌ 08-Spielsitzungen (Nur Spielleiter)
- ❌ 98-Templates
- ❌ 99-Admin
- ❌ .obsidian

# CLAUDE.md

Anweisungen für Claude Code bei der Arbeit in diesem Repository.

## Projektübersicht

Pokemon Pen-and-Paper RPG mit Homebrew-Regeln, dokumentiert in Obsidian Markdown.

### Aktuelles Ziel: Online-Wiki für Spieler

Quartz-basiertes Wiki das automatisch aus dem Obsidian-Vault gebaut wird.
- **Ziel-URL:** `https://kjunicke.github.io/Pokemon-PnP`
- **Anleitung:** [Wiki-Setup-Anleitung.md](Pokemon%20PnP/99-Admin/Wiki-Setup-Anleitung.md)
- **Status:** In Umsetzung

## Kernprinzipien

### 1. YAGNI (You Aren't Gonna Need It)
- Nur erstellen, was **jetzt** gebraucht wird
- Keine spekulativen Features oder Dokumentation
- Fokus auf aktuelle Spielbedürfnisse
- Inhalte erweitern, wenn tatsächlich benötigt
- Weniger ist mehr, Kurze klare Seiten sind langen und Ausführlichen zu bevorzugen.

### 2. Single Source of Truth
- **Regeldex** (`01-Regeldex/`) = kanonische Regeldefinitionen
- **Spielerhandbuch** = roter Faden, bindet Regeldex-Inhalte ein
- Änderungen an Regeln **nur im Regeldex**

### 3. Transclusion-First
- Spielerhandbuch bettet Regeldex-Inhalte ein (keine Duplikate!)
- Syntax: `![[Datei#Abschnitt]]`
- Regeldex-Dateien transclusion-freundlich strukturieren
- Keine Unnötigen Überschriften. Erstelle nur neue Überschriften, wenn diese für eine Transclusion irgendwo benötigt werden.

## Dokumentstruktur

### Spielerhandbuch als Leitdokument
[Spielerhandbuch.md](Pokemon%20PnP/Spielerhandbuch.md) ist der lineare Einstieg für neue Spieler:
- Alle Regelentwicklung orientiert sich am Handbuch-Aufbau
- Neue Regeln müssen ins Handbuch passen
- Regeldex-Struktur folgt Handbuch-Reihenfolge

### Dokumentenstruktur
```
Pokemon PnP/                    # Obsidian-Vault
├── 01-Regeldex/                # ✅ Wiki: Regelwerk
├── 02-Attackendex/             # ✅ Wiki: Attacken
├── 03-Kommandodex/             # ✅ Wiki: Kampfkommandos
├── 04-Talentdex/               # ✅ Wiki: Trainer-Talente
├── 05-Pokédex/                 # ✅ Wiki: Pokémon-Einträge
├── 06-Itemdex/                 # ✅ Wiki: Items & Ausrüstung
├── 07-Welt/                    # ✅ Wiki: Weltdetails
├── 10-Spieler/                 # ✅ Wiki: Spielercharaktere
├── 11-Aspekte/                 # ✅ Wiki: Aspekte
├── 96-Kampagne (Nur SL)/       # ❌ Privat: Kampagnenplanung
├── 97-Spielsitzungen (Nur SL)/ # ❌ Privat: Session Notes
├── 98-Templates/               # ❌ Privat: Vorlagen
├── 99-Admin/                   # ❌ Privat: TODOs, Anleitungen
└── Spielerhandbuch.md          # ✅ Wiki: Einstiegsdokument

quartz/                         # Wiki-Generator (Quartz v4)
├── quartz.config.ts            # Hauptkonfiguration
├── scripts/sync-content.cjs    # Kopiert öffentliche Inhalte
└── content/                    # Wird beim Build gefüllt

.github/workflows/deploy.yml    # Automatisches Wiki-Deployment
```

**Legende:** ✅ = öffentlich im Wiki, ❌ = nur lokal/privat

### Quartz-Hinweise
- **Quartz nutzt git zum Finden von Dateien** - Ordner in `.gitignore` werden beim Build ignoriert!
- `quartz/content/` darf NICHT in `.gitignore` stehen, sonst findet Quartz keine Dateien
- Script-Endung `.cjs` nötig (Quartz nutzt ES Modules)


## Design-Entscheidungen

### Vereinfachung für Pen & Paper
- **Level 1-20** (statt 1-100)
- **Stats 0-20 Bereich** (Kopfrechnung)
- **Ausdauer = Level** (stark vereinfacht)
- **A-Kraft ÷ 20** (herunterskaliert)

### Aspekt-System
- **Fate-inspirierte Aspekte** für Charaktereigenschaften und Situationen
- **Aspektpunkte-Mechanik** (Start: 3 pro Spielrunde)
- **Vorteil/Nachteil-System** (2W20, höheres/niedrigeres Ergebnis)

### Trainer-Mechaniken
- **Trainer-Level 1-20** mit EP-System
- **Fertigkeiten, Wissen, Talente** für Charakterentwicklung
- **Start-Pokémon**: Basis-Form mit Statuswerten < 400

### Pokémon-Formeln
| Mechanik | Formel |
|----------|--------|
| Statuswert | `Basis ÷ 100 × Level` |
| KP | `(Basis-KP ÷ 50 × Level) + 5` |
| EP benötigt | `(Summe BW ÷ 100) × Level` |
| Max. Ausdauer | `Level` |
| Zuneigungsbonus | `ZW ÷ 10` |

### Kampfsystem
- **Kampfrunden-basiert** mit Kommandos
- **6 Basis-Kommandos**: Zielen, Ausweichen, Abwehren, Blocken, Bewegen, Durchschnaufen
- **Reichweiten-System**: Relatives Zonen-System (Nah/Mittel/Fern/Außer Reichweite)
- **Ausdauer-Management** für Attacken

## Arbeitsanweisungen

### Schreibstil
- **Spieler-Dokumente** (Spielerhandbuch, Regeldex): Konsequent **"du"** verwenden

### Dateiverwaltung
- **NEVER** create files unless absolutely necessary
- **ALWAYS** prefer editing existing files to creating new ones
- **NEVER** proactively create documentation files (*.md) or READMEs
- **NEVER** die [Changelog.md](Pokemon%20PnP/Changelog.md) leeren oder löschen — sie ist eine fortlaufende Übersicht aller Regeländerungen

### Aufgabenverwaltung
- Offene Aufgaben in [TODO.md](Pokemon%20PnP/99-Admin/TODO.md)
- Wiki-Setup: [Wiki-Setup-Anleitung.md](Pokemon%20PnP/99-Admin/Wiki-Setup-Anleitung.md)
- Priorisierung: Kritisch → Hoch → Medium → Niedrig
- Fokus auf aktuell blockierende Probleme

### Grundregel
**Do what has been asked; nothing more, nothing less.**

### Pokemon erstellen
- Erstelle Pokemon immer wie in der Pokemon Vorlage im Template ordner vorgegeben
- Erstelle nicht von dir aus Attacken
- Wenn nicht anders angemerkt erstelle die Pokemon auf level 1
- Runde bei den Statuswerten immer
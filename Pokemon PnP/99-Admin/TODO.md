# 📋 Pokemon PnP - Development TODO

*Aufgabenliste für die Weiterentwicklung des Pokemon Pen & Paper Systems*

---

## 🚨 Kritisch (blockiert Kampf-Simulation)

### Kommandos-Inhalte fehlen komplett
- [x] **[[Zielen]]** - Datei existiert aber ist leer, nur Link zu Attacken
- [x] **[[Ausweichen]]** - Datei existiert aber ist leer
- [x] **[[Abwehren]]** - Datei existiert aber ist leer
- [x] **[[Blocken]]** - Datei existiert aber ist leer
- [x] **[[Bewegen]]** - ✅ Hat Inhalt
- [x] **[[Durchschnaufen]]** - ✅ Hat Inhalt

### Kern-Mechaniken nicht definiert
- [x] **[[Zone]]** - Reichweiten/Zonen-System fehlt komplett (was ist "nah" vs "mittel"?)
- [x] **[[Kategorie]]** - Physisch vs Spezial nicht dokumentiert (A vs V oder SA vs SV?)
- [x] **[[Typ]]** - Typ-Effektivität-Tabelle fehlt komplett
- [x] **[[Kampfunfähig]]** - Wann ist ein Pokémon kampfunfähig? (KP=0, Max AP=0, beides?)

### Unklare Mechaniken
- [x] **Anstrengung detailliert** - Wie genau funktioniert Überanstrengung? (Max AP sinkt um wie viel?)
- [x] **Reichweiten-Interpretation** - Bedeutet "Mittel" = bis zu Mittel oder genau Mittel?

### Balance-Probleme
- [x] **Level 1 Problem** - Alle Stats = +0, Kämpfe sind reines Würfelglück → Start-Level auf 3-5 erhöhen?


---

## 📖 Inhalts-Entwicklung (Hoch)

### Aus Session 2
- [ ] **[[Lichtel]] Attacken erstellen**
- [ ] **[[Piccochilla]] erstellen** + Attacken
- [ ] **[[Ruckzuckhieb]] erstellen**

### Attacken-System ausbauen
- [x] **Mehr Beispiel-Attacken** - Mehr als nur die 5 erstellten
- [x] **Typen-spezifische Attacken** - Feuer, Wasser, Elektro etc.
- [x] **Attacken mit komplexen Effekten** - Kombination von Schaden + Status
- [ ] **Attacken-Kategorien** - Templates für verschiedene Arten

---

## 🏗️ Struktur & Organisation (Medium)

### Templates erweitern
- [x] **Pokemon-Vorlage** - ✅ Template existiert in 05-Templates/
- [x] **Attacke-Vorlage** - ✅ Template existiert in 05-Templates/
- [ ] **Trainer-Vorlage** - Character Sheet Template
- [ ] **Kampagne-Vorlage** - Session-Dokumentation Template

### Beispiele & Referenzen
- [ ] **Mehr Pokemon-Beispiele** - Verschiedene Level und Typen (aktuell: Pikachu, Porenta, Ponita, Lapras)
- [ ] **Kampf-Beispiele** - Vollständige Kampf-Durchläufe dokumentiert
- [ ] **Trainer-Beispiele** - NPC und Spieler-Character Sheets

---

## 🔧 Technische Verbesserungen (Niedrig)  

### Metadaten standardisieren
- [ ] **YAML Frontmatter** - Einheitliche Properties für alle Dateien
- [ ] **Tags-System** - Konsistente Verschlagwortung
- [ ] **Type-System** - regel/attacke/pokemon/mechanik Kategorisierung

### Qualitätssicherung
- [ ] **Link-Audit** - Alle gebrochenen Links systematisch prüfen
- [ ] **Konsistenz-Check** - Einheitliche Terminologie und Formatierung  
- [ ] **Rechtschreibung** - Deutsche Rechtschreibung durchgehen

### Obsidian-Features nutzen  
- [ ] **Graph View** - Links optimieren für bessere Visualisierung
- [ ] **Search/Filter** - Properties für erweiterte Suchfunktionen
- [ ] **Plugins evaluieren** - Nützliche Community-Plugins finden

---

## 🎯 Langfristige Ziele (Zukunft)

### Content-Erweiterung
- [ ] **Pokemon-Datenbank** - Vollständige Pokedex mit PnP-Stats
- [ ] **Regions-Dokumentation** - Spielwelt-Beschreibungen
- [ ] **Abenteuer-Module** - Vorgefertigte Kampagnen
- [ ] **GM-Tools** - Spielleiter-Hilfsmittel

### Software-Integration
- [ ] **Digital Tools** - Apps/Websites für Berechnungen
- [ ] **Character Sheets** - Digitale Bögen
- [ ] **Online-Wiki** - Web-basiertes Nachschlagewerk

---

## 🏃‍♂️ Nächste Schritte - Prioritäten

### Top 5 zum spielbaren Kampfsystem
1. **Kommandos ausformulieren** - Zielen, Ausweichen, Abwehren, Blocken mit vollständigen Regeln
2. **Zone/Reichweite definieren** - Was ist nah/mittel, wie funktioniert Bewegung
3. **Kategorie dokumentieren** - Physisch vs Spezial mit A/V vs SA/SV Mechanik
4. **Typ-Effektivität-Tabelle** - Standard Pokémon Typen-Chart oder vereinfacht
5. **Balance-Fix** - Start-Level auf 3-5 erhöhen oder Formel anpassen

---

*📅 Letzte Aktualisierung: 2026-02-05*
*🔄 Status: Session 2 TODOs hinzugefügt*
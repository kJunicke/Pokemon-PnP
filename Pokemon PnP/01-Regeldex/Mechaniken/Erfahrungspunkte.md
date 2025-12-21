# Erfahrungspunkte

Jedes [[Pokémon]] hat ein **Level**, welches die generelle Stärke beschreibt.

**Level-Bereich:** 1-20

## EP sammeln

Wenn Pokémon Kämpfe und Herausforderungen bestreitet, erhält es **Erfahrungspunkte** (EP).

> 🚧 **TODO:** Wann und wie viel EP werden vergeben?

## Level-Up

Erreicht ein Pokémon genug EP, steigt es ein Level auf.

### Benötigte EP

```
Benötigte EP = (Summe BW ÷ 100) × aktuelles Level
```

(Ergebnis abrunden)

### Ablauf

Erreicht ein Pokémon ein neues Level:

1. **Entwicklung prüfen**
   - Entwickelt sich das Pokémon?
   - Falls ja: Aktualisiere [[Basiswerte]] auf Entwicklungsform
2. **Neue Attacken lernen**
   - Lernt es neue Attacke(n)?
3. **[[Statuswerte]] aktualisieren**
   - Berechne alle Statuswerte neu mit neuem Level

## Beispiel

**Pikachu Level 3 → Level 4**

**BW-Summe:** 320

**Benötigte EP:**
```
(320 ÷ 100) × 3 = 3,2 × 3 = 9,6 → 9 EP
```

Pikachu benötigt **9 EP** um auf Level 4 aufzusteigen.

**Nach Level-Up:**
- Keine Entwicklung
- Neue Attacke: Funkensprung
- Statuswerte neu berechnen mit Level 4
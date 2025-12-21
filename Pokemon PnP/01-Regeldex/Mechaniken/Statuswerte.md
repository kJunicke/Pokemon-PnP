# Statuswerte

Jedes [[Pokémon]] hat folgende Statuswerte (SW):

| Statuswert (SW)           | Erklärung                         |
| ------------------------- | --------------------------------- |
| Kraftpunkte (KP)          | Durchhaltevermögen                |
| Angriff (A)               | direkte Angriffe oft Nahkampf     |
| Spezial Angriff (SA)      | "Magische" Angriffe oft Fernkampf |
| Verteidigung (V)          | Abwehr von direkten Angriffen     |
| Spezial Verteidigung (SV) | Abwehr von speziellen Angriffen   |
| Geschwindigkeit (G)       | Ausweichen                        |
Statuswerte werden aus [[Basiswerte|Basiswerten]] und Level berechnet:
```
Statuswert = Basiswert ÷ 100 × Level
```
(Ergebnis abrunden)

Nur KP werden anders berechnet:
```
KP = (Basis-KP ÷ 50 × Level) + 5
```

Bei KP werden zum Ergebnis noch **+5** addiert und man teilt nur durch 50. So kriegt man also doppelt so viele KP pro Level wie punkte in den anderen SW

## Beispiel

**Pikachu Level 3** mit folgenden Basiswerten:

| Statuswert | Basiswert | Berechnung | Ergebnis |
|---|---|---|---|
| KP | 35 | (35 ÷ 50 × 3) + 5 = 2,1 + 5 | **7 KP** |
| Angriff | 55 | 55 ÷ 100 × 3 = 1,65 | **+1** |
| Spezial-Angriff | 50 | 50 ÷ 100 × 3 = 1,50 | **+1** |
| Verteidigung | 40 | 40 ÷ 100 × 3 = 1,20 | **+1** |
| Spezial-Verteidigung | 50 | 50 ÷ 100 × 3 = 1,50 | **+1** |
| Geschwindigkeit | 90 | 90 ÷ 100 × 3 = 2,70 | **+2** |
# Hauptgedanken
- Ein System mit 20 seitigem Würfel lässt uns Wahrscheinlichkeiten gut in 5% Schnipsel mappen.

# Stats

| Statuswert (SW)      | Abbreviation | Erklärung                                                                                                                  |
| -------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------- |
| Kraftpunkte          | KP           | Durchhaltevermögen                                                                                                         |
| Angriff              | A            | direkte Angriffe oft Nahkampf                                                                                              |
| Spezial Angriff      | SA           | "Magische" Angriffe oft Fernkampf                                                                                          |
| Verteidigung         | V            | Abwehr von direkten Angriffen                                                                                              |
| Spezial Verteidigung | SV           | Abwehr von speziellen Angriffen                                                                                            |
| Geschwindigkeit      | G            | Ausweichen <br>(entspricht dem Initiative Statuswert aus den Spielen. Wird zum Vorbeugen von Missverständnissen umbenannt) |
## In den Videospielen:
### HP
```
HP = (2 × Base + IV + 1/4 × EV) ÷ 100 × Level + 10
```

### Andere Stats
```
Stat = ((2 × Base + IV + 1/4 × EV) ÷ 100 × Level + 5) × Nature
```

## Simplifikation fürs PnP
### Ziel
Pokemon sollen Stats c.a. von 0-20 haben, damit die folgengenden Berrechnungen einfacher im Kopf am Tisch zu machen sind. Die Pokemon sollen außerdem Level von 1-20 haben anstelle von 1-100, damit Level ups weniger häufig passieren und mehr Wert sind für die Simplifikation
**Level-Anpassung**: 
- PnP verwendet PnP-Level 1-20 anstatt Videospiel-Level 1-100
- Umrechnung: `Videospiel-Level = PnP-Level × 5`
### Formel
```
Stat = Base ÷ 50 × Level
Stat = Base ÷ 50 × PnP-level x 5
Stat = Base ÷ 10 x PnP-level
```
### Problem
Stats und später Schaden werden so zu hoch
#### Lösung
Wir Teilen Stats und Schaden nochmal durch 10
### Endformel Stats
```
Stat = Base ÷ 100 x PnP-level (+ 5 bei HP)
```

So kann einfach berechnet werden wie viel die Stats höher werden bei jedem Level up
- Bei HP +5 am besten, damit Pokemon auf level 1 zumindest einen Treffer aushalten im schnitt. 
- Auf höheren Leveln wird der +5 Bonus dann eh weniger relevant und er steigert so die Survivabitlity im early game, wo sie am wichtigsten ist.
#### Beispiel
**Pokemon**: PnP-Level 5 Rattfratz mit Base Angriff von 56

**Berechnung**:
```
Angriff = Base ÷ 100 × PnP-Level
Angriff = 56 ÷ 100 × 5
Angriff = 2,8 → 3 (gerundet)
```

**Ergebnis**: Rattfratz hat einen Angriffs-Stat von 3

# Schaden

## In Videospielen
### Grundformel (Generation V+)
```
Schaden = ((((2 × Videospiel-Level ÷ 5 + 2) × Attacke-Power × (Angriff ÷ Verteidigung)) ÷ 50) + 2) × Modifikatoren
```
#### Modifikatoren:
- **STAB (Same Type Attack Bonus)**: 1.5x wenn Attacken-Typ = Pokemon-Typ
- **Typ-Effektivität**: 0.5x (nicht sehr effektiv), 1x (normal), 2x (sehr effektiv)
- **Kritischer Treffer**: 1.5x (Gen VI+) oder 2x (frühere Generationen)
- **Zufallsfaktor**: 85-100% (zufällig)
- **Weitere**: Wetter, Fähigkeiten, Items, etc.

## Simplifikation für PnP

### Anpassungen der Videospiel-Formel:

**Level-Anpassung**: 
- PnP verwendet PnP-Level 1-20 anstatt Videospiel-Level 1-100
- Umrechnung: `Videospiel-Level = PnP-Level × 5`

**Konstanten entfernen**: 
- Die +2 Konstanten werden weggelassen, da sie im PnP-Maßstab zu klein sind um relevant zu sein

**Attacke-Power vereinfachen**: 
- Original Attacke-Power wird durch 10 geteilt für einfachere Zahlen
- `A-Pow = Attacke-Power ÷ 10`
- `Attacke-Power × 10 = A-Pow`

### Rechenschritte der Vereinfachung:

**Schritt 1**: Angepasste Formel mit PnP-Werten
```
Schaden = (((2 × PnP-Level) × A-Pow × (Angriff ÷ Verteidigung)) ÷ 5) × Modifikatoren
```

**Schritt 2**: Faktor 2/5 vereinfachen
Der Faktor 2/5 (= 0,4) kann als 1/2 (= 0,5) approximiert werden für einfachere Kopfrechnung.
Diese Approximation rechnen wir direkt in A-Pow ein:

```
Neue A-Pow = (Attacke-Power ÷ 10) × 0,5 = Attacke-Power ÷ 20
```

**Schritt 3**: Finale vereinfachte Formel
```
Schaden = PnP-Level × A-Pow × (Angriff ÷ Verteidigung) × Modifikatoren
```
### Problem

Division und Multiplikation ist am Spieltisch unpraktisch. Addition wäre einfacher zu berechnen, würde aber die Schadensmechanik grundlegend verändern.

- Multiplikation kann man durch Mehrere Würfel simulieren.
	- Eigentlich müsste A-Pow dann die Größe der Würfel sein, da das am stabilsten ist und klar definiert werden kann. 
	- Angriff könnte dann die Anzahl der Würfel sein
	- Wenn man das allerdings macht wird es schwer die Verteidigung reinzurechnen es sei denn man macht nen riesen Würfelfest draus 

Ich glaub wir müssen das System nochmal von Grund auf durchdenken. Was soll denn drin sein:

## Ziele
- Es soll eine Mechanik zum Treffen, verfehlen und Ausweichen geben. 
	-  das weicht ja schonmal von Pokemon ab. 

#  Kampfsystem

## Treffen
- Wirf einen D20 + G + [[Genauigkeit]] Angreifer gegen 10 + G Verteidiger ~ 50% Hit chance
	- Wenn du deinem Pokemon die Anweisung zu [[Zielen]] dann darf es seinen A oder Sp.A anstelle des G zum treffen benutzen. 
	- [[Ausweichen]]-Anweisung gibt dem angreifendem Pokemon [[Nachteil]] auf seinen Angriff
	- [[Abwehren]]-Anweisung erlaubt dem Verteidiger 10 + D statt 10 + G zu benutzen um dem Angriff zu wiederstehen
## Schaden
- Bei einem Treffer fügt das Angreifende Pokemon dem Verteidigendem Pokemon Schaden zu.
- Der zugefügte Schaden wird wie folgt ermittelt.
	1. Jede [[Attacke-Vorlage]] hat ihre eigenen Schadenswürfel und Effekte.
	   z.B. [[Kratzer]] fügt 1d4 Schaden zu
	2. Je nach typ der Attacke (physisch oder speziell) werden zu dem Schaden der Attacke der A oder Sp.A des angreifenden Pokemon addiert
	3. gleichermaßen werden vom Angreifenden Pokemon D oder Sp.D vom Schaden der Attacke abgezogen.
		- Die [[Blocken]]-Anweisung verdoppelt die Menge an verhindertem Schaden.
## Aktionen
Pro Runde kann jeder Trainer seinem aktivem Pokemon [[Anweisungen]] geben. Davon darf eine Anweisung eine Attacke sein. Zu beginn wird jeder [[Trainer]] seinem Pokemon 2 Anweisungen geben können. 
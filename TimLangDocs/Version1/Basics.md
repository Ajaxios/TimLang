# Variables
#### Boolean
```python
produktiv? nein
istCool? ja
```

#### Integer and Float
```python
autos? 1
preis? 1999.99
```

#### String
```python
name? "Tims Bücherzimmer"
```

#### Random
Zur Generierung von zufälligen Zahlen kann man Würfel würfeln. Man kann einen
- D4
- D6
- D8
- D10
- D12
- D20
- oder D100
würfeln, über den Command `{Variable}? /roll{Anzahl der Würfel}d{Würfeltyp}`

Beispiele:
##### Random Number
```python
# Generiert eine Zahl zwischen 1 und 20
nummer? /roll 1d20
```

##### Random Numbers
```python
# Generiert ein Array aus 3 zufälligen Zahlen zwischen 1 und 100
nummern? /roll 3d100
```

Wenn man einen ungültigen Würfel eingibt, werden alle Würfelergebnisse auf 0 gesetzt
##### Wrong Dice
```python
seltsam? /roll 1d500
```
`-> 0`
##### Wrong Dices
```python
seltsamer? /roll 5d500
```
`-> [0, 0, 0, 0, 0]`
### String Concatenation
TimLang unterstützt die gleiche String Conatenation wie in Python. Bei Tupeln wird es generell eher empfohlen, mit einem Komma `,` statt dem Plus `+` zu arbeiten, falls Zahlen beteiligt sind. Anderseits kann man einfach die Methode `str(...)` verwenden. Hier ein Beispiel:
```python
# satz ist ein Tupel
name? "Tim"
buecher? 50
satz? "Ich heiße", name, "und habe", buecher, "Bücher gebunkert."
rede satz
```
`-> ('Ich heiße', 'Tim', 'und habe', 50, 'Bücher gebunkert.')`

```python
# satz ist ein String
name? "Tim"
buecher? 50
satz? "Ich heiße " + name + " und habe " + str(buecher) + " Bücher gebunkert."
rede satz
```
`-> Ich heiße Tim und habe 50 Bücher gebunkert.`

# Methods

#### `rede ...` -> Printing to the console
Entfernt mehrere Leerzeichen in Strings
```python
rede "Hello World!"
# equivalent to print("Hello World!") in Python
```
`-> Hello World!`
```python
rede "Hello        World!"
```
`-> Hello World!`


#### `Schere` -> Printing out "Schere"
Gibt "Schere" aus. Auf Groß- und Kleinschreibung wird bei dem Funktionsaufruf nicht geachtet
```python
Schere
```
`-> Schere`
```python
schere
```
`-> Schere`

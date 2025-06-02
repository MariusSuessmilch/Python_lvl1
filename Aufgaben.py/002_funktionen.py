# Funktionen - Code wiederverwenden + Code von Anderen Nutzen
# ========================================

# Was sind Funktionen?
# Funktionen sind wie Zaubersprüche, die wir immer wieder verwenden können!
# Stell dir vor, du müsstest jedes Mal den ganzen Code neu schreiben...

# ====================================================
# 1. VERGLEICH: MIT UND OHNE FUNKTIONEN
# ====================================================

# Ohne Funktionen (umständlich):
# Jedes Mal den gleichen Code schreiben
name1 = "Anna"
print(f"Hallo {name1}! Schön dich zu sehen!")
print(f"{name1}, du bist großartig!")
print()

name2 = "Ben"
print(f"Hallo {name2}! Schön dich zu sehen!")
print(f"{name2}, du bist großartig!")
print()

name3 = "Clara"
print(f"Hallo {name3}! Schön dich zu sehen!")
print(f"{name3}, du bist großartig!")
print()

# Mit Funktionen (einfach):
# Einmal schreiben, immer wieder verwenden!
def begruesse_person(name):
    print(f"Hallo {name}! Schön dich zu sehen!")
    print(f"{name}, du bist großartig!")
    print()

# Jetzt können wir die Funktion einfach aufrufen
begruesse_person("Anna")
begruesse_person("Ben") 
begruesse_person("Clara")

# ====================================================
# 2. FUNKTIONEN MIT RÜCKGABEWERTEN
# ====================================================

# Beispiel: Funktion die etwas berechnet und zurückgibt
def addiere_zahlen(zahl1, zahl2):
    ergebnis = zahl1 + zahl2
    return ergebnis

# Die Funktion verwenden
summe = addiere_zahlen(5, 3)
print(f"5 + 3 = {summe}")

summe2 = addiere_zahlen(10, 15)
print(f"10 + 15 = {summe2}")

summe3 = addiere_zahlen(100, 200)
print(f"100 + 200 = {summe3}")
print()

# ====================================================
# TODO: AUFGABE - Erstelle eine Funktion zur Berechnung des Notendurchschnitts
# Die Funktion soll:
# 1. Eine Liste von Noten als Parameter (Eingabe) bekommen
# 2. Den Durchschnitt berechnen (sum() und len() verwenden)
# 3. Das Ergebnis zurückgeben (return)
# 4. Teste deine Funktion mit verschiedenen Notenlisten
# ====================================================

# TODO: Teste deine Funktion mit diesen Notenlisten:
mathe_noten = [2, 1, 3, 2, 1]
deutsch_noten = [1, 2, 2, 1, 3, 2]
sport_noten = [1, 1, 2, 1]

# TODO: BONUS - Erweitere deine Funktion
# Lass sie auch eine Bewertung ausgeben:
# Durchschnitt <= 2.0: "Sehr gut!"
# Durchschnitt <= 3.0: "Gut!"
# Durchschnitt > 3.0: "Du schaffst das!"
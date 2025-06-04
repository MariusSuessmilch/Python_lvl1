# Listen - "Digitale Sammelboxen" 📦
# ===============================================

# Was sind Listen?
# Stell dir vor, du hast eine große Schachtel und kannst viele Sachen hineinlegen!
# Listen sind wie digitale Sammelboxen für unsere Daten.

# ====================================================
# Vergleich: Mit Liste vs ohne Liste
# ====================================================

# Ohne Listen (umständlich):
# Jeder Freund braucht eine eigene Variable
freund1 = "Anna"
freund2 = "Ben" 
freund3 = "Clara"
freund4 = "David"

# Mit Listen (einfach):
# Alle Freunde in einer Variable!
freunde = ["Anna", "Ben", "Clara", "David"]
print("Ohne Listen:", freund1, freund2, freund3, freund4)
print("Mit Listen:", freunde)
print()

# ====================================================
# Beispiel 1: Liste erstellen und Elemente ausgeben
# ====================================================

# Beispiel: Liste mit Lieblingsfilmen erstellen
filme = ["Harry Potter", "Die Eiskönigin", "Spider-Man", "Toy Story"]

print("Meine Lieblingsfilme:")
print(filme)
print()

# Schön ausgeben - jeden Film einzeln mit einer Schleife
for film in filme:
    print(f"🎬 {film}")
print()

# Beispiel: Bestimmte Filme finden 
# Listen sind wie nummerierte Boxen!
# Python zählt ab 0: [0] = Harry, [1] = Eiskönigin, [2] = Spider, [3] = Toy
# Diese zahlen geben die Position des Elementes in der Liste an und werden 'Index' genannt

print("Zugriff auf bestimmte Filme:")
print(f"Erster Film: {filme[0]}")
print(f"Zweiter Film: {filme[1]}")
print(f"Letzter Film: {filme[-1]}")  # -1 = letztes Element in der Liste

# TODO 1: Erstelle deine eigene Hobby-Liste mit 4 Hobbys
# Ändere diese Liste mit deinen eigenen Hobbys!


# TODO 2: Gib dein Lieblingshobby mit der Index-Notation aus


# ====================================================
# Beispiel 2 - Arbeite mit Zahlen-Listen
# Lerne len() und sum() kennen und berechne damit Statistiken
# ====================================================

# Beispiel: Notenliste erstellen
noten = [2, 1, 3, 2, 1, 3, 2]
print("Meine Noten:", noten)
print()

# len() zählt, wie viele Elemente in der Liste sind
anzahl_noten = len(noten)
print(f"Anzahl Noten: {anzahl_noten}")
print()

# Beispiel mit anderen Listen:
faecher = ["Mathe", "Deutsch", "Englisch", "Sport", "Bio", "Kunst", "Musik"]
print(f"Anzahl Fächer: {len(faecher)}")
print()

# sum() addiert alle Zahlen in der Liste
noten_summe = sum(noten)
print(f"Summe aller Noten: {noten_summe}")
print()

# TODO 3: Erstelle deine eigene Notenliste mit 5-7 Noten
# Ändere diese Liste mit deinen eigenen Noten
# Gib folgendes mit print aus: 1) Alle Elemente 2) Die Länger der Liste 3) Die Summe aller noten

# TODO 4: Berechne den Notendurchschnitt aus deiner Notenliste
# Tutorial: Python Listen - Einkaufsliste verwalten
# ===================================================

"""
🎯 WARUM BRAUCHEN WIR LISTEN?

Stell dir vor, du willst einkaufen gehen und musst dir merken:
- Äpfel, Brot, Milch, Käse, Bananen

Ohne Listen würdest du für jeden Artikel eine eigene Variable brauchen:
artikel1 = "Äpfel"
artikel2 = "Brot"  
artikel3 = "Milch"
artikel4 = "Käse"
artikel5 = "Bananen"

Was ist, wenn du 20 Artikel brauchst? Oder 100? 😱

Listen lösen dieses Problem:
✅ Viele Werte in einer Variable speichern
✅ Einfach neue Artikel hinzufügen/entfernen
✅ Durch alle Artikel durchgehen
✅ Artikel sortieren, suchen, zählen

Listen sind wie digitale Einkaufslisten - nur viel mächtiger!
"""

# ====================================================
# 😫 SCHRITT 1: DAS PROBLEM OHNE LISTEN
# ====================================================

print("=== Einkaufen OHNE Listen ===")
print()

# Ohne Listen: Jeder Artikel eine eigene Variable
artikel1 = "Äpfel"
artikel2 = "Brot"
artikel3 = "Milch"

print("Meine Einkäufe:")
print(f"1. {artikel1}")
print(f"2. {artikel2}")
print(f"3. {artikel3}")

print()
print("😩 Was ist, wenn ich 20 Artikel brauche?")
print("😩 Wie füge ich einen neuen Artikel hinzu?")
print("😩 Wie zähle ich alle Artikel?")
print()
print("💡 Listen machen alles einfacher!")
print()

# ====================================================
# 🚀 SCHRITT 2: LISTEN ERSTELLEN UND VERWENDEN
# ====================================================

print("=== Meine erste Liste ===")
print()

# Eine Liste erstellen - alle Artikel in einer Variable!
einkaufsliste = ["Äpfel", "Brot", "Milch", "Käse", "Bananen"]

print("Meine Einkaufsliste:")
print(einkaufsliste)
print()

# Einzelne Artikel abrufen (Index startet bei 0!)
print("Der erste Artikel:", einkaufsliste[0])
print("Der zweite Artikel:", einkaufsliste[1])
print("Der letzte Artikel:", einkaufsliste[-1])  # -1 = letzter Index
print()

# Wie viele Artikel habe ich?
anzahl_artikel = len(einkaufsliste)
print(f"Ich brauche {anzahl_artikel} Artikel")
print()

# ====================================================
# ➕ SCHRITT 3: ARTIKEL HINZUFÜGEN UND ENTFERNEN
# ====================================================

print("=== Listen verändern ===")
print()

# Neuen Artikel hinzufügen
print("Vor dem Hinzufügen:", einkaufsliste)
einkaufsliste.append("Schokolade")  # Am Ende hinzufügen
print("Nach dem Hinzufügen:", einkaufsliste)
print()

# Artikel an bestimmter Position einfügen
einkaufsliste.insert(1, "Butter")  # An Position 1 einfügen
print("Nach dem Einfügen von Butter:", einkaufsliste)
print()

# Artikel entfernen
einkaufsliste.remove("Milch")  # Bestimmten Artikel entfernen
print("Nach dem Entfernen von Milch:", einkaufsliste)
print()

# Letzten Artikel entfernen
letzter_artikel = einkaufsliste.pop()  # Entfernt und gibt zurück
print(f"Ich habe '{letzter_artikel}' von der Liste entfernt")
print("Liste jetzt:", einkaufsliste)
print()

# ====================================================
# 🔍 SCHRITT 4: DURCH LISTEN DURCHGEHEN
# ====================================================

print("=== Alle Artikel durchgehen ===")
print()

# Alle Artikel ausgeben (schöner als print(liste))
print("📝 Meine komplette Einkaufsliste:")
for i, artikel in enumerate(einkaufsliste, 1):  # enumerate für Nummerierung
    print(f"{i}. {artikel}")
print()

# Artikel suchen
gesuchter_artikel = "Brot"
if gesuchter_artikel in einkaufsliste:
    print(f"✅ '{gesuchter_artikel}' steht auf der Liste!")
else:
    print(f"❌ '{gesuchter_artikel}' fehlt auf der Liste!")
print()

# Artikel zählen, die mit 'B' anfangen
b_artikel = []
for artikel in einkaufsliste:
    if artikel.startswith('B'):
        b_artikel.append(artikel)

print(f"Artikel mit 'B': {b_artikel}")
print()

# ====================================================
# 🎯 SCHRITT 5: LISTEN SORTIEREN UND ORGANISIEREN
# ====================================================

print("=== Listen organisieren ===")
print()

# Liste sortieren
unsortierte_liste = ["Zucchini", "Äpfel", "Brot", "Milch"]
print("Unsortiert:", unsortierte_liste)

sortierte_liste = sorted(unsortierte_liste)  # Neue sortierte Liste
print("Sortiert (neue Liste):", sortierte_liste)
print("Original unverändert:", unsortierte_liste)

# Original-Liste sortieren
unsortierte_liste.sort()  # Verändert die Original-Liste
print("Original jetzt sortiert:", unsortierte_liste)
print()

# Liste umkehren
zahlen = [1, 2, 3, 4, 5]
print("Zahlen:", zahlen)
zahlen.reverse()
print("Umgekehrt:", zahlen)
print()

# ====================================================
# 🛒 SCHRITT 6: PRAKTISCHES BEISPIEL - SMARTE EINKAUFSLISTE
# ====================================================

def zeige_einkaufsliste(liste, titel="Einkaufsliste"):
    """Zeigt eine schön formatierte Einkaufsliste an."""
    print(f"\n📋 {titel}")
    print("=" * (len(titel) + 4))
    if len(liste) == 0:
        print("Die Liste ist leer!")
    else:
        for i, artikel in enumerate(liste, 1):
            print(f"{i:2}. {artikel}")
    print(f"\nGesamt: {len(liste)} Artikel")

def artikel_hinzufuegen(liste, artikel):
    """Fügt einen Artikel hinzu, wenn er noch nicht da ist."""
    if artikel not in liste:
        liste.append(artikel)
        print(f"✅ '{artikel}' zur Liste hinzugefügt!")
    else:
        print(f"⚠️  '{artikel}' ist bereits auf der Liste!")

# Demonstration der smarten Einkaufsliste
print("=== Smarte Einkaufsliste Demo ===")

meine_liste = []

# Artikel hinzufügen
artikel_hinzufuegen(meine_liste, "Äpfel")
artikel_hinzufuegen(meine_liste, "Brot") 
artikel_hinzufuegen(meine_liste, "Äpfel")  # Schon da!

zeige_einkaufsliste(meine_liste, "Mein Einkauf")

# ====================================================
# 📝 AUFGABEN FÜR DICH
# ====================================================

print("\n" + "="*50)
print("🎯 DEINE AUFGABEN")
print("="*50)

print("\n🎯 AUFGABE 1 (mit Hilfe):")
print("Erstelle eine Funktion 'finde_lange_artikel', die alle Artikel mit mehr als 5 Buchstaben findet")
print()

def finde_lange_artikel(artikel_liste):
    """
    Findet alle Artikel mit mehr als 5 Buchstaben.
    
    TIPP: Verwende len() um die Länge eines Strings zu messen
    TIPP: Erstelle eine neue leere Liste für die Ergebnisse
    TIPP: Gehe durch alle Artikel mit einer for-Schleife
    
    Parameter:
    artikel_liste (list): Liste von Artikel-Namen
    
    Rückgabe:
    list: Liste der Artikel mit mehr als 5 Buchstaben
    """
    # TODO: Schreibe hier deinen Code
    # lange_artikel = []
    # for artikel in artikel_liste:
    #     if len(artikel) > 5:
    #         lange_artikel.append(artikel)
    # return lange_artikel
    pass

# Test deine Funktion:
test_artikel = ["Äpfel", "Brot", "Schokolade", "Milch", "Bananen", "Käse"]
# print("Lange Artikel:", finde_lange_artikel(test_artikel))

print("\n🎯 AUFGABE 2 (ohne Hilfe):")
print("Schreibe eine Funktion 'einkauf_verwalten', die folgendes kann:")
print("- Artikel hinzufügen (ohne Duplikate)")
print("- Artikel entfernen")
print("- Liste anzeigen")
print("- Nach Artikeln suchen")
print()

def einkauf_verwalten():
    """
    Ein einfaches Einkaufslisten-Verwaltungssystem.
    
    Die Funktion soll eine Endlos-Schleife haben mit einem Menü:
    1. Artikel hinzufügen
    2. Artikel entfernen  
    3. Liste anzeigen
    4. Artikel suchen
    5. Beenden
    
    Rückgabe:
    None (interaktive Funktion)
    """
    # TODO: Schreibe hier dein komplettes Programm!
    # TIPP: Verwende eine while-Schleife und input() für Benutzereingaben
    # TIPP: Erstelle eine Liste am Anfang der Funktion
    pass

# Test deine Funktion:
# einkauf_verwalten()  # Entkommentieren zum Testen

print("\n🎯 AUFGABE 3 (Listen vergleichen):")
print("Erstelle eine Funktion, die zwei Listen vergleicht und gemeinsame Artikel findet")

def gemeinsame_artikel(liste1, liste2):
    """
    Findet Artikel, die in beiden Listen vorkommen.
    
    Parameter:
    liste1 (list): Erste Liste
    liste2 (list): Zweite Liste
    
    Rückgabe:
    list: Liste der gemeinsamen Artikel
    """
    # TODO: Schreibe hier deinen Code
    pass

# Test:
# liste_a = ["Äpfel", "Brot", "Milch", "Käse"]
# liste_b = ["Brot", "Bananen", "Milch", "Butter"]
# print("Gemeinsame Artikel:", gemeinsame_artikel(liste_a, liste_b))

print("\n🎯 BONUS-AUFGABE:")
print("Erstelle ein Programm, das eine Einkaufsliste nach Alphabet sortiert und nummeriert ausgibt!")

def sortierte_einkaufsliste(artikel_liste):
    """
    Sortiert eine Einkaufsliste und gibt sie schön formatiert aus.
    
    Parameter:
    artikel_liste (list): Unsortierte Liste von Artikeln
    
    Rückgabe:
    None (gibt direkt aus)
    """
    # TODO: Bonus-Aufgabe für die Schnellen!
    # TIPP: Verwende sorted() oder .sort()
    # TIPP: Verwende enumerate() für die Nummerierung
    pass

# Test:
# test_liste = ["Zucchini", "Äpfel", "Milch", "Brot", "Bananen"]
# sortierte_einkaufsliste(test_liste)

print("\n💫 Viel Erfolg beim Programmieren!")
print("💡 Listen sind überall - in Apps, Spielen, Websites!")
print("🤔 Nutze den Cascade Chat, wenn du Hilfe brauchst!")
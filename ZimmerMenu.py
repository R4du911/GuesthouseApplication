from Zimmer import Zimmer
from UI import *


def datei_lesen_zimmer(ZimmerListe):
    """
    :param ZimmerListe: Liste von Zimmern die am Anfang leer ist

    Die Methode geht durch die Datei 'zimmerliste' und speichert alle Zimmer in der ZimmerListe
    """
    g = open("zimmerliste", 'r')
    line = g.readline()
    while line != '':
        p = line.split(',')
        zimmer = Zimmer(p[0], p[1], p[2], p[3], p[4])
        ZimmerListe.append(zimmer)
        line = g.readline()
    g.close()


def add_zimmer(ZimmerListe):
    """
    :param ZimmerListe: Liste von Zimmern aus der Datei 'zimmerliste'

    Die Methode liest von der Tastatur einen neuen Nummer, Anzahl von Gasten, Preis, Farbe und ob das Zimmer ein
    Meerblick hat oder nicht, und speichert sie in den Variablen 'nr', 'anzahlG', 'preis', 'farbe' bzw 'meerblick'.
    Das neue Zimmer wird danach in der Zimmerliste hinzugefugt.
    """
    nr, anzahlG, preis, farbe, meerblick = add_zimmer_input()
    ZimmerListe.append(Zimmer(nr,anzahlG,preis,farbe,meerblick))


def change_preis(ZimmerListe,nr,preis):
    """
    :param ZimmerListe: Liste von Zimmern aus der Datei 'zimmerliste'
    :param nr: Von der Tastatur eingetippter Nummer umd das Zimmer zu suchen
    :param preis: Von der Tastatur eingetippter neuer Preis um den alten Preis zu aktualisieren

    Die Methode geht durch die Zimmerliste und sucht das eingetippte Zimmer. Falls man es findet, verandert man den Preis
    und die Variable 'found'=1. Andernfalls, bleibt 'found'=0. Falls man das eingetippte Zimmer nicht findet, schreibt
    man auf dem Bildschirm, dass das Zimmer nicht gefunden wurde.
    """
    found = 0
    for obj in ZimmerListe:
        if int(obj.nummer) == int(nr):
            obj.preis = preis
            found = 1
    if found == 0:
        print("Zimmer nicht gefunden! Bitte typen Sie nochmals")


def del_zimmer(ZimmerListe,nr):
    """
    :param ZimmerListe: Liste von Zimmern aus der Datei 'zimmerliste'
    :param nr: Von der Tastatur eingetippter Nummer umd das Zimmer zu suchen

    Die Methode geht durch die Zimmerliste und sucht das eingetippte Zimmer. Falls man es findet, loscht man es von
    der ZimmerListe und die Variable 'found' wird den Wert 1 haben. Andernfalls, bleibt 'found'=0. Falls
    man das eingetippte Zimmer nicht findet, schreibt man auf dem Bildschirm, dass das Zimmer nicht gefunden wurde.
    """
    found = 0
    for obj in ZimmerListe:
        if int(obj.nummer) == int(nr):
            ZimmerListe.remove(obj)
            found = 1
    if found == 0:
        print("Zimmer nicht gefunden! Bitte typen Sie nochmals")


def to_string_zimmer(ZimmerListe):
    """
    :param ZimmerListe: Liste von Zimmern aus der Datei 'zimmerliste'

    Die Elemente der Zimmerliste werden formatiert und auf dem Bildschirm geschrieben.
    """
    for obj in ZimmerListe:
        print(f'Nummer:{obj.nummer}, Anzahl Gaste:{obj.anzahlG}, Preis:{obj.preis}, Farbe:{obj.farbe}, Meerblick:{obj.meerblick}')


def ZimmerMenu():
    print("""
    ==== ZimmerMenu ====
    1: Fuge ein Zimmer hin
    2: Aktualisierung des Preises eines Zimmers
    3: Loschung eines Zimmers
    4: Anzeige die Liste von Zimmern
    5: return to main menu
    """)
    ZimmerListe = []
    datei_lesen_zimmer(ZimmerListe)
    opt = int(input("opt="))
    if opt == 1:
        add_zimmer(ZimmerListe)
        write_in_zimmer_datei(ZimmerListe)
        ZimmerMenu()
    if opt == 2:
        nr, preis = change_preis_input()
        change_preis(ZimmerListe,nr,preis)
        write_in_zimmer_datei(ZimmerListe)
        ZimmerMenu()
    if opt == 3:
        nr = del_zimmer_input()
        del_zimmer(ZimmerListe,nr)
        write_in_zimmer_datei(ZimmerListe)
        ZimmerMenu()
    if opt == 4:
        to_string_zimmer(ZimmerListe)
        ZimmerMenu()



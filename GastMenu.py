from Gaste import Gaste
from UI import *


def datei_lesen_guest(GastListe):
    """
    :param GastListe: Liste von Gasten aus der Datei 'gastliste'

    Die Methode geht durch die Datei 'gastliste' und speichert alle Gaste in der GastListe
    """
    f = open("gastliste", 'r')
    line = f.readline()
    while line != '':
        p = line.split(',')
        gast = Gaste(p[0], p[1])
        GastListe.append(gast)
        line = f.readline()
    f.close()


def add_guest(GastListe):
    """
    :param GastListe: Liste von Gasten aus der Datei 'gastliste'

    Die Methode liest einen neuen Vorname und Nachname von der Tastatur und speichert sie in den
    Variablen 'firstname' bzw 'lastname'. Der neue Gast wird danach in der Gastliste hinzugefugt.
    """
    firstname, lastname = add_guest_input()
    GastListe.append(Gaste(firstname,lastname))


def change_lastname(GastListe,lastname,firstname,Neulastname):
    """
    :param GastListe: List von Gasten aus der Datei 'gastliste'
    :param lastname: Von der Tastatur eingetippter Nachname um die gewunschte Person zu suchen
    :param firstname: Von der Tastatur eingetippter Vorname um die gewunschte Person zu suchen
    :param Neulastname: Von der Tastatur eingetippter Nachname, der an Stelle des alten Nachnamens geschrieben wird

    Die Methode geht durch die Gastliste und sucht den eingetippten Gast. Falls man ihn findet, verandert man den Nachnamen
    und die Variable 'found'=1. Andernfalls, bleibt 'found'=0. Falls man den eingetippten Gast nicht findet, schreibt
    man auf dem Bildschirm, dass der Gast nicht gefunden wurde.
    """
    found = 0
    for obj in GastListe:
        if obj.nachname == lastname and obj.vorname == firstname:
            obj.nachname = Neulastname
            found = 1
    if found == 0:
        print("Person nicht gefunden! Bitte typen Sie nochmals")


def del_guest(GastListe,lastname,firstname):
    """
    :param GastListe: List von Gasten aus der Datei 'gastliste'
    :param lastname: Von der Tastatur eingetippter Nachname um die gewunschte Person zu suchen
    :param firstname:  Von der Tastatur eingetippter Vorname um die gewunschte Person zu suchen

    Die Methode geht durch die Gastliste und sucht den eingetippten Gast. Falls man ihn findet, loscht man ihn von
    der GastListe und die Variable 'found' wird den Wert 1 haben. Andernfalls, bleibt 'found'=0. Falls
    man den eingetippten Gast nicht findet, schreibt man auf dem Bildschirm, dass der Gast nicht gefunden wurde.
    """
    found = 0
    for obj in GastListe:
        if obj.nachname == lastname and obj.vorname == firstname:
            GastListe.remove(obj)
            found = 1
    if found == 0:
        print("Person nicht gefunden! Bitte typen Sie nochmals")


def to_string_guest(GastListe):
    """
    :param GastListe: List von Gasten aus der Datei 'gastliste'

    Die Elemente der Gastliste werden formatiert und auf dem Bildschirm geschrieben.
    """
    for obj in GastListe:
        print(f'Vorname: {obj.vorname}, Nachname: {obj.nachname}')


def GastMenu():
    print("""
     ==== GastMenu ====
    1: Fuge ein neuer Gast hin
    2: Aktualisierung des Nachnamens eines Gastes
    3: Loschung eines Gastes
    4: Anzeige die Liste von Gasten
    5: return to main menu
    """)
    GastListe = []
    datei_lesen_guest(GastListe)
    opt = int(input("opt="))
    if opt == 1:
        add_guest(GastListe)
        write_in_guest_datei(GastListe)
        GastMenu()
    if opt == 2:
        firstname,lastname,Neulastname = change_nachname_input()
        change_lastname(GastListe,lastname,firstname,Neulastname)
        write_in_guest_datei(GastListe)
        GastMenu()
    if opt == 3:
        firstname,lastname = del_guest_input()
        del_guest(GastListe,lastname,firstname)
        write_in_guest_datei(GastListe)
        GastMenu()
    if opt == 4:
        to_string_guest(GastListe)
        GastMenu()
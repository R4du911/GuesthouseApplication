from UI import *
from datetime import date
from Reservirung import Reservierung
from ZimmerMenu import *
from GastMenu import *
from Time import *


def datei_lesen_reserv(ReservListe):
    """
        :param ReservListe: Liste von Reservierungen aus der Datei 'Reservliste'

        Die Methode geht durch die Datei 'Reservliste' und speichert alle Reservierungen in der ReservierungenListe
        """
    h = open('Reservliste', 'r')
    line = h.readline()
    while line != '':
        p = line.split(',')
        reserv = Reservierung(p[0], p[1], p[2], p[3], p[4])
        ReservListe.append(reserv)
        line = h.readline()
    h.close()

def test_if_reserv_good(ReservListe,datum,nr):
    """
    :param ReservListe: Liste von Reservierungen aus der Datei 'Reservliste'
    :param datum: Ein Datum geschrieben im Format ZZ/MM/YYYY
    :param nr: Nummer des Zimmers

    Die Methode geht durch alle Reservierungen und selektiert die Reservierungen, deren Zimmernummer mit dem Parameter 'nr' gleich sind.
    Man testet dann, ob das Parameter 'datum' sich zwischen dem Anfang und dem Ende einer Reservierung befindet. Falls man eine
    solche Reservierung findet, returniert die Methode den Wert 0. Andernfalls, returniert die Methode den Wert 1.
    """
    for obj in ReservListe:
        if int(obj.zimmer) == nr:
            if compare_two_dates(datum,obj.anfang) == 0 and compare_two_dates(datum,obj.ende) == 1:
                return 0
    return 1

def do_reserv(ReservListe, ZimmerListe, GastListe, firstname, lastname):
    """
    :param ReservListe: Liste von Reservierungen aus der Datei 'Reservliste'
    :param ZimmerListe: Liste von Zimmern aus der Datei 'zimmerliste'
    :param GastListe: Liste von Gaste aus der Datei 'dateiliste'
    :param firstname: Von der Tastatur eingetippter Vorname
    :param lastname: Von der Tastatur eingetippter Nachname

    Die Methode macht eine Reservierung, indem sie noch nach den Zimmernummer, der Anzahl der Gaste, dem Anfangsdatum und dem
    Enddatum der Reservierung. Die Methode testet dann auch, ob die eingetippte Daten richtig sind und, ob das gewahlte Zimmer
    in der eingetippten Periode frei ist. Die neue Reservierung wird danach in der Reservierungliste hinzugefugt.
    """
    found = 0
    for i in range(len(GastListe)):
        if GastListe[i].nachname == lastname and GastListe[i].vorname == firstname:
            found = 1
            index = i
    if found == 0:
        print("Person nicht gefunden! Bitte typen Sie nochmals")
    else:
        found = 0
        print('\n')
        to_string_zimmer(ZimmerListe)
        nr = int(input("Nummer:"))
        for obj in ZimmerListe:
            if int(obj.nummer) == int(nr):
                found = 1
        if found == 0:
            print("Zimmer nicht gefunden! Bitte typen Sie nochmals")
        else:
            nrGaste = int(input("Anzahl Gaste:"))
            if int(nrGaste) > int(ZimmerListe[nr-1].anzahlG):
                print("Zu viele Gaste. Bitte wahlen Sie sich ein anderes Zimmer")
            else:
                anfang = input("Anfang(Format ZZ/MM/YYYY):")
                ende = input("Ende(Format ZZ/MM/YYYY):")
                if compare_two_dates(anfang,ende) == 0:
                    print("Falscher input! Bitte typen Sie nochmal")
                else:
                    if test_if_reserv_good(ReservListe,anfang,nr) == 0 or test_if_reserv_good(ReservListe,ende,nr) == 0:
                        print("Zimmer nicht frei! Bitte typen Sie neue Daten")
                    else:
                        ReservListe.append(Reservierung(index, nr, nrGaste, anfang, ende))

def aktuelle_Res(ReservListe):
    """
    :param ReservListe: Liste von Reservierungen aus der Datei 'Reservliste'
    :param GastListe: Liste von Gaste aus der Datei 'dateiliste'

    Die Methode geht durch alle Reservierungen aus der Reservierungenliste und testet, ob der heutige Tag kleiner,gleich oder
    grosser als das Enddatum der Reservierung(man bestimmt also, ob die Reservierungen aktuell sind). Falls das Enddatum grosser
    ist, loscht man die Reservierung aus der Reservierungliste
    """
    heute = date.today()
    for obj in ReservListe:
        if compare_date_with_heute(heute, obj.ende) == 0:
            ReservListe.remove(obj)

def Zimmer_filter(ZimmerFilter,ZimmerListe, seaview, price):
    """
    :param ZimmerFilter: Liste von Zimmern, die die gefilterte Zimmer speichern wird
    :param ZimmerListe: Liste von Zimmern aus der Datei 'zimmerliste'
    :param seaview: Von der Tastatur eingetippter Meerblickwunsch
    :param price: Von der Tastatur eingetippter Preislimit

    Die Methode geht durch die Zimmerliste und sucht Zimmer, die die eingetippte Kriterien erfullen.
    Wenn man solche Zimmer findet, schreibt man diese in der ZimmerFilter Liste.
    """
    for obj in ZimmerListe:
        if obj.meerblick == seaview and int(obj.preis) < int(price):
            ZimmerFilter.append(obj)
    return ZimmerFilter

def Zimmer_frei(ReservListe,ZimmerListe):
    """
    :param ReservListe: Liste von Reservierungen aus der Datei 'Reservliste'
    :param ZimmerListe: Liste von Zimmern aus der Datei 'zimmerliste'

    Die Methode geht durch alle Zimmer aus der Zimmerliste und testet, indem sie auch durch alle Reservierungen geht, ob
    das heutige Datum sich zw dem Anfang und dem Ende einer Reservierung befindet. Falls man eine solche Reservierung findet,
    wird die Variable 'frei' den Wert 0 haben. Andernfalls, bleibt die Variable 'found' mit dem Wert 1. Am Ende testet man, ob die
    Variable 'found'=0 (also ob das Zimmer nicht frei ist) und loscht das Zimmer aus der ZimmerListe.
    """
    heute = date.today()
    for i in range(len(ZimmerListe)):
        frei = 1
        for obj in ReservListe:
            if int(obj.zimmer) == i+1:
                if compare_date_with_heute(heute,obj.anfang) == 0 and compare_date_with_heute(heute,obj.ende) == 1:
                    frei = 0
        if frei == 0:
           ZimmerListe.remove(ZimmerListe[i])



def MenuGemeinsam():
    print("""
    ==== Gemeinsam Menu ====
    1: Mach eine Reservierung
    2: Anzeige die Liste von Gasten, die aktuelle Reservierungen haben
    3: Anzeige alle Zimmer gefiltert mit Preis und Meerblick Kriterien
    4: Anzeige alle Zimmer, die heute frei sind
    5: return to main menu
    """)
    opt = int(input('opt='))

    GastListe = []
    datei_lesen_guest(GastListe)

    ZimmerListe = []
    datei_lesen_zimmer(ZimmerListe)

    ReservListe = []
    datei_lesen_reserv(ReservListe)

    if opt == 1:
        firstname,lastname = do_reserv_input()
        do_reserv(ReservListe, ZimmerListe, GastListe, firstname, lastname)
        write_in_reserv_datei(ReservListe)
        MenuGemeinsam()
    if opt == 2:
        aktuelle_Res(ReservListe)
        output_aktuelle_Reserv(ReservListe,GastListe)
        MenuGemeinsam()
    if opt == 3:
        ZimmerFilter = []
        seaview, price = zimmer_filter_input()
        Zimmer_filter(ZimmerFilter,ZimmerListe, seaview, price)
        to_string_zimmer(ZimmerFilter)
        MenuGemeinsam()
    if opt == 4:
        Zimmer_frei(ReservListe,ZimmerListe)
        to_string_zimmer(ZimmerListe)
        MenuGemeinsam()

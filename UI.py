def add_zimmer_input():
    nr = int(input("Nummer:"))
    anzahlG = int(input("AnzahlGaste:"))
    preis = int(input("Preis:"))
    farbe = input("Farbe:")
    meerblick = input("Meerblick:")
    return nr, anzahlG, preis, farbe, meerblick

def change_preis_input():
    nr = int(input("Nummer des gewunschten Zimmers:"))
    preis = int(input("Neuer Preis:"))
    return nr,preis

def del_zimmer_input():
    nr = int(input("Nummer des gewunschten Zimmers:"))
    return nr

def add_guest_input():
    firstname = input("Vorname=")
    lastname = input("Nachname=")
    return firstname,lastname

def change_nachname_input():
    firstname = input("Vorname des gewunschten Gastes:")
    lastname = input("Nachname des gewunschten Gastes:")
    Neulastname = input("Neuer Nachname:")
    return firstname,lastname,Neulastname

def del_guest_input():
    firstname = input("Vorname des gewunschten Gastes:")
    lastname = input("Nachname des gewunschten Gastes:")
    return firstname,lastname

def do_reserv_input():
    firstname = input("Vorname=")
    lastname = input("Nachname=")
    return firstname,lastname

def zimmer_filter_input():
    seaview = input("Wollen Sie ein Meerblick haben=")
    price = int(input("Preis soll billiger als="))
    return seaview,price

def output_aktuelle_Reserv(ReservListe,GastListe):
    for obj in ReservListe:
        print(f'Gast:{GastListe[int(obj.indexGast)].vorname} {GastListe[int(obj.indexGast)].nachname}, '
            f'Reservierung(Zimmer:{obj.zimmer}, Anzahl Gaste:{obj.nrG}, Anfangdatum:{obj.anfang}, Enddatum:{obj.ende}')

def write_in_reserv_datei(ReservListe):
    h = open('Reservliste', 'w')
    for obj in ReservListe:
        h.write(f'{obj.indexGast},{obj.zimmer},{obj.nrG},{obj.anfang},{obj.ende},' + '\n')
    h.close()

def write_in_guest_datei(GastListe):
    f = open('gastliste', 'w')
    for obj in GastListe:
        f.write(obj.vorname + ',' + obj.nachname + ',' + '\n')
    f.close()

def write_in_zimmer_datei(ZimmerListe):
    g = open('zimmerliste', 'w')
    for obj in ZimmerListe:
        g.write(f'{obj.nummer},{obj.anzahlG},{obj.preis},{obj.farbe},{obj.meerblick},' + '\n')
    g.close()
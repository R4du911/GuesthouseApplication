from Gaste import Gaste
from Zimmer import Zimmer
from Reservirung import Reservierung
from MenuGemeinsam import do_reserv
from GastMenu import add_guest,change_lastname
from ZimmerMenu import add_zimmer,change_preis
from MenuGemeinsam import Zimmer_frei, Zimmer_filter, aktuelle_Res


def test_aktuelle_Res():
    ReservList = []
    testres = Reservierung(0,2,3,'12/12/2022','31/12/2022')

    ZimmerList = []
    testzimmer = Zimmer(2,3,200,'rot','ja')
    ZimmerList.append(testzimmer)

    GastList = []
    testgast = Gaste('Jorje','Boss')
    GastList.append(testgast)

    do_reserv(ReservList,ZimmerList,GastList,'Jorje','Boss')
    assert testres == ReservList[len(ReservList)-1]

def test_add_guest():
    GastList = []
    testgast = Gaste('Jorje','Boss')

    add_guest(GastList)
    assert testgast == GastList[len(GastList)-1]

def test_change_lastname():
    GastList = []
    testgast = Gaste('Jorje','Boss')
    GastList.append(testgast)

    change_lastname(GastList,'Jorje','Boss','Hermanos')
    assert testgast == GastList[0]

    testgast = Gaste('Jorje','Hermanos')
    assert testgast == GastList[0]

def test_add_zimmer():
    ZimmerListe = []
    testzimmer = Zimmer(1,2,150,'blau','nein')

    add_zimmer(ZimmerListe)
    assert testzimmer == ZimmerListe[len(ZimmerListe)-1]

def test_change_preis():
    ZimmerList = []
    testzimmer = Zimmer(1,2,150,'blau','nein')
    ZimmerList.append(testzimmer)

    change_preis(ZimmerList,1,120)
    assert testzimmer == ZimmerList[0]

    testzimmer = Zimmer(1,2,120,'blau','nein')
    assert testzimmer == ZimmerList[0]

def test_aktuelle_reserv():
    ReservListe=[]
    testreserv = Reservierung(0, 2, 3, '12/12/2022', '31/12/2022')
    ReservListe.append(testreserv)

    aktuelle_Res(ReservListe)
    assert testreserv == ReservListe[len(ReservListe)-1]

def test_zimmer_filter():
    ZimmerListe = []
    testzimmer = Zimmer(3, 3, 200, 'rot', 'ja')
    ZimmerListe.append(testzimmer)

    ZimmerFilter = []

    Zimmer_filter(ZimmerFilter,ZimmerListe,'ja',300)
    assert testzimmer == ZimmerFilter[len(ZimmerFilter)-1]


def test_zimmer_frei():
    ReservList = []
    testres = Reservierung(0, 2, 3, '12/12/2022', '31/12/2022')
    ReservList.append(testres)

    ZimmerList = []
    testzimmer = Zimmer(3, 3, 200, 'rot', 'ja')
    ZimmerList.append(testzimmer)

    Zimmer_frei(ReservList,ZimmerList)
    assert testzimmer == ZimmerList[0]

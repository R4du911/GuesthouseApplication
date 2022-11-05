class Zimmer:
    def __init__(self,nummer,anzahlG,preis,farbe,meerblick):
        self._Nummer = nummer
        self._AnzahlG = anzahlG
        self._Preis = preis
        self._Farbe = farbe
        self._Meerblick = meerblick

    @property
    def nummer(self):
        return self._Nummer
    @nummer.setter
    def nummer(self,nummer):
        self._Nummer = nummer

    @property
    def anzahlG(self):
        return self._AnzahlG
    @anzahlG.setter
    def anzahlG(self,anzahlG):
        self._AnzahlG = anzahlG

    @property
    def preis(self):
        return self._Preis
    @preis.setter
    def preis(self,preis):
        self._Preis = preis

    @property
    def farbe(self):
        return self._Farbe
    @farbe.setter
    def farbe(self,farbe):
        self._Farbe=farbe

    @property
    def meerblick(self):
        return self._Meerblick
    @meerblick.setter
    def meerblick(self,meerblick):
        self._Meerblick = meerblick




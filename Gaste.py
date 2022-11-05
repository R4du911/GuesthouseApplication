class Gaste:
    def __init__(self,vorname,nachname):
        self._Vorname = vorname
        self._Nachname = nachname

    @property
    def vorname(self):
        return self._Vorname
    @vorname.setter
    def vorname(self,vorname):
        self._Vorname = vorname

    @property
    def nachname(self):
        return self._Nachname
    @nachname.setter
    def nachname(self,nachname):
        self._Nachname = nachname






class Reservierung:
    def __init__(self,indexGast,zimmer,nrg,anfang,ende):
        self._IndexGast = indexGast
        self._NrG = nrg
        self._zimmer = zimmer
        self._Anfang = anfang
        self._Ende = ende

    @property
    def indexGast(self):
        return self._IndexGast
    @indexGast.setter
    def indexGast(self,indexGast):
        self._IndexGast = indexGast

    @property
    def nrG(self):
        return self._NrG
    @nrG.setter
    def nrG(self,nrG):
        self._NrG = nrG

    @property
    def zimmer(self):
        return self._zimmer
    @zimmer.setter
    def zimmer(self,zimmer):
        self._zimmer = zimmer

    @property
    def anfang(self):
        return self._Anfang
    @anfang.setter
    def anfang(self,anfang):
        self._Anfang = anfang

    @property
    def ende(self):
        return self._Ende
    @ende.setter
    def ende(self,ende):
        self._Ende = ende

    def to_string_res(self):
        print(f'{self.indexGast},{self.zimmer},{self.nrG},{self.anfang},{self.ende}')




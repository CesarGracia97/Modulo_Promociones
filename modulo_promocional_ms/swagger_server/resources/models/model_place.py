class Provincia:
    def __init__(self, PROVINCIA_ID, PROVINCIA):
        self.PROVINCIA_ID = PROVINCIA_ID
        self.PROVINCIA = PROVINCIA


class Ciudad:
    def __init__(self, CIUDAD_ID, CIUDAD, PROVINCIA):
        self.PROVINCIA = PROVINCIA
        self.CIUDAD_ID = CIUDAD_ID
        self.CIUDAD = CIUDAD


class Sector:
    def __init__(self,  SECTOR_ID, SECTOR, CIUDAD):
        self.SECTOR_ID = SECTOR_ID
        self.SECTOR = SECTOR
        self.CIUDAD = CIUDAD

class Provincia:
    def __init__(self, PROVINCIA_ID, PROVINCIA):
        self.PROVINCIA_ID = PROVINCIA_ID
        self.PROVINCIA = PROVINCIA


class Ciudad:
    def __init__(self, PROVINCIA_ID, CIUDAD_ID, CIUDAD):
        self.PROVINCIA_ID = PROVINCIA_ID
        self.CIUDAD_ID = CIUDAD_ID
        self.CIUDAD = CIUDAD


class CiudadxProvincia:
    def __init__(self, CIUDAD_ID, CIUDAD):
        self.CIUDAD_ID = CIUDAD_ID
        self.CIUDAD = CIUDAD


class Sector:
    def __init__(self, CIUDAD_ID, SECTOR_ID, SECTOR):
        self.CIUDAD_ID = CIUDAD_ID
        self.SECTOR_ID = SECTOR_ID
        self.SECTOR = SECTOR


class SectorxCiudad:
    def __init__(self, SECTOR_ID, SECTOR):
        self.SECTOR_ID = SECTOR_ID
        self.SECTOR = SECTOR


class Subsector:
    def __init__(self, SECTOR_ID, SUBSECTOR_ID, SUBSECTOR):
        self.SECTOR_ID = SECTOR_ID
        self.SUBSECTOR_ID = SUBSECTOR_ID
        self.SUBSECTOR = SUBSECTOR


class SubsectorxSector:
    def __init__(self, SUBSECTOR_ID, SUBSECTOR):
        self.SUBSECTOR_ID = SUBSECTOR_ID
        self.SUBSECTOR = SUBSECTOR

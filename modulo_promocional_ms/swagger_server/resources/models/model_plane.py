class Ofertas:
    def __init__(self, OFERTA_ID, OFERTA):
        self.OFERTA_ID = OFERTA_ID
        self.OFERTA = OFERTA


class Servicios:
    def __init__(self, SERVICIO):
        self.SERVICIO = SERVICIO


class Tecnologias:
    def __init__(self, TECNOLOGIA):
        self.TECNOLOGIA = TECNOLOGIA


class Producto:
    def __init__(self, PRODUCTID, PRODUCTO):
        self.PRODUCTID = PRODUCTID
        self.PRODUCTO = PRODUCTO


class Tipo_Servicios:
    def __init__(self, TIPO_SERVICIO):
        self.TIPO_SERVICIO = TIPO_SERVICIO


class TariffPlanes:
    def __init__(self, TARIFFPLANID, TARIFFPLAN):
        self.TARIFFPLANID = TARIFFPLANID
        self.TARIFFPLAN = TARIFFPLAN


class TariffPlanVariant:
    def __init__(self, TARIFFPLANVARIANTID, TARIFFPLANVARIANT):
        self.TARIFFPLANVARIANTID = TARIFFPLANVARIANTID
        self.TARIFFPLANVARIANT = TARIFFPLANVARIANT


class TariffPlan_X_TariffPlanVariant:
    def __init__(self, TARIFFPLANID, TARIFFPLAN, TARIFFPLANVARIANTID, TARIFFPLANVARIANT):
        self.TARIFFPLANID = TARIFFPLANID
        self.TARIFFPLAN = TARIFFPLAN
        self.TARIFFPLANVARIANTID = TARIFFPLANVARIANTID
        self.TARIFFPLANVARIANT = TARIFFPLANVARIANT

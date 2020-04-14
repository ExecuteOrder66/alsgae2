class LineaDeDetalle:
    def init(self, concepto, precio, unidades, importeBruto, iva, importeTotal):
        self._concepto = concepto
        self._precio = precio
        self._unidades = unidades
        self._importeBruto = importeBruto
        self._iva = iva
        self._importeTotal = importeTotal

    @property
    def concepto(self):
        return self._concepto

    @concepto.setter
    def concepto(self, concepto):
        self._concepto = concepto

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, precio):
        self._precio = precio

    @property
    def unidades(self):
        return self._unidades

    @unidades.setter
    def unidades(self, unidades):
        self._unidades = unidades

    @property
    def importeBruto(self):
        return self._importeBruto

    @importeBruto.setter
    def importeBruto(self, importeBruto):
        self._importeBruto = importeBruto

    @property
    def iva(self):
        return self._iva

    @iva.setter
    def iva(self, iva):
        self._iva = iva

    @property
    def importeTotal(self):
        return self._importeTotal

    @importeTotal.setter
    def importeTotal(self, importeTotal):
        self._importeTotal = importeTotal

    def str(self):
        toret = "Concepto: " + self._concepto + "\n" + \
                "Precio por unidad: " + self._precio + "\n" +\
                "Unidades: " + self._unidades + "\n"+\
                "Importe Bruto: " + self._importeBruto + "\n"+\
                "% IVA: " + self._iva + "\n"+\
                "Importe Total: " + self._importeTotal + "\n"
        return toret


class Factura:
    def __init__(self, fecha):
        self._fecha = fecha
        self._lineas_de_detalle = []

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, v):
        self._fecha = v

    @property
    def lineas_de_detalle(self):
        return self._lineas_de_detalle

    def inserta(self, v):
        self._lineas_de_detalle.append(v)

    def __str__(self):
        toret = "Fecha: " + self._fecha
        for linea in self._lineas_de_detalle:
            toret += linea.__str__

        return toret


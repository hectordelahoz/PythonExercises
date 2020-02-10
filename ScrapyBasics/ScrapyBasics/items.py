from scrapy.item import Field
from scrapy.item import Item


class Row(Item):
    id = Field()
    placa = Field()
    nroComparendo = Field()
    #idDocument = Field()
    #fechaResolucion = Field()
    #nroResolucion = Field()
    #tipoSancion = Field()
    estadoComparendo = Field()
    #valorMulta = Field()
    #interes = Field()
    #costas = Field()
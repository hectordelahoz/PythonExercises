import sqlite3
from sqlite3 import Error

from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from scrapy import FormRequest
from scrapy.crawler import CrawlerProcess


class Row(Item):
    nroComparendo = Field()
    idDocument = Field()
    fechaResolucion = Field()
    nroResolucion = Field()
    tipoSancion = Field()
    estadoComparendo = Field()
    valorMulta = Field()
    interes = Field()
    costas = Field()

class MultasSpider(Spider):
    name = "MultasSpider"
    conslutaURL = "https://portal.barranquilla.gov.co/ConsultaEstadoCuenta/consultaPlaca"
    start_urls = [conslutaURL]

    def parse(self, response):
        tokenViewState = response.xpath('/html/body/div[3]/table/tr[1]/td[5]/form/input[2]/@value').extract_first()
        dataUsuario = {
            'form': 'form',
            'form:hora': 'KKA987',
            'javax.faces.ViewState': tokenViewState,
            'form:btnIngresar': 'form:btnIngresar'
        }
        yield FormRequest(url=self.conslutaURL, formdata=dataUsuario, callback=self.parse_multas)        

    def parse_multas(self, response):
        selector = Selector(response)
        tabla = selector.xpath('/html/body/div[4]/form/div[2]/div/div/div/div[2]/table/tbody/tr')
        
        #register = {}
        for index, row in enumerate(tabla):
            field = ItemLoader(Row(), row)
            field.add_xpath('costas','.//td[9]/text()')
            field.add_xpath('interes','.//td[8]/text()')
            field.add_xpath('valorMulta','.//td[7]/text()')
            field.add_xpath('estadoComparendo','.//td[6]/text()')
            field.add_xpath('tipoSancion','.//td[5]/text()')
            field.add_xpath('nroResolucion','.//td[4]/text()')
            field.add_xpath('fechaResolucion','.//td[3]/text()')
            field.add_xpath('idDocument','.//td[2]/text()')
            field.add_xpath('nroComparendo','.//td[1]/a/text()')            
            #register[index] = field.load_item()
            yield field.load_item()

def CreateDataBase():
    conn = None
    try:
        conn = sqlite3.connect("MyfirstDb")
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    CreateDataBase()
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
    })

    process.crawl(MultasSpider)
    process.start()
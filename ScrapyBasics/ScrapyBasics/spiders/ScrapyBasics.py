from ScrapyBasics.items import Row
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from scrapy import FormRequest
from scrapy import Request

class MultasSpider(Spider):
    name = "MultasSpider"
    conslutaURL = "https://portal.barranquilla.gov.co/ConsultaEstadoCuenta/consultaPlaca"
    parameters = {
        'placas': ['KKA987', 'HGM755', 'QIC457']
    }

    def start_requests(self):
        urls = [self.conslutaURL]
        for url in urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        tokenViewState = response.xpath('/html/body/div[3]/table/tr[1]/td[5]/form/input[2]/@value').extract_first()

        for placas in self.parameters.values():
            for placa in placas:                
                dataUsuario = {
                    'form': 'form',
                    'form:hora': placa,
                    'javax.faces.ViewState': tokenViewState,
                    'form:btnIngresar': 'form:btnIngresar'
                }

                yield FormRequest(url=self.conslutaURL, formdata=dataUsuario, 
                                callback=self.parse_multas, cb_kwargs=dict(placa=placa))

    def parse_multas(self, response, placa):       
        selector = Selector(response)
        tabla = selector.xpath('/html/body/div[4]/form/div[2]/div/div/div/div[2]/table/tbody/tr')        
        
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
            field.add_value('placa',placa)
            field.add_value('id',index)
            yield field.load_item()
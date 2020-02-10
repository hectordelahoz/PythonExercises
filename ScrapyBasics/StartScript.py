from ScrapyBasics.database import DataBase
from ScrapyBasics.email import Email
from os import system
import sys

placas = str(sys.argv[1]) #'''['KKA987','HGM755','QIC457']'''
system("scrapy crawl MultasSpider -a arguments="+placas)

myDataBase = DataBase()
connection = myDataBase.create_connection()
numberOfRegisters = myDataBase.count_all_registers(connection)
numberOfNewRegisters = myDataBase.count_new_registers(connection)

#if numberOfNewRegisters != 0:
table = myDataBase.fetch_all_registers(connection)
message = placas + ' have ' + str(numberOfRegisters) + ' registers and ' + str(numberOfNewRegisters) + ' of them are new\n\n'
for register in table:
    message += str('|' + register[2] + '\t|\t' + register[3] + '\t|\t' + register[4] + '\t|\n')
email = Email()
email.send_email(message)
print('e-mail have been sent')
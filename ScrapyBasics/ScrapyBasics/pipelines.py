from ScrapyBasics.database import DataBase

class ScrapybasicsPipeline(object):

    myDataBase = DataBase()
    connection = None

    def __init__(self):
        self.connection = self.myDataBase.create_connection() 
        if self.connection is not None:           
            self.myDataBase.create_register_table(self.connection)            
        else:
            print("Error! cannot create the database connection.")
        return

    def process_item(self, item, spider):
        with self.connection:                        
            mydata = (item['id'][0], item['placa'][0], item['nroComparendo'][0])           
            self.myDataBase.insert_register(self.connection,mydata)            
        return
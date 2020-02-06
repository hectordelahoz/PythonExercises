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
            ret = self.myDataBase.check_register(self.connection, item['nroComparendo'][0])            
            if ret is None:
                mydata = (1, item['id'][0], item['placa'][0], item['nroComparendo'][0])
                self.myDataBase.insert_register(self.connection,mydata)
            else:
                self.myDataBase.update_register(self.connection,(0,item['nroComparendo'][0]))
        return
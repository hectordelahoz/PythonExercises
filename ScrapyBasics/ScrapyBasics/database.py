import sqlite3
from sqlite3 import Error

class DataBase():

    conn = None

    name = 'myDataBase.db'

    def create_connection(self, db_file = name):
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e) 
        return conn
    
    def create_register_table(self, conn):
        sql_create_register_table = """ CREATE TABLE IF NOT EXISTS registers (
                                        is_new integer,
                                        id integer,                                        
                                        placa text,
                                        estado_comparendo text,
                                        nro_comparendo text PRIMARY KEY); """
        try:
            cursor = conn.cursor()
            cursor.execute(sql_create_register_table)
        except Error as e:
            print(e)
    
    def insert_register(self, conn, reg_data):        
        sql_cmd = ''' INSERT INTO registers(is_new, id, placa, estado_comparendo, nro_comparendo)
                  VALUES(?,?,?,?,?) '''        
        cursor = conn.cursor()
        cursor.execute(sql_cmd, reg_data)
        return cursor.lastrowid

    def update_register(self, conn, reg_data):
        sql = ''' UPDATE registers
              SET is_new = ?,
              estado_comparendo = ?
              WHERE nro_comparendo = ?'''
        cursor = conn.cursor()        
        cursor.execute(sql, reg_data)
        conn.commit()

    def check_register(self, conn, reg_data):      
        cursor = conn.cursor()
        data=(reg_data,)
        cursor.execute('SELECT id, nro_comparendo FROM registers WHERE nro_comparendo=?',data)        
        return cursor.fetchone()
    
    def fetch_all_registers(self, conn):
        sql_cmd = ''' SELECT * FROM registers'''
        cursor = conn.cursor()
        cursor.execute(sql_cmd)
        return cursor.fetchall()
    
    def count_all_registers(self, conn):
        sql_cmd = ''' SELECT COUNT(*) FROM registers'''
        cursor = conn.cursor()
        cursor.execute(sql_cmd)
        return cursor.fetchone()[0]

    def count_new_registers(self, conn):
        sql_cmd = ''' SELECT COUNT(*) FROM registers WHERE is_new=1'''
        cursor = conn.cursor()
        cursor.execute(sql_cmd)
        return cursor.fetchone()[0]
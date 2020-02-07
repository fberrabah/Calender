from model.connection import *
from model.hydra import *

class Read():
    """class for user read this account"""
    def __init__(self):
        self.choice = connection()


    def read(self, date):
        
        sql="""SELECT id, title, date, hour, description FROM rdv WHERE date = %s;"""
        self.choice.initialize_connection()
        self.choice.cursor.execute(sql, (date,))
        test = self.choice.cursor.fetchall()
        self.choice.close_connection()
        for key, value in enumerate(test):
            test[key]= Hydra(value)
        return test



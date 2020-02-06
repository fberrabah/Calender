from model.connection import *

class Read():
    """class for user read this account"""
    def __init__(self):
        self.choice = connection()
        self.month = None
        self.year = None

    def read(self):
        self.choice.initialize_connection()
        self.date =  input("Enter la date :")
        self.hour =  input("Enter l'heure :")
        self.choice.cursor.execute("SELECT * FROM rdv WHERE date = %s AND hour = %s;", (self.date, self.hour,))
        test = self.choice.cursor.fetchall()
        self.choice.close_connection()
        print(test)
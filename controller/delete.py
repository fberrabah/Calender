from model.connection import *

class Delete():
    """class for user delete this account"""
    def __init__(self):
        self.user_choice = connection()
        self.hour = None
        self.date = None

    def del_rdv(self):
        """"method for delte user account after connect to bdd"""
        self.user_choice.initialize_connection()
        self.date =  input("Enter la date :")
        self.hour =  input("Enter l'heure :")
        self.user_choice.cursor.execute("DELETE FROM rdv WHERE date = %s AND hour = %s;", (self.date, self.hour,))
        self.user_choice.connection.commit()
        self.user_choice.close_connection()
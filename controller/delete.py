from model.connection import *

class Delete():
    """class for user delete this account"""
    def __init__(self, date, hour):
        self.user_choice = connection()
        self.hour = hour
        self.date = date

    def del_account(self):
        """"method for delte user account after connect to bdd"""
        self.user_choice.initialize_connection()
        self.user_choice.cursor.execute("DELETE FROM rdv WHERE date = %s AND hour = %s;", (self.date, self.hour))
        self.user_choice.connection.commit()
        self.user_choice.close_connection()
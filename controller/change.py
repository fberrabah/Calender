from model.connection import *


class Change():
    """class for user delete this account"""

    def __init__(self):
        self.user_choice = connection()
        self.hour = None
        self.date = None

    def change_datta(self):
        """"method for delte user account after connect to bdd"""
        column = ""
        while column not in ['title', 'date', 'hour', 'description']:
            column = input("Quelle information voulez vous modifier \n title, date, hour, description :")
            datta = input("Entrer la nouvelle information:")
            self.date = input("Entrer la date du rendez-vous:")
            self.hour = input("Entrer l'heure du rendez-vous:")
            self.user_choice.initialize_connection()
            self.user_choice.cursor.execute("UPDATE rdv set " + column + " = %s WHERE date = %s AND hour = %s;", (datta, self.date, self.hour,))
            self.user_choice.connection.commit()
            self.user_choice.close_connection()
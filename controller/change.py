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
            self.date = input("\033[32mEntrer la date du rendez-vous que vous souhaitez modifier:\033[0m")
            self.hour = input("\033[32mEntrer l'heure du rendez-vous que vous souhaitez modifier:\033[0m")
            column = input("\033[35mQuelle information voulez vous modifier \n title, date, hour, description :\033[0m")
            datta = input("\033[35mEntrer la nouvelle information:\033[0m")
            self.user_choice.initialize_connection()
            self.user_choice.cursor.execute("UPDATE rdv set " + column + " = %s WHERE date = %s AND hour = %s;", (datta, self.date, self.hour,))
            self.user_choice.connection.commit()
            self.user_choice.close_connection()
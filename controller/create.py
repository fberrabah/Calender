from model.connection import *

class Createrdv():

    def __init__(self,):
        self.choice = connection()
        self.title = None
        self.date = None
        self.hour = None
        self.description = None
        

    def create(self,):
        self.choice.initialize_connection()
        self.title = input("Entrer le titre :").lower()
        self.date = input("Entrer la date du rendez-vous :").lower()
        self.hour = input("Entrer l'heure du rendez-vous :").lower()
        self.description = input("Entrer une description :").lower()
        self.choice.cursor.execute("INSERT INTO rdv(title, date, hour, description) VALUES"
                                  "(%s, %s, %s, %s)" ,(self.title, self.date, self.hour,self.description))
        self.choice.connection.commit()
        self.choice.close_connection()



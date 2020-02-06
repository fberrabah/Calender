from model.connection import *
import calendar
import datetime
import locale


class Loginview():
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

    def monthcurrent(self):
        
        locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')
        year = datetime.datetime.today().year
        month = datetime.datetime.today().month
        date = calendar.month(year, month)
        self.month = month
        self.year = year
        print("\033[35m{}""\033[0m".format(date))

    def previousmonth(self):
        if self.month > 1:
            self.month -= 1 
        else :
            self.month = 12 
            self.year -= 1
        year = datetime.datetime.today().year
        date = calendar.month(self.year, self.month)
        print("\033[34m{}""\033[0m".format(date))




    def nextmonth(self):
        if self.month < 12:
            self.month += 1 
        else :
            self.month = 1
            self.year += 1
        year = datetime.datetime.today().year
        date = calendar.month(self.year, self.month)
        print("\033[31m{}""\033[0m".format(date))





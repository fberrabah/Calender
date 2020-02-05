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
        self.choice.cursor.execute("SELECT * FROM rdv;")
        test = self.choice.cursor.fetchall()
        self.choice.close_connection()
        return test

    def monthcurrent(self):
        
        locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')
        year = datetime.datetime.today().year
        month = datetime.datetime.today().month
        date = calendar.month(year, month)
        self.month = month
        self.year = year
        print(date)

    def previousmonth(self):
        if self.month > 1:
            self.month -= 1 
        else :
            self.month = 12 
            self.year -= 1
        year = datetime.datetime.today().year
        date = calendar.month(self.year, self.month)
        print(date)




    def nextmonth(self):
        if self.month < 12:
            self.month += 1 
        else :
            self.month = 1
            self.year += 1
        year = datetime.datetime.today().year
        date = calendar.month(self.year, self.month)
        print(date)





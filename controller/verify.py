from model.connection import *
from controller.create import *

class Verify():
    def __init__(self, d, date, h, hour):
        self.d = d
        self.date = date
        self.h = h
        self.hour = hour
        self.date_ok = None
        self.hour_ok = None 
        self.log = connection()
        
    def check_date(self, d, date, date_ok):
        """method for verify i pseudo entry is in
        bdd in champ pseudo"""
        for row in self.d:
            for i in row:
                if self.date == i:
                    self.date_ok = True
                    
   
   
    def check_hour(self, h, hour, hour_ok):
        """method for verify password"""

        for row in self.h:
            for i in row:
                if self.hour == i:
                    self.hour_ok = True
                    self.hour_ok


    def check_date_hour(self):
        
        if self.date_ok == True and self.hour_ok == True:
            log = Createrdv()
            log.create()
        else :
            print("Il y a déja un rendez pour cette heur la!")
            return
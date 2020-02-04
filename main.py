from model.connection import *
from controller.delete import *
from controller.change import *
from controller.create import *
from view.viewcal import *
import sys
import calendar
import datetime




test=connection()
test.initialize_connection()
test.close_connection()



if __name__=='__main__':
    x = datetime.datetime.now()
    print(x.strftime("      %x"))
    vue = Loginview()
    #print(calendar.month(2020, 2))
    vue.monthcurrent()

    
    choix=""     
    print("\n----------------------------------------\n")
    print('Bienvenue dans votre agenda personnel.')
    print("\n----------------------------------------\n")
    while choix != "q":
        choix = input("\n(p) Pour voir le mois précédent.\n(s) Pour voir le mois suivant.\n(o) Creer un événement.\n(a) Si vous souhaitez supprimer un événement \n(c) Si vous souhaitez changer un événement.\n(q) Pour quitter.\nVotre choix :").lower()
        if choix == "p":          
            vue.previousmonth()

        if choix == "s":        
            vue.nextmonth()
      
        if choix == "o":       
            log = Createrdv()
            log.create()
        

        if choix == "a":
            
            test = Delete()
            test.del_rdv()

        if choix == "q":
            
            print("A bientôt.")
            sys.exit() 



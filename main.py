from model.connection import *
from controller.delete import *
from controller.change import *
from controller.create import *
import sys
import calendar




test=connection()
test.initialize_connection()
test.close_connection()


if __name__=='__main__':
    print(calendar.month(2020, 2))

    choix=""     
    print("\n----------------------------------------\n")
    print('Bienvenue dans votre agenda personnel.')
    print("\n----------------------------------------\n")
    while choix != "q":
        choix = input("\n(o) creer un événement \n(s) si vous souhaitez supprimer un événement \n(c) Si vous souhaitez changer un événement \n(q) pour quitter\n Votre choix :").lower()
        if choix == "o":          
            log = Createrdv()
            log.create()

        if choix == "s":
            
            test = Delete()
            test.del_rdv()

        if choix == "q":
            
            print("A bientôt.")
            sys.exit() 



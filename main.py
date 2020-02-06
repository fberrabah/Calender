from model.connection import *
from controller.delete import *
from controller.change import *
from controller.create import *
from view.viewcal import *
from model.entities import *
import calendar
import datetime




if __name__=='__main__':
    x = datetime.datetime.now()
    print(x.strftime("\033[34m      %x\033[0m"))
    vue = Loginview()
    vue.monthcurrent()

    
    choix=""     
    print("\033[32m\n----------------------------------------\n\033[0m")
    print('\033[32mBienvenue dans votre agenda personnel.\033[0m')
    print("\033[32m\n----------------------------------------\n\033[0m")
    while choix != "q":
       
        choix = input("\033[33m\n(p) Pour voir le mois précédent.\n(s) Pour voir le mois suivant.\n(o) Creer un événement.\n(a) Si vous souhaitez supprimer un événement \n(c) Si vous souhaitez changer un événement.\n(q) Pour quitter.\nVotre choix :\033[0m").lower()
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
        
        if choix == "c":
            change = Change()
            change.change_datta()
            print ("Information modifié")
        
        if choix == "v":
            lire = Read()
            lire.read()
    

        if choix == "q":
            print("A bientôt.")
            



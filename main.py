from model.connection import *
from model.connectaccount import *
from model.createaccount import *
from controller.verify import *
from controller.profil import *
import sys


test=connection()
test.initialize_connection()
test.close_connection()


if __name__=='__main__':

    choix=""     
    print("\n----------------------------------------\n")
    print('Bienvenue dans votre application préférée.')
    print("\n----------------------------------------\n")
    while choix != "q":
        choix = input("\n(o) creer un évenement : \n(n) si vous souhaitez créer un compte : \n(q) pour quitter : ").lower()
        if choix == "o":          
            log = Connectaccount()
            log.connect()

        if choix == "n":
            
            test= Createaccount()
            test.create()
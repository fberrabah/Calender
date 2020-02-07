class Hydra():
    def __init__(self, i=False ): #add constructor with value none
        self.title = None
        self.hour = None
        self.date = None
        self.description = None
        if i:
            self.hydrat(i)


    def hydrat(self, i): 
        for key, value in i.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def __str__(self):
        return"""\033[36m Le titre : {} \n L'heur du rendez-vous : {}\n La description : {}\033[0m""".format(self.title, self.hour, self.description)
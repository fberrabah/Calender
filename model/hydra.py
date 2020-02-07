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
        return"""{} : {}
        {}""".format(self.hour, self.title, self.description)
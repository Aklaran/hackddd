class TextInput():
    #tuple bounds = (x, y, w, h)
    #dict vs = variables that user can set in form {"var" : NULL}
    def __init__(self, vs, bounds):
        self.vs = vs
        self.bounds = bounds

    def setVars(self):
        for key in self.vs:
            validInput = False;
            while validInput == False:
                p = input("pick a value for " + key + ": ")
                try: p = int(p)
                except:
                    print("Please provide a valid integer.")
                    continue
                validInput = True
            self.vs[key] = p



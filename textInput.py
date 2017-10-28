class TextInput():
    #tuple coords = (x, y)
    #dict vs = variables that user can set in form {"var" : NULL}
    def __init__(self, vs, coords):
        self.vs = vs
        self.coords = coords

    def setVars(self):
        variables = self.vs
        for key in self.vs:
            validInput = False;
            while validInput == False:
                p = input("pick a value for " + key + ": ")
                try: p = int(p)
                except:
                    print("Please provide a valid integer.")
                    continue
                validInput = True
            variables[key] = p
        return variables



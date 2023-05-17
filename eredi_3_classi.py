class Persona :
    def __init__(self, nome):   
        self.nome = nome
        
    def MasterD(self):                           
        print('ciao, sono ', self.nome )    

x = Persona('Luca')        
x.MasterD()


class Allievo(Persona):

    def __init__(self, nome, eta):
        super().__init__(nome)
        self.eta = eta


    def MasterD(self):
        print('ciao, sono ', self.nome , ' ' , self.eta)    

y = Allievo('mario',23)
y.MasterD()        


class Pers3(Allievo):
    def __init__(self, nome, eta,grado):
        super().__init__(nome,eta)
        self.grado = grado

    saluto = 'ciao'

    def MasterD(self):
        print(self.saluto, ', sono ', self.nome ,' ho' , self.eta , 'anni, con grado ', self.grado) 

z = Pers3('tizio',43, 'boh')     
z.MasterD()   
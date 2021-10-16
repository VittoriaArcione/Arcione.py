class retta:

    def __init__(self,a,b,c):
    
        self.__a = a  
        self.__b = b
        self.__c = c
        
    def equazione_imp(self):
        if float(self.__c) == 0:
            return f'{self.__a}x + {self.__b} = 0'
        elif float(self.__b)==0:
            return f'{self.__a}x + {self.__c} = 0'
        elif  float(self.__a)== 0:
            return f'{self.__b}y + {self.__c} = 0'
        else:
            return f'{self.__a}x +{self.__b}y + {self.__c} = 0'

    def equazione_esp(self):
        if int(self.__a) == 0:
            return f'y = -{self.__c}/{self.__b}'
        elif int(self.__c) == 0:
            return f'y = -{self.__a}x/{self.__b}' 
        elif int(self.__b) == 0:
            return f'x = -{self.__c}/{self.__a}' 
        else:
            return f'y =(-{self.__a}/{self.__c}x + -{self.__c}/{self.__c}) '
 
    def coefficiente(self):
        if int(self.__b) == 0: 
            return f'la retta è parallela all asse delle ordinate, quindi il coefficiente angolare è nullo' 
        elif int(self.__a)== 0:
            return f'la retta è parallela all asse delle ascisse, quindi il coefficiente angolare è uguale a 0 '
        else:
            return f'k = -{self.__a}/{self.__b} '

a_b_c = retta (input("a: "), input("b: "), input("c: "))

print(a_b_c.equazione_imp())
print(a_b_c.equazione_esp())
print(a_b_c.coefficiente())
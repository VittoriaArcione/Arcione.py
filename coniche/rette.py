class retta:

    def __init__(self,a,b,c):
    
        self.__a = float(a)
        self.__b = float(b)
        self.__c = float(c)
        
    def getA(self):
        print("il valore di a è: ")
        return self.__a

    def getB(self):
        print("il valore di b è: ")
        return self.__b
    
    def getC(self):
        print("il valore di c è: ")
        return self.__c
      

    def equazione_imp(self):
        if float(self.__c) == 0:
            return f'{self.__a}x + {self.__b} = 0'
        elif float(self.__b)==0:
            return f'lequazione implicita è: {self.__a}x + {self.__c} = 0'
        elif  float(self.__a)== 0:
            return f'l equazione implicita è: {self.__b}y + {self.__c} = 0'
        else:
            return f'l equazione implicita è: {self.__a}x +{self.__b}y + {self.__c} = 0'

    def equazione_esp(self):
        if int(self.__a) == 0:
            return f'l equazione esplicita è: y = -{self.__c}/{self.__b}'
        elif int(self.__c) == 0:
            return f'lequazione esplicita è: y = -{self.__a}x/{self.__b}' 
        elif int(self.__b) == 0:
            return f'l equazione esplicita è: x = -{self.__c}/{self.__a}' 
        else:
            return f'l equazione esplicita è: y =(-{self.__a}/{self.__c}x) + (-{self.__c}/{self.__c}) '

    

 
    def coefficiente(self):
        if int(self.__b) == 0: 
            return f'la retta è parallela all asse delle ordinate, quindi il coefficiente angolare è nullo' 
        elif int(self.__a)== 0:
            return f'la retta è parallela all asse delle ascisse, quindi il coefficiente angolare è uguale a 0 '
        else:
            return f'il coefficiente angolare è: k = -{self.__a}/{self.__b} '

   
    def fascio(self,a1,b1,c1): 

        if float (a1) == float(self.__a):
            return f'il fascio è improprio e la sua equazione è y= {self.__a}x + q '
        else:
            return f'il fascio è proprio e la sua equazione è {self.__a}x + {a1}kx + {self.__b}y + {b1}ky + {self.__c} +  {c1}k = 0 '


    def intersezione(self, a1, b1, c1):
        if -self.__a/self.__b == -a1/b1:
            return None
        if -self.__a == a1 and self.__b == b1 and self.__c == c1:
            return f'le rette sono coincidenti'
        if -self.__a/self.__b == -a1/b1 and -self.__c/self.__b == -c1/b1:
            return self
        
        x = ((self.__c/self.__b)-(c1/b1))/((-self.__a/self.__b)+(a1/b1))
        y = (-self.__a/self.__b)*x+(-self.__c/self.__b)
        print("le coordinate del punto di intersezione sono: ")
        return round(x, 2), round(y, 2) 
        
    def trovaY(self, x): 
        x = float(x)
        y = (self.__a)/(self.__b)*(x)-(self.__c)/(self.__b) 
        y1 = -(self.__c)/(self.__b) 
        print("il valore di y in base alla x scelta è: ")
        if x == 0:
          return y1
        else: 
          return y 
            
       


a_b_c = retta (input("a: "), input("b: "), input("c: "))
a1 = float(input("a1: "))
b1 = float(input("b1: "))
c1 = float(input("c1: "))

print(a_b_c.getA())
print(a_b_c.getB())
print(a_b_c.getC())
print(a_b_c.trovaY(input("x: ") ))
print(a_b_c.equazione_imp())
print(a_b_c.equazione_esp())
print(a_b_c.coefficiente())
print(a_b_c.fascio(a1, b1, c1))
print(a_b_c.intersezione(a1, b1, c1))
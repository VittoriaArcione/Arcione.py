class parabola:
    def __init__(self, tipo = "param", p1 = None, p2 = None, p3 = None):
       if (tipo=="param"):
        self.__a = float(p1)
        self.__b = float(p2)
        self.__c = float(p3)
       elif(tipo == "fuocoDiret"):
        self.__p1 = float(p1)
        self.__p2 = float(p2)
        self.__p3 = float(p3)
        self.__a = 1/(2*self.__p2 - 2*self.__p3)
        self.__b = -2*self.__a * self.__p1
        self.__c = (4*self.__a*self.__p2 + self.__b*self.__b - 1)/(4*self.__a)
        
    def GetA(self):
      return self.__a
 
    def GetB(self):
      return self.__b

    def GetC(self):
      return self.__c

    def fuoco(self):
     # parabola con asse parallelo all'asse y
      x =  (-self.__b)/(self.__a)*2
      y = (1) -pow((self.__b),2)+ (self.__a)*(self.__c)*4/4*(self.__a)
      print("le coordinate del fuoco con asse parallelo all'asse y sono:")
      return round(x, 2), round(y, 2)

    def fuoco1(self):
    # parabola con asse parallelo all'asse x
      x = (1) -pow((self.__b),2)+ (self.__a)*(self.__c)*4/4*(self.__a)
      y = (-self.__b)/(self.__a)*2 
      print("le coordinate del fuoco con asse parallelo all'asse x sono:")
      return round(x, 2), round(y, 2)

    def direttrice(self):
    # parabola con asse parallelo all'asse y
     y = -1 -(self.__b)**2 + 4*(self.__a)*(self.__c)/4*(self.__a)
     return f'l equazione della retta direttrice di una parabola con asse parallelo all asse y è:  y= {y}'


    def direttrice1(self):
     # parabola con asse prallelo all'asse x
     x = -1 -(self.__b)**2 + 4*(self.__a)*(self.__c)/4*(self.__a)
     return f'l equazione della retta direttrice di una parabola con asse parallelo all asse x è:  x= {x}'
    
    
    def asse(self):
    # parabola con asse parallelo all'asse delle y 
     y = -(self.__b)/(self.__a)*2
     return f'l equazione dell asse parallelo allasse y è:  y={y}'
      

    def asse1(self):
    # parabola con asse parallelo all'asse delle x
      y = -(self.__b)/(self.__a)*2
      return f'l equazione dell asse di una parabola con asse parallelo all asse y è y= {y}'




a_b_c = parabola(input("a: "), input("b: "), input("c: "))

print(a_b_c.GetA())
print(a_b_c.GetB())
print(a_b_c.GetC())
print(a_b_c.fuoco())
print(a_b_c.fuoco1())
print(a_b_c.direttrice())
print(a_b_c.direttrice1())
print(a_b_c.asse())
print(a_b_c.asse1())
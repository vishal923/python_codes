from regex import B


class Formulaa:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def sqof2num(self):
        result = self.a**2+self.b**2+2*self.a*self.b
        print(f'the sum of square of {self.a} & {self.b} is : {result}')
obj1 = Formulaa(2,3)
obj1.sqof2num()         
        
        
#کد عجیب
class Foo:

    def __init__(self,x=0):
        self._x=x
        
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self,value):
        if value>=0:
            value=str(value)
            l=len(value)
            self._x=value[l-2:l]
            self._x=int(self._x)
        elif value<0:
            self._x=-1
            
p=Foo()
# print(p.x)
# p.x=125
# print(p.x)
# p.x = 15874
# print(p.x)
# p.x = 8
# print(p.x)
# p.x = 13
# print(p.x)
# p.x = -15698
# print(p.x)

# p.x = 1234
# print(type(p.x))
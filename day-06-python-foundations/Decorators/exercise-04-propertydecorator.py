
'''Class Storing with a setter that rejects values below -273.15 with setter and conversion function without setter '''
class ValueError(Exception):
    ''' Value error when tempeature is below abssolute zero'''


class Temperature(ValueError):
    def __init__(self,c:float):
        self.celcious=c

    @property
    def celcious(self)->float:
        return self._c
    
    @celcious.setter
    def celcious(self,c:float)->float:
        if c<=-273.15 :
            raise ValueError('Below Absolute Zero Temperature')
        self._c=c
        return self._c

    @property
    def farenheit(self):
        return (self._celcious*9/5+32)
    

try:
    c=float(input("enter the tempeature"))
    t=Temperature(c)
    print(t.celcious)
    print(t.farenheit)
except ValueError as e :
    print(f"{e}")
    


from abc import ABC,abstractmethod
import math


'''Note The answer is OverEngineered for grasping every conncept'''
class InCompatibleDataType(Exception):
    ''' Raised If datatype is incompatible '''

class Shape(ABC):
    '''Base Abstract is just use for initalize and cant be use to create an object'''
    @abstractmethod
    def Area()->None:
        '''Computes Area'''

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self,radius)->None:
        if not isinstance(radius,(float,int)):
            raise InCompatibleDataType('Data type must me integer or float')
        self._radius=radius

    def Area(self):
        print(f"The area of Circle is {(math.pi*(self._radius**2)):.6f}")\

class Rectangle(Shape):
    def __init__(self,lenght,breadth):
        self.parameter=(lenght,breadth)
    
    @property
    def parameter(self)->tuple:
        return (self._lenght,self._breadth)

    @parameter.setter
    def parameter(self,data:tuple):
        lenght,breadth=data
        if not isinstance(lenght,(float,int)) or not isinstance(breadth,(float,int)):
            raise InCompatibleDataType('Data type must me float')
        self._lenght,self._breadth=lenght,breadth
    def Area(self):
        print(f"The area of rectangle is {self._lenght*self._breadth}")


def Calculate(a:object):
    a.Area()
try:
    Circle_1=Circle(1)
    Calculate(Circle_1)
    print(' ')
    Rect=Rectangle(2,4)
    Calculate(Rect)
except InCompatibleDataType as e:
    print(f"Exception Occured : {e}")




    


        
    
        

            

        

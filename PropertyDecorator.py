class Circle:
    def __init__(self,radius):
        self.radius = radius 
        
    def set_radius(self):
        return self._radius
    
    @property 
    def radius(self):
        return self._radius 
    
    @property
    def diameter(self):
        return self._radius*2
    
    @property
    def area(self):
        return 3.14*(self._radius**2) 
    
circle = Circle(5)
print(circle.radius) 
print(circle.diameter) 
print(circle.area) 
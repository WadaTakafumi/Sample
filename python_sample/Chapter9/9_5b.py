#プロパティ
class circle():
    def __init__(self,radius):
        self.radius=radius
    @property
    def diameter(self):
        return 2*self.radius
    @diameter.setter
    def radius(self,radius):
        self.radius=radius
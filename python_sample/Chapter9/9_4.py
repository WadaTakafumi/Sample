#super()
class person():
    def __init__(self,name):
        self.name=name

class Emailperson(person):
    def __init__(self,name,email):
        super().__init__(name)
        self.email=email
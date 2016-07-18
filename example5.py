class Base(object):
    pass

class Season(Base):
    def __init__(self, **kwargs):
        for i in kwargs:
            self.i = []
    
class Fruit(Base):
    pass

class Area(Season):
    def __init__(self, **kwargs):
        for i in kwargs:
            self.i = kwargs[i]
        super(Area, self).__init__()

k = Area()
k.hyderabad = "winter"
print dir(k)
k.hyderabad.winter.append("apple")
# k.hyd = {}

# Hello world whats up!!

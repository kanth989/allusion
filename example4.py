

class Fruit(object):
    def __init__(self, fruit):
        self.fruit = fruit

class Season(Fruit):
    def __init(self):
        self.seasons_by_area = {}
        self.add_season()

    def add_season(self):
        self.seasons_by_area[self.season] = [] 

class Area(Season):
    areas = {}
    def __init__(self, area, season):
        self.area = area
        self.season =season
        self.add_area()
        super(Area, self).__init__(self)

    def add_area(self):
        if not self.areas.get(self.area):
            self.areas[self.area] = {} 

    
hyd_w = Area("Hyd", "winter")
hyd_s = Area("Hyd", "summer")

# hyd.add_season("summer")

print  "-------------"
print hyd_w.season
print hyd_s.season



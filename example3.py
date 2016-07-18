class Fruits(object):
    fruits = {}
    def __init__(self, f_name, s_name, a_name):
        self.f_name = f_name
        self.s_name = s_name
        self.a_name = a_name
        self.add_to_fruits()

    def add_to_fruits(self):
        if self.f_name.endswith("kaya"):
            return "Not added because its is vegetable"
        else:
            if not self.fruits.get(self.a_name):
                self.fruits[self.a_name] = {}
            if not self.fruits.get(self.a_name).get(self.s_name):
                self.fruits[self.a_name][self.s_name] =[]
                self.fruits[self.a_name][self.s_name].append(self.f_name)
            else:
                self.fruits[self.a_name][self.s_name].append(self.f_name)
apple = Fruits("apple","winter","hyd")
mango = Fruits("mango","summer","hyd")
grapes = Fruits("grapes","winter","hyd")

print apple.fruits
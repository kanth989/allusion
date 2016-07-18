fruits = {}

'''
fruits = {
    "hyde":{
    "summer": ["grapes","mango"],
    "witer": ["appe"]
    }
    ..
}
fruits["hyde"]["winter"]
'''
def add_to_fruits(f_name, s_name, a_name):
    if f_name.endswith("kaya"):
        return "Not added because its is vegetable"
    else:
        if not fruits.get(a_name):
            fruits[a_name] = {}
        if not fruits.get(a_name).get(s_name):
            fruits[a_name][s_name] =[]
            fruits[a_name][s_name].append(f_name)
        else:
            fruits[a_name][s_name].append(f_name)
    

        return fruits

add_to_fruits("apple","winter","hyd")
add_to_fruits("papaya", "Year","hyd")
add_to_fruits("mango","summer","vja")
add_to_fruits("grapes","summer","vja")
add_to_fruits("Potal kaya","Year","xyz")
print fruits
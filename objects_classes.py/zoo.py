class Zoo:
    __animals = 0
    
    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []
        
    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
            
        Zoo.__animals += 1
         
            
    def get_info(self, species):
        if species == "mammal":
            info = f"Mammals in {self.name}: {', '.join(self.mammals)}\nTotal animals: {Zoo.__animals}" 
        elif species == "fish":
            info = f"Fishes in {self.name}: {', '.join(self.fishes)}\nTotal animals: {Zoo.__animals}" 
        elif species == "bird":
            info = f"Birds in {self.name}: {', '.join(self.birds)}\nTotal animals: {Zoo.__animals}" 
            
        return info
    
zoo_name = input()
zoo = Zoo(zoo_name)
count = int(input())

for _ in range(count):
    species, name = input().split()
    zoo.add_animal(species, name)
    
info = input()
print(zoo.get_info(info))
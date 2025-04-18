class Zoo:
    __animals = 0  #the underscores in front of the animals attribute is used to express that it is private\
    # and is not meant to be used outside the class

    def __init__(self,name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

#The other 2 methods for adding and getting the info
    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self,species):
        result = ""
        if species == "mammal":
            result += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
        elif species == "fish":
            result += f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
        elif species == "bird":
            result += f"Birds in {self.name}: {', '.join(self.birds)}\n"
        result += f"Total animals: {Zoo.__animals}"
        return result
#We make the checks for the species inside the methods
#Finally, implement the logic for reading the input and printing the result
zoo_name = input()
zoo = Zoo(zoo_name)
n = int(input())
for i in range(n):
    line = input().split()
    species = line[0]
    name = line[1]
    zoo.add_animal(species,name)

info = input()
print(zoo.get_info(info))



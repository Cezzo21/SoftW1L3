from abc import ABC, abstractmethod

class student(ABC):
    def __init__(self, species, school, name):
        self.species = species
        self.school = school
        self.name = name
    #Setters:
    def setspecies(self, species):
        self.species = species
    def setschool(self, school):
        self.school = school
    def setname(self, name):
        self.name = name
    #Getters:
    def getspecies(self):
        return self.species
    def getschool(self):
        return self.school
    def getname(self):
        return self.name
    #abstract
    @abstractmethod
    def section(self):
        pass
    @abstractmethod
    def year(self):
        pass

class senior(student):
    def __init__(self, species, school, name):
        super().__init__(species, school, name)
    def section(self):
        print("A")
    def year(self):
        print("2021")

carol = senior("Human", "IC", "Carol")
print(carol.name, "will graduate in", carol.year())
carol.year()
carol.section()


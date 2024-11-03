import math

from abc import ABC, abstractmethod

from enum import Enum
class Estate_types(float, Enum):
    land = 0.85
    building_site = 9
    forrest = 0.35
    garden = 2

class Locality:
    def __init__(self, name, locality_coefficient):
        self.name = name
        self.locality_coefficient = locality_coefficient
        
class Property(ABC):
    def __init__(self, locality):
        self.locality = locality

    @abstractmethod
    def calculate_tax():
        pass

class Estate(Property):
    def __init__(self, locality, estate_type, area):
        super().__init__(locality)
        self.estate_type = estate_type
        self.area = area

    def calculate_tax(self):
        if hasattr(Estate_types, self.estate_type):
            koeficient = Estate_types[self.estate_type].value
        else:
            koeficient = 0
            print("Chybně zadaný typ pozemku, prosím opravte, jinak daň z pozemku nebude zahrnuta v přiznání.")
        return math.ceil(self.area * koeficient * self.locality.locality_coefficient)
    
    def __str__(self):
        return f"Jedná se o typ pozemku \"{self.estate_type}\" o rozloze {self.area} m2 v lokalitě {self.locality.name} \
(místní koeficient {self.locality.locality_coefficient}) s daní z nemovitosti ve výši (v Kč):"

class Residence(Property):
    def __init__(self, locality, area, commercial):
        super().__init__(locality)
        self.area = area
        self.commercial = commercial

    def calculate_tax(self):
        if self.commercial == "False":
            return math.ceil(self.area * self.locality.locality_coefficient * 15)
        else:
            return math.ceil(self.area * self.locality.locality_coefficient * 15 * 2)
            
        
    def __str__(self):
        return f"Jedná se o stavbu o rozloze {self.area} m2 v lokalitě {self.locality.name} \
(místní koeficient {self.locality.locality_coefficient}) s daní z nemovitosti ve výši (v Kč):"

class TaxReport:
    def __init__(self, name):
        self.name = name
        self.property_list = []

    def add_property(self, property):
        if isinstance(property, Property):
            self.property_list.append(property)
        else:
            print("Je třeba vložit nemovitost.")

    def calculate_tax(self):
        total_tax = 0
        for property in self.property_list:
            total_tax = total_tax + property.calculate_tax()
        return total_tax
    
    def __str__(self):
        return f"Celková daň z nemovitosti v Kč, kde je poplatníkem {self.name} je:"

lokalita1 = Locality("Manětín", 0.8)
lokalita2 = Locality("Brno", 3)
pozemek = Estate(lokalita1, "land", 900)
dum = Residence(lokalita1, 120, "False")
kancelar = Residence(lokalita2, 90, "True")
danove_priznani = TaxReport("Pavel Novák")

danove_priznani.add_property(pozemek)
danove_priznani.add_property(dum)
danove_priznani.add_property(kancelar)

print(pozemek, pozemek.calculate_tax())
print(dum, dum.calculate_tax())
print(kancelar, kancelar.calculate_tax())
print(danove_priznani, danove_priznani.calculate_tax())
'''
Dunder Methods,
        >_ It shouldn't be modified but you could though :)  " Think It Through "...

'''


class LaptopMachine():
        def __init__(self, name="Unknown", model="Unknown", credits="Unknown", specs="Unknown") -> None:
            self._name = name
            self._model = model
            self._credit = credits
            self._specs = specs

        def Intro(self):
                return (f"This is {self._name}. Model- {self._model}.. {self._credit} credits only... Specifications- {self._specs} :)")


        def Specifications(self):
                return (f"\t {self._specs} ...")


        # Dunder Methods...
        def __str__(self):
                return ("Legendary String...")


        def __del__(self):
            print("Listening 'Go Crazy' on spotify :) ")

        
        

machine_one = LaptopMachine("Acer Predator", "2021", "119,000")
print(machine_one.Intro())


class PortableWorkstation(LaptopMachine):
        def __init__(self, name="Unknown", model="Unknown", credits="Unknown", specs="Unknown") -> None:
            super().__init__(name, model, credits, specs)
        

machine_two = PortableWorkstation("Acer Predator", "2021", "119,000", "Intel Core I7 11800H, 8C 16T/ Nvidia RTX 3060, 6GB VRAM, 105w TGP/ IPS QHD 165Hz 3ms Display/ Thunderbolt 4/ RGB Gaming Keyboard/ Durable Design")
print(machine_two.Intro())

print(type(machine_one))
print(type(machine_two))

# Specific attributes...
machine_two.upgrade = "Intel Core I7 12th Gen. CPU..."
print(machine_two.upgrade)




# Dunder Method Outputs...

print(str(machine_one))
print(machine_one.__str__())

del machine_one






"""
Developer: Master Skywalker
Purpose: Creation of the Cosmos *
Stardate: 12021.301.13:48:00

"""


class UniverseForces():
    def __init__(self, electromagnetism=True, strong_force=True, weak_force=False, gravity=True) -> None:
        self._electromagnetism = electromagnetism
        self._gravity = gravity
        self._strong_force = strong_force
        self._weak_force = weak_force



class UniverseObjects(UniverseForces):
    def __init__(self, ufo=True, space_dust=False, meteoroid=False, asteroid=False, comet=False, moon=False, planet=False, 
    rouge_planet=False, star=False, neutron_star=False, magnetar=False, solar_system=False, black_hole=False, galaxy=False) -> None:
        self._ufo = ufo
        self._space_dust = space_dust
        self._meteoroid = meteoroid
        self._asteroid = asteroid
        self._comet = comet
        self._moon = moon
        self._planet = planet
        self._rouge_planet = rouge_planet
        self._star = star
        self._neutron_star = neutron_star
        self._magnetar = magnetar
        self._solar_system = solar_system
        self._black_hole = black_hole
        self._galaxy = galaxy
        
        super().__init__()



class Life(UniverseObjects):
    def __init__(self, humans) -> None:
        self._human = humans



x_ufo = UniverseObjects()
print(x_ufo._ufo)
print(x_ufo._asteroid)
    

print(x_ufo._weak_force)
x_ufo._weak_force = True
print(x_ufo._weak_force)




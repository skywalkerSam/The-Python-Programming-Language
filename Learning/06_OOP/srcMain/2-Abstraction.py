
"""
Abstraction:
            >_ Extraction of data, as we wanted & hide all other stuff.

"""


class Universe():
    def __init__(self, _Forces="""Electromagnetism", "Gravity", "Strong & Weak Forces""", _Laws="Laws Of Physics") -> None:
        self.forces = _Forces
        self.laws = _Laws

    def life(self):
        return self.forces + " And " + self.laws


earth = Universe()
print("Fundamental Forces: \n", earth.forces)
print(f"Laws of Earth means: \n {earth.laws}")


"""
Private vs Public Variables:
                            >_ There is no such functions as private but, the python community decided that ( _ ) started variables should be private & not modified.

"""


class Dark():
    def __init__(self, matter="Dark Matter", energy="Dark Energy") -> None:
        self._matter = matter
        # Convention of private variables ( _ABC ) but, not true private, just a rule that we can bend.
        self._energy = energy


research = Dark()
print(research._matter)
print(research._energy)
print(
    f"This research topic about {research._matter} and {research._energy} are still under R&D...")


# Abstraction Functions
print(len('Mr. Skywalker'))
print("Mr. Skywalker".count("r"))



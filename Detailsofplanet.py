class Detailsofplanet:
    def __init__(self, name, surfacegasses, numberofmoons, rings ):
        self.name = name
        self.surfacegasses = surfacegasses
        self.numberofmoons = numberofmoons
        self.rings = rings    
p1 = Detailsofplanet("Mercury", '', 0, "No")
p2 = Detailsofplanet("Venus", 'Carbo Dioxide, Nitrogen', 0, "No")
p3 = Detailsofplanet("Earth", 'Nitrogen, Oxygen', 1, "No")
p4 = Detailsofplanet("Jupitor", 'Hydrogen, Helium', 79, "Yes")
p5 = Detailsofplanet("Saturn", 'Hydrogen, Helium', 83, "Yes")
p6 = Detailsofplanet("Uranus", 'Hydrogen, Helium, Methane', 27, "Yes")

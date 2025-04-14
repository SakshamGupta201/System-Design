import copy


class House:
    def __init__(self, rooms, floors, color, garden):
        self.rooms = rooms
        self.floors = floors
        self.color = color
        self.garden = garden

    def __str__(self):
        return f"House with {self.rooms} rooms, {self.floors} floors, {self.color} color and garden: {self.garden}"

    def clone(self):
        return copy.deepcopy(self)


house = House(3, 2, "blue", True)
print(house)
cloned_house = house.clone()
print(cloned_house)
cloned_house.rooms = 4
print(cloned_house)
print(house)

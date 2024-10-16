
# Reuben Hagen
# 11/9/23
# Supplier class to support assignment5 program


from part import Part

class Supplier:
    def __init__(self, name):
        self.name = name
        self.parts = []

    def add_part(self, name, price):
        part_instance = Part(name, price)
        self.parts.append(part_instance)

    def get_price(self, part_name):
        for part in self.parts:
            if part.name == part_name:
                return part.cost
        return None

    def part_exists(self, part_name):
        for part in self.parts:
            if part.name == part_name:
                return True
        return False
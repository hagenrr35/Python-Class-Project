
# Reuben Hagen
# 11/9/23
# Database class to support assignment5 program


class Database:
    def __init__(self):
        self.suppliers = []
    
    def add_supplier(self, supplier):
        self.suppliers.append(supplier)
    
    def find_part(self, part_name):
        lowest_price = float('inf')
        best_supplier = None

        for supplier in self.suppliers:
            if supplier.part_exists(part_name):
                price = supplier.get_price(part_name)
                if price < lowest_price:
                    lowest_price = price
                    best_supplier = supplier.name

        if best_supplier is None:
            return False, False

        return best_supplier, lowest_price


MAX_NUMBERS_ORDERED = 20


class Cart:
    def __init__(self):
        self.items = []

    def add_dvd(self, dvd):
        if len(self.items) > MAX_NUMBERS_ORDERED:
            print("The cart is almost full")
            return False
        self.items.append(dvd)
        print("The disc has been added")
        return True

    def total_cost(self):
        return sum(d.cost for d in self.items)

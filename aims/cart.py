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

    def print_cart(self):
        print("Ordered items:")
        for i, d in enumerate(self.items, 1):
            print(f"{i}. {d.title} - {d.cost}")
        print(f"Total cost: {self.total_cost():.2f} $")

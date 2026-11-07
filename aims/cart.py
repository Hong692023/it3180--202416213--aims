MAX_NUMBERS_ORDERED = 20


class Cart:
    def __init__(self):
        self.items = []

    def add_dvd(self, dvd):
        if len(self.items) >= MAX_NUMBERS_ORDERED:
            print("The cart is almost full")
            return False
        self.items.append(dvd)
        print("Đã thêm đĩa vào giỏ hàng")
        return True

    def total_cost(self):
        return sum(d.cost for d in self.items)

    def print_cart(self):
        if not self.items:
            print("The cart is empty")
            return
        print("Ordered items:")
        for i, d in enumerate(self.items, 1):
            print(f"{i}. {d.title} - {d.cost}")
        print(f"Total cost: {self.total_cost():.2f} $")

    def total_cost_with_discount(self, percent):
        if not 0 <= percent <= 100:
            raise ValueError("percent must be between 0 and 100")
        return self.total_cost() * (100 - percent) / 100

    def sort_by_title(self):
        self.items.sort(key=lambda d: d.title)

    def sort_by_cost(self):
        self.items.sort(key=lambda d: d.cost)

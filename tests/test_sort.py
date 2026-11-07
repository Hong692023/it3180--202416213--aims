import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestSort(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.cart.add_dvd(DigitalVideoDisc("B", cost=30.0))
        self.cart.add_dvd(DigitalVideoDisc("A", cost=20.0))
        self.cart.add_dvd(DigitalVideoDisc("C", cost=10.0))

    def test_sort_by_title(self):
        self.cart.sort_by_title()
        self.assertEqual([d.title for d in self.cart.items], ["A", "B", "C"])

    def test_sort_by_cost(self):
        self.cart.sort_by_cost()
        self.assertEqual([d.cost for d in self.cart.items], [10.0, 20.0, 30.0])


if __name__ == "__main__":
    unittest.main()

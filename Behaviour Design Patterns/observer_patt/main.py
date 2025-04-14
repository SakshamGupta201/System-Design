class Order:
    def __init__(self, value, is_placed=True):
        self.value = value
        self.is_placed = is_placed

class Driver:
    def __init__(self, name: str):
        self.name = name

    def update(self, order: Order):
        print("Order changed", order.value)


class FoodDelivery:

    def __init__(self):
        self._orders: list[Order] = []
        self._drivers = []

    def add_order(self, order: Order):
        """Add order to the list of observers"""
        self._orders.append(order)
        self.notify_drivers(order)

    def delete_order(self, order: Order):
        """Delete order to the list of observers"""

        order.is_placed = False
        self.notify_drivers(order)
        self._orders.remove(order)

    def notify_drivers(self, order):
        """Notify all drivers about the ride request."""
        for driver in self._drivers:
            driver.update(order)

    def add_driver(self, driver):
        """Add a driver to the list of observers."""
        self._drivers.append(driver)

    def remove_driver(self, driver):
        """Remove a driver from the list of observers."""
        self._drivers.remove(driver)


d1 = Driver("A")
d2 = Driver("B")
d3 = Driver("C")

fd = FoodDelivery()
fd.add_driver(d1)
fd.add_driver(d2)
fd.add_driver(d3)

order1 = Order("Pulao")

fd.add_order(order1)
fd.delete_order(order1)

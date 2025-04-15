class MenuItem:
    def __init__(self, name: str, price: str):
        self.name = name
        self.price = price

    def display(self):
        print(f"Item: {self.name}, Price: ${self.price}")


class MenuCategory:
    def __init__(self, name: str):
        self.name = name
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def display(self):
        print(f"Category Name {self.name}")
        for item in self.items:
            if isinstance(item, MenuItem):
                item.display()
            elif isinstance(item, MenuCategory):
                item.display()


burger = MenuItem("Burger", 5)
pizza = MenuItem("Pizza", 8)
main_course = MenuCategory("Main Course")
main_course.add_item(burger)
main_course.add_item(pizza)
desserts = MenuCategory("Desserts")
desserts.add_item(MenuItem("Ice Cream", 3))
menu = MenuCategory("Full Menu")
menu.add_item(main_course)
menu.add_item(desserts)
menu.display()

from abc import ABC, abstractmethod
from typing import List


class MenuComponent(ABC):
    @abstractmethod
    def display(self):
        pass


class MenuItem(MenuComponent):
    def __init__(self, name: str, price: str):
        self.name = name
        self.price = price

    def display(self):
        print(f"Item: {self.name}, Price: ${self.price}")


class MenuCategory:
    def __init__(self, name: str):
        self.name = name
        self.components: List[MenuComponent] = []

    def add_component(self, component):
        self.components.append(component)

    def display(self):
        print(f"Category: {self.name}")
        for component in self.components:
            component.display()

burger = MenuItem("Burger", 5)
pizza = MenuItem("Pizza", 8)

main_course = MenuCategory("Main Course")
main_course.add_component(burger)
main_course.add_component(pizza)

desserts = MenuCategory("Desserts")
desserts.add_component(MenuItem("Ice Cream", 3))

menu = MenuCategory("Full Menu")
menu.add_component(main_course)
menu.add_component(desserts)

menu.display()

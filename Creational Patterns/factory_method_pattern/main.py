from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        print("Drawing a Circle")


class Square(Shape):
    def draw(self):
        print("Drawing a Square")


class ShapeFactory(ABC):
    @abstractmethod
    def create_shape(self) -> Shape:
        pass

    def render(self) -> None:
        shape = self.create_shape()
        shape.draw()


class CircleFactory(ShapeFactory):
    def create_shape(self):
        return Circle()


class SquareFactory(ShapeFactory):
    def create_shape(self):
        return Square()


creator = CircleFactory()
creator.render()

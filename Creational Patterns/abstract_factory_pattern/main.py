from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def render(self):
        pass


class Checkbox(ABC):
    @abstractmethod
    def render(self):
        pass


class WindowsButton(Button):
    def render(self):
        print("Rendering a Windows-style button")


class WindowsCheckbox(Checkbox):
    def render(self):
        print("Rendering a Windows-style checkbox")


class MacOSButton(Button):
    def render(self):
        print("Rendering a MacOS-style button")


class MacOSCheckbox(Checkbox):
    def render(self):
        print("Rendering a MacOS-style checkbox")


class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


class WindowFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()


class MacOSFactory(GUIFactory):
    def create_button(self):
        return MacOSButton()

    def create_checkbox(self):
        return MacOSCheckbox()


def client_code(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()

    button.render()
    checkbox.render()


factory = WindowFactory()
client_code(factory)

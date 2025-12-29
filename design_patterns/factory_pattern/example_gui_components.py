from abc import ABC, abstractmethod

# Abstract Products
class Button(ABC):
    @abstractmethod
    def render(self):
        pass

class Checkbox(ABC):
    @abstractmethod
    def render(self):
        pass

# Concrete Products - Windows
class WindowsButton(Button):
    def render(self):
        return "Rendering Windows Button"

class WindowsCheckbox(Checkbox):
    def render(self):
        return "Rendering Windows Checkbox"

# Concrete Products -  Mac
class MacButton(Button):
    def render(self):
        return "Rendering Mac Button"

class MacCheckbox(Checkbox):
    def render(self):
        return "Rendering Mac Checkbox"

# Abstract factory
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass

# Concrete Factories
class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()

class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()

# Usage
def create_ui(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    print(button.render())
    print(checkbox.render())

windows_factory = WindowsFactory()
create_ui(windows_factory)

mac_factory = MacFactory()
create_ui(mac_factory)

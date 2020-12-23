
from abc import ABC
from typing import Optional


class Drawer(ABC):
    def draw(self, text):
        print(self.base_str.format(text))


class CircleDrawer(Drawer):
    shape = "circle"
    def __init__(self) -> None:
        super().__init__()
        # do a lot of things
        # many things
        self.base_str = "({})"


class SquareDrawer(Drawer):
    shape = "square"
    def __init__(self) -> None:
        super().__init__()
        # so many complicated things
        # random
        # important
        self.base_str = "[{}]"


class CurlyDrawer(Drawer):
    shape = "curly"
    def __init__(self) -> None:
        super().__init__()
        # necessary
        # other thing
        # another one
        self.base_str = "{{{}}}"


def DrawerFactory(chosen_shape) -> Optional[Drawer]:
    drawer = None
    for drawer_class in Drawer.__subclasses__():
        if drawer_class.shape == chosen_shape:
            drawer = drawer_class()
            break
    return drawer


if __name__ == "__main__":
    info = "curly"
    data = 666
    my_drawer = DrawerFactory(info)
    if my_drawer:
        my_drawer.draw(data)
    else:
        raise ValueError(f"Could not find {info}.")
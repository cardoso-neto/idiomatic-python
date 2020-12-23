
# abstract base class
from abc import ABC
from typing import Optional


class Drawer(ABC):
    def draw(self, text):
        print(self.base_str.format(text))


class CircleDrawer(Drawer):
    def __init__(self) -> None:
        super().__init__()
        # do a lot of things
        # many things
        self.base_str = "({})"


class SquareDrawer(Drawer):
    def __init__(self) -> None:
        super().__init__()
        # so many complicated things
        # random
        # important
        self.base_str = "[{}]"


class CurlyDrawer(Drawer):
    def __init__(self) -> None:
        super().__init__()
        # necessary
        # other thing
        # another one
        self.base_str = "{{{}}}"


def DrawerFactory(info) -> Optional[Drawer]:
    drawer = None
    if info == "circle":
        drawer = CircleDrawer()
    elif info == "square":
        drawer = SquareDrawer()
    elif info == "curly":
        drawer = CurlyDrawer()
    return drawer


if __name__ == "__main__":
    info = "curly"
    data = 666
    my_drawer = DrawerFactory(info)
    if my_drawer:
        my_drawer.draw(data)
    else:
        raise ValueError(f"Could not find {info}.")
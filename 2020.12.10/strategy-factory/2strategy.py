
class Drawer():
    def __init__(self) -> None:
        super().__init__()
        self.base_str = "{}"

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


if __name__ == "__main__":
    info = "circle"
    data = 666

    if info == "circle":
        CircleDrawer().draw(data)
    elif info == "square":
        SquareDrawer().draw(data)
    elif info == "curly":
        CurlyDrawer().draw(data)
    else:
        Drawer().draw(data)
    
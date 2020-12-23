
class Bazinga:
    def __init__(self) -> None:
        super().__init__()
        self.a = 0
        self.__banana = "secret"
    
    def get_banana(self):
        return self.__banana


if __name__ == "__main__":
    bazi = Bazinga()
    print(bazi.get_banana())
    # secret
    print(bazi.__banana)
    # AttributeError: 'Bazinga' object has no attribute '__banana'
    print(dir(bazi))
    # ['_Bazinga__banana',
    # '__class__', '__delattr__', '__dict__', '__dir__', ...,
    #  'a', 'get_banana']

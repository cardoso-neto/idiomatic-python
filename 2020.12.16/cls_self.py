import re
from pathlib import Path


class Scraper:
    url_regex = r"https?://.*.org/"  # matches supported sites or something
    def __init__(self, url: str) -> None:
        super().__init__()
        self.url = url

    def pretty_print(self):
        print(f"This is what we want: {self.url}")

    # bad
    def get_regex_times_two(self):
        two_regex = self.url_regex + self.url_regex
        return two_regex

    # good
    @classmethod
    def get_regex_times_two(cls):
        two_regex = cls.url_regex + cls.url_regex
        return two_regex

    @classmethod
    def from_unknown_url(cls, url: str) -> "Scraper":
        if re.match(cls.url_regex, url):
            return cls(url)
        else:
            raise ValueError

    @classmethod
    def from_base64(cls, url: bytes):
        # convert from base64
        return cls(url)

    @classmethod
    def from_local(cls, url: Path):
        # safety checks, get absolute path, etc
        return cls(f"file://{url}")


if __name__ == "__main__":
    my_scraper = Scraper("www.methodistchurch.org")
    safe_scraper = Scraper.from_unknown_url('https://boards.4chan.org/hr/thread/3874020/traditional-western-architecture')
    local_scraper = Scraper.from_local("/home/john/file.jpg")

    print(my_scraper.url)  # instância
    my_scraper.pretty_print()  # instância
    print(Scraper.url_regex)  # classe

    exit()
    # errors
    print(Scraper.url)
    # AttributeError: type object 'Scraper' has no attribute 'url'
    print(Scraper.pretty_print())
    # TypeError: pretty_print() missing 1 required positional argument: 'self'

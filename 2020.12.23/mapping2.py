from typing import Iterator, List

# run create_large_file.sh first
file_handler = open("large-file.dump")  # lazy
exit()
# consumes the iterator, loads all data into RAM
file_handler = open("large-file.dump").read()

# list comprehension
list_of_lines: List[str] = [x for x in file_handler]
# generator expression
uppercase_lines: Iterator[str] = (x.upper() for x in file_handler)


def parse(line: str) -> str:
    new_line = line.strip("\n")
    new_line = new_line.replace("S", "Σ")
    new_line = f"{new_line}\t{len(new_line)}"
    return new_line


if __name__ == "__main__":
    parsed_lines = map(parse, uppercase_lines)
    print(parsed_lines)
    # <map object at 0x7fbf128f8130>

    first_line = next(parsed_lines)
    print(first_line)
    # Some text       9

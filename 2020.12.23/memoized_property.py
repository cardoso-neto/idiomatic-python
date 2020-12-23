from functools import cached_property


def apply_one_hot_encoding():
    pass


class DataSet:
    def __init__(self, datarow):
        self.datarow = datarow
    
    @cached_property
    def is_classification(self) -> bool:
        return any(isinstance(x, str) for x in self.datarow)



if __name__ == "__main__":
    data = DataSet([3500, 14000, 28000, 6000])
    
    data_type = "discrete" if data.is_classification else "continuous"
    print(f"Data is {data_type}.")

    if data.is_classification:
        data = apply_one_hot_encoding(data)

    # data.is_classification runs only once

    print(data.is_classification())
    # TypeError: 'bool' object is not callable
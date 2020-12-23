import statistics


class DataSet:
    def __init__(self, datarow):
        self.datarow = datarow
        self.minimum = min(datarow)
        self.maximum = max(datarow)
    
    @property
    def is_classification(self) -> bool:
        # heavy calculation using self.datarow
        return True

    @property
    def stdev(self):
        return statistics.stdev(self.datarow)

    @property
    def variance(self):
        return statistics.variance(self.datarow)


if __name__ == "__main__":
    data = DataSet([3500, 14000, 28000, 6000])
    my_salary = data.minimum
    # stdev = data.stdev()  # no need to use the parentheses anymore

    if data.stdev > 3:
        print("Unfair salaries detected. Start socialist revolution.")
    
    # if we add more values, the stdev will update, because despite looking
    # like an attribute, it's a method and that method will run whenever
    # we try to access the attribute
    data.datarow += [5000, 6000]
    print(data.stdev)

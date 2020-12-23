
# name mangling, rarely used, becomes _ClassName__attribute
# see mangling.py
self.__attribute = 1

# can't be imported with __all__, i.e., from module import *
# see module1.py for the definitions and main.py for the experiment
def _hidden_function(): ...

# convention only, see PEP8
# implies this attribute is used only within a class
# and that messing around with may induce errors
self._private_attribute = 1

# trailing underscore, avoids conflicts
class_, cls_, def_ = ...
class, cls, def = ...

# special behaviors, syntactic sugar, overloading operators
def __magic_methods__(self): ... 
# e.g.:
obj.__eq__(other)       obj == other
obj.__le__(other)       obj <= other
obj.__hash__            hash(obj)
obj.__str__()           str(obj)
obj.__init__()          obj()
obj.__repr__()          repr(obj), f"{obj!r}"
obj.__delattr__("attr") delattr(obj, "attr")
...

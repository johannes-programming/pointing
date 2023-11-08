import dataclasses as _dataclasses


class _pointclass:
    @classmethod
    def deltaclass(cls):
        return cls._deltaclass
    def __post_init__(self, *args, **kwargs):
        if type(self.delta_from_origin) is not self.deltaclass():
            msg = f"{self.delta_from_origin} is not an instance of {self.deltaclass()}."
            raise TypeError(msg)
    def __add__(self, other):
        cls = type(self)
        delta = self.delta_from_origin + other
        return cls(delta)
    def __radd__(self, other):
        cls = type(self)
        delta = other + self.delta_from_origin
        return cls(delta)
    def __sub__(self, other):
        cls = type(self)
        if type(other) is cls:
            return self.delta_from_origin - other.delta_from_origin
        else:
            return cls(self.delta_from_origin - other)

def pointclass(typename, deltaclass):
    baseclass = type(typename, (_pointclass,), {})
    baseclass.delta_from_origin = _dataclasses.field(default_factory=deltaclass)
    baseclass.__annotations__['delta_from_origin'] = deltaclass
    baseclass._deltaclass = deltaclass
    ans = _dataclasses.dataclass(baseclass)
    return ans

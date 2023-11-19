import collections as _collections
import dataclasses as _dataclasses
import typing as _typing


class _Empty:
    pass

class _pointclass:
    @classmethod
    def deltaclass(cls):
        return cls._deltaclass
    @property
    def delta_from_origin(self):
        return self._delta_from_origin
    def __eq__(self, other):
        cls = type(self)
        if type(other) is not cls:
            return False
        return self.delta_from_origin == other.delta_from_origin
    def __hash__(self):
        return self.delta_from_origin.__hash__()
    def __init__(cls, *args, **kwargs):
        delta = cls.deltaclass()(*args, **kwargs)
        self._delta_from_origin = delta
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
    return type(typename, (_pointclass,), {'_deltaclass':deltaclass})
from enum import Enum


def patch_reprs() -> None:
    _patch_enum()


def _patch_enum() -> None:
    Enum.__repr__ = lambda self: f"{self.__class__.__name__}.{self.name}"

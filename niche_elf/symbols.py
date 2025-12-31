"""Exposes the Symbol dataclass."""

from __future__ import annotations

from dataclasses import dataclass
from typing import cast

from elftools.elf.enums import ENUM_ST_INFO_BIND, ENUM_ST_INFO_TYPE


@dataclass
class Symbol:
    """Represents a symbol (function or global variable) in the binary."""

    name: str
    bind: int
    typ: int
    size: int = 8
    value: int = 0

    @classmethod
    def function(cls, name: str) -> Symbol:
        return cls(
            name=name,
            bind=cast("int", ENUM_ST_INFO_BIND["STB_GLOBAL"]),
            typ=cast("int", ENUM_ST_INFO_TYPE["STT_FUNC"]),
        )

    @classmethod
    def object(cls, name: str) -> Symbol:
        return cls(
            name=name,
            bind=cast("int", ENUM_ST_INFO_BIND["STB_GLOBAL"]),
            typ=cast("int", ENUM_ST_INFO_TYPE["STT_OBJECT"]),
        )

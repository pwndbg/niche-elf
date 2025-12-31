from dataclasses import dataclass
from elftools.elf.enums import ENUM_ST_INFO_BIND, ENUM_ST_INFO_TYPE


@dataclass
class Symbol:
    name: str
    bind: int
    typ: int
    size: int = 0
    value: int = 0

    @classmethod
    def function(cls, name):
        return cls(
            name=name,
            bind=ENUM_ST_INFO_BIND["STB_GLOBAL"],
            typ=ENUM_ST_INFO_TYPE["STT_FUNC"],
        )

    @classmethod
    def object(cls, name):
        return cls(
            name=name,
            bind=ENUM_ST_INFO_BIND["STB_GLOBAL"],
            typ=ENUM_ST_INFO_TYPE["STT_OBJECT"],
        )

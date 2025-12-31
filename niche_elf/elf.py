import struct
from elftools.elf.constants import SH_TYPE, SH_FLAGS
from elftools.elf.enums import ENUM_E_TYPE, ENUM_E_MACHINE
from .writer import ELFWriter
from .symbols import Symbol

class ELFFile:
    def __init__(self, arch="x86_64"):
        self.arch = arch
        self.symbols: list[Symbol] = []
        self.text = b"\x90\x90\x90"

    def add_function(self, name):
        self.symbols.append(Symbol.function(name))

    def add_object(self, name):
        self.symbols.append(Symbol.object(name))

    def write(self, path: str):
        writer = ELFWriter()

        writer.add_text_section(self.text)
        writer.add_symbols(self.symbols)

        writer.write(path)

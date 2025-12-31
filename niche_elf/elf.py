"""The main library entrypoint."""

from .structures import Symbol
from .writer import ELFWriter


class ELFFile:
    """Represents an ELF file (public API)."""

    def __init__(self, arch: str = "x86_64") -> None:
        self.arch = arch
        self.symbols: list[Symbol] = []
        self.text = b"\x90\x90\x90"

    def add_symbol(self, name: str, addr: int) -> None:
        self.symbols.append(Symbol.generic(name, addr))

    def write(self, path: str) -> None:
        writer = ELFWriter()

        writer.add_text_section(self.text)
        writer.add_symbols(self.symbols)

        writer.write(path)

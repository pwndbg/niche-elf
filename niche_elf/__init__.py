"""The niche-elf library."""

from .elf import ELFFile
from .structures import Symbol

__all__ = ["ELFFile", "Symbol"]

# https://refspecs.linuxbase.org/elf/elf.pdf

from niche_elf import ELFFile

elf = ELFFile()
elf.add_function("handler")
elf.add_object("state")
elf.write("symbols.o")

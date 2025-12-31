from niche_elf import ELFFile

elf = ELFFile()
elf.add_symbol("mycoolhandler", 0x1337)
elf.add_symbol("mycoolvariable", 0x1448)
elf.write("symbols.o")

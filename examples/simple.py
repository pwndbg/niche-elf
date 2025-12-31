from niche_elf import ELFFile

elf = ELFFile()
elf.add_function("mycoolhandler")
elf.add_global("mycoolvariable")
elf.write("symbols.o")

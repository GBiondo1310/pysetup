if __name__ == "__main__":
    from os import listdir
    from . import structure_parser as sp
    from .files import STRUCT

    if "struct.json" not in listdir():
        with open("struct.json", mode="w") as struct_file:
            struct_file.write(STRUCT)
        print("File struct.json created, please edit it according to your needs")
    else:
        struct = sp.read_struct()
        sp.build_base(struct)
        sp.install_dependencies(struct)

        bm = sp.ModulesBuilder()
        bm.structure = struct
        bm.initialize(struct)
        bm.build_modules_structure()

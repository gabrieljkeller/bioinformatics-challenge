from gemmi import cif
import os

def parse():
    for filename in os.listdir("resources/cif"):
        doc = cif.read_file(f"resources/cif/{filename}")

from gemmi import cif
from collections import Counter
import os

def parse():
    totals = Counter()

    for filename in os.listdir("resources/cif"):
        doc = cif.read_file(f"resources/cif/{filename}")
        block = doc.sole_block()

        ### Code from https://gemmi.readthedocs.io/en/latest/cif.html#amino-acid-frequency
        # find table with the sequence
        seq = block.find('_entity_poly_seq.', ['entity_id', 'mon_id'])
        # convert table with chain types (protein/DNA/RNA) to dict
        entity_types = dict(block.find('_entity_poly.', ['entity_id', 'type']))
        # and count these monomers that correspond to a protein chain
        aa_counter = Counter(row.str(1) for row in seq
                             if 'polypeptide' in entity_types[row.str(0)])

        totals += aa_counter
        ###

    return totals
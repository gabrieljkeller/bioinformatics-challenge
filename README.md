# Bioinformatics Challenge
A Python script that displays statistics about the amino acids processed from a file of PDB IDs

## Usage
`python3 src/main.py --pdb_file ./resources/file.txt`

where `./resources/file.txt` is the relative path to the file to parse

`python3 src/main.py`

where cif files are already loaded in `resources/cif`

## Dependencies
- requests (2.26.0)
- matplotlib (3.5.1)
- gemmi (0.5.1)
- argparse (1.4.0)

## License
Work in the `src` directory is licensed under the MIT License, found in the LICENSE.txt file
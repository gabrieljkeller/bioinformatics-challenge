import argparse
import os
import sys
import cif_downloader
import gemmi_parser
import aa_plotter

def download_files(args):
    if not args.pdb_file:
        print("Error: Argument --pdb_file must be set to download cif files", file=sys.stderr)
        sys.exit(1)

    print(f"Downloading mmCIF files from PDB IDs located in {args.pdb_file}")
    cif_downloader.download_from_file(args.pdb_file)
    print("Done")


def check_directories():
    if not os.path.isdir("resources/cif"):
        if not os.path.isdir("resources"):
            os.mkdir("resources")
        os.mkdir("resources/cif")


if __name__ == '__main__':
    # Parse CLI args
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdb_file", type=str, required=False, help="relative path to text file with pdb ids")
    args = parser.parse_args()

    # Download cif files
    check_directories()
    if len(os.listdir("resources/cif")) > 0:
        if args.pdb_file:
            decision = input('''resources/cif is not empty. Would you like to skip downloading new cif files?
            1 or enter: continue without downloading
            2: download cif files
            3: clear cif folder then download cif files
            > ''')
            if decision.isdigit():
                decision = int(decision)
                if decision == 2:
                    download_files(args)
                elif decision == 3:
                    for f in os.path.listdir("resources/cif"):
                        os.remove(os.path.join("resources/cif", f))
                    download_files(args)
    else:
        download_files(args)

    # Parse cif fies using Gemmi
    print("Counting amino acids...")
    totals = gemmi_parser.parse()
    f = 100.0 / sum(totals.values())
    print("Done")
    print('TOTAL', *(f"{m}: {c} (%.2f%%)" % (c*f) for (m, c) in totals.most_common()))

    # Plot amino acids
    print("Plotting amino acid counts...")
    aa_plotter.plot_amino_acids(totals)



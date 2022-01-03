import argparse
import cif_downloader
import gemmi_parser

if __name__ == '__main__':
    # Parse CLI args
    parser = argparse.ArgumentParser()
    parser.add_argument("pdb_file", type=str, help="relative path to text file with pdb ids")
    args = parser.parse_args()

    # # Download cif files
    # print(f"Downloading mmCIF files from PDB IDs located in {args.pdb_file}")
    # cif_downloader.download_from_file(args.pdb_file)
    # print("Done")

    # Parse cif fies using Gemmi
    gemmi_parser.parse()




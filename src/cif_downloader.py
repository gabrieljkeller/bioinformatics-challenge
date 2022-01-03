import requests
import os


def download_from_file(file_name):
    if not os.path.isdir("resources/cif"):
        os.mkdir("resources/cif")

    with open(file_name, "r") as file:
        total_lines = sum(1 for line in file)
        i = 0
        file.seek(0)

        for line in file:
            line = line.strip()
            i += 1
            print(f"Downloading file for PDB ID {line}... ({i}/{total_lines}")
            download_cif(line)


def download_cif(pdb_id):
    request = requests.get(f"https://files.rcsb.org/view/{pdb_id}.cif", allow_redirects=True)
    with open(f"resources/cif/{pdb_id}.cif", "wb+") as file:
        file.write(request.content)

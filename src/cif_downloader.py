import requests


def download_from_file(file_name):
    with open(file_name, "r") as file:
        total_lines = sum(1 for line in file)
        i = 0
        file.seek(0)

        for line in file:
            line = line.strip()
            i += 1
            print(f"Downloading cif for {line}... ({i}/{total_lines})")
            download_cif(line)


def download_cif(pdb_id):
    request = requests.get(f"https://files.rcsb.org/download/{pdb_id}.cif.gz", allow_redirects=True)
    with open(f"resources/cif/{pdb_id}.cif.gz", "wb+") as file:
        file.write(request.content)

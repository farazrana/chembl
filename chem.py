from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Draw


def main():
    read_desi_method()


def read_desi_method():
    with open('aspirin.txt', 'r') as file:
        data = file.read()

    print(data)


if __name__ == '__main__':
    mnn
# -*- coding: utf-8 -*-
"""
Created on Wed May 31 11:20:03 2023

@author: student
"""
from Bio import PDB

kodpdb=input("Podaj kod PDB")

struktura=plik=PDB.PDBList().retrieve_pdb_file(kodpdb, pdir=".", file_format="pdb", overwrite=True)

struktura=PDB.PDBParser().get_structure('id=kodpdb',file=plik)

print("Struktura białka nazywa się "+struktura.header['name']+'.')
print("Publikacja została opublikowana "+struktura.header['release_date']+'.')
print("Nazwa białka to "+struktura.header['compound'] ['1'] ['molecule']+'.')

if nmr in metoda
    print(struktura.header['liczba modeli' + "model"])
    print (struktura.header)
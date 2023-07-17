# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 11:26:07 2023

@author: student
"""

print('Program analizuje plik PDB na podstawie podanego PDB')

from Bio import PDB

kod = input('Podaj kod PDB\n')

getit = PDB.PDBList()


readit = PDB.PDBParser()

pdbanaliza_plik = getit.retrieve_pdb_file(kod, pdir=".", file_format="pdb", overwrite=True)

struktura = readit.get_structure(id = kod, file = pdbanaliza_plik)

print("Struktura to %s\n" % (struktura.header["name"]))

print("Metoda eksperymentalna to %s\n" % (struktura.header["structure_method"]))
if "x-ray" in struktura.header["structure_method"]:

    print("Rozdzielczosc to: %s\n" % (struktura.header["resolution"]))
        
else:
        
    print("Ilosc modeli to: %s\n" % (len(struktura)))
                    
print(struktura.header["compound"]["1"]["molecule"])

struktura[0]["A"][1].child_list





# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 11:23:28 2023

@author: student
"""

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

print("Opublikowane w: %s\n" % ((struktura.header["journal"])).title)

print("Struktura składa się z łańcuchów: %s\n" % (len(struktura[0].child_list)))

atom1 = 0

atom2 = 0

liczba_wody = 0

liczba_aminokwasow = 0

liczba_ligandow = 0

liczba_cystein = 0

atom1 = struktura[0]["A"].child_list[0]["CA"]

for residue in struktura.get_residues():
    
    if residue.id[0] == 'W':
        
        liczba_wody+=1
    elif residue.id[0] == ' ':
        
        liczba_aminokwasow +=1
        
        atom2 = residue["CA"]
        
    elif residue.id[0][0] == 'H':
        
        liczba_ligandow += 1
    
    elif (residue.resname) == 'CYS':
        
        liczba_cystein += 1\
            
odleglosc = atom1 - atom2
print("liczba wód: %s\n" % liczba_wody)

print("liczba aminokwasów: %s\n" % liczba_aminokwasow)

print("liczba ligandów: %s\n" % liczba_ligandow)

print("liczba cystein: %s\n" % liczba_cystein)

print(atom2)

print("odleglosc wynosi: %s\n" % odleglosc)


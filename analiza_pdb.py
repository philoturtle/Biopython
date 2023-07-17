# -*- coding: utf-8 -*-
"""
Created on Tue May 30 12:29:10 2023

@author: student
"""
print('Program analizuje plik PDB na podstawie podanego PDB')

from Bio import PDB

kod = input('Podaj kod PDB\n')

getit = PDB.PDBList()

getit.retrieve_pdb_file(kod)


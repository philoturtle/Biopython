# -*- coding: utf-8 -*-
"""
Created on Tue May 30 11:42:41 2023

@author: Maria
"""
import sys
def silnia(n):
    if n > 0:
        wynik = n*silnia(n-1)
    elif n < 0:
        sys.exit('Niepoprawny input')
    else:
        wynik = 1
        
    return wynik
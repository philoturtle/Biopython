# -*- coding: utf-8 -*-
"""
Created on Tue May 30 12:07:31 2023

@author: student
"""

from silnia import silnia
n = 49
k = 6
wynik  = silnia(n)/(silnia(k)*silnia(n-k))
print(wynik)
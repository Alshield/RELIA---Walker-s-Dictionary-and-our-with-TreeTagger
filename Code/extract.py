# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 15:23:39 2019

@author: Dao
@arg1 nom : nom du fichier à regarder
@arg2 vers : nom du fichier de retour
Ecrit dans le fichier les caractères après \t
"""


import sys

nom = sys.argv[1]
vers = sys.argv[2]
tab = []

fichier = open(nom,'r', encoding='utf8')
texte = fichier.read()
i = 0
for ligne in texte.split("\n") :
    i = i + 1
    ens = ligne.split("\t")
    print(i)
    if len(ens)>1 and (ens[1]=="NP" or ens[1]=="CD"):
        tab.append(ens[0])
        print(ens[0])
        tab.append("\t")
        tab.append(ens[1])
        tab.append("\t")
        tab.append(ens[0])
        tab.append("\n")
fichier.close()

result = open(vers,'w', encoding='utf8')
for text in tab :
    result.write(text)
result.close()

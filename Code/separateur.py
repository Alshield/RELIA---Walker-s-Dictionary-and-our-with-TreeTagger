
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 15:23:39 2019

@author: Dao
@arg1 nom : nom du fichier à regarder
@arg2 vers : nom du fichier de retour
@arg3 sep : separateur
Ecrit dans le fichier vers le code entre <sep> et </sep> ligne par ligne
"""


import sys


"""
change
enleve les caracteres de forget de phrase
"""
def change(phrase) :
    #forget = ['<emph rend="italic">','</emph>','<xr type="entry">','</xr>','-','[Lat.]']
    forget = ['<emph rend="italic">','</emph>','To ',',']
    #forget = []
    for mot in forget :
        phrase=phrase.replace(mot,"")
    return phrase

nom = sys.argv[1]
vers = sys.argv[2]
sep = sys.argv[3]
tab = []

fichier = open(nom,'r', encoding='utf8')
texte = fichier.read()
for ligne in texte.split("\n") :
    ligne = change(ligne)
    if ("<pos>" not in ligne or "</pos>" not in ligne or "<pos></pos>" in ligne):
        
    
        ens = ligne.split("<"+sep+">")
        if len(ens)>1 :
            mot = ens[1].split("</"+sep+">") 
            if len(mot[0].strip()) != 0:
                tab.append(mot[0])

fichier.close()

result = open(vers,'w', encoding='utf8')
for text in tab :
    result.write(text)
    result.write("\n")
result.close()


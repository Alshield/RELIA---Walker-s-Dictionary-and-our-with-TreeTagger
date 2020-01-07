# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 19:28:03 2019

@author: Dao
@arg1: nom fichier
"""

from nltk.tokenize.treebank import TreebankWordTokenizer, TreebankWordDetokenizer
import sys

nom = sys.argv[1]
fichier = open(nom,'r', encoding='utf8')
texte = fichier.read()
t = TreebankWordTokenizer()
for ligne in texte.split("\n") :
    print(t.tokenize(ligne))
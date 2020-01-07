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
mapping = {
        " THE first letter of the alphabet,":"DT",
        "s.":"NN",
        "adv.":"RB",
        "v. a.":"VB",
        "v. n.":"VB",
        "adj.":"JJ",
        "prep.":"IN",
        "interj.":"UH",
        "conj.":"IN | CC",
        "first person":"VB",
        "art.":"DT",
        "pret.":"VBD",
        "part.":"VBN | VBG",
        "part. pass.":"VBN",
        "irreg. pret.":"VBD",
        "pret. imperfect.":"VBD",
        "part. adv.":"VBD",
        "particle.":"RP",
        "second person":"VB",
        "thrid person":"VBZ",
        "pron.":"PRP",
        "oblique case":"PRP",
        "pron. poss.":"PRP$",
        "pron. pers.":"PRP",
        "A negative or privative termination.":"NAN",
        "impersonal. verb.":"VB",
        "verb imperfect.":"VBD",
        "v. defective.":"VB",
        "contraction.":"NAN",
        "pron. dem.":"PRP",
        "pron. rel.":"PRP",
        "conjunct.":"IN",
        "article.":"DT",
        "pron. reciprocal.":"PRP",
        "An adverbial form of speech.":"RB",
        "plural. pret.":"VBD",
        "v.":"VB",
        "interj.":"UH",
        "accusative.":"WP",
        "genitive.":"WP",
        "solemn nominative plural.":"PRP",
        "part. adj.":"VBD | JJ",
        "pret. part. pass.":"VBD VBN",
        "pret. part.":"VBD VBN | VBG",
        "verb imperfect":"VBD",
        "adj. adv.":"JJ RB",
        "adj. s.":"JJ NN",
        "v. adj. interj.":"VB JJ UH"
        }

fichier = open(nom,'r', encoding='utf8')
texte = fichier.read()
i = 0
for ligne in texte.split("\n") :
    i = i + 1
    ens = ligne.split("\t")
    tab.append(ens[0])
    tab.append("\t")
    if len(ens)>1 :
        print(i)
        tab.append(mapping[ens[1]])
    tab.append("\n")
fichier.close()

result = open(vers,'w', encoding='utf8')
for text in tab :
    result.write(text)
result.close()

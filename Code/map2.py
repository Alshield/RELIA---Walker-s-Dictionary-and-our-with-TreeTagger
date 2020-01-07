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
        "at":"DT",
        "jj-tl":"JJ",
        "vbd":"VBD",
        "v. a.":"VB",
        "nr":"NN",
        "nn":"NN",
        "in" :"IN",
        "jj":"JJ",
        "``":"SENT",
        "''":"SENT",
        "cs":"IN",
        "dti":"DT",
        "." :"SENT",
        ",":"SENT",
        "hvd":"VBD",
        "vbz":"VBZ",
        "cc":"CC",
        "cc-tl":"CC",
        "in-tl":"IN",
        "vbn":"VBN",
        "ben":"VBN",
        "bem":"VB",
        "to":"IN",
        "vb":"VB",
        "rb":"RB",
        "dt":"DT",
        "pps":"PRP",
        "dod" :"VBN",
        "ap"  :"DT",
        "hv" : "VB",
        "dts" :"DT",
        "vbg" :"VBG",
        "ppo" :"PRP",
        "ql"  :"RB",
        "abx":"RB",
        "nn-hl":"NN",
        "vbn-hl":"VBN",
        "md":  "VBD",
        "be" : "VB",
        "vbg-tl":"VBG",
        "bez":"VBZ",
        "nn$-tl":"NN",
        "hvz":"VBZ",
        "abn":"RB",
        "pn":"PRP",
        "ppss":"PRP",
        "pp$":"PRP$",
        "do":"VB",
        "nn$":"NN",
        "wps":"WP",
        "ex":"RB",
        "vb-hl":"VB",
        ":":"SENT",
        "(":"SENT",
        ")":"SENT",
        "'":"SENT",
        "rp":"RP",
        "--":"SENT",
        "bed":"VBD",
        "od":"JJ",
        "beg":"IN | NN",
        "at-hl":"DT",
        "vbg-hl":"VBG",
        "at-tl":"DT",
        "ppl":"PRP",
        "doz":"VBZ",
        "nr$":"NN",
        "dod*":"VBD",
        "bedz*":"VBD",
        ",-hl":"SENT",
        "SENT":"SENT",
         "SENT-hl":"SENT",
        "ppss+bem":"PRP VB",
        "ppss+ber":"PRP VB",
        "md*":"VBD",
        "(-hl*":"SENT",
        ")-hl":"SENT",
        "md-hl":"VBD",
        "vbz-hl":"VBZ",
        "in-hl":"IN",
        "np-tl":"NP",
        "nn-tl":"NP",
        "np$":"NP",
        "nns":"NN",
        "np-tl":"NP",
        "nn-tl":"NP",
        "np":"NP",
        "np$":"NP",
        "rbr":"RB",
        "wdt":"DT",
        "bedz":"VB",
        "ber":"VB",
        "jjt":"JJ",
        "wrb":"RB",
        "cd":"CD",
        "jjr":"JJ",
        "nns-hl":"NN",
        "*":"RB",
        "nns-tl":"NN",
        "nps":"NN",
        "jjs":"JJ",
        "np-hl":"NP",
        "nns$":"NN",
        "np$":"NP",
        "cd-tl":"CD",
        "rbt":"JJ",
        #fichier cp28
        "ppss+md":"PRP VBD",
        "pps+md":"PRP VBD",
        "dt+md":"DT VBD",
        "qlp":"RB",
        "hvg":"VB",
        "hvn":"VBN",
        "pp$$":"PRP$",
        "pps+hvd":"PRP VBD",
        "hvd*":"VBD",
        "pps+bez":"PRP VBZ",
        "bed*":"VBD",
        "ppls":"PRP",
        "uh":"UH",
        #fichier cp29
        "ppss+hv":"PRP VB",
        "bez*":"VB",
        "abl":"RB",
        "wp$":"WP",
        "nps-tl":"NN",
        "nps$":"NN",
        "do*":"VB",
        "doz*":"VBZ",
        "ex+bez":"RB VBZ",
        "vb+ppo":"VB PRP",
        #fichier cr01
        "ber*":"VB",
        "np$-tl":"NP",
        "np$-hl":"NP",
        "jj-hl":"JJ",
        "dt-hl":"DT",
        "fw-nns":"NN", #Par defaut, fw = foreign word
        #fichier cr02
        "rb+bez":"RB VBZ",
        "wpo":"WP",
        "wps-tl":"WP",
        "do-tl":"VB",
        #fichier cr03
        "dt-tl":"DT",
        "fw-nn":"NN",
        "fw-*":"NN", #Par defautl, fw = foreign word
        "fw-jj":"JJ",
        #fichier cr04
        "pn$":"PRP",
        "wps+md":"WP VBD",
        "nn+hvz":"NN VBZ",
        "nn+bez":"NN VBZ",
        "md+to":"VBD IN",
        "dt+bez":"DT VBZ",
        "ex+md":"RB VBD",

        #fichier cr05
        "wdt+bez":"DT VBZ",
        "dtx":"DT",
        "wps+bez":"WP VBZ",
        "pps+hvz":"PRP VBZ",
        #fichier cr06
        "jjt-tl":"JJ",
        "jj-nc":"JJ",
        "hvz*":"VBZ",
        "fw-rb":"RB",
        "fw-np":"NP",
        "fw-vb":"VB",
        "fw-vbg":"VBG",
        "fw-bez":"VBZ",
        #fichier cr07
        "np+bez":"NP VBZ",
        "rb$":"RB",
        #fichier cr08
        "fw-in":"IN",
        "fw-at-tl":"DT",
        "fw-in+at-tl":"IN DT",
        "nn-nc":"NN",
        "fw-vb-nc":"VB",
        "fw-nn-nc":"NN",
        "vbn-tl":"VBN",
        "pp$-tl":"PRP",
        "fw-vbn":"VBN",
        "fw-nns-tl":"NN"
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

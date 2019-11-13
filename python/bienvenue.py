#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 13:15:15 2019

@author: pauline
"""

print("Bonjour et bienvenu dans l'atelier d'introduction à Python de ElleCode !")
prenom = input('Comment t\'appelles-tu? ')
print("Ravie de faire ta connaissance", prenom)
reponse = input('Passes-tu un bon moment parmi nous? (oui/non) ')
if reponse == 'oui':
    print('Super ! Dans ce cas, à ton tour de jouer et d\'écrire ton propre code.')
else :
    print('Dommage... J\'espère que tu es acceptes tout de même de relever le premier défi.')
print('Le premier défi du jour consiste à écrire un programme qui calcule la somme des nombres d\'une liste, par exemple [2,5,201,32]. ')
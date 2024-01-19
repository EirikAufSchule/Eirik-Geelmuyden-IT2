# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 13:11:53 2022

@author: veghar
"""

lån = 2000000
rente = 0.025
antall_terminer = 25
avdrag = lån/antall_terminer

print("År  Saldo Start  T.beløp  Rente  Restlån")

for i in range(antall_terminer):
    start = lån
    rentebeløp = lån*rente
    terminbeløp = rentebeløp + avdrag
    lån -= avdrag
    print(f"{i+1:2} {start:10.0f} {terminbeløp:10.0f} {rentebeløp:6.0f} {lån:11.2f}")
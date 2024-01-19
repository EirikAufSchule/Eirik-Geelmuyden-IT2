# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 12:13:29 2022

@author: veghar
"""

lån = 3400000
rente = 0.1
antall_terminer = 15
annuitet = (1+rente)*lån*(1/(1+rente)-1)/((1/(1+rente))**antall_terminer-1)

print("For et lån på", lån, "kr over", antall_terminer, "år med", rente*100,"% rente, vil lånevilkårene være som følger\n")
print("Anuuiteten på lånet er", round(annuitet,2), "kr\n")

print("Under ser du en nedbetalingsplan for lånet\n")

print("År  Saldo Start  Avdrag  Rente  Restlån")

for i in range(antall_terminer):
    start = lån
    rentebeløp = lån*rente
    avdrag = annuitet - rentebeløp
    lån = lån - avdrag
    print(f"{i+1:2} {start:10.0f} {avdrag:9.0f} {rentebeløp:6.0f} {lån:11.2f}")

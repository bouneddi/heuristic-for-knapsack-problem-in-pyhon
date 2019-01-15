# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 11:13:07 2018

@author: dell
"""

import numpy as np
n=int(input())
m=int(input())
#création des listes
c=list()#capacités restant dans le sac(variable)
x=list()#objets
z=list()#profits
w=list()#poids
S=np.zeros((n,m))
Cap=[]#capacités des sacs(cst)

#création des cases des listes initialisées par des 0
for i in range(0,n):
    x.append(i)
    x[i]=0

for i in range(0,m):
    z.append(i)
    z[i]=0

for i in range(0,m):
    c.append(i)
    c[i]=int(input())#faire entrer les valeurs des capacités
    Cap.append(c[i])

u=0
for i in range(0,m):
    u=u+c[i]    

for i in range(0,n):
    w.append(i)
    w[i]=int(input())#faire entrer les valeurs des poids

#remplir les sacs successivement avec les objets classés par ordre décroissant    
i=0    
for j in range(0,m):
    c[i]=c[i]-w[j]
    z[i]=z[i]+w[j]
    x[j]=1
    S[j][i]=1
    i=i+1

#remplir les sacs selon la capacité maximale qui reste 
for j in range(m+1,n):
    i=c.index(max(c))
    if w[j]<=c[i]:
     c[i]=c[i]-w[j]
     z[i]=z[i]+w[j]
     x[j]=1
     S[j][i]=1

#calculer le profit obtenu
Z=0
for i in range(0,m):
    Z=Z+int(z[i])    

#poser une valeur op égale au profit obtenu jusqu'à présent        
Op=Z   

#afficher ce profit ainsi que les objets
print(Z)
print(x)

#création des variables de test     
c_test=int(Cap[0])
z_test=0
S_test=np.zeros(n)#Sac test provisoir 
taboo=np.zeros(n)#Sac taboo des objets rejetés
a=0


def tab():  #chercher le ou les sacs min et mettre leurs objets dans le sac taboo
    global a
    a=min(z)
    for i in range(0,m):
        if z[i]==a:
            for j in range(0,n):
                if S[j][i]==1:
                    taboo[j]=S[j][i]
    return a                

tab()
k=0
while k<n and Z<u:
      
    for j in range(0,n):
        if taboo[j]==0 and x[j]==0:
            if w[j]<=c_test:            #mettre les objets qui ne sont ni
                c_test=c_test-w[j]      #taboo ni pris dans les sacs dans 
                z_test=z_test+w[j]      #un sac test
                S_test[j]=1
    for j in range(0,n):
        if taboo[j]==1:
            if w[j]<=c_test:
                c_test=c_test-w[j]      #ajouter après si c'est possible
                z_test=z_test+w[j]      #les objets taboo 
                S_test[j]=1
    if z_test>a: #au début nous avons pris le cas ou égal mais ceci mène à des alternations entre deux résultats.
        for i in range(0,m):
            if z[i]==a:
                for j in range(0,n):
                    c[i]=Cap[i]
                    z[i]=0
                    if int(S[j][i])==1:
                       x[j]=0
                       S[j][i]=0
                                              
        i=z.index(min(z))
        z[i]=z_test
        c[i]=c_test
        for j in range(0,n):            
            S[j][i]=int(S_test[j])
            if int(S[j][i])==1:
                x[j]=1
                taboo[j]=0
        for j in range(0,n):
            if taboo[j]==1:            #on complète par les objets taboo si possible
                i=c.index(max(c))      #afin d'augmenter le profit global
                if w[j]<=c[i]:         
                    c[i]=c[i]-w[j]
                    z[i]=z[i]+w[j]
                    x[j]=1
                    S[j][i]=1
        Z=0
        for i in range(0,m):
            Z=Z+int(z[i])
            Op=Z
        c_test=int(Cap[0])
        z_test=0
        S_test=np.zeros(n)
        taboo=np.zeros(n)
        tab()
        print(Z)
        print(x)
    else:
        for i in range(0,n):
            if S_test[i]==1:
                taboo[i]=1               #dans le cas contraire on met ces objets
        c_test=int(Cap[0])               #dans le sac taboo et on reprend du début
        z_test=0
        S_test=np.zeros(n)
        tab()
    k=k+1


      
        
                   
                    
                    
                
            
        
               
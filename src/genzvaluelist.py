#!/usr/bin/python
#python calculate.py edgelist singleton_list PCALL 
import sys
import fileinput
import random
hash={}
index = 1 
block = []
import networkx as nx
edgel=[]
G=nx.Graph()

for line in fileinput.FileInput(sys.argv[1]):
    a=line.split('\t')
    d=line.split(' ')

    if len( a) > len(d):
        a = a 
    else:
        a = d

    b=int(a[0])
    c=int(a[1])
    G.add_edge(b,c)
M=set()

for line in fileinput.FileInput(sys.argv[2]):

    a=line.split('\t')
    d=line.split(' ')

    if len( a) > len(d):
        a = a 
    else:
        a = d



    b=int(a[0])
    M.add(b)
   

GT=set()
for line in fileinput.FileInput(sys.argv[3]):
    a=line.split(' ')
    a=line.split('\t')
    d=line.split(' ')

    if len( a) > len(d):
        a = a 
    else:
        a = d
    b=int(a[0])
    
    GT.add(b)
GT=set(G.nodes())
#print edgel
a=M & GT


zvalue={}
for i in a:
    GT.discard(i)
c=0
for i in GT:
    zvalue[i] = 0
    count = 0 
    for j in M:
        if G.has_edge(j,i):
            count = count + 1
    zvalue[i] = count 
    c=c+1


a= list(reversed(sorted (  list(zvalue.values()))))
for i in zvalue.keys():
    print i,'\t',zvalue[i]






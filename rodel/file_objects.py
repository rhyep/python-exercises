# file_objects.py

f=open('file.txt','r')

"""
for L in f:
    print(L)

for G in f:
    print(G[0])

for H in f:
    print(H[0],end="")
    print(H[-2:])

# letters in line
for I in f:
    #print(L)
    for l in I:
        print(l,end="-")
"""

for line in f:
    print((line[0]+line[-2])*int(line[-2]))
    #    print((line[0]+line[-2])*int(line[-2:]))?

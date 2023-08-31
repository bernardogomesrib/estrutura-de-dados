cj1 = {1,2,3,4}
cj2 = {4,5,6,7}

#1
aux = cj1 & cj2
print(aux)
del aux
#2 
aux = cj1 - cj2
print(aux)
del aux
#3
aux = cj2 - cj1
print(aux)
del aux
#4 
aux = cj1 ^ cj2
print(aux)
del aux
#5
aux = cj2 ^ cj1
print(aux)
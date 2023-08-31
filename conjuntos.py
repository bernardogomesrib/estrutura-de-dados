#formas de iniciar um conjunto
f1 = set()
print(f1)
f2 = set(['ab','cd','ef','gh','ij'])
print(f2)
f3 = {'ab','cd','ef','gh','ij','kl','mn'}
lista = list(f3)
print(f3)
print(lista)
#funções com conjuntos - adição de itens
f3.add("boquete")
print(f3)
#união em grupo com outros grupos
f3.update({'palavra','cagada','peido'})
print(f3)
f4 = f3.copy()
print("f3 e f4")
f3.update({'pipipo':'ababa','bebe':'pipo','asa':'aca'}.values())
f4.update({'pipipo':'ababa','bebe':'pipo','asa':'aca'})
print(f3)
print(f4)
#removendo valores 
try:
    f3.remove('asa')
except:
    print("deu erro removendo asa do f3")    
try:
    f4.remove('asa')
except:
    print("deu erro removendo asa do f4")    
try:
    f3.discard('pipipo')
except:
    print("deu erro removendo pipipo do f3")    
try:
    f4.discard('pipipo')
except:
    print("deu erro removendo pipipo do f4")

#esvasiar conjunto 
f4.clear()
#apagando a variavel 
del f4
#união .union() junta dois conjuntos e retorna sem alterar os 2 conjuntos e retorna a união,
#  diferente do update que adciona no conjunto que está utilizando outro conjunto
f4 = f3.copy()
f5 = f3.union(f4)
if f3 == f5:
    print("os dois conjuntos são iguais por não ser possivel ter mais de um elemento duplicado")

print(f'f2: {f2} sem modificações')
for a in f3:
    f2.add(a)
    break;
print(f'f2: {f2} tem um elemento aleatorio do conjunto f3 se for um elemento que não estava em f2 já.')

# interseção entre dois conjuntos é feito com o operador & ou a função intersection
f6 = f2.intersection(f3)
print(f'{f6} é a intersessão entre f2 e f3')
# é possivel fazer update diretamente na variavel que chama a função intersection adcionando _update()
f4.intersection_update(f3)
print(f"{f4} é a intersessão entre f3 e f4")

# o metodo difference() e difference_update() funcionam como intersection mas retornam a diferença entre os 2, reza a lenda que o - também 
# pode ser utilizado
f7 =f6.difference(f3)
print(f'{f6} com a diferença entre dois conjuntos')
#diferença simetrica é a retirada de todos os itens que não estão nos dois conjuntos
f6.difference_update(f3)
print(f"{f6} é a diferença simétrica ou o oposto da intersessão entre f6 e f3")
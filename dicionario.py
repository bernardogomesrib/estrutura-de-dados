dic = {}
dic['a'] =[1,2]
dic['b'] =[2,3]
dic['c'] =[3,4]
dic['d'] =[4,5]
dic['e'] =[5,6]
dic['f'] =[6,7]
c = 0
'''
for a in dic:
    for b in dic[a]:
        print(b)
'''
'''d = {}
for letra in 'estrutura':
    print(letra.toBinary())

'''
for a in dic.keys():
    print(a)
for a in dic.values():
    print(a)
#ATRIBUINDO VALORES AO DICIONARIO USANDO AS CHAVES ATRIBUIDA A UMA VARIAVEL TEMPORARIA
for a in dic:
    dic[a] = ['não','tem','nada','aqui']

print(dic)
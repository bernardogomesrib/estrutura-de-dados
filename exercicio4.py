l = list(map(int,input().split()))
pares = [l[i] for i in range(len(l)) if l[i]%2==0]
impares = [l[i] for i in range(len(l)) if l[i]%2==1]
print("pares:",pares)
print("impares:",impares)
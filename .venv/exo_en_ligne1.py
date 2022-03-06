
nombres = int(input('Entrez de valeur voulu :'))
n1 = 0 
n2 = 1 
total=0
total = n1 + n2

print('les {} premiers nombres sont :'.format(nombres))
list=[n1,n2,total]
cpt=0
while cpt < nombres-3:

    n1=n2
    n2= total
    total=n1 + n2
    list.append(total)    
    cpt+=1

print(list)    
    

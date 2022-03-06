tab = ['abcd', 'addddd','a','fait']

def find_smallest(a_list):
    cpt = 0
    min_index = 0
    while cpt < len(a_list):
        if len(a_list[cpt]) < len(a_list[min_index]):
           min_index = cpt
        cpt = cpt + 1

    return min_index

cpt = 0
while cpt < len(tab):
    index_min = find_smallest(tab[cpt:]) + cpt
    if index_min != cpt:
        temp = tab[index_min]
        tab[index_min] = tab[cpt]  
        tab[cpt] = temp
    cpt +=1
print(tab)   
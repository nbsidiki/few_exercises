"""
exercice_9
"""
def find_smallest(a_list):
    cpt = 0
    min_index = 0
    while cpt < len(a_list):
        if len(maliste[cpt]) < len(maliste[min_index]):
           min_index = cpt
        cpt = cpt + 1

    return min_index

maliste = ['abcdg', 'efg', 'ef', 'x']
le_plus_petit = find_smallest(maliste)
print(maliste[le_plus_petit])
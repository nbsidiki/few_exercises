def find_min_value(a_list):
   
    if len(a_list) == 0:
        return None
    else:    
      min_value = a_list[0]
    cpt = 0
    while cpt < len(a_list):
        if min_value > a_list[cpt]:
           min_value = a_list[cpt]
        cpt = cpt + 1
         
        return min_value

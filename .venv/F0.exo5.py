"""
EXO_5
"""


def matrix(n_l,n_c):
   texte=[] 
   cpt_l = 0
   while cpt_l < n_l:
         cpt_c = 0
         texte1=[]
         while cpt_c< n_c:
              texte1.append(f'{cpt_l}{cpt_c}')
              cpt_c+= 1
         texte.append(texte1)
         cpt_l+= 1 
         
   return texte

print(matrix(3,2))      
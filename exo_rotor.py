alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def decale_lettre(alphabet,lettre, coef):
   new_index = alphabet.index(lettre) + coef

   if new_index >= len(alphabet):
       new_index = new_index - len(alphabet)
   return alphabet[new_index]

print()




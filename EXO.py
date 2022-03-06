alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rotor1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
rotor2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
rotor3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"

def decale_lettre(alphabet,lettre, coef):
   new_index = alphabet.index(lettre) + coef

   if new_index >= len(alphabet):
       new_index = new_index - len(alphabet)
   return alphabet[new_index]



def decode_letter(alphabet,lettre, coef):
    new_index = alphabet.index(lettre) - coef
    if new_index < 0:
       new_index = len(alphabet) + new_index
    return alphabet[new_index]

decoded = (decode_letter(alphabet, 'A',3))
print(f"A --->{decoded}")

def encode_texte(alphabet,texte, coef):
    new_text =" "
    cpt = 0
    while cpt < len(texte) :
        if texte[cpt]==" ":
            new_text = new_text + " "
        else:
            encoded = decale_lettre(alphabet,texte[cpt], coef)
            new_text = new_text + encoded
        cpt +=1 
    return new_text  

encoded = encode_texte(alphabet,"JE SUIS",2)
print(encoded)


 
def decode_texte(alphabet,texte, coef):
    new_text =" "
    cpt = 0
    while cpt < len(texte) :
        if texte[cpt]==" ":
            new_text = new_text + " "
        else:
            decoded = decode_letter(alphabet,texte[cpt], coef)
            new_text = new_text + decoded
        cpt +=1 
    return new_text  

print(decode_texte(alphabet,encoded, 2))    


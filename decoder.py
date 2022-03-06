def encode_rotor(texte, coefs_initiaux):
      
    new_text = " "
    ctp = 0
    while ctp < len(texte):
        coefs_initiaux = turn_rotors(coefs_initiaux)
        if texte[ctp]== " ":
            new_text += " "
        else:
            new_text += encode_letter(texte[ctp] ,coefs_initiaux)
        ctp += 1
    
    return new_text    
    
    
print(encode_rotor('JE SUIS',[3, 2, 1]))    

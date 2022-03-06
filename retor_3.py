ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ROTOR1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
ROTOR2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
ROTOR3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"

def encode_letter_from_rotor(rotor,lettre, coef):
    pos_letter_alphabet = ALPHABET.index(lettre)
    new_index = pos_letter_alphabet + coef

    if new_index >= len(rotor):
       new_index = new_index - len(rotor)
    return rotor[new_index]

encode=(encode_letter_from_rotor(ROTOR1, 'A', 2))   

print(f"A --->{encode} ")

def decode_letter_from_rotor(rotor,lettre, coef):
    pos_letter_alphabet = rotor.index(lettre)
    new_index = pos_letter_alphabet - coef

    if new_index < 0:
       new_index = new_index + len(ALPHABET)
    return ALPHABET[new_index]

decode = (decode_letter_from_rotor(ROTOR1, 'A', 2))    
print(f"A ---> {decode}")


def encode_letter(letter,coef):
    letter= encode_letter_from_rotor(ROTOR1,letter, coef[0])
    letter = encode_letter_from_rotor(ROTOR2, letter,coef[1])
    letter = encode_letter_from_rotor(ROTOR3,letter,coef[2])
    

    return letter

print(encode_letter('A', (0, 1, 0)))

def decode_letter(letter,coef):
    letter= decode_letter_from_rotor(ROTOR1,letter, coef[2])
    letter = decode_letter_from_rotor(ROTOR2, letter,coef[1])
    letter = decode_letter_from_rotor(ROTOR3,letter,coef[0])
    

    return letter

print(decode_letter('R', (0, 1, 0)))

def turn_rotors(rotors_coef):
    ctp = 0
    while ctp < len(rotors_coef):
        if rotors_coef[ctp] +1 < 26:
            rotors_coef[ctp]+=1
            break
        else:
            rotors_coef[ctp]=0
            ctp += 1
                
    return rotors_coef    

result = turn_rotors([25, 25, 0])

print(result)
   

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


def decode_rotor(texte, coefs_initiaux):
      
    new_text = " "
    ctp = 0
    while ctp < len(texte):
        coefs_initiaux = turn_rotors(coefs_initiaux)
        if texte[ctp]== " ":
            new_text += " "
        else:
            new_text += decode_letter_from_rotor(texte[ctp] ,coefs_initiaux)
        ctp += 1
    
    return new_text    
    
    
print(decode_rotor('Ex RNCN',[3, 2, 1]))  


alist=[2, 3, 5]

def find_biggestt(a_list):
    bigest_value = alist[0]
    cpt = 0
    
    while cpt < len(a_list):
        if alist[cpt] > bigest_value:
           bigest_value = alist[cpt]
        cpt = cpt + 1

    return bigest_value
     
print(find_biggestt(alist))
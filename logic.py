import random

def gen_pass(i): #membuat fungsi gen_pass (def = memanggil kode selanjtnya) setalh def ada kurung
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(i):
        password += random.choice(elements)
    
    return password


import string
abecedario = []
abecedario_multiplos = []
for chr in string.ascii_lowercase:
    abecedario.append(chr)
    
for i in abecedario:
    if  abecedario.index(i)% 3 == 0:
        abecedario_multiplos.append(i)

print(abecedario_multiplos)
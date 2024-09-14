entrada = input("Informe uma frase ou palavra: ")

count = 0
for c in entrada:
    if c == "A" or c == "a":
        count+=1

print(f'O caractere a ou A aparece {count} vezes na entrada de dados.')
numbers = [0, 1]

for i in range(1, 100):
    numbers.append(numbers[i-1] + numbers[i])

entrada = input("Número inteiro: ")
entrada_int = int(entrada)

if entrada_int in numbers:
    print(f'O número {entrada_int} pertence a sequência de Fibonacci!')
else:
    print(f'O número {entrada_int} não pertence a sequência de Fibonacci!')

frase = str(input('Digite uma frase: ')).strip().upper()

palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

print('Você digitou a frase {}'.format(frase))

for letra in range(len(junto) - 1, - 1, -1):
    inverso += junto[letra]

print('O inverso de {} é {}'.format(junto, inverso))

if inverso == junto:
    print('A palavra é um palindromo')
else:
    print('A palavra não é um palíndromo')

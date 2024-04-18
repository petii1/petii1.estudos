# Definição da função
def soma(a, b):
    # Dentro da função, podemos usar as variáveis 'a' e 'b' sem problemas.
    resultado = a + b
    return resultado


# Chamada da função
x = 5
y = 3
resultado_soma = soma(x, y)

# Agora, vamos tentar acessar 'resultado', que é uma variável local da função,
# de fora da função.
# Isso causará um erro, pois 'resultado' está definido apenas dentro da função.
print(resultado_soma)

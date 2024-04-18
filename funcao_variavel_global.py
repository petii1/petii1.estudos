# Variável global
numero_global = 10

# Função que multiplica um número global por um parâmetro local


def multiplicar_por_local(numero):
    resultado = numero_global * numero
    return resultado

# Função que subtrai um parâmetro global de um parâmetro local


def subtrair_global_de(local):
    global numero_global
    resultado = local - numero_global
    return resultado

# Função principal que utiliza as outras funções


def main():
    # Variável local à função principal
    valor_local = 5

    # Chamada da função multiplicar_por_local
    resultado_multiplicacao = multiplicar_por_local(valor_local)
    print("Resultado da multiplicação:", resultado_multiplicacao)

    # Chamada da função subtrair_global_de
    resultado_subtracao = subtrair_global_de(resultado_multiplicacao)
    print("Resultado da subtração:", resultado_subtracao)


# Chamada da função principal
main()

# Tentativa de acessar variáveis locais das funções dentro da função principal
# Isso causará um erro, pois as variáveis são locais às funções, não à função principal.
# print(numero)
# print(resultado)

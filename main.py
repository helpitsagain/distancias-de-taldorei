distancia = float(input("Distância no mapa: "))


def distanciasTaldorei(variavel):
    resultado = (200 * variavel) / 16.7
    unidade = str.upper(input("Você quer o resultado em km ou mi? "))
    if unidade == "KM":
        resultado *= 1.60934
        print("A distância real medida no mapa é " + str(int(resultado)) + " km.")
    elif unidade == "MI":
        print("A distância real medida no mapa é " + str(int(resultado)) + " mi.")
    else:
        print("Unidade inválida. Por favor, insira 'km' ou 'mi'.")
    print("")
    continuar = str.upper(input("Deseja calcular outra distância? S/N "))
    if continuar == "S":
        print("")
        distancia = float(input("Distância no mapa: "))
        distanciasTaldorei(distancia)
    else:
        print("")
        print("Obrigado por usar a Calculadora de Distâncias dos Herdeiros de Tal'dorei!")


distanciasTaldorei(distancia)
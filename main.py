
def distancias_taldorei():
    continuar = "S"
    while continuar == "S":

        polegadas = float(input("Distância no mapa: "))
        milhas = round(((200 * polegadas) / 16.7), 2)
        quilometros = round((milhas * 1.60934), 2)
        unidade = str.upper(input("Você quer o resultado em quilômetros (km) ou milhas (mi)? "))

        if unidade == "KM" or unidade == "QUILÔMETROS":
            print(f"A distância real medida no mapa é de {quilometros} km.")
        elif unidade == "MI" or unidade == "MILHAS":
            print(f"A distância real medida no mapa é de {milhas} mi.")
        else:
            print("Unidade inválida. Por favor, insira 'km' ou 'mi'.")

        print("")
        continuar = str.upper(input("Deseja calcular outra distância? S/N "))
        print("")

    print("Obrigado por usar a Calculadora de Distâncias do mapa do roll20 dos Herdeiros de Tal'dorei!")


distancias_taldorei()
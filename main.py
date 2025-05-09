from card_validator import identify_card_brand

def main():
    print(" Identificador de Bandeira de Cartão de Crédito")
    number = input("Digite o número do cartão: ").strip()
    brand = identify_card_brand(number)
    print(f"️  Bandeira identificada: {brand}")

if __name__ == "__main__":
    main()


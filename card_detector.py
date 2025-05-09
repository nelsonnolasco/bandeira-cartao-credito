def get_card_brand(card_number: str) -> str:
    """
    Detecta a bandeira do cartão com base no número.
    Suporta pelo menos 10 bandeiras.
    """

    card_number = card_number.replace(" ", "")

    # Validação básica do número do cartão
    if not card_number.isdigit():
        return "Número inválido"

    brands = {
        "Visa":             lambda n: n.startswith("4"),
        "MasterCard":       lambda n: 51 <= int(n[:2]) <= 55,
        "American Express": lambda n: n.startswith(("34", "37")),
        "Elo":              lambda n: n.startswith(("6362", "4389", "5041", "4011", "4576")),
        "Hipercard":        lambda n: n.startswith("606282"),
        "Discover":         lambda n: n.startswith("6011"),
        "Diners Club":      lambda n: n.startswith(("300", "301", "302", "303", "304", "305", "36", "38")),
        "JCB":              lambda n: n.startswith("35"),
        "Aura":             lambda n: n.startswith("50"),
        "Cabal":            lambda n: n.startswith("6042"),
    }

    for brand, validator in brands.items():
        try:
            if validator(card_number):
                return brand
        except ValueError:
            continue

    return "Bandeira desconhecida"
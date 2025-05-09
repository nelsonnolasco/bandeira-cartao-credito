from card_data import CARD_BRANDS

def identify_card_brand(card_number: str) -> str:
    """Identifica a bandeira do cartão com base em padrões regex."""
    clean_number = ''.join(filter(str.isdigit, card_number))

    for brand in CARD_BRANDS:
        if brand.matches(clean_number):
            return brand.name

    return "Bandeira desconhecida"

import re
from typing import List

class CardBrand:
    def __init__(self, name: str, patterns: List[str]):
        self.name = name
        self.patterns = [re.compile(pattern) for pattern in patterns]

    def matches(self, card_number: str) -> bool:
        return any(pattern.match(card_number) for pattern in self.patterns)

# Lista de bandeiras com seus respectivos padrões em regex
CARD_BRANDS = [
    CardBrand("Visa", [r"^4\d{12}(\d{3})?$"]),
    CardBrand("MasterCard", [r"^5[1-5]\d{14}$", r"^2[2-7]\d{14}$"]),
    CardBrand("American Express", [r"^3[47]\d{13}$"]),
    CardBrand("Diners Club", [r"^3(?:0[0-5]|[68]\d)\d{11}$"]),
    CardBrand("Discover", [r"^6(?:011|5\d{2})\d{12}$"]),
    CardBrand("JCB", [r"^35\d{14}$"]),
    CardBrand("Elo", [r"^(4011|4312|4389|4514|4576|5041|5066|509\d|6277|6362)\d+$"]),
    CardBrand("Hipercard", [r"^606282\d{10}$"]),
    CardBrand("Aura", [r"^50\d{14,17}$"]),
    CardBrand("Cabal", [r"^6042\d{12}$"]),
]

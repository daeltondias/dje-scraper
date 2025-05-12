def parse_valor(valor_str):
    if not valor_str or "sem" in valor_str.lower():
        return 0.0
    valor_str = valor_str.replace('R$', '').replace(' ', '')
    return float(valor_str.replace('.', '').replace(',', '.'))
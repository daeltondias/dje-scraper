from typing import Optional
import re

def converter_data_por_extenso(data_por_extenso: str) -> Optional[str]:
    meses = {
        'janeiro': '01',
        'fevereiro': '02',
        'março': '03',
        'abril': '04',
        'maio': '05',
        'junho': '06',
        'julho': '07',
        'agosto': '08',
        'setembro': '09',
        'outubro': '10',
        'novembro': '11',
        'dezembro': '12',
    }

    match = re.search(r"(\d{1,2}) de (\w+) de (\d{4})", data_por_extenso, re.IGNORECASE)
    if not match:
        return None

    dia = match.group(1).zfill(2)
    mes_nome = match.group(2).lower()
    mes = meses.get(mes_nome)
    ano = match.group(3)

    if not mes:
        return None

    return f"{dia}/{mes}/{ano}"
    
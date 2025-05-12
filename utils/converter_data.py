from datetime import datetime

def converter_data(data_str):
  try:
    meses = {
      'janeiro': 1,
      'fevereiro': 2,
      'março': 3,
      'abril': 4,
      'maio': 5,
      'junho': 6,
      'julho': 7,
      'agosto': 8,
      'setembro': 9,
      'outubro': 10,
      'novembro': 11,
      'dezembro': 12
    }
    
    partes = data_str.lower().split(' de ')
    
    if len(partes) != 3:
      return None

    dia = int(partes[0])
    mes = meses[partes[1]]
    ano = int(partes[2])

    if mes is None:
      return None
    
    return datetime(ano, mes, dia)
  except ValueError:
    return None
    
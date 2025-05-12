from utils.converter_data import converter_data
from playwright.sync_api import sync_playwright
from utils.parse_valor import parse_valor
from datetime import datetime
import fitz
import re

def extrair_publicacoes():
    resultados = []
    with sync_playwright() as p:
        navegador = p.chromium.launch(headless=True)
        pagina = navegador.new_page()
        pagina.goto("https://dje.tjsp.jus.br/cdje/index.do")
        pagina.select_option("select[name='dadosConsulta.cdCaderno']", value="12")
        pagina.fill("input[name='dadosConsulta.pesquisaLivre']", '"RPV" e "pagamento pelo INSS"')
        pagina.click("input[value='Pesquisar']")
        pagina.wait_for_selector("#divResultadosInferior")
        links = pagina.locator("#divResultadosInferior td > a:first-child").all()
        print(f"Número páginas encontradas: {len(links)}")
        for link in links:
            numero_pagina = link.inner_text().split()[-1]
            nova_pagina = navegador.new_page()
            url = f"https://dje.tjsp.jus.br/cdje/getPaginaDoDiario.do?cdVolume=19&nuDiario=4198&cdCaderno=12&nuSeqpagina={numero_pagina}&uuidCaptcha="
            response = nova_pagina.request.get(url)
            pdf_bytes = response.body()
            doc = fitz.open("pdf", stream=pdf_bytes)
            text = ""
            for page in doc:
                text += page.get_text()

            processo = re.search(r"Processo.*?(\d{7}-\d{2}\.\d{4}\.\d\.\d{2}\.\d{4})", text)
            data = re.search(r"Disponibiliza[çc][aã]o.*?(\d{1,2} de .*? de \d{4})", text, re.IGNORECASE)
            autor = re.search(r"Autor(?:\(a\))?:?\s*(.+)", text)
            advogado = re.search(r"Advogado(?:\(a\))?:?\s*(.+)", text)
            honorarios = re.search(r"Honor[aá]rios.*?R\$ ?([\d\.,]+)", text)
            principal = re.search(r"principal.*?R\$ ?([\d\.,]+)", text)
            total = re.search(r"importe total de R\$ ?([\d\.,]+)", text)
            juros = re.search(r"juros morat[oó]rios.*?(sem|R\$ ?[\d\.,]+)", text)

            data_extenso = data.group(1)
            data_convertida = converter_data(data_extenso)
            
            resultados.append({
                "numero_processo": processo.group(1) if processo else None,
                "data_disponibilizacao": data_convertida if data_convertida else None,
                "autores": autor.group(1).strip() if autor else None,
                "advogados": advogado.group(1).strip() if advogado else None,
                "conteudo": text.strip(),
                "valor_bruto": parse_valor(principal.group(1)) if principal else None,
                "valor_liquido": parse_valor(principal.group(1)) if principal else None,
                "valor_juros": parse_valor(juros.group(1)) if juros else 0.0,
                "honorarios": parse_valor(honorarios.group(1)) if honorarios else None
            })
        navegador.close()

    print(f"Número de publicações encontradas: {len(resultados)}")

    return resultados

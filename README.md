# dje-scraper
DJE - Scraper

## Descrição
DJE-Scraper é uma ferramenta para extração automatizada de dados do Diário de Justiça Eletrônico.

## Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/daeltondias/dje-scraper.git
```

2. Navegue até o diretório do projeto:
```bash
cd dje-scraper
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Configuração
1. Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:
```
MONGO_URI=mongodb://localhost:27017
MONGO_DB=dje_db
MONGO_COLLECTION=publicacoes
```

2. Ajuste os parâmetros de busca no arquivo de configuração (se aplicável).

## Uso
Para executar o scraper:
```bash
python main.py
```

### Parâmetros opcionais
- `--data`: Define a data para busca (formato: DD/MM/AAAA)
- `--output`: Define o diretório de saída para os resultados

Exemplo:
```bash
python main.py --data 01/01/2023 --output ./resultados
```

## Estrutura de Arquivos
- `main.py`: Ponto de entrada da aplicação
- `scraper/`: Módulos de extração de dados
- `utils/`: Funções utilitárias

## Solução de Problemas
Se encontrar problemas durante a execução:
1. Verifique sua conexão com a internet
2. Confirme que todas as dependências foram instaladas corretamente
3. Verifique se as credenciais no arquivo `.env` estão corretas

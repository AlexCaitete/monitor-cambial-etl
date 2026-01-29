# 💰 Monitor Cambial ETL

Um pipeline de dados desenvolvido em **Python** para monitorar, extrair e armazenar cotações de moedas em tempo real.

O projeto consome dados da **AwesomeAPI**, processa as informações de Dólar (USD), Euro (EUR) e Bitcoin (BTC), e gera um histórico persistente em formato **CSV** para análise posterior.

## 🚀 Funcionalidades

- **Extração (Extract):** Conexão via `requests` com API pública de economia.
- **Transformação (Transform):** Limpeza e formatação de dados JSON e conversão de tipos.
- **Carregamento (Load):** Salvamento automático dos dados em arquivo `moedas.csv` com verificação de cabeçalhos.
- **Log Temporal:** Registro exato da data e hora (`timestamp`) de cada coleta.

## 🛠️ Tecnologias Utilizadas

- **Python 3.12+**
- **Requests** (Consumo de API HTTP)
- **CSV** (Manipulação de planilhas)
- **Datetime** (Manipulação temporal)


## 📦 Como rodar o projeto

### Pré-requisitos
Você precisa ter o Python instalado e a biblioteca `requests`.

```bash
# Clone o repositório
git clone [https://github.com/SEU-USUARIO/monitor-cambial-etl.git](https://github.com/SEU-USUARIO/monitor-cambial-etl.git)

# Entre na pasta
cd monitor-cambial-etl

# Instale as dependências
pip install requests

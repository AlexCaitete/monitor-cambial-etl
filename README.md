# 💰 Monitor Cambial ETL

Um pipeline de dados desenvolvido em **Python** para monitorar, extrair e armazenar cotações de moedas em tempo real.

O projeto consome dados da **AwesomeAPI**, processa as informações de Dólar (USD), Euro (EUR) e Bitcoin (BTC), e gera um histórico persistente em formato **CSV** para análise posterior.

## 🚀 Funcionalidades

- **Extração (Extract):** Conexão via `requests` com API pública de economia.
- **Transformação (Transform):** Limpeza e formatação de dados JSON e conversão de tipos.
- **Carregamento (Load):** Salvamento automático dos dados em arquivo `moedas.csv` com verificação de cabeçalhos.
- **Automação:** O script roda em loop infinito, atualizando os dados a cada 30 segundos.
- **Log Temporal:** Registro exato da data e hora (`timestamp`) de cada coleta.

## 🛠️ Tecnologias Utilizadas

- **Python 3.12+**
- **Requests** (Consumo de API HTTP)
- **CSV** (Manipulação de planilhas)
- **Datetime** (Manipulação temporal)
- **Time & OS** (Controle de fluxo e sistema)

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

Executando o Robô 🤖

Para iniciar o monitoramento contínuo:Bashpython monitor_cambio.py

O script limpará a tela e atualizará as cotações a cada 30 segundos.
⚠️ Como parar: O script roda em loop infinito. Para encerrar a execução, clique no terminal e pressione CTRL + C.

📊 Exemplo de Saída (CSV)
O arquivo gerado segue este padrão:
data,nome,valor
30/01/2026 14:30:15,Dólar Americano/Real Brasileiro,5.75
30/01/2026 14:30:15,Euro/Real Brasileiro,6.20

🔜 Próximos Passos (Roadmap)
[x] Implementar automação (Loop infinito a cada 30s). ✅
[ ] Criar tratamento de erros para queda de internet (Try/Except).
[ ] Gerar gráficos simples com a biblioteca matplotlib.
👨‍💻 AutorDesenvolvido por Alex Roberto durante estudos de Python e Integração de APIs.

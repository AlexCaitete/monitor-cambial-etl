import requests
import os
import csv
from datetime import datetime
import time


ARQUIVO = 'moedas.csv'


def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def verificar_arquivo_existe():
    return os.path.exists(ARQUIVO)


def salvar_transacao(nova_transacao):
    arquivo_existe = verificar_arquivo_existe()

    with open(ARQUIVO, mode='a', newline='', encoding='utf-8') as file:
        # 1. ADICIONEI 'data' NOS CAMPOS
        campos = ['data', 'nome', 'valor']
        escritor = csv.DictWriter(file, fieldnames=campos)

        if not arquivo_existe:
            escritor.writeheader()

        escritor.writerow(nova_transacao)


def dados_moedas():
    limpar_tela()
    print("⏳ BAIXANDO INFORMAÇÕES DAS MOEDAS...\n")
    url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
    resposta = requests.get(url) #pedindo para se conectar ao endereço contido na variável url

    if resposta.status_code == 200:  #codigo 200 quer dizer que a conexção foi bem sucedida
        moedas = resposta.json() #usando o comando json para traduzir as informações na linguagem do python e colocando em uma variavel
        print(f'✅ Conectado! Baixei {len(moedas)} pares de moedas.\n')

        for item in moedas.values():
            nome = item['name']
            valor = float(item['bid']) # Convertendo texto para número. nessa pasta o valor vem como bidmas em forma de texto. aqui estou convertendo para numero

            # 2. CRIANDO O CARIMBO DE TEMPO
            data_atual = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

            print(f"💰 {nome}: R$ {valor:.2f}")

            # 3. EMPACOTANDO OS DADOS PARA ENVIAR (Isso é o Dicionário!)
            pacote_dados = {
                'data': data_atual,
                'nome': nome,
                'valor': valor
            }

            # 4. Chamando sua função de salvar
            salvar_transacao(pacote_dados)

        print("\n💾 Tudo salvo no arquivo 'moedas.csv'!")

    else:
        print('❌ ERRO NA CONEXÃO!')


# 5. O BOTÃO DE LIGAR (Execução Principal)
if __name__ == "__main__":
    while True:
        dados_moedas()

        print("💤 Pausa de 30 segundos... (Não feche)")
        time.sleep(30)
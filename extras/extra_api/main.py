import pandas as pd
import requests

arquivo_csv = "cnpj.csv"
tabela = pd.read_csv(arquivo_csv)
resultados_validacao = []

url = "https://www.4devs.com.br/ferramentas_online.php"

def validar_cnpj(cnpj):
    payload = {
        'acao': 'validar_cnpj',
        'txt_cnpj': cnpj
    }

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        return response.text
    else:
        return "Erro na validação"

def automacao_validacao():
    for cnpj in tabela['cnpj']:
        resultado = validar_cnpj(cnpj)
        
        if "verdadeiro" in resultado.lower():
            resultados_validacao.append(f"{cnpj} – válido")
        else:
            resultados_validacao.append(f"{cnpj} – inválido")

    print("## Validação de dados")
    for resultado in resultados_validacao:
        print(resultado)

if __name__ == '__main__':
    automacao_validacao()
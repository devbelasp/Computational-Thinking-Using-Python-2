"""
Passo 1 - Instalar a biblioteca requests (no terminal)
  - pip install requests
"""

import requests
import json

def consultar_cep(cep):

    url = f"https://viacep.com.br/ws/{cep}/json/"

    print(f'Consultando dados do cep {cep}')

    try:
        response = requests.get(url)

        #o código 200 indica sucesso
        if response.status_code == 200:
            dados_endereco = response.json()
        
            if 'erro' in dados_endereco:
                print(f'[ERRO] CEP não encontrado ou inválido')
                return None
            
            return dados_endereco
        else:
            print(f'\n[Erro] Falha na requisição. Código de status: {response.status_code}')
            return None
    except requests.exceptions.RequestException as e:
        print(f'[ERRO] não foi possível conectar à API: {e}')
        return None       
    except Exception as e:
        print(f'[ERRO]...outro erro!: {e}')
        return None
    
#Programa Principal
endereco = consultar_cep('01311000')
print(f' --- Resultado da consulta ---')
print(f'CEP: {endereco.get("cep")}')
print(f'Logradouro: {endereco.get("logradouro")}')
print(f'Bairro: {endereco.get("bairro")}')
print(f'Cidade/UF: {endereco.get("localidade")}/{endereco.get("uf")}')
print('-' * 30)
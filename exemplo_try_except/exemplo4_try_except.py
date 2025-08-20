try:
    arquivo = open('meu_arquivo.txr', 'r')
    conteudo = arquivo.read()
    print('Arquivo foi lido com sucesso!')
except FileNotFoundError:
    print('Erro: arquivo não encontrado!')
else:
    print('Nenhum erro ocorreu')
finally:
    arquivo.close()
    print('Arquivo fechado!')
def cabecalho(frase):
  print('-' * 30)
  print(frase)
  print('-' * 30)

def insere_candidatos(urna):
  cabecalho('INSERÇÃO DE CANDIDATOS')
  urna[-1] = ['Votos em branco', 0]
  for _ in range(5):
    numero = int(input('Número? '))
    nome = input('Nome? ')
    urna[numero] = [nome, 0]
    print()

def realiza_votacao(urna):
  cabecalho('REALIZAÇÃO DA VOTAÇÃO')
  print('Insira zero para encerrar a votação')
  numero = int(input('Voto? '))
  while numero != 0:
    if numero == -1:
      urna[numero] [1] += 1
      print('Resultado: voto em branco')
    elif numero not in urna:
      print('Resultado: voto nulo')
    else:
      urna[numero][1] += 1
      print('Resultado:', urna[numero][0])
    print()
    numero = int(input('Voto? '))

def apresenta_vencedor(urna):
  cabecalho('VENCEDOR')
  votos_vencedor = -1
  for candidato in urna.items():
    votos = candidato[1][1]
  if votos > votos_vencedor:
      votos_vencedor = votos
      numero_vencedor = candidato[0]
  print('Número:', numero_vencedor)
  print('Nome..:', urna[numero_vencedor][0])
  print('Votos.:', votos_vencedor)

def exibe_votos_em_branco(urna):
  print(f'{urna[-1][0]}: {urna[-1] [1]}')
  urna.pop(-1)

def apresenta_resultados(urna):
  cabecalho('RESULTADOS')
  exibe_votos_em_branco(urna)
  for candidato in urna.items():
    print('Número:', candidato[0])
    print('Nome..:', candidato[1][0])
    print('Votos.:', candidato[1][1])
    print()
  apresenta_vencedor(urna)

urna = {}
insere_candidatos(urna)
realiza_votacao(urna)
apresenta_resultados(urna)
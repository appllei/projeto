#sergio roberto piquet alvaro // r.a 22.223.008-8
#paulo ricardo bezerra // r.a 22.223.015-3

from datetime import datetime 

todosdocs = {} # função de criar dicionário
lista = [] # função de criar lista

# duas variáveis para armazenar os dados dos arquivos

def load_data(): #para salvar todos os dados dos clientes no arquivo
  global todosdocs # função para pegar o dicionário tododocs
  try:
      with open("teste.txt", "r") as arquivo: # abrir o arquivo
          todosdocs = eval(arquivo.read()) # ler o arquivo e tranformar em dicionário
  except FileNotFoundError: # caso o arquivo não exista
      todosdocs = {} # função de criar dicionário
def save_data(): # tem a função de salvar todos os dados do cliente novo.
  with open("teste.txt", "a") as arquivo: # abre o arquivo e salva os dados
      arquivo.write(str(todosdocs)) # pega o dicionário tododocs e o transforma em string
      arquivo.close() #importante fechar o arquivo após o uso para preservar os dados

    


def novos(): # tem a função de receber e cadastrar um novo cliente.
  
  cnpj = int(input("Digite o CNPJ: ")) # aqui ele pede para digitar o cnpj
  if cnpj in todosdocs: # essa parte verifica se o cnpj já existe 
    print("Cliente já cadastrado.") # é uma função que exibe se o cliente já existe 
  else:
    razao_social = input("Digite a razão social: ") 
    nome = input("Digite o nome: ")
    debito = float(input("Saldo inicial: "))
    conta = input("Digite sua classe de conta (comum/plus): ")
    senha = int(input("Digite a senha: "))
    todosdocs[cnpj] = {
        "Razão Social": razao_social,
        "Nome": nome,
        "Debito": debito,
        "Conta": conta,
        "Senha": senha,
        "Historico": []
    }
    print("Cliente cadastrado com sucesso.")
    save_data()
    # essa parte tem a função de salvar os dados do cliente novo
    
    


def apagar(): # tem a função de apagar dados de um cliente cadastrado
  deletar = int(input("Digite seu cnpj : "))
  del todosdocs[deletar]
  print("Sucesso seus dados foram apagados")
  print("")


def cadastro_cliente(): # tem a função de retirar dados pessoais do cliente e adicionar nos arquivos  
  for cnpj, cliente in todosdocs.items():
    print(f"CNPJ: {cnpj}")
    print(f"Razão Social: {cliente['Razão Social']}")
    print(f"Nome: {cliente['Nome']}")
    print(f"Saldo: R$ {cliente['Debito']}")
    print("-------------")
    


def debito_conta(): # tem a fução de reter o dinheiro da conta 
  valor_final = 0  # variável com a função de armazenar o valor final
  cnpj = int(input("Digite o CNPJ: "))
  senha = int(input("Digite a senha: "))

  if cnpj in todosdocs and senha == todosdocs[cnpj]["Senha"]: # verifica se o cnpj e a senha digitados são válidos
    cliente = todosdocs[cnpj] # pega o cliente e o armazena em uma variável
    nome = cliente["Nome"] # pega o nome do cliente e armazena em uma variável
    valor = float(input(f"Digite o valor a ser debitado da conta de {nome}: ")) # pede o valor a ser debitado
    

    if cliente["Conta"] == "comum":
      taxa = valor * 0.05
      valor_final -= taxa  
      limite = -1000
      # essa parte tem a função de verificar se o cliente tem o limite e o valor
    elif cliente["Conta"] == "plus":
      taxa = valor * 0.03
      valor_final = valor - taxa  
      limite = -5000
      # essa parte tem a mesma função que o de cima, ela será acionada caso o contrário se o cliente tem o limite

    if cliente["Debito"] - valor >= limite: # verifica se o valor digitado é maior que o limite da conta 
       cliente["Debito"] -= valor_final # atualiza o saldo da conta   
       data = datetime.now().strftime("%d,%m,%Y") # pega a data atual
       hora = datetime.now().strftime("%H:%M:%S") # pega a hora atual
       operacao = f"Data: {data}, Hora: {hora} Taxa:{taxa}  foram retirados da conta de {nome} (Valor: -{valor} )" #armazena a operação que foi feita
       cliente["Historico"].append(operacao)  # adiciona a operação na lista de operações  
       print(f"R$ {valor} foram retirados de sua conta. de {nome}.") # exibe o valor retirado
    else:
      print("Operação não permitida. Limite de débito excedido.") #
  else:
    print("CNPJ ou senha inválidos.") # essa parte tem a função de verificar se o cnpj e a senha digitados são válidos 


def deposito(): # função de depositar um quantia de dinheiro na conta, um dos passos para "ativar uma conta"
  cnpj = int(input("Digite o CNPJ: "))
  senha = int(input("Digite a senha: "))
  if cnpj in todosdocs and senha == todosdocs[cnpj]["Senha"]:
    cliente = todosdocs[cnpj]
    nome = cliente["Nome"]
    valor = float(input(f"Digite o valor a ser adicionado ao saldo da conta de {nome}: ")) # pede o valor a ser adicionado 
    cliente["Debito"] += valor
    taxa = 0
    data = datetime.now().strftime("%d,%m,%Y") # pega a data atual
    hora = datetime.now().strftime("%H:%M:%S") # pega a hora atual
    operacao = f"Data: {data}, Hora: {hora}  Taxa:{taxa}  +{valor} adicionados ao saldo da conta de {nome}" # armazena a data, hora e taxa juntamente com o valor
    cliente["Historico"].append(operacao)
    print(f"R$ {valor} foram adicionados ao saldo da conta de {nome}.")
  else:
    print("CNPJ ou senha inválidos.")
    #


def extrato(): # tem a função de exibir o histórico de transferências.
  cnpj = int(input("Digite o CNPJ: "))
  senha = int(input("Digite a senha: "))
  if cnpj in todosdocs and senha == todosdocs[cnpj]["Senha"]:
    cliente = todosdocs[cnpj]
    nome = cliente["Nome"]
    extrato = cliente["Historico"]
    print(f"========= Extrato da conta de {nome} =========")
    # coleta as informações e imprime o extrato 
    for operacao in extrato:
      print(operacao)
  else:
    print("CNPJ ou senha inválidos.")


def transferencia(): #tem a função de fazer a transferência bancária
  cnpj = int(input("Digite o CNPJ: "))
  senha = int(input("Digite a senha: "))

  if cnpj in todosdocs and senha == todosdocs[cnpj]["Senha"]: # 
    cliente_origem = todosdocs[cnpj] 
    nome_origem = cliente_origem["Nome"] 

    cnpj_destino = int(input("Digite o CNPJ destino: ")) # pega o cnpj do cliente destino

    if cnpj_destino in todosdocs: 
      cliente_destino = todosdocs[cnpj_destino] 
      nome_destino = cliente_destino["Nome"] 

      valor = float(input("Digite o valor que deverá ser transferido: ")) 
      # essa parte verifica se as informções são válidas para iniciar a tranferência

      if cliente_origem["Debito"] >= valor:
        cliente_origem["Debito"] -= valor
        cliente_destino["Debito"] += valor
        

        data = datetime.now().strftime("%d/%m/%Y")
        hora = datetime.now().strftime("%H:%M:%S")

        operacao_origem = f"Data: {data}, Hora: {hora} -{valor} transferidos para {nome_destino} (CNPJ: {cnpj_destino})."
        operacao_destino = f"Data: {data}, Hora: {hora} +{valor} recebidos de {nome_origem} (CNPJ: {cnpj})."

        cliente_origem["Historico"].append(operacao_origem)
        cliente_destino["Historico"].append(operacao_destino)
        # essa parte adiciona o valor transferido ao histórico do cliente origem e destino

        print(
            f"R$ {valor} foram transferidos da conta de {nome_origem} para a conta de {nome_destino}."
          # se estiver certo, essa parte exibe o resultado da transferência 
        )
      else:
        print("Saldo insuficiente na conta de origem.")
    else:
      print("CNPJ destino não encontrado.")
  else:
    print("CNPJ ou senha inválidos.")


def sair():  # finaliza o atendimento
  print("ATENDIMENTO FINALIZADO :") 

while True:
  print("menu: ")
  print("//////////////////")
  print("1. novo cliente")
  print("2. apagar cliente")
  print("3. listar cliente")
  print("4. debito")
  print("5. Depósito")
  print("6. extrato")
  print("7. transferencia")
  print("8. Operaçao livre/Cadastrar cliente")
  print("9. Sair ")
  opçoes = int(input("informe o numero da opçao desejada:\n "))

  #recebe a variavel

  if opçoes == 1: 
    novos()
  elif opçoes == 2: 
    apagar()
  elif opçoes == 3: 
    cadastro_cliente()
  elif opçoes == 4: 
    debito_conta()
  elif opçoes == 5: 
    deposito()
  elif opçoes == 6: 
    extrato()
  elif opçoes == 7: 
    transferencia()
  elif opçoes ==  8: 
    novos()
  elif opçoes ==  9: 
    sair()
#função de escolhas para o cliente selecionar 
    
    
    
    

import string
invalidChars = set(string.punctuation.replace("_", ""))

decisao = 1
saldo = 0
nomeL = []
sobrenomeL = []
nomeComlpetoLista = []
cpfLista = []
enderecoLista = []
telefoneLista = []
senhaLista = []
emailLista = []

while (decisao != 0):
    nomeP = input("Insira seu primeiro nome: ")
    sobrenomeP = input("Insira seu primeiro sobrenome: ")
    cpf = input("Insira seu cpf: ")
    endereco = input("Insira seu endereço: ")
    email = input("Insira seu email: ")
    celular = input("Insira seu número de telefone (celular): ") 
    senha = input("Insira uma senha: ")

    checkEmail = email.__contains__("@")

    def checar_digito(s):
        return any(i.isdigit() for i in s)


    def verificacaoBanco(nomeP1, sobrenomeP1, cpf1, checkEmail1, endereco1, celular1, senha1):
        if len(nomeP1) < 3:
            print("Nome inválido, favor inserir uma palavra com mais de 3 caracteres")
            return False
        if len(sobrenomeP1) < 3:
            print("Sobrenome inválido, favor inserir uma palavra com mais de 3 caracteres")
            return False
        if checkEmail1 == False:
            print("Email inválido, favor inserir um e-mail válido")
            return False
        if len(senha1) < 5:
            print("Senha inválida, favor inserir uma palavra com mais de 5 caracteres")
            return False
        if checar_digito(senha1) == False:
            print("Senha inválida, favor inserir uma palavra com pelo menos 1 número.")
            return False
        if any(char in invalidChars for char in senha1) == False:
            print("Senha inválida, favor inserir uma palavra com pelo menos 1 caractere especial")
            return False
        else:
            return True

    retornoBanco = verificacaoBanco(nomeP, sobrenomeP, cpf, checkEmail, endereco, celular, senha)

    if retornoBanco == True:
        nomeL.insert(0, nomeP)
        sobrenomeL.insert(0, sobrenomeP)
        nomeComlpetoLista = nomeL[0] + " " + sobrenomeL[0]
        cpfLista.insert(0, cpf)
        emailLista.insert(0, email)
        enderecoLista.insert(0, endereco)
        telefoneLista.insert(0, celular)
        senhaLista.insert(0, senha)
        decisao = int(input("""Você quer realizar mais algum cadastro?
        0- Não (Sair do sistema)
        1- Sim.
        """)) 
    else:
        decisao = int(input("""Você quer corrigir seus erros do cadastro?
        0- Não (Sair do sistema)
        1- Sim.
        """))

decisao = 1

while (decisao != 0):
    operacao = int(input("""Escolha uma operação para realizar (digito o número da respectiva operação.):
    1- Depositar
    2- Sacar
    3- Conferir Saldo
    4- Transferir
    5- Encerrar Conta
    """))

    if operacao == 1: 
        deposito = int(input("Insira a quantidade para depositar: "))
        if deposito < 0:
            print("Número invalido, favor inserir somente positivos")
        else:
            saldo = saldo + deposito
    if operacao == 2: 
        saque = int(input("Insira a quantidade para sacar: "))
        if saque > saldo:
            print("Número invalido, seu saldo é insuficiente para o saque.")
        else:
            saldo = saldo - saque
    if operacao == 3: 
        print("A sua quantidade de saldo no banco é:", saldo)
    if operacao == 4:   
        transferencia = int(input("Insira a quantidade para transferir: "))
        if transferencia > saldo:
            print("Número invalido, a quantidade de saldo é insuficiente para a transferencia.")
        else:
             saldo = saldo - transferencia
    if operacao == 5: 
        decisao = int(input("""Você realmente deseja encerrar sua conta?
        0- Sim.
        1- Não.
        """))

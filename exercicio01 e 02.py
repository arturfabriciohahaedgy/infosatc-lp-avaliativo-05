import string
invalidChars = set(string.punctuation.replace("_", ""))

decisao = 1
saldo = 0
nomeL = []
sobrenomeL = []
nomeInteiro = []
nomeComlpetoLista = []
cpfLista = []
enderecoLista = []
telefoneLista = []
senhaLista = []
emailLista = []
saldoLista = []
decisaoGeral = 1

while (decisaoGeral != 0):
    decisao = 1
    decisaoGeral = int(input("""Insira a operação que deseja realizar: 
    0- Sair do programa
    1- (Exericio 1) - Cadastrar Cliente/ Realizar operações bancarias
    2- (Exercicio 2) - Conta administrativa 
    """))

    if (decisaoGeral == 1):
        while (decisao != 0):
            decisao = 1
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
                nomeInteiro = nomeL[0] + " " + sobrenomeL[0]
                nomeComlpetoLista.insert(0, nomeInteiro) 
                cpfLista.insert(0, cpf)
                emailLista.insert(0, email)
                enderecoLista.insert(0, endereco)
                telefoneLista.insert(0, celular)
                senhaLista.insert(0, senha)
                saldoLista.insert(0, saldo)
                operacaoBancaria = 1
                decisao = int(input("""Você quer realizar mais algum cadastro?
                0- Não (Sair do sistema)
                1- Sim.
                """))
            else:
                decisao = int(input("""Você quer corrigir seus erros do cadastro?
                0- Não (Sair do sistema)
                1- Sim.
                """))
                operacaoBancaria = 0
        while (operacaoBancaria != 0):
            operacaoBancaria = int(input("""Escolha uma operação para realizar (digito o número da respectiva operação.):
            1- Depositar
            2- Sacar
            3- Conferir Saldo
            4- Transferir
            5- Encerrar Conta
            """))
            def depositoOperacao(deposito1):
                if deposito1 < 0:
                    return False
                else:
                    return True
            def saqueOperacao(saque1, saldo1):
                if saque1 > saldo1:
                    return False
                else:
                    return True
            def saldoOperacao(saldoLista1):
                print("A sua quantidade de saldo no banco é:", saldoLista1[0])

            def transferenciaOperacao(transferencia1, saldo1):
                if transferencia1 > saldo1:
                    return False
                else:
                    return True
            if operacaoBancaria == 1: 
                deposito = int(input("Insira a quantidade para depositar: "))
                depositoOperacao(deposito)
                if depositoOperacao == False:
                    print("Número invalido, favor inserir somente positivos")
                else:
                    saldo = saldo + deposito
                    saldoLista[0] = saldo
            if operacaoBancaria == 2: 
                saque = int(input("Insira a quantidade para sacar: "))
                saqueOperacao(saque, saldo)
                if saqueOperacao == False:
                    print("Número invalido, seu saldo é insuficiente para o saque.")
                else:
                    saldo = saldo - saque
                    saldoLista[0] = saldo
            if operacaoBancaria == 3: 
                saldoOperacao(saldoLista)
            if operacaoBancaria == 4: 
                transferencia = int(input("Insira a quantidade para transferir: "))
                transferenciaOperacao(transferencia, saldo)
                if transferenciaOperacao == False:
                    print("Número invalido, a quantidade de saldo é insuficiente para a transferencia.")
                else:
                    saldo = saldo - transferencia
                    saldoLista[0] = saldo
            if operacaoBancaria == 5: 
                operacaoBancaria = int(input("""Você realmente deseja encerrar sua conta?
                0- Sim.
                1- Não.
                """))
    if (decisaoGeral == 2):
        decisao = 1
        usuario = input("Insira seu usuario: ")
        senha = input("Insira sua senha: ")
        alterar = 1

        #usario = "b"
        #senha = "1"

        def login(usuario1, senha1):
            if (usuario1 != "b"):
                return False 
            if (senha1 != "1"):
                return False
            else:
                return True
        retornoLogin = login(usuario, senha)
        def Consulta():
            input("Insira o nome do cliente: ")
        def consultaParticular(lista, valorCliente1):
            print(lista[valorCliente1])
        def deletarCliente(lista,valorCliente1):
            del lista[valorCliente1]
        def atualizarCliente(lista,valorCliente1):
            alterarInput = input("Alterar para: ")
            lista[valorCliente1] = alterarInput
            print("Valor alterado com sucesso!")
        if retornoLogin == True:
            while (decisao != 0):
                alterar = 1
                decisao = int(input("""Selecione a operação: 
                0- Sair da conta administrativa
                1- Consultar um cliente 
                2- Consultar lista de clientes
                3- Deletar um cliente
                4- Atualizar dados de um cliente especifico
                """))
                if decisao == 1:
                    comparacao = input("Insira o nome completo do cliente: ")
                    for i in nomeComlpetoLista:
                        valorCliente = nomeComlpetoLista.index(comparacao)
                    print("Nome:",nomeComlpetoLista[valorCliente])
                    print("CPF:",cpfLista[valorCliente])
                    print("Endereço:",enderecoLista[valorCliente])
                    print("Telefone:",telefoneLista[valorCliente])
                    print("Senha:",senhaLista[valorCliente])
                    print("Email:",emailLista[valorCliente])
                    print("Saldo:",saldoLista[valorCliente])
                if decisao == 2:
                    print("Nome de todos os clientes:", nomeComlpetoLista[0:])
                    print("CPF de todos os clientes:", cpfLista[0:])
                    print("Endereço de todos os clientes:", enderecoLista[0:])
                    print("Telefone de  todos os clientes:", telefoneLista[0:])
                    print("Senha de todos os clientes:", senhaLista[0:])
                    print("Email de todos os clientes:", emailLista[0:])
                    print("Saldo de todos os clientes:", saldoLista[0:])
                if decisao == 3:
                    deletar = input("Insira o nome completo do cliente: ")
                    for i in nomeComlpetoLista:
                        valorCliente = nomeComlpetoLista.index(deletar)
                    deletarCliente(nomeComlpetoLista,valorCliente)
                    deletarCliente(cpfLista,valorCliente)
                    deletarCliente(enderecoLista,valorCliente)
                    deletarCliente(telefoneLista,valorCliente)
                    deletarCliente(senhaLista,valorCliente)
                    deletarCliente(emailLista,valorCliente)
                    deletarCliente(saldoLista,valorCliente)
                if decisao == 4:
                    atualizar = input("Insira o nome completo do cliente: ")
                    for i in nomeComlpetoLista:
                        valorCliente = nomeComlpetoLista.index(atualizar)
                    while (alterar != 0):
                        alterar = int(input("""Selecione que dado alterar:
                        0- Sair do menu.
                        1- Alterar nome
                        2- Alterar CPF
                        3- Alterar Endereço
                        4- Alterar Telefone
                        5- Alterar Senha
                        6- Alterar Email
                        7- Alterar Saldo
                        """))
                        if alterar == 1:
                            atualizarCliente(nomeComlpetoLista,valorCliente)
                        if alterar == 2:
                            atualizarCliente(cpfLista,valorCliente)
                        if alterar == 3:
                            atualizarCliente(enderecoLista,valorCliente)
                        if alterar == 4:
                            atualizarCliente(telefoneLista,valorCliente)
                        if alterar == 5:
                            atualizarCliente(senhaLista,valorCliente)
                        if alterar == 6:
                            atualizarCliente(emailLista,valorCliente)
                        if alterar == 7:
                            atualizarCliente(saldoLista,valorCliente)
            if retornoLogin == False:
                print("Credenciais incorretas.")
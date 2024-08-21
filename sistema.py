# 1 - Pessoa Física / 2 - Pessoa Jurídica / 3 - Sair
# 1 - Cadastrar Pessoa Física / 2 - Listar Pessoa Física / 3 - Sair
# 1 - Cadastrar Pessoa Juridica / 2 - Listar Pessoa Juridica / 3 - Sair

from main import PF, PJ, Address
from datetime import datetime, date
from time import sleep

def main():
    
    listPF = []
    listPJ = []

    while True:
        sleep(1)
        option = int(input('Escolha uma opção:\n1 - Pessoa Física\n2 - Pessoa Jurídica\n0 - Sair\n\n'))
        
        if option == 1:
            while True:
                sleep(1)
                optionF = int(input('Escolha uma opção:\n1 - Cadastrar Pessoa Física\n2 - Listar Pessoa Física\n3 - Remover ou Alterar Pessoa Física\n0 - Voltar ao Menu anterior\n\n'))
                # Cadastrar Pessoa Física
                if optionF == 1:
                    cadPF = PF()
                    endPF = Address()
                    cadPF.name = input('Digite o nome: ')
                    cadPF.cpf = input('Digite o CPF: ')
                    cadPF.performance = float(input('Digite o rendimento mensal: R$'))
                    
                    dateBirth = input('Digite a data de nascimento (dd/MM/aaaa): ')
                    cadPF.dBirth = datetime.strptime(dateBirth, '%d/%m/%Y').date()
                    age = (date.today() - cadPF.dBirth).days // 365

                    if age >= 18: print('A pessoa tem mais de 18 anos.')
                    else:
                        print('ERROR! Pessoa com menos de 18 anos. Recomeçando...')
                        continue

                    # Cadastro de Endereço
                    endPF.address = input('Digite o logradouro: ')
                    endPF.number = input('Digite o número: ')
                    cAddress = input('Este endereço é comercial? (S/N)')
                    endPF.comercial_address = cAddress.strip().upper() == 'S'
                    cadPF.address = endPF
                    
                    listPF.append(cadPF)
                    print('Cadastro realizado com sucesso!')
                
                
                elif optionF == 2:
                    if listPF:
                        for i in listPF:
                            print(f'Nome: {i.name}\n'
                                  f'CPF: {i.cpf}\n'
                                  f'Endereço: {i.address.address}, {i.address.number}\n'
                                  f'Data Nascimento: {i.dBirth.strftime('%d/%m/%Y')}\n'
                                  f'Imposto a ser pago: R${i.calcular_imposto(i.performance)}\n'
                                  'Digite 0 para sair.\n\n')
                            input()
                    else: print('Lista Vazia')
                
                
                elif optionF == 3:
                    rCPF = input('Digite o CPF a ser removido: ')
                    indice = 0

                    while True:
                        escolha = int(input('Você deseja alterar algum dado ou remove-lo?\n[1] Alterar\n[2] Remover\n\n'))
                        if escolha == 1 or escolha == 2: break
                    

                    if escolha == 1:
                        for i in listPF:
                            if i.cpf== rCPF:
                                indice = i
                                while True:
                                    secao = int(input('Qual opção deve ser alterada?\n[1] Nome\n[2] CPF\n[3] Endereço\n[4] Número\n\n'))
                                    if secao == 1 or secao == 2 or secao == 3 or secao == 4 or secao == 5: break
                                    else: print('ERROR! Digite um valor válido!')

                                if secao == 1: i.name = input('Digite o nome: ')
                                elif secao == 2: i.cpf = input('Digite o CNPJ: ')
                                elif secao == 3: i.address.address = input('Digite o endereço: ')
                                elif secao == 4: i.address.numero = input('Digite o número: ')

                                sleep(.4)
                                print('Alteração realizada com sucesso!')  

                    else:
                        for i in listPF:
                            if i.cpf == rCPF:
                                indice = i
                                listPF.remove(cadPF)
                                print('Pessoa Física removida com sucesso!\n\n')
                                break
                    if indice == 0: print(f'Nenhuma Pessoa Física com o CPF foi identificada\n\n')

                elif optionF == 0: break
                else: print('ERROR! OPÇÃO INVÁLIDA')



        elif option == 2:
            # Repetir MENU
            # Seleção de Opções

            while True:
                sleep(1)
                optionJ = int(input('Escolha uma opção:\n1 - Cadastrar Pessoa Jurídica\n2 - Listar Pessoa Jurídica\n3 - Remover ou Alterar Pessoa Jurídica\n0 - Voltar ao Menu anterior\n\n'))
                
                if optionJ == 1:
                    cadPJ = PJ()
                    endPJ = Address()
                    cadPJ.nome = input('Digite a Razão Social: ')
                    cadPJ.cnpj = input('Informe o CNPJ: ')
                    cadPJ.performance = int(input('Digite o faturamento bruto mensal da empresa: R$'))
                    
                    while True:
                        cadPJ.lucro = int(input('Digite o lucro mensal da empresa: R$'))
                        if cadPJ.lucro > cadPJ.performance: print('ERROR! O lucro não pode ser maior que o rendimento.')
                        else: break
                    
                    # Cadastro de Endereço
                    endPJ.address = input('Digite o nome do logradouro: ')
                    endPJ.numero = int(input('Digite o número: '))
                    endPJ.comercial_address = input("Este endereço é comercial? (S/N)").upper()
                    cadPJ.address = endPJ
                    
                    # Adicionando a lista
                    listPJ.append(cadPJ)
                    
                    print('Cadastro de Pessoa Jurídica efetuada com sucesso!')


                elif optionJ == 2:
                    if listPJ:
                        for k in listPJ:
                            print(f'Nome: {k.nome}\n'
                                  f'CNPJ: {k.cnpj}\n'
                                  f'Endereço: {k.address.address}, {k.address.numero}\n'
                                  f'Imposto a ser pago: R${k.calcular_impostoPJ(k.performance, k.lucro)}\n'
                                  'Digite 0 para prosseguir: ')
                            input()
                    else: print('ERROR! LISTA VAZIA.')
                

                elif optionJ == 3:
                    cCNpj = input('Digite o CNPJ: ')

                    while True:
                        escolha = int(input('Você deseja alterar algum dado CNPJ ou remove-lo?\n[1] Alterar\n[2] Remover\n\n'))
                        if escolha == 1 or escolha == 2: break
                    indice = 0

                        
                    if escolha == 1:
                        for i in listPJ:
                            if i.cnpj == cCNpj:
                                indice = i
                                while True:
                                    secao = int(input('Qual opção deve ser alterada?\n[1] Nome\n[2] CNPJ\n[3] Endereço\n[4] Número\n\n'))
                                    if secao == 1 or secao == 2 or secao == 3 or secao == 4: break
                                    else: print('ERROR! VALOR INVÁLIDO')
                                if secao == 1: i.nome = input('Digite o nome: ')
                                elif secao == 2: i.cnpj = input('Digite o CNPJ: ')
                                elif secao == 3: i.address.address = input('Digite o endereço: ')
                                elif secao == 4: i.address.numero = input('Digite o número: ')
                                sleep(.4)
                                print('Alteração realizada com sucesso!')  
                    else:
                        for i in listPJ:
                            if i.cnpj == cCNpj:
                                indice = i
                                listPJ.remove(cadPJ)
                                print('Pessoa Jurídica removida com sucesso!')

                    if indice == 0: print('Nenhuma Pessoa Jurídica com este CNPJ foi identificado')


                elif optionJ == 0: break
                else: print('ERROR! OPÇÃO INVÁLIDA')

        elif option == 0:
            print('Obrigado pela preferência em nosso sistema! Até mais!')
            break
        else: print('ERROR! OPÇÃO INVÁLIDA')




if True: main()
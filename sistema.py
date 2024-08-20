# 1 - Pessoa Física / 2 - Pessoa Jurídica / 3 - Sair
# 1 - Cadastrar Pessoa Física / 2 - Listar Pessoa Física / 3 - Sair
# 1 - Cadastrar Pessoa Juridica / 2 - Listar Pessoa Juridica / 3 - Sair

from main import PF
from main import Address
from datetime import datetime, date

def main():
    
    listPF = []

    while True:
        option = int(input('Escolha uma opção:\n1 - Pessoa Física\n2 - Pessoa Jurídica\n0 - Sair\n\n'))
        
        if option == 1:
            while True:
                optionF = int(input('Escolha uma opção:\n1 - Cadastrar Pessoa Física\n2 - Listar Pessoa Física\n0 - Voltar ao Menu anterior\n\n'))
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
                elif optionF == 0: break
                else: print('ERROR! OPÇÃO INVÁLIDA')



        elif option == 2:
            while True:
                optionJ = int(input('Escolha uma opção'))
        elif option == 0:
            print('Obrigado pela preferência em usar nosso sistema! Até mais!')
            break
        else: print('ERROR! OPÇÃO INVÁLIDA')

if __name__ == '__main__':
    main()
from datetime import date


#CLASSE ENDERECO
class Address:
    def init(self, logradouro="",number="", comercial_address=False):
        #Inicializar os nossos atributos com valores padrao
        self.logradouro = logradouro
        self.numero = number
        self.address = comercial_address


#CLASSE PESSOA
class user:
    def init(self, name="", performance=0.0, address=None):
        self.name = name
        self.performance = performance
        self.address = address

    def calcular_imposto(self, performance: float):
        return performance


#CLASSE PESSOA FISICA
class PF(user):
    #Inicializar os atributos que foram herdados e proprios atributos da classe
    def init(self, name="", performance=0.0, address=None, cpf="", dBirth=None):
        if address is None:
            #Se nenhum endereco for fornecido, cria um objeto Endereco padrao
            address = Address()

        if dBirth is None:
            dBirth = date.today()
        

        super().init(name, performance, address)
        #Chama o construtor da superclasse Pessoa para inicializar os atributos herdados

        #Atributos da propria classe
        self.cpf = cpf
        self.dBirth = dBirth

    def calcular_imposto(self, performance: float) -> float:
       #Sem imposto para rendimentos ate R$1500
        if performance <= 1500:
            return 0
        
        #2% de imposto para rendimentos entre 1500 e 3500
        elif 1500 < performance <= 3500:
            return (performance /100)* 2
        #3.5% de imposto para rendimentos entre 3500 e 6000
        elif 3500 < performance <= 6000:
            return (performance / 100) * 3.5
        #5% de imposto para rendimentos acima de 6000
        else:
            return (performance / 100) * 5



#CLASSE PESSOA JURIDICA
class PJ(user):
    def init(self, name="", performance=0, address=None, cnpj='', lucro = 0):
        if address is None:
            address = Address

        super().init(name, performance, address)

        #Atributos PJ
        self.cnpj = cnpj
        self.lucro = lucro

        # Calculando imposto
    def calcular_impostoPJ(self, perfomance, lucro):
        if lucro > 2000: 
            return (perfomance * 0.15) + (perfomance * 0.1)
        else: 
            return (perfomance * 0.15)


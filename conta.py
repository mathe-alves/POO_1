

class Conta:

    #função construtora
    def __init__(self, numero, titular, saldo, limite):
        """ Aqui vamos criar os atributos"""
        #self é a referência(0x00000...) que sabe encontrar o objeto construído em memória.
        print('Construindo objeto... {}'.format(self))

        # utilizaremos self para acessar o objeto e definir seus atributos e características.
        # self sabe o endereço e pega o objeto. referencia.objeto
        #'__' em frente ao atributo é para dizer que é privada(private)
        # O encapsulamento refere-se ao ato de tornar os atributos privados e
        # permitir seu acesso apenas por meio dos métodos da classe, usando o prefixo __
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    
    ### Criando os métodos
    def extrato(self):
        print('Saldo {} do titular {}'.format(self.__saldo, self.__titular))

    def depositar(self, valor):
        self.__saldo += valor

    #deixando o metodo privado para que haja a função no código, mas q o usuario n possa usar
    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saque(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print('O valor {} passou o limite'.format(valor))

    def transfere(self, valor, destino):
        self.saque(valor)
        destino.depositar(valor)

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    @staticmethod
    def codigo_banco():
        return "001"

    #o nome de estáticos, porque eles fazem parte da classe. São chamados quando tem coisas em comum
    #método estático deve ser algo que não dependa do estado da classe
    @staticmethod
    def codigos_dos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}



class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    #o property é para conseguir chamar a função sem "()"
    @property
    def nome(self):
        print("Getter Nome")
        #title() aumenta a primeira letra da palavra
        return self.__nome.title()

    #atributo que receberá o setter. não será necessário o "()"
    @nome.setter
    def nome(self, novo_nome):
        print("Setter Nome")
        self.__nome = novo_nome.title()

    #Sempre se lembrar de deixar os atributos privados
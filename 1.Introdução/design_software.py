'''
Princípio do aberto/fechado

Classes ou métodos devem estar abertos para extensão, mas fechados para modificações.

Devemos escrever nossas classes e métodos de forma genérica.
'''
from abc import ABC, abstractmethod
from uuid import uuid4


class Pessoa(ABC):
    def __init__(self: object, nome: str) -> None:
        self.nome = nome

    @abstractmethod
    def ganhar_dinheiro(self: object) -> None:
        pass


class Aluno(Pessoa):
    def __init__(self: object, nome: str) -> None:
        super().__init__(nome)
        self.__matricula = str(uuid4()).split('-')[0].upper()

    def ganhar_dinheiro(self: object) -> None:
        print('Como ganhar dinheiro')


aluno1 = Aluno('Felicity')
print(aluno1.__dict__)
# {'nome': 'Felicity', '_Aluno__matricula': '0636E6FB'}

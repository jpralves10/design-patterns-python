'''
Usamos em casos como logging (logs) ou operações de bancos de dados, spoolers de impressão e outros cenários que seja
necessário que haja apenas uma única instância.

Pode evitar requisições conflitantes.
'''

# Toda classe herda de object
class Singleton(object):
    # Executado antes do metodo __init__
    # __new__ cria um novo objeto
    def __new__(cls):
        # Verifica se essa classe possui o atributo instance
        if not hasattr(cls, 'instance'):
            #  Caso não tenha, está colocando uma instância da classe nesse objeto
            cls.instance = super(Singleton, cls).__new__(cls)
            print(f'Criando o objeto {cls.instance}')
            # Criando o objeto <__main__.Singleton object at 0x000002E36274BCA0>
        # Caso já exista, apenas retorna
        return cls.instance


s1 = Singleton()
print(f'Instância 1: {id(s1)}')
# Instância 1: 140719578605560

s2 = Singleton()
print(f'Instância 2: {id(s2)}')
# Instância 2: 140719578605560

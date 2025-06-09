'''
Metaclasse -> Uma classe de outra classe, ou seja, qualquer classe que criamos é uma instância de outra classe
'''


class University(type):
    # __call__ -> Quando o objeto precisa ser criado para uma classe já existente
    def __call__(cls, *args, **kwargs):
        print(f'=== Estes são os argumentos: {args}')
        # === Estes são os argumentos: (42, 23)
        return type.__call__(cls, *args, **kwargs)


class Geek(metaclass=University):
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2


obj = Geek(42, 23)

print(obj)
# <__main__.Geek object at 0x0000023A30C0BD30>

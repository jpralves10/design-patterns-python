'''
Monostate -> Instâncias diferentes da classe, porém com o mesmo estado
'''


class Monostate:
    __estado = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__estado
        return obj


m1 = Monostate()
print(f'M1 ID: {id(m1)}')
# M1 ID: 1699685776688
print(m1.__dict__)
# {}

m2 = Monostate()
print(f'M2 ID: {id(m2)}')
# M2 ID: 1699685776640
print(m2.__dict__)
# {}

m1.nome = 'Felicity'

print(f'M1: {m1.__dict__}')
# M1: {'nome': 'Felicity'}
print(f'M2: {m2.__dict__}')
# M2: {'nome': 'Felicity'}

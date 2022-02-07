'''
Lazy Instance -> O objeto só é criado quando for utilizado 
'''


class Singleton:
    
    __instance = None

    def __init__(self: object):
        if not Singleton.__instance:
            print('O método __init__ foi chamado...')
        else:
            print(f'A instância já foi criada: {self.get_instance()}')

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance

s1 = Singleton()  # A classe é inicializada, mas o objeto não é criado...

print(f'O objeto é criado agora: {Singleton.get_instance()}')

s2 = Singleton()  # Instância já criada...
# A instância já foi criada: <__main__.Singleton object at 0x0000026AF9C4BC70>

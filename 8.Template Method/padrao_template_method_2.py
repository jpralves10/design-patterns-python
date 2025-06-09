from abc import ABCMeta, abstractmethod

class ClasseAbstrata(metaclass=ABCMeta):
    def __init__(self):
        pass
    
    @abstractmethod
    def operacao1(self):
        pass
    
    @abstractmethod
    def operacao2(self):
        pass
    
    def template_method(self):
        print('Definindo o algoritmo: Operação 1 após Operação 2')
        self.operacao1()
        self.operacao2()
        
class ClasseContreta(ClasseAbstrata):
    def operacao1(self):
        print('Minha operação concreta 1')
    
    def operacao2(self):
        print('Minha operação concreta 2')
        
class Cliente:
    def main(self):
        self.concreta = ClasseContreta()
        self.concreta.template_method()
        
cliente = Cliente()
cliente.main()
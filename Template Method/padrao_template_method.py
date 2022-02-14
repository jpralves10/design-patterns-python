'''
O Padrão Template Method ajuda a redefinir ou personalizar os passos do algoritmo adiando a implementação
de alguns desses passos para as subclasses. Ou seja, as subclasses pode redefinir o seu próprio comportamento.

Desta forma uma subclasse poderia fazer uso do Método Template para preparar uma bebida e preparar chá
enquanto outra subclasse poderia usar o mesmo Método Template para preparar café já que ambas são bebidas.

O padrão Template Method é usado nos seguintes casos:
    - Quando vários algoritmos ou classes implementam uma lógica semelhante ou idêntica;
    - Quando a implementação dos algoritmos em subclasses ajuda a reduzir a duplicação de código;
    - Quando vários algoritmos podem ser definidos ao deixar que as subclasses implementem o comportamento usando
    o recurso de sobrescrita;

Os principais objetivos do padrão Template Method são:
    - Definir o esqueleto de um algoritmo com operações primitivas;
    - Redefinir determinadas operações na subclasse sem alterar a estrutura do algoritmo;
    - Reutilizar o código e evitar esforços duplicados;
    - Tirar proveito de interfaces ou implementações comuns;
'''

from abc import ABCMeta, abstractmethod


'''
Classe Abstrata, que define as operações ou os passos de um algoritmo com a ajuda de métodos abstratos. Estes
passos são sobrescritos pelas subclasses concretas.
'''
class Compilador(metaclass=ABCMeta):

    @abstractmethod
    def coletar_fonte(self):
        pass

    @abstractmethod
    def compilar_objeto(self):
        pass

    @abstractmethod
    def executar(self):
        pass
    
    '''
    templame_method(), que define o esqueleto do algoritmo. Vários passos, conforme definidos pelos métodos abstratos,
    são chamados no método Template para definir a sequencia ou o algoritmo propriamente dito.
    '''
    def compliar_e_executar(self):
        self.coletar_fonte()
        self.compilar_objeto()
        self.executar()


'''
Classe Concreta, que implementa os passos, conforme definidos pelos métodos abstratos, específicos do algoritmo
para a subclasse.
'''
class CompiladorIOS(Compilador):
    def coletar_fonte(self):
        print('Colentando código fonte Swift')

    def compilar_objeto(self):
        print('Compilando código Swift para bytecode LLVM')

    def executar(self):
        print('Programa executando no ambiente de execução')


class CompiladorAndroid(Compilador):
    def coletar_fonte(self):
        print('Colentando código fonte Kotlin')

    def compilar_objeto(self):
        print('Compilando código Kotlin para bytecode JVM')

    def executar(self):
        print('Programa executando no ambiente de execução')


ios = CompiladorIOS()
ios.compliar_e_executar()

android = CompiladorAndroid()
android.compliar_e_executar()

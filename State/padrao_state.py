'''
State -> Um objeto pode encapsular vários comportamentos de acordo com o seu estado interno. 
O padrão State permite que um objeto altere o seu comportamento quando o seu estado interno muda. É usado para 
desenvolver Máquinas de Estado Finitas e ajuda a acomodar ações de transição de estados.

----------------------------------------------------------------

State: É considerada uma interface que encapsula o comportamento do objeto. Esse comportamento está
associado ao estado do objeto.

StateConcreto: É uma subclasse que implementa a interface State. Esta subclasse implementa o comportamento
propriamente dito associado ao estado particular do objeto.

Context: Define a interface de interesse dos cloentes. Context também mantém uma instância da subclasse
StateConcreto que, internamente, define a implementação do estado particular do objeto.
'''

from abc import ABCMeta, abstractmethod

class State(metaclass=ABCMeta):
    @abstractmethod
    def manipular(self):
        pass
    
class StateConcretoA(State):
    def manipular(self):
        print('StateConcretoA')
        
class StateConcretoB(State):
    def manipular(self):
        print('StateConcretoB')
        
class Contexto(State):
    def __init__(self):
        self.state = None
        
    def get_state(self):
        return self.state
    
    def set_state(self, state):
        self.state = state
    
    def manipular(self):
        self.state.manipular()
        
contexto = Contexto()
state_a = StateConcretoA()
state_b = StateConcretoB()

contexto.set_state(state_a)
contexto.manipular()

contexto.set_state(state_b)
contexto.manipular()
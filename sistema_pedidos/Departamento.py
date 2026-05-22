#Criando a classe Departamento
from sistema_pedidos.RH import Funcionario
class  Departamento:

    def __init__(self,nome):
        if not isinstance(nome,str):
            raise ValueError('Nome invalido')
        nome=nome.strip()

        if not nome.replace(' ','').isalpha():
            raise ValueError('Nome invalido')
        
        self.nome=nome
        self.funcionarios=[]

    def adicionar_funcionario(self,funcionario):
        if not isinstance(funcionario,Funcionario):
            raise ValueError('Funcionario invalido')
        
        self.funcionarios.append(funcionario)

    def remover_funcionario(self,nome):
        if not isinstance(nome,str):
            raise ValueError('Nome invalido')
        nome=nome.strip()

        if not nome.replace(' ','').isalpha():
            raise ValueError('Nome invalido')
        
        for funcionario in self.funcionarios:
            if funcionario.nome==nome:
                self.funcionarios.remove(funcionario)
                return True
        return False
        
    def maior_salario(self):
        if not self.funcionarios:
            raise ValueError('Nao ha funcionarios cadastrados no departamento')
        maior=max(self.funcionarios, key= lambda item:item.salario)

        return maior
    
    def menor_salario(self):
        if not self.funcionarios:
            raise ValueError('Nao ha funcionarios cadastrados no departamento')
        minimo=min(self.funcionarios,key= lambda item:item.salario)

        return minimo
    


    def media_salarial(self):
        
        if not self.funcionarios:
            raise ValueError('Nao ha funcionarios cadastrados no departamento')
        
        total=0
        for funcionario in self.funcionarios:
            total+=funcionario.salario

        media=round(total/len(self.funcionarios),2)
        return media

    def __len__(self):
        return len(self.funcionarios)



    def relatorio(self):
        total=len(self.funcionarios)
        salario_maior=self.maior_salario()
        salario_menor=self.menor_salario()
        media_salario=self.media_salarial()

        return f' Departamento: nome={self.nome} funcionarios={total} maior salario={salario_maior} menor salario={salario_menor} media salarial={media_salario}'

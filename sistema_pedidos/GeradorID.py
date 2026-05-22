#Começando exercicio 18

class GeradorID:

    contador=0

    def __init__(self,prefixo='PREFIXO'):
        
        if not isinstance(prefixo,str):
            raise ValueError('Prefixo invalido')
                
        self.prefixo=prefixo

    def gerar(self):
        GeradorID.contador+=1
        numero=f'{GeradorID.contador:04}'
        separador='-'
        id=self.prefixo+separador+numero
        return id

    @classmethod
    def total_gerados(cls):
        return cls.contador
    
    @classmethod
    def resetar(cls):
        cls.contador=0
    
    @staticmethod
    def validar(identificador):
        if not isinstance(identificador,str):
            return False
        
        partes_id=identificador.split('-')
        if len(partes_id)!=2:
            return False
        if  not partes_id[0].isalpha():
            return False
        if not partes_id[1].isdigit():
            return False
        return True
    

    @staticmethod
    def extrair_prefixo(identificador):
       if not isinstance(identificador,str):
           raise ValueError('ID invalida')
       
       if '-' not in identificador:
           raise ValueError('ID invalida')
       
       partes=identificador.split('-')
       
       if len(partes)!=2:
           raise ValueError('ID invalida')
       
       if not partes[0].isalpha():
           raise ValueError('ID invalida')
       
       if not partes[1].isdigit():
           raise ValueError('ID invalida')
    
       return partes[0] 
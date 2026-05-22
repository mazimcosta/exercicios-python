
# =============================================================================
# EXERCÍCIO 20 | Classe + herança básica
# Nível: Difícil | Contexto: Sistema de notificações
# Status: [ ] Pendente | [ ] Enviado | [ ] Revisado | [ ] Corrigido
# =============================================================================
"""
CONTEXTO:
Sistema que envia notificações por diferentes canais.

TAREFA:
Crie a hierarquia de classes:

Notificacao (classe base):
- __init__(destinatario, mensagem, prioridade)
- validar() -> bool  (mensagem não vazia, destinatario válido)
- formatar() -> str  (deve ser sobrescrito nas filhas)
- enviar() -> dict   (chama validar e formatar)
- __str__()

EmailNotificacao(Notificacao):
- __init__(destinatario, mensagem, prioridade, assunto)
- formatar() → formato de e-mail com assunto e corpo

SMSNotificacao(Notificacao):
- __init__(destinatario, mensagem, prioridade)
- formatar() → máximo 160 caracteres, trunca se necessário
- validar() → também valida se destinatário tem 11 dígitos

PushNotificacao(Notificacao):
- __init__(destinatario, mensagem, prioridade, titulo)
- formatar() → título + mensagem curta (máximo 100 chars)

RESTRIÇÕES:
- super().__init__() obrigatório nas filhas
- formatar() sobrescrito em cada filha
- try/except em enviar()
"""
# SUA SOLUÇÃO:

#Criando a classe Notificaçao:

class  Notificacao:

    def __init__(self,destinatario,mensagem,prioridade):
        if not isinstance(destinatario,str):
            raise ValueError('Destinatario invalido')
        
        if not isinstance(mensagem,str):
            raise ValueError('Mensagem invalida')
        
        
        if not isinstance(prioridade,str):
            raise ValueError('Prioridade invalida')

        prioridade=prioridade.lower()

        if  prioridade not in ['baixa','media','alta']:
            raise ValueError('Prioridade invalida')
        
        self.destinatario=destinatario
        self.mensagem=mensagem
        self.prioridade=prioridade

    def validar(self):
        if not self.mensagem:
            return False
        
        if not self.mensagem.replace(' ',''):
            return False
        

        if not self.destinatario:
            return False
        
        if not self.destinatario.replace(' ',''):
            return False



        return True
    
    def enviar(self):
        try:
            if not self.validar():
                raise ValueError("Dados invalidos")

            mensagem = self.formatar()

            return {
                "status": "enviado",
                "conteudo": mensagem
            }

        except Exception as error:
            return {
                "status": "erro",
                "erro": str(error)
            }
        
   
    def __str__(self):
        return f'Notificação: destinatario={self.destinatario} mensagem={self.mensagem} prioridade={self.prioridade}'
    



    #Classe Email:
class EmailNotificacao(Notificacao):

    def __init__(self,destinatario,mensagem,prioridade,assunto):
        super().__init__(destinatario,mensagem,prioridade)
        
        if not isinstance(assunto,str):
            raise ValueError('Assunto invalido')
        
        if not assunto.replace(' ',''):
            raise ValueError('Assunto invalido')
        
        self.assunto=assunto
    
    def formatar(self):
        return{
            'destinario':self.destinatario,'prioridade':self.prioridade,
            'assunto':self.assunto,
            'mensagem':self.mensagem
        }
    


# Classe SMS

class SMSNotificacao(Notificacao):

    def __init__(self, destinatario, mensagem, prioridade):
        super().__init__(destinatario, mensagem, prioridade)

    def formatar(self):
        if len(self.mensagem)>160:
             self.mensagem= self.mensagem[:160]

        return{
            'destinario':self.destinatario,
            'prioridade':self.prioridade,
            'mensagem':self.mensagem
        }
    
    def validar(self):
        if len(self.destinatario)!=11:
            return False
        
        if not self.destinatario.isdigit():
            return False
                            
        return super().validar()
    


#Criando push notificação:

class PushNotificacao(Notificacao):

    def __init__(self, destinatario, mensagem, prioridade,titulo):
        super().__init__(destinatario, mensagem, prioridade)

        if  not isinstance(titulo,str):
            raise ValueError('Titulo invalido')
        
        if not titulo.replace(' ',''):
            raise ValueError('Titulo invalido')
        
        self.titulo=titulo

    def formatar(self):
        if len(self.titulo)>100:
            raise ValueError('Titulo deve conter no maximo 100 caracteres')
        
        return {
            'destinatario':self.destinatario,
            'prioridade':self.prioridade,
            'titulo':self.titulo,
            'mensagem':self.mensagem
        }
import telepot
from Comandos import Comandos

#ID BOT: ID DO SEU BOT
#ID ID DO USUARIO: E O ID DO SEU TELEGRAM 
#Classe recebe msg do telegram e verifica se é um comando, sendo ele chama a classe comandos e ezecuta algo

class Telegram:


    def __init__(self , ID):
        self.bot = telepot.Bot(ID)


    # Metodo para pega id, nome e Mensagem, vinda do Usuario 
    def __msg_recebida(self, msg): 
        temp = msg["from"]
        id = temp["id"]
        nome = temp["first_name"]
        try:
            texto = msg["text"]
        except Exception:
            texto = "So é permitido Texto"
        Mensagem = {"id":id, "nome":nome, "texto": texto}
        self.__tratar_msg(Mensagem)


    #Metodo para verificar comando, so funciona se Usuario for Admin
    def __verificar_comando(self, texto):
            Comando = Comandos()
            return Comando.Verificar(texto)


    #Metodo para verificar se o usuario é admin
    def __verificar_usuarios(self, id):
       return True if id == 000000000 else False


    # Metodo que trabalha com id, nome, texto, vindo do metodo __mensagem_usuario
    def __tratar_msg(self, msg):
        id = msg["id"]
        nome = msg["nome"]
        texto = msg["texto"]
        #print(id, nome, texto)
        super_usuario = self.__verificar_usuarios(id)
        if texto.startswith("/") and super_usuario:
            texto = self.__verificar_comando(texto)
        else:
            texto = "Comando nao existe, ou voce nao é Admin"
        self.mandar_msg(id, texto)
   

   # Recebe um dicionario do Usuario
    def receber_msg(self):
        self.bot.message_loop(self.__msg_recebida)
        while True:  # Esse while esta sem otimizaçao, por esta em loop infinito, consome muito recuso
            pass     # Para melhora, pensei em fazer toda vez que ele entra no loop ele espera 1 segundo
                     # e ai proseguir, porem em Python nao sei fazer o Sleep(1000) do C#


    #Manda Msg para usuario
    def mandar_msg(self, id, msg):
        self.bot.sendMessage(id, msg)

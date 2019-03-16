import telepot
from Comandos import Comandos

#ID BOT: ID DO SEU BOT
#ID ID DO USUARIO: E O ID DO SEU TELEGRAM 
#Classe recebe msg do telegram e verifica se é um comando, sendo ele chama a classe comandos e ezecuta algo

class Telegram:

    def __init__(self , ID):
        self.bot = telepot.Bot(ID)

    # Metodo para pega id, nome e Mensagem, vinda do Usuario 
    def __MSG(self, msg): 
        Mensagem = ""
        temp = msg["from"]
        id = temp["id"]
        nome = temp["first_name"]
        #print(msg) ESSE COMANDO, IMPRIME O DICIONARIO VINDO DO TELEGRAM
        try:
            texto = msg["text"]
            Mensagem = {"id":id, "nome":nome, "texto": texto} 
        except Exception:
            texto = "So é permitido Texto"

        Mensagem = {"id":id, "nome":nome, "texto": texto}
        self.__DisparaMSG(Mensagem)

    #Metodo para verificar comando, so funciona se Usuario for Admin
    def __Verificar_Comando(self, usuario, texto):
        Texto = str(texto)
        Comando = Comandos()

        if Texto.startswith("/"):
            if usuario:
                return Comando.Verificar(Texto)
            else:
                return "Voce nao é Admin"
        return Texto

    #Metodo para verificar se o usuario é admin
    def __Verificar_Usuarios(self, id):
        if str(id) == "ID DO USUARIO":
            return True 
        else:
           return False

    # Metodo que trabalha com id, nome, texto, vindo do metodo __MSG
    def __DisparaMSG(self, msg):
        id = msg["id"]
        nome = msg["nome"]
        texto = msg["texto"]
        print(id, nome, texto)
        Super_Usuario = self.__Verificar_Usuarios(id)
        texto = self.__Verificar_Comando(Super_Usuario, texto)
        self.MandarMsg(id, texto)
   
   # Recebe um dicionario do Usuario
    def RecebeMSG(self):
        self.bot.message_loop(self.__MSG)
        while True:  # Esse while esta sem otimizaçao, por esta em loop infinito, consome muito recuso
            pass     # Para melhora, pensei em fazer toda vez que ele entra no loop ele espera 1 segundo
                     # e ai proseguir, porem em Python nao sei fazer o Sleep(1000) do C#
    #Manda Msg para usuario
    def MandarMsg(self, id, msg):
        self.bot.sendMessage(id, msg)

   
import telepot
import time

# ID BOT: ID DO SEU BOT
# ID ID DO USUARIO: E O ID DO SEU TELEGRAM

class Telegram:

    def __init__(self, ID):
        self.bot = telepot.Bot(ID)

    # Metodo responsavel por pegar o id, nome e msg vinda do Telegram do 
    # usuario, e al final chama o __tratar_msg para fazer algo com a msg
    def __msg_recebida(self, msg):
        temp = msg["from"]
        id = temp["id"]
        nome = temp["first_name"]
        try:
            texto = msg["text"]
        except Exception:
            texto = "So é permitido Texto"
        Mensagem = {"id": id, "nome": nome, "texto": texto}
        self.__tratar_msg(Mensagem)

    # Esse metodo é responsavel por tratar a msg vinda do usuario, e com
    # ele que posso agregar funçao as msg vinda do usuario
    def __tratar_msg(self, msg):
        id = msg["id"]
        nome = msg["nome"]
        texto = msg["texto"]
        print(id, nome, texto)  # gera um long no terminal
        self.mandar_msg(id, texto)

    def receber_msg(self):
        """ Metodo onde abilita o recebimento de mensagem """
        self.bot.message_loop(self.__msg_recebida)
        while True:        # self.bot.message_loop nao é bloquenate, com isso
            time.sleep(10) # ao executar ele abilita o recebimento de msg e 
                           # quando o metodo receber_msg termina fecha o recebimento
                           # o while True, é para que o receber_msg nao feche o 
                           # bot.message_loop

    def mandar_msg(self, id, msg):
        """ Para mandar uma msg, basta saber o id, com ele é so
        enviar a mensagem """
        self.bot.sendMessage(id, msg)

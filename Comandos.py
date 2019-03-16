class Comandos:

    def Verificar(self, msg):
        if msg == "/desligar_tela":
            return "tela desligada"
        elif msg == "/desligar_monitor":
            return "Monitor desligado"
        else:
            return "Comando nao Conhecido"
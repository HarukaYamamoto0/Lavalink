from os import system, environ

class Lavalink:
    def __init__(self):
        self.replace_port_command = 'sed -i "s|DYNAMICPORT|$PORT|" application.yml'

        self.replace_password_command = 'sed -i "s|DYNAMICPASSWORD|$PASSWORD|" application.yml'
        self.replace_password_command_no_password = 'sed -i "s|DYNAMICPASSWORD|youshallnotpass|" application.yml'
    
        self.run_command = f"java -jar Lavalink.jar"

    def replace_password_and_port(self):
        print('[INFO] A substituir a porta...')
        try:
            system(self.replace_port_command)
            
            if not environ.get("PASSWORD"):
                print('[AVISO] Password nao encontrada no .env')
    
                return system(self.replace_password_command_no_password)
            
            system(self.replace_password_command)

        except BaseException as exc:
            print(f'[ERRO] Erro ao substituir a porta ou a password. Info: {exc}')

        else:
            print('[INFO] Configuracao concluida')
    
    def run(self):
        self.replace_password_and_port()

        print('[INFO] A iniciar Lavalink...')

        try:
            system(self.run_command)
        
        except BaseException as exc:
            print(f'[ERROR] Falha ao iniciar o Lavalink. Info: {exc}')

if __name__ == "__main__":
    Lavalink().run()

import os
import traceback
import discord
from discord.ext import commands
from decouple import config

'''
No Discord.py, "intents" se referem a uma forma de controlar quais eventos você deseja que seu bot receba informações.

Existem atualmente 26 intents no Discord.py, e é aconselhável ativar apenas as intents que seu bot irá usar. Quanto mais intents você habilitar, mais informações seu bot receberá, o que pode aumentar o consumo de RAM. Por exemplo:
	discord.Intents(messages=True, guilds=True)
'''

intents = discord.Intents.default() #Ativa todas as intents menos as "Privileged Gateway Intents" que são 3, estarei deixando as logo abaixo.
intents.message_content = True #Uma das 3 intents privilegiadas. Ela está ativada, pois o bot usa um prefixo, sendo necessário para que ele leia o conteúdo da mensagem. Isso também é válido para alguns eventos como "on_message".
#intents.members = True
#intents.presences = True

'''
Para mais informações em relação as intents, visite a documentação do discord.py:
	https://discordpy.readthedocs.io/en/latest/intents.html
	https://discordpy.readthedocs.io/en/latest/intents.html#privileged-intents
	https://discordpy.readthedocs.io/en/stable/api.html#discord.Intents
'''

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=commands.when_mentioned_or(config("PREFIX")),
            application_id=int(config("BOT_ID")),
            intents=intents,
            case_insensitive=True,
            help_command=None
        )
        self.run(config("TOKEN"))
        
    #Função que irá carregar as extensões, nescessário colocar somente o caminho da pasta onde estão os comandos/eventos.
    async def load_cogs(self, path:str):
    	for f in os.listdir(path):
    		if f.endswith(".py"):
    			try:
    				await self.load_extension(f"{path[2:]}.{f[:-3]}")
    				print(f"\033[32m✅Carregado {f} de {path}\033[0;0m")
    			except Exception:
    				print(f"\033[31m❌Falha ao carregar {f} de {path}\033[0;0m")
    				traceback.print_exc()
    				
    async def on_ready(self):
    	print(f"Estou online como {self.user}!")
    				
    async def setup_hook(self):
    	await self.load_cogs("./commands")

if __name__ == "__main__":
        MyBot()
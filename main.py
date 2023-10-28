import discord
from discord.ext import commands
from decouple import config

'''
No Discord.py, "intents" se referem a uma forma de controlar quais eventos você deseja que seu bot receba informações.
Para mais informações em relação as intents, visite a documentação do discord.py:
	https://discordpy.readthedocs.io/en/latest/intents.html
	https://discordpy.readthedocs.io/en/latest/intents.html#privileged-intents

Existem atualmente 26 intents no Discord.py, e é aconselhável ativar apenas as intents que seu bot irá usar. Quanto mais intents você habilitar, mais informações seu bot receberá, o que pode aumentar o consumo de RAM. Por exemplo:
	discord.Intents(messages=True, guilds=True)
'''

intents = discord.Intents.default() #Ativa todas as intents menos as "Privileged Gateway Intents" que são 3, estarei deixando as logo abaixo.
intents.message_content = True #Uma das 3 intents privilegiadas. Ela está ativada, pois o bot usa um prefixo, sendo necessário para que ele leia o conteúdo da mensagem. Isso também é válido para alguns eventos como "on_message".
#intents.members = True
#intents.presences = True

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

    async def setup_hook(self):
            print(f"Estou online como {self.user}!")

if __name__ == "__main__":
        MyBot()
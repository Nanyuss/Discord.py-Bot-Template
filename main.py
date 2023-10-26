import discord
from discord.ext import commands
from decouple import config

intents = discord.Intents.default()
intents.message_content =True

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
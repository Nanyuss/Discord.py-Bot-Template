import discord
from discord.ext import commands

class OwnerCommands(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	#Comando para sincronizar os comandos slash
	@commands.is_owner()
	@commands.command(name="sync")
	async def sync(self, ctx:commands.Context):
		try:
			await self.bot.tree.sync()
			await ctx.reply(f"Comandos de barra sincronizados")
		except Exception as e:
			await ctx.reply(embed=discord.Embed(title="Falha ao carregar os comandos de barra", description=e, color=discord.Color.red()))
		
async def setup(bot:commands.Bot):
	await bot.add_cog(OwnerCommands(bot))
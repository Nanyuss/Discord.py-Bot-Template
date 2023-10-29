import discord
import asyncio
from utils import PERMISSIONS_PT
from discord import SelectOption, app_commands
from discord.ext import commands
from discord.ui import TextInput, View, Button

class EmbedTitulo(discord.ui.Modal):
	def __init__(self, embed):
		super().__init__(title="Altere o Título da sua Embed.")
		self.embed=embed
		self.titulo=TextInput(
				label="Título da Embed:",
				placeholder="Defina o Título da sua Embed...",
				default=embed.title,
				max_length=256,
				style=discord.TextStyle.long
			)
		self.url=TextInput(
				label="URL do Título: (opcional)",
				placeholder="URL que ficará no título da Embed...",
				default=embed.url,
				style=discord.TextStyle.long,
				required=False
			)
		self.add_item(self.titulo)
		self.add_item(self.url)
		
	async def on_submit(self, inter:discord.Interaction):
		self.embed.title = str(self.titulo)
		self.embed.url = str(self.url)
		await inter.response.edit_message(embed=self.embed)
		
class EmbedDescrição(discord.ui.Modal):
	def __init__(self, embed):
		super().__init__(title="Altere a Descrição da sua Embed.")
		self.embed=embed
		self.descrição=TextInput(
				label="Descrição da Embed:",
				placeholder="Defina a descrição da sua Embed...",
				default=embed.description,
				style=discord.TextStyle.paragraph
			)
		self.add_item(self.descrição)
		
	async def on_submit(self, inter:discord.Interaction):
		self.embed.description = str(self.descrição)
		await inter.response.edit_message(embed=self.embed)
		
class EmbedCor(discord.ui.Modal):
	def __init__(self, embed):
		super().__init__(title="Altere a Cor da sua Embed.")
		self.embed=embed
		self.cor=TextInput(
				label="Cor da sua Embed:(Hex)",
				placeholder="Defina a Cor da sua Embed em Hex(Ex:#4D4DFF).",
				style=discord.TextStyle.short
			)
		self.add_item(self.cor)
		
	async def on_submit(self, inter:discord.Interaction):
		try:
			self.embed.color = int(self.cor.value[1:], 16)
			self.cor.default = self.cor.value
			await inter.response.edit_message(embed=self.embed)
		except:
			await inter.response.send_message("❌ Coloque uma cor válida em HEX", delete_after=5, ephemeral=True)
		
class EmbedCorView(discord.ui.Select):
    def __init__(self, embed):
        self.embed = embed
        options=[SelectOption(value="Hex", label="Código HEX", emoji="➕"), 
                         SelectOption(value=str(discord.Color.red()), label="Vermelho", emoji="🟥"),
                         SelectOption(value=str(discord.Color.blue()), label="Azul", emoji="🟦"),
                         SelectOption(value=str(discord.Color.green()), label="Verde", emoji="🟩"),
                         SelectOption(value=str(discord.Color.yellow()), label="Amarelo", emoji="🟨"),
                         SelectOption(value=str(discord.Color.orange()), label="Laranja", emoji="🟧"),
                         SelectOption(value=str(discord.Color.purple()), label="Roxo", emoji="🟪"),
                         SelectOption(value=str(discord.Color.dark_embed()), label="Preto", emoji="⬛"),
                         SelectOption(value="random", label="Cor Aleatória", emoji="🌈")
                         ]
        super().__init__(options=options,
                                     placeholder="Selecione uma cor...")
                                     
    async def callback(self, interaction:discord.Interaction):
        option = self.values[0]
        if option == "Hex":
            await interaction.response.send_modal(EmbedCor(self.embed))
        elif option == "random":
            self.embed.color = color=discord.Color.random()
            await interaction.response.edit_message(embed=self.embed)
        else:
            int_cor = int(option[1:], 16)
            self.embed.color = int_cor
            await interaction.response.edit_message(embed=self.embed)
		
class EmbedAuthor(discord.ui.Modal):
	def __init__(self, embed):
		super().__init__(title="Altere o Author da sua Embed.")
		self.embed=embed
		self.nome=TextInput(
				label="Nome do Author da sua Embed:",
				placeholder="Nome pequeno que fica acima do título...",
				default=embed.author.name,
				max_length=256,
				style=discord.TextStyle.long,
				required=False
			)
		self.icone_url=TextInput(
				label="Imagem do Author:",
				placeholder="Imagem que irá ficar lado do Nome...",
				default=embed.author.icon_url,
				style=discord.TextStyle.long,
				required=False
			)
		self.url=TextInput(
				label="URL do Author",
				placeholder="Link que ficará no nome do Author...",
				default=embed.author.url,
				style=discord.TextStyle.long,
				required=False
			)
		self.add_item(self.nome)
		self.add_item(self.icone_url)
		self.add_item(self.url)
		
	async def on_submit(self, inter:discord.Interaction):
		self.embed.set_author(name=str(self.nome), icon_url=str(self.icone_url), url=str(self.url))
		await inter.response.edit_message(embed=self.embed)
		
class EmbedImgTumb(discord.ui.Modal):
	def __init__(self, embed):
		super().__init__(title="Altere a Imagem/Thumbnail da Embed.")
		self.embed=embed
		self.imagem=TextInput(
				label="URL da Imagem:",
				placeholder="Insira uma URL de Imagem válida...",
				default=embed.image.url,
				style=discord.TextStyle.long,
				required=False
			)
		self.thumbnail=TextInput(
				label="URL da Thumbnail:",
				placeholder="Insira uma URL de Thumbnail válida...",
				default=embed.thumbnail.url,
				style=discord.TextStyle.long,
				required=False
			)
		self.add_item(self.imagem)
		self.add_item(self.thumbnail)
		
	async def on_submit(self, inter:discord.Interaction):
		self.embed.set_image(url=str(self.imagem))
		self.embed.set_thumbnail(url=str(self.thumbnail))
		await inter.response.edit_message(embed=self.embed)
		
class EmbedRodape(discord.ui.Modal):
	def __init__(self, embed):
		super().__init__(title="Altere o Rodapé da Embeds.")
		self.embed=embed
		self.texto=TextInput(
				label="Texto do Rodapé:", 
				placeholder="Texto pequeno que ficará abaixo de toda Embed...",
				default=embed.footer.text,
				style=discord.TextStyle.long,
				max_length=2048,
				required=False
			)
		self.url=TextInput(
				label="URL da Rodapé:",
        		placeholder="Imagem que ficará ao lado do Texto...",
        		default=embed.footer.icon_url,
        		style=discord.TextStyle.long,
        		required=False
        	)
		self.add_item(self.texto)
		self.add_item(self.url)
		
	async def on_submit(self, inter:discord.Interaction):
		self.embed.set_footer(text=str(self.texto), icon_url=str(self.url))
		await inter.response.edit_message(embed=self.embed)
		
class EmbedCamposEditar(discord.ui.Select):
	def __init__(self, embed, bot):
		options=[]
		if embed.fields:
			disabled=False
			for i, f in enumerate(embed.fields):
				options.append(SelectOption(label=f"{i+1}. {f.name}", emoji="✏️", description=f.value, value=f"{i}"))
		else:
			options.append(SelectOption(label="Oi"))
			disabled=True
		super().__init__(
				options=options,
				placeholder="Escolha um campo para Editar...",
				disabled=disabled
			)
		self.embed=embed
		self.bot=bot
		
	async def callback(self, inter:discord.Interaction):
		index=int(self.values[0])
		field = self.embed.fields[index]
		await inter.response.send_modal(ModalCampos(self.embed, index, field, self.bot))
		
class EmbedCamposExcluir(discord.ui.Select):
	def __init__(self, embed, bot):
		options=[]
		if embed.fields:
			disabled=False
			for i, f in enumerate(embed.fields):
				options.append(SelectOption(label=f"{i+1}. {f.name}", emoji="<:Lixeira:1140701991228686346>", description=f.value, value=f"{i}"))
		else:
			options.append(SelectOption(label="Oi"))
			disabled=True
		super().__init__(
				options=options,
				placeholder="Escolha um campo para Excluir...",
				disabled=disabled
			)
		self.embed=embed
		self.bot=bot
		
	async def callback(self, inter:discord.Interaction):
		index=int(self.values[0])
		self.embed.remove_field(index)
		await inter.response.edit_message(embed=self.embed, view=EmbedCampos(self.embed, self.bot))
		
		
class ModalCampos(discord.ui.Modal):
	def __init__(self, embed, index, field, bot):
		super().__init__(title="Configure um Campo.")
		self.field = field
		self.embed = embed
		self.index = index
		self.bot = bot
		
		if field.inline:
			linha="Sim"
		else:
			linha="Não"
			
		self.nome=TextInput(
				label="Nome do Campo:",
				placeholder="Insira o nome do campo...",
				default=field.name,
				style=discord.TextStyle.long,
				max_length=256,
			)
		self.valor=TextInput(
				label="Valor do Campo:",
				placeholder="Insira o valor do campo",
				default=field.value,
				style=discord.TextStyle.paragraph,
				max_length=1024
			)
		self.inline=TextInput(
				label="Em linha?:",
				placeholder="Sim ou Não",
				default=linha
			)
		self.add_item(self.nome)
		self.add_item(self.valor)
		self.add_item(self.inline)
		
	async def on_submit(self, inter:discord.Interaction):
		if str(self.inline) == "Sim":
			linha=True
		elif str(self.inline) == "Não":
			linha=False
		else:
			return await inter.response.send_message("Somente as respostas **Sim** ou **Não** são permitidas na pergunta **”Em Linha?“**.", ephemeral=True, delete_after=5)
			
		self.embed.set_field_at(index=self.index, name=str(self.nome), value=str(self.valor), inline=linha)
		await inter.response.edit_message(embed=self.embed, view=EmbedCampos(self.embed, self.bot))

class ModalCamposCriar(discord.ui.Modal):
	def __init__(self, embed, bot):
		super().__init__(title="Configure um Campo.")
		self.embed=embed
		self.bot=bot
			
		self.nome=TextInput(
				label="Nome do Campo:",
				placeholder="Insira o nome do campo...",
				style=discord.TextStyle.long,
				max_length=256,
			)
		self.valor=TextInput(
				label="Valor do Campo:",
				placeholder="Insira o valor do campo",
				style=discord.TextStyle.paragraph,
				max_length=1024
			)
		self.inline=TextInput(
				label="Em linha?:",
				placeholder="Sim ou Não",
				default="Sim"
			)
		self.add_item(self.nome)
		self.add_item(self.valor)
		self.add_item(self.inline)
		
	async def on_submit(self, inter:discord.Interaction):
		if str(self.inline) == "Sim":
			linha=True
		elif str(self.inline) == "Não":
			linha=False
		else:
			return await inter.response.send_message("Somente as respostas **Sim** ou **Não** são permitidas na pergunta **”Em Linha?“**.", ephemeral=True, delete_after=5)
			
		self.embed.add_field(name=str(self.nome), value=str(self.valor), inline=linha)
		await inter.response.edit_message(embed=self.embed, view=EmbedCampos(self.embed, self.bot))
		
		
class EmbedCampos(discord.ui.View):
	def __init__(self, embed, bot):
		super().__init__(timeout=None)
		self.embed = embed
		self.bot = bot
		button_create=discord.ui.Button(label="Adicionar Campo", emoji="➕", style=discord.ButtonStyle.blurple)
		
		self.add_item(EmbedCamposEditar(embed, bot))
		self.add_item(EmbedCamposExcluir(embed, bot))
		self.add_item(ReturnButton(embed, bot))
		self.add_item(button_create)
		
		if embed.fields:
			if len(embed.fields) >= 25:
				button_create.disabled = True
			
		button_create.callback = self.add_field
			
	async def add_field(self, inter:discord.Interaction):
		await inter.response.send_modal(ModalCamposCriar(self.embed, self.bot))
			

class EmbedEdit(discord.ui.Select):
	def __init__(self, embed, bot):
		self.embed = embed
		self.bot = bot
		options = [
				SelectOption(label="Título", value="título"),
				SelectOption(label="Descrição",value="descrição"),
				SelectOption(label="Cor", value="cor"),
				SelectOption(label="Author", value="author"),
				SelectOption(label="Imagem e Thumbnail", value="imagens"),
				SelectOption(label="Editar Campos", value="campos"),
				SelectOption(label="Rodapé", value="rodapé")
			]
		super().__init__(
				options=options,
				placeholder="Edite a embed..."
			)
			
	async def callback(self, inter:discord.Interaction):
		option = self.values[0]
		
		if option == "título":
			await inter.response.send_modal(EmbedTitulo(self.embed))
		elif option == "descrição":
			await inter.response.send_modal(EmbedDescrição(self.embed))
		elif option == "cor":
			button_url = Button(label="Encontrar cores", style=discord.ButtonStyle.link, url="https://www.homehost.com.br/blog/tutoriais/tabela-de-cores-html/")
			
			view = View(timeout=None).add_item(EmbedCorView(self.embed)).add_item(ReturnButton(self.embed, self.bot)).add_item(button_url)
			await inter.response.edit_message(view=view)
		elif option == "author":
			await inter.response.send_modal(EmbedAuthor(self.embed))
		elif option == "imagens":
			await inter.response.send_modal(EmbedImgTumb(self.embed))
		elif option == "campos":
			await inter.response.edit_message(view=EmbedCampos(self.embed, self.bot))
		elif option == "rodapé":
			await inter.response.send_modal(EmbedRodape(self.embed))
			
class ModalWebhook(discord.ui.Modal):
    def __init__(self, channel, inter, embed, bot):
        super().__init__(title="Configure sua Webhook")
        self.channel = channel
        self.embed = embed
        self.bot = bot
        self.name = TextInput(label="Nome da WebHook:", default=inter.user.display_name, style=discord.TextStyle.short)
        
        self.avatar = TextInput(label="Avatar da WebHook", placeholder="Insira uma URL de Imagem válida...", default=inter.user.display_avatar.url, style=discord.TextStyle.long)
        self.add_item(self.name)
        self.add_item(self.avatar)
        
    async def on_submit(self, interaction:discord.Interaction):
    	embed=discord.Embed(description="Enviando <a:carregando:1117177450275803197>", color=discord.Color.green())
    	await interaction.response.edit_message(embed=embed, view=None)
    	webhook = await self.channel.create_webhook(name="Embed criar", reason=f"Para a embed criada e enviada por {interaction.user.display_name}({interaction.user.id})")
    	await webhook.send(embed=self.embed, username=str(self.name.value), avatar_url=str(self.avatar.value))
    	view = View(timeout=None).add_item(EmbedEdit(self.embed, self.bot)).add_item(EnviarEmbed(self.embed, self.bot)).add_item(EnviarPerson(self.embed, self.bot))
    	await interaction.edit_original_response(embed=self.embed, view=view)
    	await asyncio.sleep(5)
    	await webhook.delete(reason="Não chegar ao limite de webhook(Atualmente o máximo é 15)")
			
class EmbedEnviar(discord.ui.ChannelSelect):
    def __init__(self, enviar, embed, bot):
        self.enviar = enviar
        self.embed = embed
        self.bot = bot
        super().__init__(placeholder="Escolha o Canal...",channel_types=[discord.ChannelType.text, discord.ChannelType.news])
                                     
    async def callback(self, inter:discord.Interaction):
        canal = self.values[0]
        channel = inter.guild.get_channel(canal.id)
        if self.enviar == "bot":
            try:
            	await channel.send(embed=self.embed)
            	view = View(timeout=None).add_item(EmbedEdit(self.embed, self.bot)).add_item(EnviarEmbed(self.embed, self.bot)).add_item(EnviarPerson(self.embed, self.bot))
            	await inter.response.edit_message(view=view)
            except discord.Forbidden:
            	await inter.response.send_message("❌ Não tenho permissões suficientes para enviar a Embed nesse canal:\n**Enviar Mensagens**\n**Inserir Links**", ephemeral=True, delete_after=5)
        elif self.enviar == "webhook":
            bot = inter.guild.get_member(self.bot.user.id)
            if channel.permissions_for(bot).manage_webhooks:
            	await inter.response.send_modal(ModalWebhook(channel, inter, self.embed, self.bot))
            else:
            	await inter.response.send_message("❌ Não tenho permissões para enviar a Embed nesse canal:\n**Gerenciar Webhooks**", ephemeral=True, delete_after=5)
            	
class ReturnButton(discord.ui.Button):
    def __init__(self, embed, bot):
        self.embed=embed
        self.bot = bot
        super().__init__(emoji="↩️", style=discord.ButtonStyle.gray)
            
    async def callback(self, interaction: discord.Interaction):
        view = View(timeout=None).add_item(EmbedEdit(self.embed, self.bot)).add_item(EnviarEmbed(self.embed, self.bot)).add_item(EnviarPerson(self.embed, self.bot))
        await interaction.response.edit_message(view=view)
        
class EnviarEmbed(discord.ui.Button):
    def __init__(self, embed, bot):
        self.enviar = "bot"
        self.embed = embed
        self.bot = bot
        super().__init__(label="Enviar Embed", emoji="📨", style=discord.ButtonStyle.green)
        
    async def callback(self, interaction:discord.Interaction):
        view = discord.ui.View(timeout=None).add_item(EmbedEnviar(self.enviar, self.embed, self.bot)).add_item(ReturnButton(self.embed, self.bot))
        await interaction.response.edit_message(view=view)
        
class EnviarPerson(discord.ui.Button):
    def __init__(self, embed, bot):
        self.enviar = "webhook"
        self.embed = embed
        self.bot = bot
        super().__init__(label="Enviar em Webhook", emoji="🌐", style=discord.ButtonStyle.green)
        
    async def callback(self, interaction:discord.Interaction):
        view = View(timeout=None).add_item(EmbedEnviar(self.enviar, self.embed, self.bot)).add_item(ReturnButton(self.embed, self.bot))
        await interaction.response.edit_message(view=view)

@app_commands.guild_only()
class EmbedCriar(commands.GroupCog, name="embed"):
    def __init__(self, bot):
        self.bot = bot
       
    @app_commands.command(name="criar",description="Painel para criar embed")
    @app_commands.checks.has_permissions(manage_messages=True, embed_links=True)
    @app_commands.checks.bot_has_permissions(manage_webhooks=True, embed_links=True)
    async def _embed(self, inter: discord.Interaction):
        embed = discord.Embed(title="Título", description="Descrição da embed", color=discord.Color.random())
        
        view = View(timeout=None).add_item(EmbedEdit(embed, self.bot)).add_item(EnviarEmbed(embed, self.bot)).add_item(EnviarPerson(embed, self.bot))
        await inter.response.send_message(embed=embed, view=view, ephemeral=True)
        
      
    @_embed.error
    async def embed_erro(self, inter:discord.Interaction, erro):
        if isinstance(erro, app_commands.MissingPermissions):
            perms = PERMISSIONS_PT[str(erro.missing_permissions)[2:-2]]
            await inter.response.send_message(f"❌ Você não tem a permissão **{perms}**", ephemeral=True)
        elif isinstance(erro, app_commands.BotMissingPermissions):
            perm=[]
            for p in erro.missing_permissions:
                perm.append(PERMISSIONS_PT[p])
            
            perms = "\n".join(perm)
            await inter.response.send_message(f"❌ Preciso das seguintes permissões para esse comando:\n**{perms}**", ephemeral=True)

async def setup(bot: commands.Bot):
    await bot.add_cog(EmbedCriar(bot))
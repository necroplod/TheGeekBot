import discord
import config
from discord import Intents
from discord.ext import commands

class Setup(commands.Bot):
	def main(self):	
		self.remove_command('help')
		self.line = '----------------------------------------------'

		self.EXTENSIONS = [
			'cogs.dev',
			'cogs.events',
			'cogs.suggest'
		]
	
	async def setup_hook(self):
		self.main()
		for extension in self.EXTENSIONS:
			try:
				await self.load_extension(extension)
			except Exception as e:
				print(f'{self.line}\n[!] Не удалось загрузить модуль {extension}.')
				print(f'[!] {e}\n{self.line}')
			else:
				print(f'[!] Модуль {extension} успешно загружен.')


client = Setup(
	status = discord.Status.idle,
	activity = discord.Streaming(name=f'TheGeekBot', url='https://www.youtube.com/channel/UCzgnKOieA67fBwNXhV53a_g'),
	case_insensitive = True, 
	command_prefix = config.PREFIX, 
	intents = Intents.all()
)
client.run(config.TOKEN)
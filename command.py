from abc import abstractmethod
import discord


# This is the parent class where all the children(modules) extends
class Command:
	# name of the command
	name: str

	# Basically like the constructor method in java
	def __init__(self, name):
		self.name = name

	@abstractmethod
	async def on_command(self, args: list, command: str, event):
		pass


# The info command
class Info(Command):
	def __init__(self, name):
		super().__init__(name)

	async def on_command(self, args, command, event):
		embed = discord.Embed(title='Info', description='Information about this bot', color=0xffffff)
		embed.add_field(name='Creator', value='Keviniest#9805', inline=False)
		embed.add_field(name='Source code', value='https://github.com/keviniest/Friends-Server-Bot', inline=False)
		embed.add_field(name='How to get started', value='?help', inline=False)
		await event.channel.send(embed=embed)


# The help command
class Help(Command):
	def __init__(self, name):
		super().__init__(name)

	async def on_command(self, args, command, event):
		await event.channel.send('`help ... prints this message\n info ... little info about this bot`')

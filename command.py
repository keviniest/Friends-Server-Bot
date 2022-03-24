from abc import ABC, abstractmethod
import discord

# This is the parent class where all the children(modules) extends
class Command:
	# name of the command
	name: str

	# Basically like the constructor method in java
	def __init__(self, name):
		self.name = name

	@abstractmethod
	def on_command(self, args: list, command: str, event):
		pass


# The info command
class Info(Command):
	def __init__(self, name):
		super().__init__(name)

	def on_command(self, args, command, event):
		embed = discord.Embed(title="Info", description="Information about this bot", color=0xffffff)
		embed.add_field(name="undefined", value="undefined", inline=False)
		event.channel.send(embed=embed)


# The help command
class Help(Command):
	def __init__(self, name):
		super().__init__(name)

	def on_command(self, args, command, event):
		event.channel.send("`ask ming or smth, idk`")

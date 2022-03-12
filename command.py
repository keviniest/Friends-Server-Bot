from abc import ABC, abstractmethod
import discord


# from main import event

# This is the parent class where all the children(module) extends
class Command:
	# name of the command
	name: str

	# Basically like the constructor method in java
	def __init__(self, name):
		self.name = name

	@abstractmethod
	def on_command(self, args: list, command: str):
		pass


# The info command
class Info(Command, ABC):
	def __init__(self):
		super(Command, self).__init__("self")

	def on_command(self, args, command):
		embed = discord.Embed(title="Info", description="Information about this bot", color=0xffffff)
		embed.add_field(name="undefined", value="undefined", inline=False)
		# event.channel.send(embed=embed)
		print("info command executed")


# The help command
class Help(Command, ABC):
	def __init__(self):
		super(Command, self).__init__("help")

	def on_command(self, args, command):
		# event.channel.send("`ask ming or smth, idk`")
		print("help command executed")

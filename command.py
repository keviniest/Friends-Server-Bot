import random
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

	async def on_command(self, args: list, command: str, event):
		embed = discord.Embed(title='Info', description='Information about this bot', color=0xffffff)
		embed.add_field(name='Creator', value='Keviniest#9805', inline=False)
		embed.add_field(name='Source code', value='https://github.com/keviniest/Friends-Server-Bot', inline=False)
		embed.add_field(name='How to get started', value='?help', inline=False)
		await event.channel.send(embed=embed)


# The help command
class Help(Command):
	def __init__(self, name):
		super().__init__(name)

	async def on_command(self, args: list, command: str, event):
		await event.channel.send('`help ... prints this message\n info ... little info about this bot`')


class PpLength(Command):
	def __init__(self, name):
		super(PpLength, self).__init__(name)

	async def on_command(self, args: list, command: str, event):
		pp = "8"
		percentage = random.randint(0, 20)
		for i in range(percentage):
			pp = pp + "="
		pp = pp + "D"
		if len(args) == 1:
			await event.channel.send(f"your pp length : \n {pp}")
		await event.channel.send(f"{args[1]}'s pp length : \n {pp}")


class BitchesCounter(Command):
	def __init__(self, name):
		super(BitchesCounter, self).__init__(name)

	async def on_command(self, args: list, command: str, event):
		bitches_count = random.randint(0, 100)
		if len(args) == 1:
			if args[1] == "<@!640892808105820162>":
				await event.channel.send(f"{args[1]} will get 0 bitches in their lifetime")
			else:
				await event.channel.send(f"{args[1]} will get {bitches_count} bitches in their lifetime")
		elif len(args) == 0:
			if event.author.id == "640892808105820162":
				await event.channel.send(f"you will get 0 bitches in your lifetime")
			else:
				await event.channel.send(f"you will get {bitches_count} bitches in your lifetime")


class MaterialGirlness(Command):
	def __init__(self, name):
		super(MaterialGirlness, self).__init__(name)

	async def on_command(self, args: list, command: str, event):
		girl = ""
		percentage = random.randint(0, 10)
		for i in range(percentage):
			girl = girl + "🍑"

		moons = 10 - percentage

		for i in range(moons):
			girl = girl + "🌑"

		if len(args) == 1:
			await event.channel.send(f"you are {girl} level of material girlness 💅")
		elif len(args) == 2:
			await event.channel.send(f"{args[1]}'is {girl} level of material girlness 💅")


class EightBall(Command):
	def __init__(self, name):
		super(EightBall, self).__init__(name)

	async def on_command(self, args: list, command: str, event):
		temps = [
			"🎱 Yesssss!",
			"🎱 Nope.",
			"🎱 nah bro",
			"🎱 Not in mood to answer",
			"🎱 when you grow a braincell, yes",
			"🎱 hell to the yes",
			"🎱 No, you dingleberry",
			"🎱 no!!!!",
			"🎱 yes???"
		]
		number = random.randint(0, len(temps) - 1)
		await event.channel.send(temps[number])

import re
import discord

import command

client = discord.Client()  # Creates a client instance
prefix = '~'  # The bot prefix
# List of modules (commands)
commands = [
	command.Info('info'),
	command.Help('help'),
	command.PpLength('pplength'),
	command.BitchesCounter('bitchescounter'),
	command.MaterialGirlness('materialgirlness'),
	command.EightBall('8ball'),
	command.BanWord('banwords')
]


# reads and returns content of file called "token.txt"
# (which is usually the bot's authentication token)
def get_token() -> str:
	with open('token.txt', 'r') as f:
		return f.read()


# This method is called everytime the bot starts up
@client.event
async def on_ready():
	print(f'Logged in as {client.user}')
	# Sets the bot's rich presence ("watching 💌 friends!")
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='💌 friends!'))


# This method is called everytime message is received from any of the server that the bot is in.
@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if list(message.content)[0] == prefix:

		if message.guild.id == 888038527550521384:
			if message.channel.id != 893262564530720799:
				return

		msg = message.content
		msg = msg[len(prefix):]  # Prefix gets stripped from the message

		if len(re.split('\\s+', msg)[0]) > 0:
			# the name of the command (the first argument without the prefix)
			command_name = re.split('\\s+', msg)[0]

			# Iterates through list of commands
			for c in commands:
				# Finds command matching command_name
				if c.name == command_name:
					# Calls on_command function in the child with the matching name
					await c.on_command(re.split('\\s+', msg)[0:len(re.split('\\s+', msg))], msg, message)
					break
	else:
		msg = message.content
		ban_words: list
		with open('BanWords.txt', 'r') as words:
			ban_words = words.read().splitlines()

		for i in ban_words:
			word: str = i.split(',')[0]
			moderation_level: int = int(i.split(',')[1])
			caps_sensitive: bool = i.split(',')[2] == 'true'

			if word in (msg if caps_sensitive else msg.lower()):
				if moderation_level == 1:
					await message.channel.send(f'`{word}` is a banned word, {message.author.name}!')
				elif moderation_level == 2:
					await message.channel.send(
						f'`{word}` is a banned word, {message.author.name}! You will be kicked from this server.')
					await message.author.kick(reason='Banned word usage')
				elif moderation_level == 3:
					await message.channel.send(
						f'`{word}` is a banned word, {message.author.name}! You will be banned from this server.')
					await message.author.ban(reason='Banned word usage')


client.run(get_token())
